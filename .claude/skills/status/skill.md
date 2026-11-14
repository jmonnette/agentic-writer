# Status Skill

## Purpose

Show the pipeline state for a draft folder — which steps are complete, which are pending, and what comes next.

## Trigger

Use when the user asks about the status of a draft, what stage an article is at, or what step comes next.

## Execution

```bash
# Check a specific draft folder (name fragment works)
python3 .claude/scripts/status.py drafts/[folder]/

# Auto-detect most recent draft folder
python3 .claude/scripts/status.py
```

## Output

Display the script output verbatim. Do not reformat or add prose.
