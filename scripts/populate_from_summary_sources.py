#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

METHOD_RE = re.compile(r"^(GET|POST|PUT|DELETE)\s*$")
SUMMARY_LINK_RE = re.compile(r"^(\s*)-\s+\[([^\]]+)\]\(([^)]+\.md)\)\s*$")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)")
H1_RE = re.compile(r"^\s*#\s+.+$")


@dataclass
class Target:
    title: str
    rel_path: str
    abs_path: Path
    level: int
    crumbs: list[str]


def norm(s: str) -> str:
    s = s.strip().lower()
    s = s.replace("（", "(").replace("）", ")")
    s = s.replace(" ", "")
    return s


def key_tokens(s: str) -> list[str]:
    x = norm(s)
    tokens = re.split(r"[^a-z0-9\u4e00-\u9fff]+", x)
    return [t for t in tokens if t and t not in {"api", "new", "format"}]


def parse_summary(summary_path: Path) -> list[Target]:
    targets: list[Target] = []
    stack: list[str] = []
    for line in summary_path.read_text(encoding="utf-8").splitlines():
        m = SUMMARY_LINK_RE.match(line)
        if not m:
            continue
        indent, title, rel = m.groups()
        level = len(indent) // 2
        if level <= len(stack):
            stack = stack[:level]
        stack.append(title)
        targets.append(Target(title=title, rel_path=rel, abs_path=summary_path.parent / rel, level=level, crumbs=stack.copy()))
    return targets


def non_empty_line_count(p: Path) -> int:
    if not p.exists():
        return 0
    return sum(1 for ln in p.read_text(encoding="utf-8", errors="ignore").splitlines() if ln.strip())


def parse_index_links(index_path: Path) -> dict[str, Path]:
    out: dict[str, Path] = {}
    if not index_path.exists():
        return out
    text = index_path.read_text(encoding="utf-8", errors="ignore")
    for t, lnk in MD_LINK_RE.findall(text):
        out[norm(t)] = (index_path.parent / lnk).resolve()
    return out


def load_move_map(tsv_path: Path) -> dict[str, str]:
    move_map: dict[str, str] = {}
    if not tsv_path.exists():
        return move_map
    lines = tsv_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    for ln in lines[1:]:
        if not ln.strip() or "\t" not in ln:
            continue
        src, dst = ln.split("\t", 1)
        move_map[src.strip()] = dst.strip()
    return move_map


def load_mapping_candidates(mapping_path: Path, docs_root: Path) -> list[tuple[list[str], Optional[Path], float]]:
    out: list[tuple[list[str], Optional[Path], float]] = []
    if not mapping_path.exists():
        return out
    data = json.loads(mapping_path.read_text(encoding="utf-8"))
    move_map = load_move_map(docs_root / "_restructure_moves.tsv")
    for k, v in data.items():
        parts = [p.strip() for p in k.split(">")]
        mf = v.get("matched_file") if isinstance(v, dict) else None
        conf = float(v.get("confidence", 0.0)) if isinstance(v, dict) else 0.0
        src_path = None
        if mf:
            rel = move_map.get(mf, mf)
            p = docs_root / rel
            if p.exists():
                src_path = p.resolve()
        out.append((parts, src_path, conf))
    return out


def score_mapping(target: Target, parts: list[str], conf: float) -> float:
    tnorm = norm(target.title)
    score = conf
    if parts:
        last = parts[-1]
        last = re.sub(r"\s*\((GET|POST|PUT|DELETE)\)\s*$", "", last, flags=re.I)
        if tnorm in norm(last) or norm(last) in tnorm:
            score += 5
    for c in target.crumbs:
        cn = norm(c)
        if any(cn in norm(p) or norm(p) in cn for p in parts):
            score += 0.8
    return score


def fuzzy_pick(target: Target, candidates: list[Path]) -> Optional[Path]:
    best = None
    best_score = -1.0
    tkns = key_tokens(target.title)
    tnorm = norm(target.title)
    for p in candidates:
        name = norm(p.stem)
        text = p.read_text(encoding="utf-8", errors="ignore")
        h1 = ""
        for ln in text.splitlines()[:40]:
            if ln.strip().startswith("#"):
                h1 = norm(re.sub(r"^#+\s*", "", ln.strip()))
                break
        s = 0.0
        for tk in tkns:
            if tk in name:
                s += 1.2
            if tk and tk in h1:
                s += 1.5
        if tnorm and (tnorm in name or tnorm in h1):
            s += 3.0
        if s > best_score:
            best_score = s
            best = p
    return best if best_score > 0 else None


def sanitize_content(src_text: str, title: str) -> str:
    lines = src_text.splitlines()
    # drop standalone HTTP method lines
    lines = [ln for ln in lines if not METHOD_RE.match(ln.strip())]
    # remove first encountered H1 (if any), we'll insert our own
    first_h1_idx = None
    for i, ln in enumerate(lines):
        if H1_RE.match(ln):
            first_h1_idx = i
            break
    if first_h1_idx is not None:
        lines.pop(first_h1_idx)
        # trim leading blank lines after removing H1
        while lines and not lines[0].strip():
            lines.pop(0)
    body = "\n".join(lines).rstrip() + "\n"
    return f"# {title}\n\n{body}"


def main() -> None:
    root = Path.cwd()
    docs = root / "docs"
    summary = docs / "SUMMARY.md"

    if not summary.exists():
        raise SystemExit("docs/SUMMARY.md not found")

    targets = parse_summary(summary)
    index_map = parse_index_links(docs / "_index.md")
    mapping_entries = load_mapping_candidates(docs / "_mapping.json", docs)

    # fuzzy candidates: NOT within docs/ai-model/** or docs/management/**
    fuzzy_candidates: list[Path] = []
    for p in docs.rglob("*.md"):
        rp = p.relative_to(docs).as_posix()
        if rp.startswith("ai-model/") or rp.startswith("management/"):
            continue
        if rp == "SUMMARY.md":
            continue
        fuzzy_candidates.append(p.resolve())

    filled = 0
    examples: list[tuple[str, str, str]] = []

    for t in targets:
        t.abs_path.parent.mkdir(parents=True, exist_ok=True)

        if t.abs_path.exists() and non_empty_line_count(t.abs_path) > 30:
            continue

        src: Optional[Path] = None

        # 1) index visible text exact match
        src = index_map.get(norm(t.title))
        if src is not None and not src.exists():
            src = None

        # 2) mapping.json
        if src is None and mapping_entries:
            best_src = None
            best_score = -1e9
            for parts, mp, conf in mapping_entries:
                if mp is None:
                    continue
                s = score_mapping(t, parts, conf)
                if s > best_score:
                    best_score = s
                    best_src = mp
            src = best_src

        # 3) fuzzy
        if src is None:
            src = fuzzy_pick(t, fuzzy_candidates)

        if src is None or not src.exists():
            # keep existing content if present; else minimal stub
            if not t.abs_path.exists():
                t.abs_path.write_text(f"# {t.title}\n", encoding="utf-8")
            examples.append((t.title, t.rel_path, "<none>"))
            continue

        src_text = src.read_text(encoding="utf-8", errors="ignore")
        out = sanitize_content(src_text, t.title)
        t.abs_path.write_text(out, encoding="utf-8")
        filled += 1
        examples.append((t.title, t.rel_path, str(src.relative_to(root))))

    # validate missing targets from summary
    missing = [t for t in targets if not t.abs_path.exists()]

    print(f"total targets: {len(targets)}")
    print(f"filled targets count: {filled}")
    print(f"still-missing count: {len(missing)}")
    print("examples (title -> target <- source):")
    for title, target, source in examples[:30]:
        print(f"- {title} -> docs/{target} <- {source}")


if __name__ == "__main__":
    main()
