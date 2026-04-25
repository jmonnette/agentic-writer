# Publish Check Skill

## Purpose

Run a preflight checklist before publishing an article. Verifies FINAL.md exists, word count is in range, required sections are present, no placeholder text remains, and key pipeline steps (critique, fact-check) were completed.

## Trigger

Use when the user asks if an article is ready to publish, wants a preflight check, or is about to move an article to the library.

## Execution

```bash
# Check a specific draft folder
python3 .claude/scripts/publish_check.py drafts/[folder]/

# Auto-detect most recent draft folder
python3 .claude/scripts/publish_check.py
```

## Output

Display the script output verbatim. If all checks pass, confirm the article is ready. If checks fail, surface the failures clearly and suggest what to address — do not add padding.
