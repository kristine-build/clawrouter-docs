#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PREFIX = "zh__docs__api__"
COLLISION_LOG = DOCS / "_rename_collisions.txt"
MOVE_LOG = DOCS / "_restructure_moves.tsv"


@dataclass
class MoveRecord:
    src: Path
    dst: Path
    collided: bool


def iter_source_files(docs_root: Path) -> list[Path]:
    files = []
    for path in docs_root.rglob("*.md"):
        if not path.is_file():
            continue
        if path.name.startswith("_"):
            continue
        if path.name.startswith(PREFIX):
            files.append(path)
    return sorted(files, key=lambda p: p.as_posix())


def target_from_name(name: str, docs_root: Path) -> Path:
    # name example: zh__docs__api__ai-model__audio__openai.md
    stem = name[:-3] if name.endswith(".md") else name
    remaining = stem[len(PREFIX) :]
    parts = [p for p in remaining.split("__") if p]
    if len(parts) < 2:
        raise ValueError(f"Cannot restructure filename: {name}")

    *dirs, filename = parts
    return docs_root.joinpath(*dirs, f"{filename}.md")


def resolve_collision(path: Path) -> tuple[Path, int]:
    if not path.exists():
        return path, 0

    idx = 1
    while True:
        candidate = path.with_name(f"{path.stem}-{idx}{path.suffix}")
        if not candidate.exists():
            return candidate, idx
        idx += 1


def final_tree_depth(docs_root: Path) -> int:
    max_depth = 0
    for path in docs_root.rglob("*.md"):
        rel = path.relative_to(docs_root)
        depth = len(rel.parts) - 1  # directory depth, exclude filename
        if depth > max_depth:
            max_depth = depth
    return max_depth


def main() -> None:
    if not DOCS.exists():
        raise SystemExit(f"docs directory not found: {DOCS}")

    sources = iter_source_files(DOCS)
    moves: list[MoveRecord] = []
    collisions: list[str] = []

    for src in sources:
        dst_base = target_from_name(src.name, DOCS)
        dst, collision_index = resolve_collision(dst_base)

        dst.parent.mkdir(parents=True, exist_ok=True)
        src.rename(dst)

        collided = collision_index > 0
        if collided:
            collisions.append(
                f"{src.relative_to(DOCS).as_posix()} -> {dst.relative_to(DOCS).as_posix()}"
            )

        moves.append(MoveRecord(src=src, dst=dst, collided=collided))

    COLLISION_LOG.write_text(
        ("\n".join(collisions) + "\n") if collisions else "",
        encoding="utf-8",
    )

    MOVE_LOG.write_text(
        "source\tdestination\n"
        + "".join(
            f"{m.src.relative_to(DOCS).as_posix()}\t{m.dst.relative_to(DOCS).as_posix()}\n"
            for m in moves
        ),
        encoding="utf-8",
    )

    depth = final_tree_depth(DOCS)
    print(f"total files moved: {len(moves)}")
    print(f"collisions: {len(collisions)}")
    print(f"final folder tree depth: {depth}")


if __name__ == "__main__":
    main()
