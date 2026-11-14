#!/usr/bin/env python3
"""Compute Flesch-Kincaid readability metrics for a draft."""

import re
import sys
from pathlib import Path
from draft_utils import resolve_draft_file

ROOT = Path(__file__).parent.parent.parent
WORDS_PER_MINUTE = 238

# Grade-level labels for Flesch Reading Ease score
EASE_LABELS = [
    (90, "Very Easy (5th grade)"),
    (80, "Easy (6th grade)"),
    (70, "Fairly Easy (7th grade)"),
    (60, "Standard (8th–9th grade)"),
    (50, "Fairly Difficult (10th–12th grade)"),
    (30, "Difficult (College)"),
    (0,  "Very Difficult (College graduate)"),
]

VOWELS = set("aeiouAEIOU")


def strip_markdown(text: str) -> str:
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"!\[.*?\]\(.*?\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"[#*_~>|]", " ", text)
    return text


def count_syllables(word: str) -> int:
    word = word.lower().strip(".,!?;:\"'()-")
    if not word:
        return 0
    # Count vowel groups
    count = len(re.findall(r"[aeiou]+", word))
    # Subtract silent e
    if word.endswith("e") and count > 1:
        count -= 1
    return max(1, count)


def analyze(text: str) -> dict:
    text = strip_markdown(text)
    words = text.split()
    word_count = len(words)

    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    sentence_count = max(1, len(sentences))

    syllable_count = sum(count_syllables(w) for w in words)

    # Flesch Reading Ease
    if word_count and sentence_count:
        ease = 206.835 - 1.015 * (word_count / sentence_count) - 84.6 * (syllable_count / word_count)
    else:
        ease = 0

    # Flesch-Kincaid Grade Level
    if word_count and sentence_count:
        grade = 0.39 * (word_count / sentence_count) + 11.8 * (syllable_count / word_count) - 15.59
    else:
        grade = 0

    ease = max(0, min(100, ease))
    grade = max(0, grade)

    label = EASE_LABELS[-1][1]
    for threshold, lbl in EASE_LABELS:
        if ease >= threshold:
            label = lbl
            break

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "syllable_count": syllable_count,
        "syllables_per_word": round(syllable_count / word_count, 2) if word_count else 0,
        "words_per_sentence": round(word_count / sentence_count, 1) if sentence_count else 0,
        "flesch_ease": round(ease, 1),
        "flesch_grade": round(grade, 1),
        "label": label,
    }


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

    stats = analyze(path.read_text(encoding="utf-8"))

    print(f"File: {path}")
    print()
    print(f"  Flesch Reading Ease    {stats['flesch_ease']:>6.1f}  ({stats['label']})")
    print(f"  Flesch-Kincaid Grade   {stats['flesch_grade']:>6.1f}")
    print()
    print(f"  Words                  {stats['word_count']:>6}")
    print(f"  Sentences              {stats['sentence_count']:>6}")
    print(f"  Words / sentence       {stats['words_per_sentence']:>6.1f}")
    print(f"  Syllables / word       {stats['syllables_per_word']:>6.2f}")


if __name__ == "__main__":
    main()
