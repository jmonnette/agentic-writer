# Reading Level Skill

## Purpose

Compute Flesch Reading Ease and Flesch-Kincaid Grade Level for a draft using deterministic formulas. Useful for checking if voice is drifting academic or if the article is appropriately accessible for the target audience.

## Trigger

Use when the user asks about readability, reading level, or whether a draft is too complex or too simple.

## Execution

```bash
# Score a specific file
python3 .claude/scripts/reading_level.py drafts/[folder]/FINAL.md

# Auto-detect most recent draft
python3 .claude/scripts/reading_level.py
```

## Interpreting Results

- **Flesch Reading Ease**: Higher = easier. 60–70 is standard business writing. Below 50 is college-level difficulty.
- **Flesch-Kincaid Grade**: US grade level equivalent. Target ~12 (high school senior) for most business articles.

## Output

Display the script output verbatim. Do not add interpretation beyond what the script provides.
