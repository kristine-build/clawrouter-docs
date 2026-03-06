#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

DOCS = Path("docs")
SUMMARY = DOCS / "SUMMARY.md"
MAPPING = DOCS / "_mapping.json"
MOVES = DOCS / "_restructure_moves.tsv"
OPENAPI_ROOT = Path("openapi/generated")

JSX_PAT = re.compile(r"<APIPage|^import\s+\{|\{/\*", re.M)
METHOD_PAT = re.compile(r"^(GET|POST|PUT|DELETE)\s*$", re.M)
CUR_DOC: dict[str, Any] = {}


@dataclass
class Node:
    title: str
    link: Optional[str]
    level: int
    parent: Optional["Node"] = None
    children: list["Node"] = field(default_factory=list)

    def crumbs(self) -> list[str]:
        cur: Optional[Node] = self
        out = []
        while cur and cur.parent is not None:
            out.append(cur.title)
            cur = cur.parent
        return list(reversed(out))


def norm(s: str) -> str:
    s = s.strip().lower().replace("（", "(").replace("）", ")")
    s = re.sub(r"\s*\((get|post|put|delete)\)\s*$", "", s, flags=re.I)
    s = re.sub(r"\s+", "", s)
    return s


def parse_summary(path: Path) -> tuple[Node, list[Node]]:
    root = Node("ROOT", None, -1)
    stack = [root]
    linked: list[Node] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        m_link = re.match(r"^(\s*)-\s+\[([^\]]+)\]\(([^)]+\.md)\)\s*$", raw)
        m_group = re.match(r"^(\s*)-\s+([^\[].+?)\s*$", raw)
        if not m_link and not m_group:
            continue
        if m_link:
            indent, title, link = m_link.groups()
        else:
            indent, title = m_group.groups()
            link = None
        level = len(indent) // 2
        while stack and stack[-1].level >= level:
            stack.pop()
        parent = stack[-1]
        n = Node(title, link, level, parent)
        parent.children.append(n)
        stack.append(n)
        if link:
            linked.append(n)
    return root, linked


def load_moves() -> dict[str, str]:
    mp: dict[str, str] = {}
    if not MOVES.exists():
        return mp
    lines = MOVES.read_text(encoding="utf-8", errors="ignore").splitlines()[1:]
    for ln in lines:
        if "\t" not in ln:
            continue
        s, d = ln.split("\t", 1)
        mp[s.strip()] = d.strip()
    return mp


def load_mapping_entries() -> list[tuple[list[str], str]]:
    out: list[tuple[list[str], str]] = []
    if not MAPPING.exists():
        return out
    data = json.loads(MAPPING.read_text(encoding="utf-8"))
    moves = load_moves()
    for k, v in data.items():
        if not isinstance(v, dict):
            continue
        mf = v.get("matched_file")
        if not mf:
            continue
        rel = moves.get(mf, "")
        if not rel:
            continue
        out.append(([p.strip() for p in k.split(">")], rel))
    return out


def collect_openapi_files() -> list[Path]:
    if not OPENAPI_ROOT.exists():
        return []
    return sorted(OPENAPI_ROOT.rglob("*.json"))


def find_operation(doc: dict) -> Optional[tuple[str, str, dict]]:
    paths = doc.get("paths", {}) if isinstance(doc, dict) else {}
    for p, item in paths.items():
        if not isinstance(item, dict):
            continue
        for m, op in item.items():
            if str(m).lower() not in {"get", "post", "put", "delete", "patch"}:
                continue
            if isinstance(op, dict):
                return p, str(m).upper(), op
    return None


def score_openapi_for_target(node: Node, rel_path: str, json_path: Path) -> float:
    txt = json_path.as_posix().lower()
    t = norm(node.title)
    score = 0.0
    rel_l = rel_path.lower()
    crumbs_l = " ".join(node.crumbs()).lower()

    if "audio" in rel_l and ("audio" in txt or "音频" in txt):
        score += 2.0
    if "audio" not in rel_l and ("audio" in txt or "音频" in txt):
        score -= 1.5

    if "gemini" in t and "gemini" in txt:
        score += 2.0
    if "openai" in t and "openai" in txt:
        score += 1.0
    if "audio" in t and "audio" in txt:
        score += 1.0
    if "音频" in crumbs_l and "音频" in txt:
        score += 1.0
    # title token match
    for token in re.split(r"[^a-z0-9\u4e00-\u9fff]+", t):
        if token and len(token) >= 2 and token in txt:
            score += 0.2

    try:
        doc = json.loads(json_path.read_text(encoding="utf-8"))
        op = find_operation(doc)
        if op:
            path, method, payload = op
            blob = (path + " " + method + " " + str(payload.get("summary", "")) + " " + str(payload.get("operationId", ""))).lower()
            if "gemini" in t and "gemini" in blob:
                score += 2.0
            if ("texttospeech" in t or "语音" in t) and ("speech" in blob or "audio" in blob):
                score += 1.0
    except Exception:
        pass
    return score


def choose_openapi_for_leaf(node: Node, rel_path: str, mapping_entries: list[tuple[list[str], str]], openapi_files: list[Path]) -> Optional[Path]:
    # 1) mapping hint by crumbs/title
    hint_rel = None
    ncrumbs = [norm(x) for x in node.crumbs()]
    best = -1
    for parts, rel in mapping_entries:
        nparts = [norm(x) for x in parts]
        score = 0
        k = min(len(ncrumbs), len(nparts))
        for i in range(1, k + 1):
            if ncrumbs[-i:] == nparts[-i:]:
                score = max(score, i * 2)
        if score > best:
            best = score
            hint_rel = rel

    # 2) choose json by fuzzy
    best_file = None
    best_score = -1.0
    for jf in openapi_files:
        s = score_openapi_for_target(node, rel_path, jf)
        if hint_rel:
            # if mapping hint has keyword tokens, boost
            h = hint_rel.lower()
            if any(tok in jf.as_posix().lower() for tok in re.split(r"[^a-z0-9]+", h) if tok):
                s += 0.5
        if s > best_score:
            best_score = s
            best_file = jf
    # Tight threshold to avoid copying wrong OpenAPI into unrelated pages.
    title_n = norm(node.title)
    if "gemini" in title_n and rel_path.startswith("ai-model/audio/") and best_score >= 3.0:
        return best_file
    if best_score >= 4.5:
        return best_file
    return None


def resolve_ref(doc: dict, obj: Any) -> Any:
    if isinstance(obj, dict):
        if "$ref" in obj:
            ref = obj["$ref"]
            if isinstance(ref, str) and ref.startswith("#/"):
                cur: Any = doc
                for p in ref[2:].split("/"):
                    p = p.replace("~1", "/").replace("~0", "~")
                    cur = cur[p]
                return resolve_ref(doc, cur)
        return {k: resolve_ref(doc, v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [resolve_ref(doc, x) for x in obj]
    return obj


def schema_type(s: dict) -> str:
    t = s.get("type") if isinstance(s, dict) else None
    if t == "array":
        it = resolve_ref(CUR_DOC, s.get("items", {})) if isinstance(s, dict) else {}
        return f"array<{it.get('type', 'object')}>"
    if t:
        return str(t)
    if isinstance(s, dict) and "properties" in s:
        return "object"
    return "object"


def flatten_schema(s: dict, prefix: str = "", req: set[str] | None = None) -> list[tuple[str, str, str, str, str, str, str]]:
    s = resolve_ref(CUR_DOC, s)
    req = req or set(s.get("required", []))
    rows: list[tuple[str, str, str, str, str, str, str]] = []
    for k, v in s.get("properties", {}).items():
        vv = resolve_ref(CUR_DOC, v)
        name = f"{prefix}.{k}" if prefix else k
        tp = schema_type(vv)
        required = "yes" if k in req else "no"
        desc = str(vv.get("description", "-")).replace("\n", " ")
        enum = ", ".join(map(str, vv.get("enum", []))) if isinstance(vv.get("enum"), list) else "-"
        default = str(vv.get("default", "-"))
        rng = "-"
        if "minimum" in vv or "maximum" in vv:
            rng = f"{vv.get('minimum', '')}..{vv.get('maximum', '')}".strip(".")
        if vv.get("type") == "array":
            arr = name + "[]"
            rows.append((arr, tp, required, desc, enum, default, rng))
            it = resolve_ref(CUR_DOC, vv.get("items", {}))
            if it.get("type") == "object" or "properties" in it:
                rows.extend(flatten_schema(it, arr, set(it.get("required", []))))
        elif vv.get("type") == "object" or "properties" in vv:
            rows.append((name, tp, required, desc, enum, default, rng))
            rows.extend(flatten_schema(vv, name, set(vv.get("required", []))))
        else:
            rows.append((name, tp, required, desc, enum, default, rng))
    return rows


def minimal_example(schema: dict) -> Any:
    s = resolve_ref(CUR_DOC, schema)
    if "example" in s:
        return s["example"]
    t = s.get("type")
    if t == "string":
        return "string"
    if t in {"integer", "number"}:
        return 0
    if t == "boolean":
        return False
    if t == "array":
        return [minimal_example(resolve_ref(CUR_DOC, s.get("items", {})))]
    if t == "object" or "properties" in s:
        out = {}
        required = s.get("required", [])
        keys = required if required else list(s.get("properties", {}).keys())[:2]
        for k in keys:
            out[k] = minimal_example(resolve_ref(CUR_DOC, s["properties"][k]))
        return out
    return {}


def clean_text_md(txt: str, title: str) -> str:
    txt = re.sub(r"(?m)^import\s+.*$\n?", "", txt)
    txt = re.sub(r"\{\/\*[\s\S]*?\*\/\}", "", txt)
    txt = re.sub(r"<APIPage[\s\S]*?/>", "", txt)
    txt = re.sub(r"<Cards[\s\S]*?</Cards>", "", txt)
    txt = re.sub(r"<Callout[\s\S]*?</Callout>", "", txt)
    lines = []
    skip_openapi = False
    for ln in txt.splitlines():
        s = ln.strip()
        if re.match(r"^##\s*OpenAPI\b", s, flags=re.I) or "OpenAPI JSON" in s or "OpenAPI.JSON" in s:
            skip_openapi = True
            continue
        if skip_openapi and s.startswith("#"):
            skip_openapi = False
        if skip_openapi:
            continue
        if METHOD_PAT.match(s):
            continue
        lines.append(ln)
    # Drop only the existing first H1 and nearby blank lines, keep lower-level headings.
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and re.match(r"^#\s+", lines[0]):
        lines.pop(0)
    while lines and not lines[0].strip():
        lines.pop(0)
    body = "\n".join(lines).strip()
    return f"# {title}\n\n{body}\n" if body else f"# {title}\n"


def render_endpoint_md(node: Node, doc: dict) -> str:
    op_info = find_operation(doc)
    if not op_info:
        return ""
    path, method, op = op_info
    op = resolve_ref(doc, op)

    summary = op.get("summary") or node.title
    desc = op.get("description", "")

    params = []
    for p in op.get("parameters", []):
        pp = resolve_ref(doc, p)
        sch = resolve_ref(doc, pp.get("schema", {}))
        params.append((pp.get("name", "-"), schema_type(sch), "yes" if pp.get("required") else "no", pp.get("description", "-"), pp.get("in", "-")))

    # auth
    auth_lines = ["通过 Authorization / API Key（以平台说明为准）。"]
    if op.get("security"):
        auth_lines = ["使用 BearerAuth。", "示例请求头：`Authorization: Bearer YOUR_API_KEY`"]

    # request
    req_schema = {}
    req_example = None
    req_content = resolve_ref(doc, op.get("requestBody", {})).get("content", {}) if op.get("requestBody") else {}
    if req_content:
        first_ct = next(iter(req_content.keys()))
        entry = resolve_ref(doc, req_content[first_ct])
        req_schema = resolve_ref(doc, entry.get("schema", {}))
        if entry.get("example") is not None:
            req_example = entry.get("example")
        elif isinstance(entry.get("examples"), dict) and entry["examples"]:
            req_example = next(iter(entry["examples"].values())).get("value")
        else:
            req_example = minimal_example(req_schema)
    else:
        first_ct = "application/json"

    # responses
    responses = op.get("responses", {})
    ok_code = "200" if "200" in responses else next(iter(responses.keys()), "200")
    ok = resolve_ref(doc, responses.get(ok_code, {})) if responses else {}
    ok_schema = {}
    ok_example = None
    if isinstance(ok, dict):
        c = ok.get("content", {})
        if c:
            ct = next(iter(c.keys()))
            centry = resolve_ref(doc, c[ct])
            ok_schema = resolve_ref(doc, centry.get("schema", {}))
            ok_example = centry.get("example")
            if ok_example is None and isinstance(centry.get("examples"), dict) and centry["examples"]:
                ok_example = next(iter(centry["examples"].values())).get("value")
    if ok_example is None and ok_schema:
        ok_example = minimal_example(ok_schema)

    err_rows = []
    for code, payload in responses.items():
        if str(code).startswith("2"):
            continue
        pd = resolve_ref(doc, payload)
        err_rows.append((str(code), pd.get("description", "错误")))

    out = [f"# {node.title}", "", summary + ("。" if not str(summary).endswith("。") else "")]
    if desc:
        out += ["", desc]
    out += ["", "## Endpoint", "", f"`{method} {path}`", "", "## Authorization", ""]
    out += auth_lines + [""]

    out += ["## Request Body", "", f"Content-Type: `{first_ct}`", ""]
    rows = flatten_schema(req_schema) if req_schema else []
    out += ["| name | type | required | description | enum | default | range |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        out.append(f"| `{r[0]}` | `{r[1]}` | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} |")
    if not rows:
        out.append("| - | - | - | - | - | - | - |")

    out += ["", "## Response Body", "", f"### {ok_code}", ""]
    ok_rows = flatten_schema(ok_schema) if ok_schema else []
    out += ["| name | type | required | description | enum | default | range |", "|---|---|---|---|---|---|---|"]
    for r in ok_rows:
        out.append(f"| `{r[0]}` | `{r[1]}` | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} |")
    if not ok_rows:
        out.append("| - | - | - | - | - | - | - |")

    out += ["", "```json", json.dumps(ok_example if ok_example is not None else {}, ensure_ascii=False, indent=2), "```", ""]

    out += ["### 4xx/5xx", "", "| status | meaning |", "|---|---|"]
    for c, d in err_rows:
        out.append(f"| `{c}` | {d} |")
    if not err_rows:
        out.append("| - | - |")

    req_ex = req_example if req_example is not None else {}
    out += ["", "## Code Examples", "", "### cURL", "", "```bash"]
    out += [
        f"curl -X {method} \"https://docs.newapi.pro{path.replace('{model}', 'gemini-2.5-flash-preview-tts')}\" \\",
        "  -H \"Authorization: Bearer YOUR_API_KEY\" \\",
        "  -H \"Content-Type: application/json\" \\",
        f"  -d '{json.dumps(req_ex, ensure_ascii=False)}'",
    ]
    out += ["```", "", "### Python requests", "", "```python"]
    out += [
        "import requests",
        f"url = \"https://docs.newapi.pro{path.replace('{model}', 'gemini-2.5-flash-preview-tts')}\"",
        "headers = {",
        "    \"Authorization\": \"Bearer YOUR_API_KEY\",",
        "    \"Content-Type\": \"application/json\"",
        "}",
        f"payload = {json.dumps(req_ex, ensure_ascii=False, indent=4)}",
        "resp = requests.request(\"" + method + "\", url, headers=headers, json=payload, timeout=30)",
        "print(resp.status_code)",
        "print(resp.text)",
    ]
    out += ["```", ""]

    text = "\n".join(out)
    text = re.sub(r"(?m)^(GET|POST|PUT|DELETE)\s*$\n?", "", text)
    text = re.sub(r"(?m)^##\s*OpenAPI\b[\s\S]*$", "", text)
    return text


def rel_link(from_rel: str, to_rel: str) -> str:
    return Path(os.path.relpath((DOCS / to_rel).as_posix(), (DOCS / from_rel).parent.as_posix())).as_posix()


def write_readme_page(node: Node) -> None:
    assert node.link and node.link.endswith("README.md")
    p = DOCS / node.link
    p.parent.mkdir(parents=True, exist_ok=True)

    if node.link == "README.md":
        ai = next((c for c in node.children if c.title == "AI 模型接口"), None)
        mgmt = next((c for c in node.children if c.title == "管理接口"), None)
        lines = [
            "# API 参考",
            "",
            "## 概述",
            "",
            "New API 提供完整的 RESTful API 接口，分为 **AI 模型接口** 和 **管理接口** 两大类。您可以通过这些接口实现 AI 能力调用和系统管理功能。",
            "",
            "## AI 模型接口",
            "",
        ]
        ai_desc = {
            "音频（Audio）": "语音识别和语音合成接口。",
            "聊天（Chat）": "对话补全接口。",
            "补全（Completions）": "传统文本补全接口。",
            "嵌入（Embeddings）": "文本嵌入向量生成接口。",
            "图像（Images）": "AI 图像生成接口。",
            "模型（Models）": "模型查询与管理接口。",
            "审查（Moderations）": "内容安全审核接口。",
            "实时语音（Realtime）": "实时音频流接口。",
            "重排序（Rerank）": "文档重排序接口。",
            "未实现（Unimplemented）": "占位接口，暂未实现。",
            "微调（Fine-tuning）": "模型微调相关接口。",
            "视频（Videos）": "AI 视频生成接口。",
        }
        if ai:
            for c in ai.children:
                if c.link:
                    lines.append(f"- [{c.title}]({c.link})：{ai_desc.get(c.title, 'API 接口文档。')}")

        lines += ["", "## 管理接口", ""]
        mg_desc = {
            "鉴权体系说明（Auth）": "鉴权体系说明。",
            "渠道管理": "API 渠道配置管理接口。",
            "default": "默认功能接口。",
            "分组": "用户分组管理接口。",
            "日志": "使用日志查询接口。",
            "模型管理": "模型配置管理接口。",
            "OAuth": "第三方 OAuth 登录接口。",
            "充值": "支付与充值接口。",
            "兑换码": "兑换码管理接口。",
            "安全验证": "安全验证相关接口。",
            "数据统计": "数据统计接口。",
            "系统": "系统信息和状态接口。",
            "系统设置": "系统配置管理接口。",
            "任务": "异步任务管理接口。",
            "令牌管理": "API 令牌管理接口。",
            "两步验证": "2FA 双因素认证接口。",
            "用户登陆注册": "用户登录、注册、密码管理接口。",
            "用户管理": "用户信息管理接口。",
            "供应商": "供应商管理接口。",
        }
        if mgmt:
            for c in mgmt.children:
                if c.link:
                    lines.append(f"- [{c.title}]({c.link})：{mg_desc.get(c.title, '管理接口文档。')}")
        lines += [
            "",
            "**Next：** [原生Gemini格式](ai-model/audio/gemini-native.md)",
        ]
        p.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        return

    lines = [f"# {node.title}", "", f"{node.title} 文档导航。", "", "## 本章内容", ""]

    if node.link == "ai-model/README.md":
        lines.append("- 👉 从这里开始：[原生Gemini格式](./audio/gemini-native.md)")
    if node.link == "ai-model/audio/README.md":
        lines.append("- 👉 从这里开始：[原生Gemini格式](./gemini-native.md)")

    for c in node.children:
        target = c.link
        if not target:
            # first descendant
            stack = [c]
            target = None
            while stack:
                cur = stack.pop(0)
                if cur.link:
                    target = cur.link
                    break
                stack.extend(cur.children)
        if target:
            lines.append(f"- [{c.title}]({rel_link(node.link, target)})")

    p.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def cleanup_file(path: Path, title: str) -> None:
    txt = path.read_text(encoding="utf-8", errors="ignore")
    txt = clean_text_md(txt, title)
    path.write_text(txt, encoding="utf-8")


def run_render(only_prefix: str | None) -> int:
    root, linked = parse_summary(SUMMARY)
    mapping_entries = load_mapping_entries()
    openapi_files = collect_openapi_files()

    fetched_ok = 0
    skipped = 0
    failed = 0
    unresolved: list[tuple[str, str]] = []

    for n in linked:
        rel = n.link or ""
        if only_prefix and not rel.startswith(only_prefix):
            continue

        path = DOCS / rel
        path.parent.mkdir(parents=True, exist_ok=True)

        if rel.endswith("README.md"):
            write_readme_page(n)
            continue

        jf = choose_openapi_for_leaf(n, rel, mapping_entries, openapi_files)
        if not jf:
            # keep existing if cannot resolve
            if path.exists():
                cleanup_file(path, n.title)
                skipped += 1
            else:
                failed += 1
                unresolved.append((rel, "no openapi match and file missing"))
            continue

        try:
            doc = json.loads(jf.read_text(encoding="utf-8"))
            global CUR_DOC
            CUR_DOC = doc
            md = render_endpoint_md(n, doc)
            if not md.strip():
                raise RuntimeError("render empty")
            path.write_text(md, encoding="utf-8")
            fetched_ok += 1
        except Exception as e:
            if path.exists():
                cleanup_file(path, n.title)
                skipped += 1
            else:
                failed += 1
                unresolved.append((rel, f"render error: {e}"))

    # cleanup pass for processed scope
    for n in linked:
        rel = n.link or ""
        if only_prefix and not rel.startswith(only_prefix):
            continue
        p = DOCS / rel
        if p.exists():
            cleanup_file(p, n.title)

    print(f"total targets: {len(linked)}")
    print(f"fetched ok: {fetched_ok}")
    print(f"skipped: {skipped}")
    print(f"failed: {failed}")
    if unresolved:
        print("unresolved:")
        for rel, reason in unresolved[:20]:
            print(f"- {rel}: {reason}")
    return 0


def run_check() -> int:
    _, linked = parse_summary(SUMMARY)
    errs: list[str] = []
    for n in linked:
        p = DOCS / (n.link or "")
        if not p.exists():
            errs.append(f"missing: {n.link}")
            continue
        txt = p.read_text(encoding="utf-8", errors="ignore")
        non_empty = [ln for ln in txt.splitlines() if ln.strip()]
        if not non_empty:
            errs.append(f"empty: {n.link}")
            continue
        if not non_empty[0].startswith("# "):
            errs.append(f"first line not H1: {n.link}")
        if JSX_PAT.search(txt):
            errs.append(f"jsx residue: {n.link}")
        if METHOD_PAT.search(txt):
            errs.append(f"standalone method line: {n.link}")

    if errs:
        print("CHECK FAILED")
        for e in errs[:50]:
            print("-", e)
        return 1
    print("CHECK OK")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--only", default=None)
    args = ap.parse_args()

    if args.check:
        return run_check()
    return run_render(args.only)


if __name__ == "__main__":
    raise SystemExit(main())
