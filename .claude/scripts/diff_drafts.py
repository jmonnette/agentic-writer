#!/usr/bin/env python3
"""Compare two draft versions and report changes."""

import re
import sys
from pathlib import Path
from difflib import unified_diff
from draft_utils import get_current_folder, resolve_folder as _resolve_folder

ROOT = Path(__file__).parent.parent.parent


def strip_markdown(text: str) -> str:
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"!\[.*?\]\(.*?\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"[#*_~>|]", " ", text)
    return text


def word_count(text: str) -> int:
    return len(strip_markdown(text).split())


def extract_headings(text: str) -> list[str]:
    return re.findall(r"^#{1,3} .+", text, flags=re.MULTILINE)


def resolve_path(arg: str, folder: Path | None) -> Path:
    p = Path(arg)
    if p.is_absolute():
        return p
    full = ROOT / arg
    if full.exists():
        return full
    if folder and (folder / arg).exists():
        return folder / arg
    return full


def find_draft_folder() -> Path | None:
    drafts = ROOT / "drafts"
    folders = sorted([f for f in drafts.iterdir() if f.is_dir()], reverse=True)
    return folders[0] if folders else None


def latest_two_versions(folder: Path) -> tuple[Path, Path] | None:
    versions = sorted(folder.glob("v*.md"),
                      key=lambda p: int(re.search(r"\d+", p.stem).group()))
    if len(versions) >= 2:
        return versions[-2], versions[-1]
    final = folder / "FINAL.md"
    if final.exists() and versions:
        return versions[-1], final
    return None


def main():
    args = sys.argv[1:]
    file_a, file_b = None, None

    if len(args) >= 2:
        folder = get_current_folder()
        file_a = resolve_path(args[0], folder)
        file_b = resolve_path(args[1], folder)
    elif len(args) == 1:
        # Single arg = draft folder
        folder = ROOT / args[0] if not Path(args[0]).is_absolute() else Path(args[0])
        pair = latest_two_versions(folder)
        if not pair:
            print(f"Could not find two versions in {folder}", file=sys.stderr)
            sys.exit(1)
        file_a, file_b = pair
    else:
        folder = get_current_folder()
        if not folder:
            print("No active draft set. Run /switch to select one.", file=sys.stderr)
            sys.exit(1)
        pair = latest_two_versions(folder)
        if not pair:
            print(f"Could not find two versions in {folder}", file=sys.stderr)
            sys.exit(1)
        file_a, file_b = pair

    for f in (file_a, file_b):
        if not f.exists():
            print(f"File not found: {f}", file=sys.stderr)
            sys.exit(1)

    text_a = file_a.read_text(encoding="utf-8")
    text_b = file_b.read_text(encoding="utf-8")

    wc_a = word_count(text_a)
    wc_b = word_count(text_b)
    delta = wc_b - wc_a
    pct = (delta / wc_a * 100) if wc_a else 0
    sign = "+" if delta >= 0 else ""

    headings_a = set(extract_headings(text_a))
    headings_b = set(extract_headings(text_b))
    added_sections = headings_b - headings_a
    removed_sections = headings_a - headings_b

    print(f"Comparing: {file_a.name}  →  {file_b.name}")
    print()
    print(f"  Words         {wc_a:>6} → {wc_b:<6}  ({sign}{delta}, {sign}{pct:.1f}%)")

    if added_sections:
        print()
        print("  Sections added:")
        for h in sorted(added_sections):
            print(f"    + {h}")

    if removed_sections:
        print()
        print("  Sections removed:")
        for h in sorted(removed_sections):
            print(f"    - {h}")

    if not added_sections and not removed_sections:
        print()
        print("  Sections: no structural changes")

    # Line-level diff summary
    lines_a = text_a.splitlines()
    lines_b = text_b.splitlines()
    diff = list(unified_diff(lines_a, lines_b, lineterm=""))
    added_lines = sum(1 for l in diff if l.startswith("+") and not l.startswith("+++"))
    removed_lines = sum(1 for l in diff if l.startswith("-") and not l.startswith("---"))
    print()
    print(f"  Lines added    {added_lines:>6}")
    print(f"  Lines removed  {removed_lines:>6}")


if __name__ == "__main__":
    main()
