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
INLINE_COLLAPSED_TOKENS = re.compile(r"cURLJavaScriptGoPythonJavaC#")
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


def sample_value_for_name(name: str, schema: dict | None = None) -> Any:
    lname = name.lower().strip()
    if lname == "file":
        return "@/path/to/audio.mp3"
    if lname in {"input", "prompt"}:
        return "请用中文朗读今天的新闻摘要"
    if lname in {"model", "pathmodel"}:
        return "whisper-1"
    if lname == "voice":
        return "alloy"
    if lname == "response_format":
        return "json"
    if lname == "language":
        return "zh"
    if lname == "temperature":
        return 1
    if lname == "speed":
        return 1
    if schema is not None:
        if "enum" in schema and schema["enum"]:
            return schema["enum"][0]
        if schema.get("type") == "array":
            item_type = (schema.get("items") or {}).get("type", "string")
            return [sample_value_for_name(item_type)]
        if schema.get("type") in {"number", "integer"}:
            return 0
        if schema.get("type") == "boolean":
            return False
    return "string"


def guess_request_payload(content_type: str, req_schema: dict, req_example: Any | None) -> tuple[str, dict[str, Any]]:
    if isinstance(req_example, dict) and req_example:
        return content_type, dict(req_example)

    payload: dict[str, Any] = {}
    if isinstance(req_schema, dict):
        for k, v in req_schema.get("properties", {}).items():
            payload[str(k)] = sample_value_for_name(str(k), resolve_ref(CUR_DOC, v))
    if not payload:
        if "multipart/form-data" in content_type.lower():
            payload = {"file": "@/path/to/audio.mp3", "model": "whisper-1"}
        else:
            payload = {"model": "tts-1", "input": sample_value_for_name("input")}
    return content_type, payload


def _fmt_json_for_block(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2)


def _go_literal(payload_json: str) -> str:
    return payload_json.replace("\n", "")


def _java_literal(payload_json: str) -> str:
    return payload_json.replace('\\', '\\\\').replace('"', '\\"').replace("\n", "")


def _csharp_literal(payload_json: str) -> str:
    return payload_json.replace('"', '""').replace("\n", "")


def _js_value(val: Any) -> str:
    if isinstance(val, str) and val.startswith("@"):
        return f'"{val[1:]}"'
    return json.dumps(val, ensure_ascii=False)


def render_code_examples(method: str, path: str, content_type: str, request_payload: dict[str, Any], endpoint_params: list[tuple[str, str]]) -> str:
    method = method.upper()
    url = f"https://docs.newapi.pro{path}"
    for k, v in endpoint_params:
        url = url.replace(f"{{{k}}}", str(v))

    is_multipart = "multipart/form-data" in content_type.lower()
    payload_json = _fmt_json_for_block(request_payload)

    if is_multipart:
        curl_lines = [
            f"curl -X {method} \"{url}\" \\",
            "  -H \"Authorization: Bearer YOUR_API_KEY\" \\",
        ]
        for k, v in request_payload.items():
            if str(v).startswith("@"):
                curl_lines.append(f"  -F \"{k}=@{v[1:]}\" \\")
            else:
                curl_lines.append(f"  -F \"{k}={v}\" \\")
        if curl_lines:
            curl_lines[-1] = curl_lines[-1].rstrip(" \\")

        js_lines = ["const formData = new FormData();"]
        for k, v in request_payload.items():
            if str(v).startswith("@"):
                js_lines.append(f'formData.append("{k}", fileInput.files[0]);')
            else:
                js_lines.append(f'formData.append("{k}", {_js_value(v)});')
        js_lines += [
            f"const response = await fetch(\"{url}\", {{",
            f'  method: "{method}",',
            '  headers: {',
            '    "Authorization": "Bearer YOUR_API_KEY"',
            "  },",
            "  body: formData",
            "});",
            "const text = await response.text();",
            "console.log(text);",
        ]

        python_lines = [
            "import requests",
            f'url = "{url}"',
            'headers = {"Authorization": "Bearer YOUR_API_KEY"}',
            "files = {}",
            "data = {}",
        ]
        for k, v in request_payload.items():
            if str(v).startswith("@"):
                python_lines.append(f'files["{k}"] = open("{v[1:]}", "rb")')
            else:
                python_lines.append(f'data["{k}"] = "{v}"')
        python_lines += [
            "resp = requests.post(url, headers=headers, files=files, data=data, timeout=30)",
            "print(resp.status_code)",
            "print(resp.text)",
        ]

        go_lines = [
            "package main",
            "",
            "import (",
            '\t\"bytes\"',
            '\t\"io\"',
            '\t\"mime/multipart\"',
            '\t\"net/http\"',
            '\t\"os\"',
            ")",
            "",
            "func main() {",
            "\tvar buf bytes.Buffer",
            "\twriter := multipart.NewWriter(&buf)",
            '\t_ = writer.WriteField(\"model\", \"whisper-1\")',
            '\tfile, _ := os.Open(\"audio.mp3\")',
            "\tdefer file.Close()",
            '\tpart, _ := writer.CreateFormFile(\"file\", \"audio.mp3\")',
            "\t_, _ = io.Copy(part, file)",
            "\t_ = writer.Close()",
            f'\treq, _ := http.NewRequest("{method}", "{url}", &buf)',
            '\treq.Header.Set("Authorization", "Bearer YOUR_API_KEY")',
            '\treq.Header.Set("Content-Type", writer.FormDataContentType())',
            "\thttp.DefaultClient.Do(req)",
            "}",
        ]

        java_lines = [
            "HttpClient client = HttpClient.newHttpClient();",
            "HttpRequest request = HttpRequest.newBuilder()",
            f'    .uri(URI.create("{url}"))',
            '    .header("Authorization", "Bearer YOUR_API_KEY")',
            "    .POST(HttpRequest.BodyPublishers.noBody())",
            "    .build();",
            "HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());",
            "System.out.println(response.statusCode());",
            "System.out.println(response.body());",
        ]

        csharp_lines = [
            'var client = new HttpClient();',
            'client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", "YOUR_API_KEY");',
            'var form = new MultipartFormDataContent();',
            '\tform.Add(new StringContent("whisper-1"), "model");',
            '\tform.Add(new ByteArrayContent(File.ReadAllBytes("audio.mp3")), "file", "audio.mp3");',
            f'var request = new HttpRequestMessage(HttpMethod.{method.title()}, "{url}") {{',
            "\tContent = form",
            "};",
            "var response = await client.SendAsync(request);",
            "Console.WriteLine((int)response.StatusCode);",
            "Console.WriteLine(await response.Content.ReadAsStringAsync());",
        ]
    else:
        curl_lines = [
            f"curl -X {method} \"{url}\" \\",
            "  -H \"Authorization: Bearer YOUR_API_KEY\" \\",
            '  -H "Content-Type: application/json" \\',
            f"  -d '{payload_json.replace(chr(10), ' ')}'",
        ]
        js_lines = [
            "const payload = " + payload_json + ";",
            f'const response = await fetch("{url}", {{',
            f'  method: "{method}",',
            '  headers: {',
            '    "Authorization": "Bearer YOUR_API_KEY",',
            '    "Content-Type": "application/json"',
            "  },",
            "  body: JSON.stringify(payload),",
            "});",
            "console.log(await response.text());",
        ]
        python_lines = [
            "import requests",
            f'url = "{url}"',
            "headers = {",
            '    "Authorization": "Bearer YOUR_API_KEY",',
            '    "Content-Type": "application/json",',
            "}",
            f"payload = {payload_json}",
            f"resp = requests.request(\"{method}\", url, headers=headers, json=payload, timeout=30)",
            "print(resp.status_code)",
            "print(resp.text)",
        ]
        go_lines = [
            "package main",
            "",
            "import (",
            '\t"bytes"',
            '\t"encoding/json"',
            '\t\"net/http\"',
            ")",
            "",
            "func main() {",
            f"\tpayloadJSON := `{_go_literal(payload_json)}`",
            "\tvar payload map[string]interface{}",
            "\t_ = json.Unmarshal([]byte(payloadJSON), &payload)",
            "\tdata, _ := json.Marshal(payload)",
            f'\treq, _ := http.NewRequest("{method}", "{url}", bytes.NewReader(data))',
            '\treq.Header.Set("Authorization", "Bearer YOUR_API_KEY")',
            '\treq.Header.Set("Content-Type", "application/json")',
            "\thttp.DefaultClient.Do(req)",
            "}",
        ]
        java_lines = [
            "HttpClient client = HttpClient.newHttpClient();",
            f'    String json = "{_java_literal(payload_json)}";',
            "HttpRequest request = HttpRequest.newBuilder()",
            f'    .uri(URI.create("{url}"))',
            '    .header("Authorization", "Bearer YOUR_API_KEY")',
            '    .header("Content-Type", "application/json")',
            "    .POST(HttpRequest.BodyPublishers.ofString(json))",
            "    .build();",
            "HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());",
            "System.out.println(response.statusCode());",
            "System.out.println(response.body());",
        ]
        csharp_lines = [
            'var client = new HttpClient();',
            'client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", "YOUR_API_KEY");',
            f'var payload = new StringContent(@"{_csharp_literal(payload_json)}", Encoding.UTF8, "application/json");',
            f'var request = new HttpRequestMessage(HttpMethod.{method.title()}, "{url}") {{',
            "\tContent = payload",
            "};",
            "var response = await client.SendAsync(request);",
            "Console.WriteLine((int)response.StatusCode);",
            "Console.WriteLine(await response.Content.ReadAsStringAsync());",
        ]

    out = [
        "",
        "## Code Examples",
        "",
        "### cURL",
        "",
        "```bash",
        *curl_lines,
        "```",
        "",
        "### JavaScript",
        "",
        "```javascript",
        *js_lines,
        "```",
        "",
        "### Go",
        "",
        "```go",
        *go_lines,
        "```",
        "",
        "### Python",
        "",
        "```python",
        *python_lines,
        "```",
        "",
        "### Java",
        "",
        "```java",
        *java_lines,
        "```",
        "",
        "### C#",
        "",
        "```csharp",
        *csharp_lines,
        "```",
    ]
    return "\n".join(out)




def clean_text_md(txt: str, title: str) -> str:
    txt = re.sub(r"(?m)^import\s+.*$\n?", "", txt)
    txt = re.sub(r"\{\/\*[\s\S]*?\*\/\}", "", txt)
    txt = re.sub(r"<APIPage[\s\S]*?/>", "", txt)
    txt = re.sub(r"<Cards[\s\S]*?</Cards>", "", txt)
    txt = re.sub(r"<Callout[\s\S]*?</Callout>", "", txt)
    txt = INLINE_COLLAPSED_TOKENS.sub(" ", txt)
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
        if s in {"loading...", "loading…", "loading"}:
            continue
        if s == "Send":
            continue
        if METHOD_PAT.match(s):
            continue
        if re.match(r"^\S+\*\S+$", s):
            # remove collapsed schema rows like model*string / messages*array<object>
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


def extract_endpoint_signature(txt: str) -> tuple[str, str, str]:
    method = "POST"
    path = "/"
    content_type = "application/json"
    flat = txt.lower().replace("**", "")
    for ln in txt.splitlines():
        s = ln.replace("**", "").replace("`", "")
        m = re.search(r"\b(GET|POST|PUT|DELETE)\s+(/[^\s]+)", s, flags=re.I)
        if m:
            method = m.group(1).upper()
            path = m.group(2)
            break
    if path == "/":
        s = txt.replace("`", "")
        m = re.search(r"(/v\d+/[\w./-]+)", s)
        if not m:
            m = re.search(r"(/v[^\s\]]+)", s)
        if m:
            path = m.group(1)
    if "multipart/form-data" in txt.lower() or " -f " in txt.lower() or " -F " in txt:
        content_type = "multipart/form-data"
    return method, path, content_type


def extract_json_examples(txt: str) -> Optional[Any]:
    if "```json" not in txt:
        return None
    inside = False
    buf = []
    for ln in txt.splitlines():
        if ln.strip().startswith("```json"):
            inside = True
            buf = []
            continue
        if inside:
            if ln.strip().startswith("```"):
                break
            buf.append(ln)
    if not buf:
        return None
    try:
        return json.loads("\n".join(buf))
    except Exception:
        return None


def replace_or_append_code_examples(txt: str, section: str) -> str:
    lines = txt.splitlines()
    original_lines = list(lines)
    start = None
    end = len(lines)
    for i, ln in enumerate(lines):
        if ln.startswith("## Code Examples"):
            start = i
            break
    if start is not None:
        for j in range(start + 1, len(lines)):
            if lines[j].startswith("## "):
                end = j
                break
        before = original_lines[:start]
        after = original_lines[end:] if end > start + 1 else []
        lines = before + [""] + section.strip().splitlines() + after
    else:
        lines.extend(["", section.rstrip()])
    return "\n".join(lines).rstrip() + "\n"


def strip_inline_language_blocks(txt: str) -> str:
    # remove old broken standalone examples so we can inject clean multi-language examples
    txt = txt.replace("cURLJavaScriptGoPythonJavaC#", "")
    txt = txt.replace("### Python requests", "### Python")
    lines = txt.splitlines()
    out: list[str] = []
    i = 0
    lang_heads = {"### cURL", "### JavaScript", "### Python", "### Go", "### Java", "### C#", "### Python requests"}
    while i < len(lines):
        ln = lines[i]
        if any(ln.startswith(x) for x in lang_heads):
            i += 1
            if i < len(lines) and lines[i].startswith("```"):
                fence = lines[i].strip()
                i += 1
                while i < len(lines) and lines[i].strip() != fence:
                    i += 1
                if i < len(lines):
                    i += 1
            else:
                while i < len(lines) and not lines[i].startswith("### "):
                    i += 1
            continue
            out.append(ln)
        i += 1
    return "\n".join(out)


def render_param_section(params: list[tuple[str, str, str, str, str]], loc: str) -> list[str]:
    rows = [p for p in params if p[4] == loc]
    if not rows:
        return []
    out = [f"## {loc.title()} Parameters", "", "| Name | Type | Required | Description |", "| --- | --- | --- | --- |"]
    for name, typ, req, desc, _ in rows:
        out.append(f"| `{name}` | `{typ}` | {req} | {desc} |")
    return out + [""]


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

    for loc in ("path", "query", "header"):
        out.extend(render_param_section(params, loc))

    out += ["## Request Body", "", f"Content-Type: `{first_ct}`", ""]
    rows = flatten_schema(req_schema) if req_schema else []
    out += ["| name | type | required | description | enum | default | range |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        out.append(f"| `{r[0]}` | `{r[1]}` | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} |")
    if not rows:
        out.append("| - | - | - | - | - | - | - |")
    out += ["", "## Response Body", ""]
    for code, payload in responses.items():
        pd = resolve_ref(doc, payload)
        desc = pd.get("description", "").strip()
        cts = pd.get("content", {})
        ct = next(iter(cts.keys()), "application/json")
        centry = resolve_ref(doc, cts[ct]) if ct else {}
        rs = resolve_ref(centry, centry.get("schema", {}))
        rex = centry.get("example")
        if rex is None and isinstance(centry.get("examples"), dict) and centry["examples"]:
            rex = next(iter(centry["examples"].values())).get("value")
        if rex is None and rs:
            rex = minimal_example(rs)

        out += [f"### {code} {ct}", ""]
        if desc:
            out.append(desc)
            out.append("")
        rs_rows = flatten_schema(rs) if rs else []
        out += ["| name | type | required | description | enum | default | range |", "|---|---|---|---|---|---|---|"]
        for r in rs_rows:
            out.append(f"| `{r[0]}` | `{r[1]}` | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} |")
        if not rs_rows:
            out.append("| - | - | - | - | - | - | - |")
        out += ["", "```json", json.dumps(rex if rex is not None else {}, ensure_ascii=False, indent=2), "```", ""]

    if err_rows:
        out += ["### 4xx/5xx", "", "| status | meaning |", "|---|---|"]
        for c, d in err_rows:
            out.append(f"| `{c}` | {d} |")
        out.append("")

    path_params = [(name, loc) for (name, _type, _required, _desc, loc) in params if loc == "path"]
    content_type, req_payload = guess_request_payload(first_ct, req_schema, req_example)
    out.append(render_code_examples(method, path, content_type, req_payload, path_params))

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
                raw = path.read_text(encoding="utf-8")
                cleaned = strip_inline_language_blocks(clean_text_md(raw, n.title))
                method, ep_path, ct = extract_endpoint_signature(cleaned)
                req_example = extract_json_examples(cleaned)
                ct, payload = guess_request_payload(ct, {}, req_example if isinstance(req_example, dict) else None)
                extra = render_code_examples(method, ep_path, ct, payload, [])
                cleaned = replace_or_append_code_examples(cleaned, extra)
                path.write_text(cleaned, encoding="utf-8")
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
