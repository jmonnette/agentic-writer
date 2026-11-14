#!/usr/bin/env python3
"""Show pipeline status for a draft folder."""

import re
import sys
from pathlib import Path
from draft_utils import get_current_folder, resolve_folder as _resolve_folder, list_draft_folders

ROOT = Path(__file__).parent.parent.parent

PIPELINE_STEPS = [
    ("Interview",        ["interview_brief.md"]),
    ("Research",         ["research_pack.md"]),
    ("POV Brief",        ["pov_brief.md"]),
    ("Outline",          ["outline.md"]),
    ("First Draft",      ["v1.md"]),
    ("Critique",         ["critique.md", "critique_v2.md", "critique_v3.md", "critique_final.md"]),
    ("Revised Draft",    ["v2.md"]),
    ("Fact Check",       ["fact_check.md", "fact_check_final.md"]),
    ("Persona Review",   None),   # detected by glob
    ("Final Edit",       ["FINAL.md"]),
    ("Social Posts",     ["social_posts.md"]),
]


def find_latest_folder() -> Path | None:
    drafts = ROOT / "drafts"
    folders = sorted([f for f in drafts.iterdir() if f.is_dir()], reverse=True)
    return folders[0] if folders else None


def resolve_folder(arg: str) -> Path:
    p = Path(arg)
    if p.is_absolute():
        return p
    full = ROOT / arg
    if full.exists():
        return full
    # Try matching by name fragment
    drafts = ROOT / "drafts"
    matches = [f for f in drafts.iterdir() if f.is_dir() and arg in f.name]
    if matches:
        return sorted(matches)[-1]
    return full


def main():
    args = sys.argv[1:]
    if args:
        folder = _resolve_folder(args[0])
    else:
        folder = get_current_folder()
        if not folder:
            folders = list_draft_folders()
            if not folders:
                print("No draft folders found and .current_draft is not set.", file=sys.stderr)
                sys.exit(1)
            print("No active draft set. Run /switch to select one. Available drafts:", file=sys.stderr)
            for f in folders[:10]:
                print(f"  {f.name}", file=sys.stderr)
            sys.exit(1)

    if not folder or not folder.exists():
        print("No draft folder found.", file=sys.stderr)
        sys.exit(1)

    files = {f.name for f in folder.iterdir() if f.is_file()}
    versions = sorted(
        [f for f in folder.glob("v*.md") if re.match(r"v\d+\.md", f.name)],
        key=lambda p: int(re.search(r"\d+", p.stem).group())
    )
    persona_files = [f for f in folder.iterdir() if f.name.startswith("persona_review_")]

    print(f"Draft: {folder.name}")
    print()

    last_done = -1
    rows = []
    for i, (step, markers) in enumerate(PIPELINE_STEPS):
        if step == "Persona Review":
            done = bool(persona_files)
            detail = f"({len(persona_files)} reviews)" if done else ""
        elif markers:
            done = any(m in files for m in markers)
            found = next((m for m in markers if m in files), None)
            detail = found if done else ""
        else:
            done = False
            detail = ""

        if step == "Revised Draft" and versions:
            count = len(versions)
            done = count >= 2
            detail = f"({count} versions total)" if done else f"(v1.md only)" if "v1.md" in files else ""

        symbol = "✓" if done else "○"
        rows.append((symbol, step, detail, done))
        if done:
            last_done = i

    for i, (symbol, step, detail, done) in enumerate(rows):
        suffix = f"  {detail}" if detail else ""
        next_marker = " ← next" if i == last_done + 1 else ""
        print(f"  {symbol}  {step}{suffix}{next_marker}")

    print()
    if versions:
        latest = versions[-1]
        print(f"  Latest version : {latest.name}")
    if "FINAL.md" in files:
        print(f"  FINAL.md       : present")
    print(f"  Total files    : {len(files)}")


if __name__ == "__main__":
    main()
