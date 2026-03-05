#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

OPENAPI_PATH = Path("openapi/generated/ai-model/音频（Audio）/post-v1beta-models-model-generatecontent-geminirelayv1beta-383836364-383836364.json")
TARGET_MD = Path("docs/ai-model/audio/gemini-native.md")
TARGET_PATH = "/v1beta/models/{model}:generateContent"
TARGET_METHOD = "post"


def resolve_json_pointer(doc: Any, ref: str) -> Any:
    if not ref.startswith("#/"):
        raise ValueError(f"Only local refs supported: {ref}")
    cur = doc
    for part in ref[2:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        cur = cur[part]
    return cur


def deref(obj: Any, doc: dict) -> Any:
    if isinstance(obj, dict):
        if "$ref" in obj:
            resolved = resolve_json_pointer(doc, obj["$ref"])
            return deref(resolved, doc)
        return {k: deref(v, doc) for k, v in obj.items()}
    if isinstance(obj, list):
        return [deref(v, doc) for v in obj]
    return obj


def type_of(schema: dict) -> str:
    if not isinstance(schema, dict):
        return "object"
    t = schema.get("type")
    if t == "array":
        item = deref(schema.get("items", {}), DOC)
        it = item.get("type", "object") if isinstance(item, dict) else "object"
        return f"array<{it}>"
    if t:
        return str(t)
    if "properties" in schema:
        return "object"
    return "object"


def flatten_schema(schema: dict, prefix: str = "", required: set[str] | None = None) -> list[tuple[str, str, str, str]]:
    rows: list[tuple[str, str, str, str]] = []
    schema = deref(schema, DOC)
    required = required or set(schema.get("required", []))

    props = schema.get("properties", {}) if isinstance(schema, dict) else {}
    for name, raw in props.items():
        s = deref(raw, DOC)
        full = f"{prefix}.{name}" if prefix else name
        t = type_of(s)
        desc = (s.get("description") or "").replace("\n", " ") if isinstance(s, dict) else ""
        req = "yes" if name in required else "no"

        if isinstance(s, dict) and s.get("type") == "array":
            full_arr = full + "[]"
            rows.append((full_arr, t, req, desc))
            item = deref(s.get("items", {}), DOC)
            if isinstance(item, dict) and (item.get("properties") or item.get("type") == "object"):
                child_required = set(item.get("required", []))
                rows.extend(flatten_schema(item, full_arr, child_required))
        elif isinstance(s, dict) and (s.get("properties") or s.get("type") == "object"):
            rows.append((full, t, req, desc))
            child_required = set(s.get("required", []))
            rows.extend(flatten_schema(s, full, child_required))
        else:
            rows.append((full, t, req, desc))
    return rows


def synth_example(schema: dict) -> Any:
    schema = deref(schema, DOC)
    if isinstance(schema, dict) and "example" in schema:
        return schema["example"]
    t = schema.get("type") if isinstance(schema, dict) else None
    if t == "string":
        return "string"
    if t in {"integer", "number"}:
        return 0
    if t == "boolean":
        return False
    if t == "array":
        item = deref(schema.get("items", {}), DOC)
        return [synth_example(item)]
    if t == "object" or (isinstance(schema, dict) and "properties" in schema):
        out = {}
        props = schema.get("properties", {}) if isinstance(schema, dict) else {}
        required = set(schema.get("required", [])) if isinstance(schema, dict) else set()
        keys = list(required) if required else list(props.keys())[:2]
        for k in keys:
            if k in props:
                out[k] = synth_example(deref(props[k], DOC))
        return out
    return {}


def pick_operation(doc: dict) -> tuple[str, dict]:
    paths = doc.get("paths", {})
    if TARGET_PATH in paths and TARGET_METHOD in paths[TARGET_PATH]:
        return TARGET_PATH, deref(paths[TARGET_PATH][TARGET_METHOD], doc)
    for p, item in paths.items():
        if not isinstance(item, dict):
            continue
        for m, op in item.items():
            if str(m).lower() != TARGET_METHOD:
                continue
            op_d = deref(op, doc)
            opid = str(op_d.get("operationId", "")).lower()
            if "generate" in opid and "content" in opid:
                return p, op_d
            if "generatecontent" in p.lower():
                return p, op_d
    raise RuntimeError("Target operation not found")


def md_table(rows: list[tuple[str, str, str, str]]) -> str:
    if not rows:
        return "_无_\n"
    out = ["| 字段 | 类型 | 必填 | 说明 |", "| --- | --- | --- | --- |"]
    for a, b, c, d in rows:
        d = d.replace("|", "\\|")
        out.append(f"| `{a}` | `{b}` | {c} | {d or '-'} |")
    return "\n".join(out) + "\n"


def render(doc: dict) -> str:
    path, op = pick_operation(doc)
    summary = op.get("summary") or "Gemini 音频生成接口"
    desc = op.get("description") or "可使用 Gemini 模型生成语音相关内容。"

    params = []
    for p in op.get("parameters", []):
        pp = deref(p, doc)
        sch = deref(pp.get("schema", {}), doc)
        params.append((pp.get("name", "-"), pp.get("in", "-"), type_of(sch), "yes" if pp.get("required") else "no", pp.get("description", "-")))

    req_body = op.get("requestBody", {})
    req_body = deref(req_body, doc) if req_body else {}
    req_content = req_body.get("content", {}) if isinstance(req_body, dict) else {}
    req_cts = list(req_content.keys())
    req_schema = {}
    req_example = None
    if req_cts:
        first = req_content[req_cts[0]]
        req_schema = deref(first.get("schema", {}), doc)
        req_example = first.get("example")
        if req_example is None and isinstance(first.get("examples"), dict) and first["examples"]:
            req_example = next(iter(first["examples"].values())).get("value")
        if req_example is None:
            req_example = synth_example(req_schema)

    responses = op.get("responses", {})
    success_code = "200" if "200" in responses else ("default" if "default" in responses else next(iter(responses.keys()), "200"))
    success = deref(responses.get(success_code, {}), doc)
    success_content = success.get("content", {}) if isinstance(success, dict) else {}
    success_schema = {}
    success_example = None
    s_ct = list(success_content.keys())
    if s_ct:
        first = success_content[s_ct[0]]
        success_schema = deref(first.get("schema", {}), doc)
        success_example = first.get("example")
        if success_example is None and isinstance(first.get("examples"), dict) and first["examples"]:
            success_example = next(iter(first["examples"].values())).get("value")
    if success_example is None:
        success_example = synth_example(success_schema)

    error_rows = []
    for code, payload in responses.items():
        if str(code).startswith("2") or code == success_code:
            continue
        pd = deref(payload, doc)
        error_rows.append((str(code), pd.get("description", "错误"), pd))

    sec = op.get("security") or []
    auth_line = "通过 Authorization / API Key（以平台说明为准）。"
    if sec:
        auth_line = "使用 Bearer Token（`Authorization: Bearer YOUR_API_KEY`）。"

    openapi_rel = Path("../../../") / OPENAPI_PATH

    md = []
    md.append("# 原生Gemini格式")
    md.append("")
    md.append(f"{summary}。")
    md.append(desc)
    md.append("")
    md.append("## Endpoint")
    md.append("")
    md.append(f"`POST {path}`")
    md.append("")
    md.append("## Authentication")
    md.append("")
    md.append(auth_line)
    md.append("")

    md.append("## Parameters")
    md.append("")
    if params:
        md.append("| 名称 | 位置 | 类型 | 必填 | 说明 |")
        md.append("| --- | --- | --- | --- | --- |")
        for n, loc, t, req, d in params:
            d = (d or "-").replace("|", "\\|")
            md.append(f"| `{n}` | `{loc}` | `{t}` | {req} | {d} |")
    else:
        md.append("_无_")
    md.append("")

    md.append("## Request Body")
    md.append("")
    if req_cts:
        md.append("Content-Type:")
        for ct in req_cts:
            md.append(f"- `{ct}`")
    else:
        md.append("Content-Type: `application/json`")
    md.append("")
    md.append(md_table(flatten_schema(req_schema)))

    md.append("### Minimal Request JSON")
    md.append("")
    md.append("```json")
    md.append(json.dumps(req_example, ensure_ascii=False, indent=2))
    md.append("```")
    md.append("")

    md.append("## Responses")
    md.append("")
    md.append(f"### {success_code}")
    md.append("")
    md.append(md_table(flatten_schema(success_schema)))

    md.append("### Minimal Response JSON")
    md.append("")
    md.append("```json")
    md.append(json.dumps(success_example, ensure_ascii=False, indent=2))
    md.append("```")
    md.append("")

    md.append("### Error Responses")
    md.append("")
    if error_rows:
        md.append("| 状态码 | 含义 |")
        md.append("| --- | --- |")
        for c, d, _ in error_rows:
            md.append(f"| `{c}` | {d} |")
    else:
        md.append("_无_")
    md.append("")

    md.append("## Examples")
    md.append("")
    md.append("```bash")
    md.append("curl -X POST \"")
    md.append("https://YOUR_BASE_URL/v1beta/models/gemini-2.5-flash-preview-tts:generateContent\" \\")
    md.append("  -H \"Authorization: Bearer YOUR_API_KEY\" \\")
    md.append("  -H \"Content-Type: application/json\" \\")
    md.append("  -d @- <<'JSON'")
    md.append(json.dumps(req_example, ensure_ascii=False, indent=2))
    md.append("JSON")
    md.append("```")
    md.append("")

    if error_rows:
        first_err = error_rows[0][2]
        econtent = first_err.get("content", {}) if isinstance(first_err, dict) else {}
        eexample = None
        if econtent:
            first = next(iter(econtent.values()))
            eexample = first.get("example")
            if eexample is None and isinstance(first.get("examples"), dict) and first["examples"]:
                eexample = next(iter(first["examples"].values())).get("value")
        if eexample is not None:
            md.append("### Error Example")
            md.append("")
            md.append("```json")
            md.append(json.dumps(eexample, ensure_ascii=False, indent=2))
            md.append("```")
            md.append("")

    md.append("## OpenAPI")
    md.append("")
    md.append(f"- [OpenAPI JSON]({openapi_rel.as_posix()})")
    md.append("")

    text = "\n".join(md)
    # extra safety: remove standalone method lines
    text = re.sub(r"(?m)^(GET|POST|PUT|DELETE)\s*$\n?", "", text)
    return text


def check_file(path: Path) -> int:
    txt = path.read_text(encoding="utf-8", errors="ignore")
    ok = True
    if not txt.startswith("# 原生Gemini格式\n"):
        print("CHECK FAIL: H1 mismatch")
        ok = False
    forbidden = ["<APIPage", "{/*", "*/}", "import ", "<Cards", "<Card", "<Callout"]
    for token in forbidden:
        if token in txt:
            print(f"CHECK FAIL: found token {token}")
            ok = False
    if re.search(r"(?m)^(GET|POST|PUT|DELETE)\s*$", txt):
        print("CHECK FAIL: standalone method line found")
        ok = False
    if ok:
        print("CHECK OK")
        return 0
    return 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    if args.check:
        raise SystemExit(check_file(TARGET_MD))

    DOC = json.loads(OPENAPI_PATH.read_text(encoding="utf-8"))
    out = render(DOC)
    TARGET_MD.write_text(out, encoding="utf-8")
    print(f"Wrote {TARGET_MD}")
