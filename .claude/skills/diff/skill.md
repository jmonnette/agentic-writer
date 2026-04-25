# Diff Skill

## Purpose

Compare two draft versions and report what changed: word count delta, structural changes, and line-level edits.

## Trigger

Use when the user asks to compare drafts, see what changed between versions, or check the net impact of a revision.

## Execution

```bash
# Compare two specific files
python3 .claude/scripts/diff_drafts.py drafts/[folder]/v2.md drafts/[folder]/v3.md

# Auto-compare the two most recent versions in a folder
python3 .claude/scripts/diff_drafts.py drafts/[folder]/

# Auto-detect most recent folder and compare latest two versions
python3 .claude/scripts/diff_drafts.py
```

## Output

Display the script output verbatim. Do not reformat or add prose.
