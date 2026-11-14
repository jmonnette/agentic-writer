#!/usr/bin/env python3
"""Histogram of sentence lengths to diagnose rhythm monotony."""

import re
import sys
from pathlib import Path
from draft_utils import resolve_draft_file

ROOT = Path(__file__).parent.parent.parent

BUCKETS = [
    (1,  5,  "  1–5  (punch)      "),
    (6,  10, "  6–10 (short)      "),
    (11, 18, " 11–18 (medium)     "),
    (19, 30, " 19–30 (standard)   "),
    (31, 50, " 31–50 (complex)    "),
    (51, 999,"   51+ (very long)  "),
]

BAR_WIDTH = 30


def strip_markdown(text: str) -> str:
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"!\[.*?\]\(.*?\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"[#*_~>|]", " ", text)
    return text


def get_sentence_lengths(text: str) -> list[int]:
    text = strip_markdown(text)
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    return [len(s.split()) for s in sentences if len(s.split()) > 0]


def find_latest_draft() -> Path | None:
    drafts = ROOT / "drafts"
    if not drafts.exists():
        return None
    for folder in sorted(drafts.iterdir(), reverse=True):
        if not folder.is_dir():
            continue
        final = folder / "FINAL.md"
        if final.exists():
            return final
        versions = sorted(folder.glob("v*.md"),
                          key=lambda p: int(re.search(r"\d+", p.stem).group()), reverse=True)
        if versions:
            return versions[0]
    return None


def main():
    args = sys.argv[1:]
    path = resolve_draft_file(args)

    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)

    lengths = get_sentence_lengths(path.read_text(encoding="utf-8"))
    total = len(lengths)
    if not total:
        print("No sentences found.")
        return

    counts = []
    for lo, hi, label in BUCKETS:
        n = sum(1 for l in lengths if lo <= l <= hi)
        counts.append((label, n))

    max_count = max(n for _, n in counts) or 1

    print(f"File: {path}")
    print(f"Sentences: {total}  |  Avg length: {sum(lengths)/total:.1f} words")
    print()

    for label, n in counts:
        pct = n / total * 100
        bar_len = int(n / max_count * BAR_WIDTH)
        bar = "█" * bar_len
        print(f"{label} {bar:<{BAR_WIDTH}}  {n:>3} ({pct:4.1f}%)")

    print()
    # Flag monotony: any single bucket > 50%
    for label, n in counts:
        if n / total > 0.5:
            print(f"  ⚠  Over 50% of sentences fall in one bucket — consider varying rhythm.")
            break

    # Highlight punch sentence usage
    punch = counts[0][1]
    if punch == 0:
        print("  ℹ  No punch sentences (1–5 words) found — consider adding emphasis lines.")
    elif punch / total > 0.15:
        print(f"  ℹ  High punch sentence ratio ({punch/total:.0%}) — may feel choppy at sustained levels.")


if __name__ == "__main__":
    main()
