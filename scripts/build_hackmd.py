#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = ROOT / "hackmd_api_docs.md"

IGNORE_BASENAMES = {"_sidebar.md", "_index.md"}
IGNORE_EXACT = {
    "_sidebar.md",
    "_index.md",
    "_mapping.json",
    "_missing.txt",
}


def readable(text: str) -> str:
    text = text.strip()
    text = re.sub(r"-new-api$", "", text)
    text = re.sub(r"-未实现$", "", text)
    text = text.replace("_", " ")
    text = text.replace("-", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text or "Untitled"


def category_priority(rel: Path) -> tuple[int, str]:
    top = rel.parts[0] if rel.parts else ""
    if top == "ai-model":
        return (0, rel.as_posix())
    if top == "management":
        return (1, rel.as_posix())
    return (2, rel.as_posix())


def iter_docs_files() -> list[Path]:
    files: list[Path] = []
    for path in DOCS.rglob("*.md"):
        rel = path.relative_to(DOCS)
        if rel.as_posix() in IGNORE_EXACT:
            continue
        if path.name in IGNORE_BASENAMES:
            continue
        files.append(path)
    files.sort(key=lambda p: category_priority(p.relative_to(DOCS)))
    return files


def remove_frontmatter(lines: list[str]) -> list[str]:
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].strip() == "---":
        j = i + 1
        while j < len(lines) and lines[j].strip() != "---":
            j += 1
        if j < len(lines):
            return lines[j + 1 :]
    return lines


def clean_content(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = remove_frontmatter(text.split("\n"))

    in_fence = False
    fence_marker = "```"
    out: list[str] = []

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = "```" if stripped.startswith("```") else "~~~"
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
            out.append(line)
            continue

        if in_fence:
            out.append(line)
            continue

        if stripped.startswith("# "):
            continue

        if re.match(r"^>\s*(Migrated from|Auto-generated).*$", stripped, re.IGNORECASE):
            continue

        if re.match(r"^\s*[-*]\s*\[[^\]]+\]\((?!https?://)(?!#)[^)]+\)\s*$", line):
            continue
        if re.match(r"^\s*\[[^\]]+\]\((?!https?://)(?!#)[^)]+\)\s*$", line):
            continue
        if re.search(r"\]\(/?docs/[^)]+\)", line):
            continue

        if stripped in {"复制 Markdown打开", "这篇文档对您有帮助吗？", "有帮助没帮助", "最后更新于"}:
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            level = len(heading.group(1))
            title = heading.group(2)
            if level > 4:
                level = 4
            out.append(f"{'#' * level} {title}")
            continue

        out.append(line)

    cleaned = "\n".join(out)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    return cleaned


def section_titles(rel: Path) -> tuple[str, str, str]:
    parts = list(rel.parts)
    top = readable(parts[0]) if parts else "Other"

    # Example path after restructure:
    # ai-model/audio/openai/createspeech/文本转语音-new-api/58cfed05.md
    # use second segment as subsection, parent dir before hash file as endpoint title.
    subsection = readable(parts[1]) if len(parts) > 1 else "General"

    endpoint_dir = rel.parent.name
    if re.fullmatch(r"[0-9a-f]{8}", endpoint_dir):
        endpoint_dir = rel.parent.parent.name if rel.parent.parent != rel.parent else rel.stem
    endpoint = readable(endpoint_dir)

    return top, subsection, endpoint


def main() -> None:
    if not DOCS.exists():
        raise SystemExit(f"docs folder not found: {DOCS}")

    files = iter_docs_files()

    out: list[str] = ["# ClawRouter API 文档", "", "[TOC]", "", "---", ""]

    current_top = None
    current_sub = None

    for path in files:
        rel = path.relative_to(DOCS)
        top, sub, endpoint = section_titles(rel)

        if top != current_top:
            if current_top is not None:
                out.extend(["", "---", ""])
            out.append(f"## {top}")
            out.append("")
            current_top = top
            current_sub = None

        if sub != current_sub:
            out.append(f"### {sub}")
            out.append("")
            current_sub = sub

        out.append(f"#### {endpoint}")
        out.append("")

        content = path.read_text(encoding="utf-8", errors="ignore")
        cleaned = clean_content(content)
        if cleaned:
            out.append(cleaned)
            out.append("")

        out.extend(["---", ""])

    OUT.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")

    print(f"merged files: {len(files)}")
    print(f"output: {OUT}")


if __name__ == "__main__":
    main()
