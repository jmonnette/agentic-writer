#!/usr/bin/env python3
"""Word count utility for agentic_writer drafts."""

import re
import sys
from pathlib import Path
from draft_utils import resolve_draft_file

WORDS_PER_MINUTE = 238


def count(text: str) -> dict:
    # Strip YAML front matter
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    # Strip markdown syntax (headers, bold, italic, links, code blocks)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"!\[.*?\]\(.*?\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"[#*_~>|]", " ", text)

    words = text.split()
    word_count = len(words)

    # Sentences: split on . ! ? followed by whitespace or end
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    sentence_count = len(sentences)

    # Paragraphs: split on blank lines
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    paragraph_count = len(paragraphs)

    read_seconds = (word_count / WORDS_PER_MINUTE) * 60
    read_minutes = read_seconds / 60
    # Round to nearest 0.5
    read_time = round(read_minutes * 2) / 2

    avg_sentence = round(word_count / sentence_count, 1) if sentence_count else 0
    avg_paragraph = round(word_count / paragraph_count, 1) if paragraph_count else 0

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "paragraph_count": paragraph_count,
        "avg_sentence_length": avg_sentence,
        "avg_paragraph_length": avg_paragraph,
        "read_time_minutes": read_time,
    }


def format_report(path: Path, stats: dict, target: int | None = None) -> str:
    lines = [f"File: {path}", ""]
    lines.append(f"  Words          {stats['word_count']:>6}")
    lines.append(f"  Read time      {stats['read_time_minutes']:>5.1f} min")
    lines.append(f"  Sentences      {stats['sentence_count']:>6}")
    lines.append(f"  Avg sent len   {stats['avg_sentence_length']:>6.1f} words")
    lines.append(f"  Paragraphs     {stats['paragraph_count']:>6}")
    lines.append(f"  Avg para len   {stats['avg_paragraph_length']:>6.1f} words")
    if target is not None:
        diff = stats["word_count"] - target
        pct = (diff / target) * 100
        sign = "+" if diff >= 0 else ""
        lines.append(f"  Target         {target:>6}")
        lines.append(f"  Difference     {sign}{diff:>5} ({sign}{pct:.1f}%)")
    return "\n".join(lines)


def main():
    args = sys.argv[1:]
    target = None
    file_args = []

    for arg in args:
        if arg.startswith("--target="):
            target = int(arg.split("=", 1)[1])
        elif arg.startswith("-t"):
            target = int(arg[2:])
        else:
            file_args.append(arg)

    path = resolve_draft_file(file_args)

    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    stats = count(text)
    print(format_report(path, stats, target))


if __name__ == "__main__":
    main()
