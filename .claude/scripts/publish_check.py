#!/usr/bin/env python3
"""Preflight check before publishing a draft."""

import re
import sys
from pathlib import Path
from draft_utils import resolve_draft_folder

ROOT = Path(__file__).parent.parent.parent
WORDS_PER_MINUTE = 238

MIN_WORDS = 600
MAX_WORDS = 3000

PLACEHOLDER_PATTERNS = [
    r"\[INSERT",
    r"\[TODO",
    r"\[PLACEHOLDER",
    r"\[TBD",
    r"\bTK\b",
    r"\[CITE\]",
    r"\[SOURCE\]",
    r"FIXME",
]

REQUIRED_SECTIONS = ["## "]  # at least one H2
SOURCES_PATTERNS = [r"## Sources", r"## References", r"## Bibliography"]


def strip_markdown(text: str) -> str:
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"!\[.*?\]\(.*?\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"[#*_~>|]", " ", text)
    return text


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
    drafts = ROOT / "drafts"
    matches = [f for f in drafts.iterdir() if f.is_dir() and arg in f.name]
    if matches:
        return sorted(matches)[-1]
    return full


def check(label: str, passed: bool, detail: str = "") -> tuple[str, bool, str]:
    return (label, passed, detail)


def main():
    args = sys.argv[1:]
    folder = resolve_draft_folder(args)

    if not folder or not folder.exists():
        print("No draft folder found.", file=sys.stderr)
        sys.exit(1)

    final = folder / "FINAL.md"
    results = []

    # 1. FINAL.md exists
    results.append(check("FINAL.md exists", final.exists()))

    if not final.exists():
        for label, passed, detail in results:
            sym = "✓" if passed else "✗"
            suffix = f"  {detail}" if detail else ""
            print(f"  {sym}  {label}{suffix}")
        print("\n  Cannot continue — FINAL.md not found.")
        sys.exit(1)

    text = final.read_text(encoding="utf-8")
    clean = strip_markdown(text)
    words = len(clean.split())

    # 2. Word count in range
    wc_ok = MIN_WORDS <= words <= MAX_WORDS
    results.append(check("Word count in range",
                         wc_ok,
                         f"{words} words (target {MIN_WORDS}–{MAX_WORDS})"))

    # 3. Has at least one H2 section
    has_sections = bool(re.search(r"^## ", text, re.MULTILINE))
    results.append(check("Has section headings (##)", has_sections))

    # 4. Has a sources/references section
    has_sources = any(re.search(p, text, re.MULTILINE) for p in SOURCES_PATTERNS)
    results.append(check("Has Sources / References section", has_sources))

    # 5. No placeholder text
    placeholders_found = []
    for pat in PLACEHOLDER_PATTERNS:
        matches = re.findall(pat, text, re.IGNORECASE)
        placeholders_found.extend(matches)
    results.append(check("No placeholder text",
                         not placeholders_found,
                         f"found: {', '.join(set(placeholders_found))}" if placeholders_found else ""))

    # 6. fact_check.md exists
    fact_check = any((folder / f).exists() for f in ["fact_check.md", "fact_check_final.md"])
    results.append(check("Fact check completed", fact_check))

    # 7. Critique completed
    critique = any((folder / f).exists()
                   for f in ["critique.md", "critique_v2.md", "critique_v3.md", "critique_final.md"])
    results.append(check("Critic review completed", critique))

    # 8. More than one version (shows iteration)
    versions = list(folder.glob("v*.md"))
    iterated = len(versions) >= 2
    results.append(check("Article went through revision",
                         iterated,
                         f"{len(versions)} version(s) found"))

    # Print
    print(f"Publish Preflight: {folder.name}")
    print()
    all_pass = True
    for label, passed, detail in results:
        sym = "✓" if passed else "✗"
        suffix = f"  {detail}" if detail else ""
        print(f"  {sym}  {label}{suffix}")
        if not passed:
            all_pass = False

    print()
    if all_pass:
        print("  ✓  Ready to publish.")
    else:
        fails = sum(1 for _, p, _ in results if not p)
        print(f"  ✗  {fails} check(s) failed. Resolve before publishing.")
    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
