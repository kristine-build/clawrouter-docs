#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

try:
    import requests
except Exception:  # pragma: no cover
    requests = None

DOCS = Path("docs")
SUMMARY = DOCS / "SUMMARY.md"
MAP_JSON = DOCS / "_mapping.json"
CACHE_JSON = DOCS / "_newapi_source_map.json"
BASE = "https://clawrouter.com/zh/llms.mdx/"
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)

METHOD_LINE_RE = re.compile(r"^(GET|POST|PUT|DELETE)\s*$")


@dataclass
class Node:
    title: str
    link: Optional[str] = None
    level: int = 0
    parent: Optional["Node"] = None
    children: list["Node"] = field(default_factory=list)

    def crumbs(self) -> list[str]:
        out = []
        cur: Optional[Node] = self
        while cur and cur.parent is not None:
            out.append(cur.title)
            cur = cur.parent
        return list(reversed(out))


def normalize(s: str) -> str:
    s = s.strip().replace("（", "(").replace("）", ")")
    s = re.sub(r"\s*\((GET|POST|PUT|DELETE)\)\s*$", "", s, flags=re.I)
    s = s.lower()
    s = re.sub(r"\s+", "", s)
    return s


def parse_summary_tree(path: Path) -> tuple[Node, list[Node]]:
    root = Node("ROOT", level=-1)
    stack: list[Node] = [root]
    linked: list[Node] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(\s*)-\s+\[([^\]]+)\]\(([^)]+\.md)\)\s*$", raw)
        m2 = re.match(r"^(\s*)-\s+(.+?)\s*$", raw)
        if not m and not m2:
            continue
        if m:
            indent, title, link = m.groups()
        else:
            indent, title = m2.groups()
            link = None
            if title.startswith("["):
                continue
        level = len(indent) // 2
        while stack and stack[-1].level >= level:
            stack.pop()
        parent = stack[-1]
        n = Node(title=title, link=link, level=level, parent=parent)
        parent.children.append(n)
        stack.append(n)
        if link and link.endswith(".md"):
            linked.append(n)
    return root, linked


def load_cache() -> dict:
    if CACHE_JSON.exists():
        try:
            return json.loads(CACHE_JSON.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_cache(cache: dict) -> None:
    CACHE_JSON.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def derive_original_from_matched_file(mf: str) -> Optional[str]:
    stem = mf[:-3] if mf.endswith(".md") else mf
    parts = [p for p in stem.split("__") if p]
    if len(parts) < 3:
        return None
    if parts[0] != "zh":
        return None
    # zh/docs/api/.../__<title-new-api>__<hash>
    if parts[-1] and re.fullmatch(r"[0-9a-f]{8}", parts[-1]):
        parts = parts[:-1]
    if parts and "new-api" in parts[-1]:
        parts = parts[:-1]
    return "/" + "/".join(parts)


def mapping_entries() -> list[tuple[list[str], str]]:
    if not MAP_JSON.exists():
        return []
    data = json.loads(MAP_JSON.read_text(encoding="utf-8"))
    out: list[tuple[list[str], str]] = []
    for k, v in data.items():
        if not isinstance(v, dict):
            continue
        mf = v.get("matched_file")
        if not mf:
            continue
        op = derive_original_from_matched_file(str(mf))
        if not op:
            continue
        parts = [p.strip() for p in k.split(">")]
        out.append((parts, op))
    return out


def infer_original_from_target(rel: str) -> str:
    p = rel
    if p == "README.md":
        return "/zh/docs/api"
    if p.endswith("/README.md"):
        p = p[: -len("/README.md")]
    else:
        p = p[:-3] if p.endswith(".md") else p
    return "/zh/docs/api/" + p


def choose_original(node: Node, cache: dict, map_entries: list[tuple[list[str], str]]) -> tuple[Optional[str], str]:
    rel = node.link or ""
    if rel in cache and cache[rel].get("original_path"):
        return cache[rel]["original_path"], "cache"

    crumbs = node.crumbs()
    ncrumbs = [normalize(x) for x in crumbs]

    best_score = -1
    best_op = None
    for parts, op in map_entries:
        nparts = [normalize(x) for x in parts]
        score = 0
        # suffix matching by crumbs
        maxk = min(len(ncrumbs), len(nparts))
        for k in range(1, maxk + 1):
            if ncrumbs[-k:] == nparts[-k:]:
                score = max(score, k * 2)
        # last title fuzzy
        if ncrumbs and nparts and (ncrumbs[-1] in nparts[-1] or nparts[-1] in ncrumbs[-1]):
            score += 1
        if score > best_score:
            best_score = score
            best_op = op

    if best_op and best_score >= 3:
        return best_op, "mapping"

    return infer_original_from_target(rel), "infer"


def to_mdx_url(original: str) -> str:
    x = original
    if x.startswith("/zh/docs/"):
        x = x[len("/zh/docs/") :]
    x = x.lstrip("/")
    return BASE + x


def fetch_text(url: str) -> tuple[bool, str]:
    if requests is None:
        return False, "requests not available"
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=12)
    except Exception as e:
        return False, f"request error: {e}"
    if r.status_code != 200:
        return False, f"http {r.status_code}"
    return True, r.text


def convert_callouts(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        title = (m.group(1) or "提示").strip()
        body = m.group(2).strip()
        lines = [f"> **{title}**"]
        for ln in body.splitlines():
            lines.append("> " + ln)
        return "\n".join(lines)

    return re.sub(r"<Callout(?:\s+title=\"([^\"]*)\")?[^>]*>(.*?)</Callout>", repl, text, flags=re.S)


def parse_attrs(s: str) -> dict[str, str]:
    return {k: v for k, v in re.findall(r"(\w+)=\"([^\"]*)\"", s)}


def convert_cards(text: str) -> str:
    def cards_block_repl(m: re.Match[str]) -> str:
        body = m.group(1)
        cards = re.findall(r"<Card\s+([^>/]*?)/>", body, flags=re.S)
        lines = []
        for c in cards:
            a = parse_attrs(c)
            t = a.get("title", "链接")
            h = a.get("href", "#")
            d = a.get("description", "")
            lines.append(f"- [{t}]({h})")
            if d:
                lines.append(f"  {d}")
        return "\n".join(lines) if lines else ""

    text = re.sub(r"<Cards[^>]*>(.*?)</Cards>", cards_block_repl, text, flags=re.S)

    # standalone self-closing Card
    def card_repl(m: re.Match[str]) -> str:
        a = parse_attrs(m.group(1))
        t = a.get("title", "链接")
        h = a.get("href", "#")
        d = a.get("description", "")
        out = f"- [{t}]({h})"
        if d:
            out += f"\n  {d}"
        return out

    text = re.sub(r"<Card\s+([^>/]*?)/>", card_repl, text, flags=re.S)
    return text


def convert_apipage(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        tag = m.group(0)
        p = re.search(r'"path"\s*:\s*"([^"]+)"', tag)
        meth = re.search(r'"method"\s*:\s*"([a-zA-Z]+)"', tag)
        lines = []
        if p and meth:
            lines.append("## 接口")
            lines.append("")
            lines.append(f"`{meth.group(1).upper()} {p.group(1)}`")
            lines.append("")
        return "\n".join(lines)

    return re.sub(r"<APIPage[\s\S]*?/>", repl, text)


def clean_mdx_to_md(text: str, title: str) -> str:
    # remove frontmatter
    text = re.sub(r"\A---\n[\s\S]*?\n---\n", "", text)
    # imports
    text = re.sub(r"(?m)^import\s+.*$\n?", "", text)
    # comments {/* ... */}
    text = re.sub(r"\{\/\*[\s\S]*?\*\/\}", "", text)

    text = convert_callouts(text)
    text = convert_cards(text)
    text = convert_apipage(text)

    # remove raw JSX tags still remaining
    text = re.sub(r"(?m)^<[^>]+>$", "", text)

    lines = text.splitlines()
    out: list[str] = []
    skip_openapi = False
    for ln in lines:
        s = ln.strip()
        if re.match(r"^#+\s*openapi", s, flags=re.I) or "OpenAPI JSON" in s:
            skip_openapi = True
            continue
        if skip_openapi and s.startswith("#"):
            skip_openapi = False
        if skip_openapi:
            continue
        if METHOD_LINE_RE.match(s):
            continue
        out.append(ln)

    body = "\n".join(out)
    # remove leading headings and blanks; we'll set H1
    body_lines = body.splitlines()
    while body_lines and (not body_lines[0].strip() or body_lines[0].lstrip().startswith("#")):
        body_lines.pop(0)

    body = "\n".join(body_lines).strip()
    if body:
        return f"# {title}\n\n{body}\n"
    return f"# {title}\n"


def first_descendant_link(n: Node) -> Optional[str]:
    for c in n.children:
        if c.link:
            return c.link
        x = first_descendant_link(c)
        if x:
            return x
    return None


def rel_link(from_file: Path, to_rel: str) -> str:
    return os.path.relpath((DOCS / to_rel).as_posix(), from_file.parent.as_posix())


def write_parent_readmes(root: Node) -> None:
    # linked README nodes in summary
    def walk(n: Node):
        if n.link and n.link.endswith("README.md"):
            p = DOCS / n.link
            p.parent.mkdir(parents=True, exist_ok=True)
            lines = [f"# {n.title}", "", f"{n.title} 相关文档导航。", "", "## 本章内容", ""]

            # special start links for AI / Audio pages
            if n.link in {"ai-model/README.md", "ai-model/audio/README.md"}:
                lines.append("- 👉 从这里开始：[原生Gemini格式](./audio/gemini-native.md)" if n.link == "ai-model/README.md" else "- 👉 从这里开始：[原生Gemini格式](./gemini-native.md)")

            for c in n.children:
                target = c.link or first_descendant_link(c)
                if not target:
                    continue
                lines.append(f"- [{c.title}]({rel_link(p, target)})")
            p.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        for c in n.children:
            walk(c)

    walk(root)

    # ensure AI / Audio overview pages exist even if non-clickable in SUMMARY
    ai = DOCS / "ai-model/README.md"
    ai.parent.mkdir(parents=True, exist_ok=True)
    ai.write_text(
        "# AI 模型接口\n\nAI 模型接口导航。\n\n## 本章内容\n\n- 👉 从这里开始：[原生Gemini格式](./audio/gemini-native.md)\n",
        encoding="utf-8",
    )
    au = DOCS / "ai-model/audio/README.md"
    au.parent.mkdir(parents=True, exist_ok=True)
    au.write_text(
        "# 音频（Audio）\n\n音频接口导航。\n\n## 本章内容\n\n- 👉 从这里开始：[原生Gemini格式](./gemini-native.md)\n",
        encoding="utf-8",
    )


def grep_checks(targets: list[Node]) -> tuple[int, int]:
    bad_jsx = 0
    bad_method = 0
    jsx_pat = re.compile(r"<APIPage|import\s+\{|\{/\*")
    m_pat = re.compile(r"(?m)^(GET|POST|PUT|DELETE)\s*$")
    for n in targets:
        p = DOCS / (n.link or "")
        if not p.exists():
            continue
        t = p.read_text(encoding="utf-8", errors="ignore")
        if jsx_pat.search(t):
            bad_jsx += 1
        if m_pat.search(t):
            bad_method += 1
    return bad_jsx, bad_method


def main() -> None:
    root, targets = parse_summary_tree(SUMMARY)
    cache = load_cache()
    m_entries = mapping_entries()

    total = len(targets)
    fetched_ok = 0
    skipped = 0
    failed = 0
    failed_list: list[tuple[str, str]] = []

    fetch_cache: dict[str, tuple[bool, str]] = {}

    for n in targets:
        rel = n.link or ""
        if not rel.endswith(".md"):
            skipped += 1
            continue
        target = DOCS / rel
        target.parent.mkdir(parents=True, exist_ok=True)

        original, source = choose_original(n, cache, m_entries)
        if not original:
            skipped += 1
            failed_list.append((rel, "no source mapping"))
            continue

        cache[rel] = {
            "title": n.title,
            "original_path": original,
            "source": source,
        }

        url = to_mdx_url(original)
        if url not in fetch_cache:
            ok, payload = fetch_text(url)
            fetch_cache[url] = (ok, payload)
        else:
            ok, payload = fetch_cache[url]

        if not ok:
            failed += 1
            failed_list.append((rel, payload))
            continue

        md = clean_mdx_to_md(payload, n.title)
        target.write_text(md, encoding="utf-8")
        fetched_ok += 1

    save_cache(cache)

    write_parent_readmes(root)

    bad_jsx, bad_method = grep_checks(targets)

    print(f"total targets: {total}")
    print(f"fetched ok: {fetched_ok}")
    print(f"skipped: {skipped}")
    print(f"failed: {failed}")
    print("first 20 failed:")
    for rel, reason in failed_list[:20]:
        print(f"- {rel}: {reason}")
    print(f"grep check jsx residue count: {bad_jsx}")
    print(f"grep check standalone method lines count: {bad_method}")


if __name__ == "__main__":
    main()
