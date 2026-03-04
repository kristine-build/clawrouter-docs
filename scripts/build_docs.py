#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from clean_markdown import clean_file

ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = ROOT / "docs"
SIDEBAR_SOURCE = ROOT / "sidebar_source.txt"

METHOD_RE = re.compile(r"\((GET|POST|PUT|DELETE|PATCH)\)\s*$", re.IGNORECASE)
TOKEN_RE = re.compile(r"[a-z0-9\u4e00-\u9fff]+", re.IGNORECASE)
STOP_TOKENS = {
    "api",
    "参考",
    "管理",
    "接口",
    "原生",
    "格式",
    "post",
    "get",
    "put",
    "delete",
    "patch",
    "openai",
    "gemini",
}

GENERATED_DOC_FILES = {"_sidebar.md", "_missing.txt", "_mapping.json", "_rename_collisions.txt"}


@dataclass
class SidebarNode:
    title: str
    level: int
    children: list["SidebarNode"] = field(default_factory=list)
    parent: Optional["SidebarNode"] = None

    def add_child(self, node: "SidebarNode") -> None:
        node.parent = self
        self.children.append(node)

    @property
    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def path_titles(self) -> list[str]:
        out: list[str] = []
        cur: Optional[SidebarNode] = self
        while cur is not None and cur.parent is not None:
            out.append(cur.title)
            cur = cur.parent
        out.reverse()
        return out

    def path_str(self) -> str:
        return " > ".join(self.path_titles())


@dataclass
class DocCandidate:
    path: Path
    rel_path: str
    filename_tokens: set[str]
    h1_tokens: set[str]
    fulltext: str


@dataclass
class MatchResult:
    matched_file: Optional[str]
    confidence: float
    reason: str


def normalize_text_for_tokens(value: str) -> str:
    value = value.lower().strip()
    value = value.replace("（", "(").replace("）", ")")
    value = value.replace("2fa", "twofactor")
    value = value.replace("oauth", "oauth")
    value = value.replace("passkey", "passkey")
    value = value.replace("midjourney", "midjourney")
    value = value.replace("kling", "kling")
    value = value.replace("sora", "sora")
    return value


def tokenize(value: str) -> set[str]:
    normalized = normalize_text_for_tokens(value)
    return set(TOKEN_RE.findall(normalized))


def extract_method(value: str) -> Optional[str]:
    m = METHOD_RE.search(value)
    if not m:
        return None
    return m.group(1).lower()


def title_without_method(value: str) -> str:
    return METHOD_RE.sub("", value).strip()


def first_h1(text: str) -> str:
    in_fence = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if stripped.startswith("# "):
            heading = stripped[2:].strip()
            heading = heading.replace("| New API", "").strip()
            return heading
    return ""


def parse_sidebar_source(path: Path) -> SidebarNode:
    if not path.exists():
        raise SystemExit(f"sidebar source missing: {path}")

    raw_text = path.read_text(encoding="utf-8")
    non_empty_lines = [ln for ln in raw_text.splitlines() if ln.strip()]
    if len(non_empty_lines) < 10:
        raise SystemExit(
            "sidebar_source.txt looks invalid: too few lines. "
            "Please provide multi-line hierarchy with 2-space indentation."
        )

    root = SidebarNode(title="ROOT", level=-1)
    stack: list[SidebarNode] = [root]

    for lineno, raw in enumerate(raw_text.splitlines(), start=1):
        if not raw.strip():
            continue

        leading = len(raw) - len(raw.lstrip(" "))
        if leading % 2 != 0:
            raise SystemExit(f"Invalid indent at line {lineno}: use 2 spaces per level")

        level = leading // 2
        title = raw.strip()

        while len(stack) > 1 and stack[-1].level >= level:
            stack.pop()

        parent = stack[-1]
        node = SidebarNode(title=title, level=level)
        parent.add_child(node)
        stack.append(node)

    return root


def iter_nodes(root: SidebarNode) -> list[SidebarNode]:
    out: list[SidebarNode] = []

    def walk(node: SidebarNode) -> None:
        for child in node.children:
            out.append(child)
            walk(child)

    walk(root)
    return out


def iter_leaf_nodes(root: SidebarNode) -> list[SidebarNode]:
    return [n for n in iter_nodes(root) if n.is_leaf]


def list_doc_candidates(docs_root: Path) -> list[DocCandidate]:
    candidates: list[DocCandidate] = []
    for path in sorted(docs_root.rglob("*.md")):
        if path.name in GENERATED_DOC_FILES:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        h1 = first_h1(text)
        rel = path.relative_to(docs_root).as_posix()
        candidates.append(
            DocCandidate(
                path=path,
                rel_path=rel,
                filename_tokens=tokenize(path.stem),
                h1_tokens=tokenize(h1),
                fulltext=normalize_text_for_tokens(path.stem + " " + h1),
            )
        )
    return candidates


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def score_node_to_doc(node: SidebarNode, doc: DocCandidate) -> tuple[float, str]:
    method = extract_method(node.title)
    node_text = title_without_method(node.title)
    path_text = " ".join(node.path_titles())

    node_tokens = tokenize(node_text)
    path_tokens = tokenize(path_text)

    filename_score = jaccard(node_tokens, doc.filename_tokens)
    heading_score = jaccard(node_tokens, doc.h1_tokens)
    path_score = jaccard(path_tokens, doc.filename_tokens | doc.h1_tokens)

    score = filename_score * 0.40 + heading_score * 0.40 + path_score * 0.10

    ancestor_text = ""
    parent = node.parent
    grandparent = node.parent.parent if node.parent else None
    if parent and parent.parent is not None:
        ancestor_text += " " + title_without_method(parent.title)
    if grandparent and grandparent.parent is not None:
        ancestor_text += " " + title_without_method(grandparent.title)
    ancestor_tokens = {t for t in tokenize(ancestor_text) if t not in STOP_TOKENS}
    doc_tokens = doc.filename_tokens | doc.h1_tokens
    ancestor_overlap = len(ancestor_tokens & doc_tokens)
    ancestor_bonus = min(0.22, ancestor_overlap * 0.08) if ancestor_tokens else 0.0
    score += ancestor_bonus

    method_bonus = 0.0
    method_reason = ""
    if method:
        if method in doc.fulltext:
            method_bonus = 0.08
            method_reason = f", method={method} matched"
        else:
            score -= 0.05
            method_reason = f", method={method} not found"

    final = max(0.0, min(1.0, score + method_bonus))
    reason = (
        f"filename={filename_score:.3f}, h1={heading_score:.3f}, path={path_score:.3f}, "
        f"ancestor_bonus={ancestor_bonus:.3f}{method_reason}"
    )
    return final, reason


def pick_mapping_for_node(node: SidebarNode, candidates: list[DocCandidate], used: set[str]) -> MatchResult:
    scored: list[tuple[float, str, DocCandidate]] = []
    for doc in candidates:
        if doc.rel_path in used:
            continue
        score, reason = score_node_to_doc(node, doc)
        scored.append((score, reason, doc))

    if not scored:
        return MatchResult(None, 0.0, "no candidates")

    scored.sort(key=lambda x: (-x[0], x[2].rel_path))
    best_score, best_reason, best_doc = scored[0]
    second_score = scored[1][0] if len(scored) > 1 else 0.0

    min_confidence = 0.42
    ambiguity_delta = 0.04

    if best_score < min_confidence:
        return MatchResult(None, best_score, f"low confidence: {best_reason}")

    if second_score >= min_confidence and (best_score - second_score) <= ambiguity_delta:
        return MatchResult(
            None,
            best_score,
            f"ambiguous: top={best_score:.3f}, second={second_score:.3f}",
        )

    used.add(best_doc.rel_path)
    return MatchResult(best_doc.rel_path, best_score, f"matched: {best_reason}")


def render_sidebar(root: SidebarNode, mapping: dict[str, MatchResult]) -> str:
    lines: list[str] = []

    def walk(node: SidebarNode, depth: int) -> None:
        indent = "  " * depth
        key = node.path_str()
        match = mapping.get(key)
        if match and match.matched_file:
            lines.append(f"{indent}- [{node.title}](/docs/{match.matched_file})")
        else:
            lines.append(f"{indent}- {node.title}")
        for child in node.children:
            walk(child, depth + 1)

    for child in root.children:
        walk(child, 0)

    return "\n".join(lines).rstrip() + "\n"


def write_missing(path: Path, mapping: dict[str, MatchResult]) -> None:
    missing_lines: list[str] = []
    for node_path in sorted(mapping.keys()):
        result = mapping[node_path]
        if result.matched_file is None:
            missing_lines.append(f"{node_path}\t{result.reason}")
    path.write_text("\n".join(missing_lines).rstrip() + ("\n" if missing_lines else ""), encoding="utf-8")


def write_mapping_json(path: Path, mapping: dict[str, MatchResult]) -> None:
    payload = {
        node_path: {
            "matched_file": result.matched_file,
            "confidence": round(result.confidence, 4),
            "reason": result.reason,
        }
        for node_path, result in sorted(mapping.items(), key=lambda x: x[0])
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def remove_ds_store(root: Path) -> int:
    count = 0
    for path in root.rglob(".DS_Store"):
        path.unlink(missing_ok=True)
        count += 1
    return count


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(1024 * 64)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def fix_shadow_txt_files(root: Path) -> list[str]:
    collisions: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        name = path.name
        if not (name.endswith(".html.txt") or name.endswith(".md.txt") or name.endswith(".json.txt")):
            continue

        target = path.with_name(name[:-4])
        if not target.exists():
            path.rename(target)
            continue

        if sha256(path) == sha256(target):
            path.unlink()
            continue

        collisions.append(f"collision kept: {path.relative_to(root)} -> {target.relative_to(root)}")

    return collisions


def ensure_required_root_files(root: Path) -> None:
    index = root / "index.html"
    if not index.exists():
        index.write_text(
            """<!DOCTYPE html>
<html lang=\"zh-Hant\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>ClawRouter Docs</title>
  <link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css\" />
</head>
<body>
  <div id=\"app\">Loading...</div>
  <script>
    window.$docsify = {
      name: 'ClawRouter Docs',
      loadSidebar: true,
      homepage: '/docs/_index.md',
      alias: {
        '/.*/_sidebar.md': '/docs/_sidebar.md'
      }
    };
  </script>
  <script src=\"https://cdn.jsdelivr.net/npm/docsify@4\"></script>
</body>
</html>
""",
            encoding="utf-8",
        )

    vercel = root / "vercel.json"
    if not vercel.exists():
        vercel.write_text(
            json.dumps(
                {
                    "cleanUrls": False,
                    "rewrites": [
                        {"source": "/", "destination": "/index.html"},
                        {"source": "/(.*)", "destination": "/index.html"},
                    ],
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )


def ensure_docs_index(docs_root: Path) -> None:
    idx = docs_root / "_index.md"
    if idx.exists():
        return
    idx.write_text(
        "# ClawRouter Docs\n\n文件已迁移，請使用 sidebar 瀏覽各 API。\n",
        encoding="utf-8",
    )


def main() -> None:
    if not DOCS_ROOT.exists():
        raise SystemExit("docs directory not found")
    if not SIDEBAR_SOURCE.exists():
        raise SystemExit("sidebar_source.txt not found")

    collisions = fix_shadow_txt_files(ROOT)
    removed_ds = remove_ds_store(ROOT)

    ensure_required_root_files(ROOT)
    ensure_docs_index(DOCS_ROOT)

    clean_changed = 0
    doc_files = sorted(DOCS_ROOT.rglob("*.md"))
    for path in doc_files:
        if path.name in GENERATED_DOC_FILES:
            continue
        if clean_file(path):
            clean_changed += 1

    sidebar_tree = parse_sidebar_source(SIDEBAR_SOURCE)
    leaves = iter_leaf_nodes(sidebar_tree)
    candidates = list_doc_candidates(DOCS_ROOT)

    mapping: dict[str, MatchResult] = {}
    used_files: set[str] = set()

    for node in leaves:
        key = node.path_str()
        mapping[key] = pick_mapping_for_node(node, candidates, used_files)

    sidebar_content = render_sidebar(sidebar_tree, mapping)
    (DOCS_ROOT / "_sidebar.md").write_text(sidebar_content, encoding="utf-8")
    write_missing(DOCS_ROOT / "_missing.txt", mapping)
    write_mapping_json(DOCS_ROOT / "_mapping.json", mapping)

    collision_file = DOCS_ROOT / "_rename_collisions.txt"
    if collisions:
        collision_file.write_text("\n".join(collisions) + "\n", encoding="utf-8")
    elif collision_file.exists():
        collision_file.unlink()

    print(f"Done. markdown cleaned: {clean_changed}")
    print(f"Done. sidebar leaves mapped: {sum(1 for v in mapping.values() if v.matched_file)} / {len(mapping)}")
    print(f"Done. removed .DS_Store: {removed_ds}")
    print(f"Done. rename collisions: {len(collisions)}")


if __name__ == "__main__":
    main()
