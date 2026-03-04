#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

INVISIBLE_CHARS = ["\ufeff", "\u200b", "\u200c", "\u200d", "\u2060"]

JUNK_LINE_PATTERNS = [
    re.compile(r"^>\s*Auto-generated.*", re.IGNORECASE),
    re.compile(r"^>\s*Migrated from .*", re.IGNORECASE),
    re.compile(r"^>\s*Links below point to local Markdown files\.?$", re.IGNORECASE),
    re.compile(r"^Auto-generated.*", re.IGNORECASE),
    re.compile(r"^Links below point to local Markdown files\.?$", re.IGNORECASE),
    re.compile(r"^复制 Markdown打开$"),
    re.compile(r"^这篇文档对您有帮助吗？$"),
    re.compile(r"^有帮助没帮助$"),
    re.compile(r"^最后更新于$"),
]


def _normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    for ch in INVISIBLE_CHARS:
        text = text.replace(ch, "")
    return text


def _should_drop_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    for pattern in JUNK_LINE_PATTERNS:
        if pattern.match(stripped):
            return True
    return False


def clean_markdown_text(text: str) -> str:
    text = _normalize_text(text)
    lines = text.split("\n")
    out: list[str] = []

    in_fence = False
    fence_marker = "```"

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

        if _should_drop_line(line):
            continue

        out.append(line.rstrip())

    cleaned = "\n".join(out)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip() + "\n"
    return cleaned


def clean_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8", errors="ignore")
    cleaned = clean_markdown_text(original)
    if cleaned != original:
        path.write_text(cleaned, encoding="utf-8")
        return True
    return False


def iter_markdown_files(docs_root: Path) -> list[Path]:
    files = sorted(docs_root.rglob("*.md"))
    ignored = {"_sidebar.md", "_missing.txt", "_mapping.json", "_rename_collisions.txt"}
    return [p for p in files if p.name not in ignored]


def main() -> None:
    parser = argparse.ArgumentParser(description="Safely clean markdown files under docs/.")
    parser.add_argument("--docs-root", default="docs", help="Docs root path")
    args = parser.parse_args()

    docs_root = Path(args.docs_root)
    if not docs_root.exists():
        raise SystemExit(f"docs root not found: {docs_root}")

    changed = 0
    files = iter_markdown_files(docs_root)
    for path in files:
        if clean_file(path):
            changed += 1

    print(f"Scanned {len(files)} markdown files, changed {changed} files")


if __name__ == "__main__":
    main()
