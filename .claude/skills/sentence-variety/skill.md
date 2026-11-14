# Sentence Variety Skill

## Purpose

Generate a histogram of sentence lengths to diagnose rhythm monotony. Surfaces whether the article over-relies on one length range, lacks punch sentences, or reads as uniformly complex.

## Trigger

Use when the user asks about sentence rhythm, variety, cadence, or whether the writing feels monotonous.

## Execution

```bash
# Analyze a specific file
python3 .claude/scripts/sentence_variety.py drafts/[folder]/FINAL.md

# Auto-detect most recent draft
python3 .claude/scripts/sentence_variety.py
```

## Output

Display the script output verbatim. Do not reformat or add prose.
