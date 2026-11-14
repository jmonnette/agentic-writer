Switch the active draft so all skills target it by default.

## Steps

1. List all folders in `/drafts/` sorted newest first, numbered starting at 1. For each, show:
   - Number
   - Folder name
   - Whether it has a FINAL.md (mark with ✓) or highest vN.md present
   - Mark the currently active draft (from `.current_draft`) with `← active`

2. Ask the user to pick a number (or accept a folder name/fragment as an argument if provided).

3. Write the selected folder path (relative, e.g. `drafts/ai_regulation_20260329`) to `.current_draft` using Bash:
   ```bash
   echo "drafts/[folder_name]" > .current_draft
   ```

4. Confirm: "Active draft set to: [folder_name]"

## Notes

- If the user passes a folder name or fragment as an argument, skip the interactive list and switch directly.
- If `.current_draft` doesn't exist yet, just create it.
