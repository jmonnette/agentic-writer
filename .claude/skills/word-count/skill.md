# Word Count Skill

## Purpose

Run the deterministic Python word counter on a draft file and display the results.

## Trigger

Use when the user asks for a word count, read time, or length metrics on any draft.

## Execution

Run the script with Bash:

```bash
python3 .claude/scripts/word_count.py [file_path] [--target=N]
```

**Arguments:**
- `file_path` (optional): relative path from the repo root (e.g. `drafts/ai_regulation_20260329/FINAL.md`). Omit to auto-detect the most recent draft.
- `--target=N` (optional): target word count. When provided, the report includes words over/under and percentage difference.

## Output

Display the script output verbatim. Do not reformat, summarize, or add prose around it.
