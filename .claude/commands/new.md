Scaffold a new article draft and initialize the pipeline.

## Steps

1. **Get the topic**: If not provided as an argument, ask the user for a short topic slug (e.g., `ai_regulation`, `engineering_metrics`).

2. **Create the draft folder**: Make `/drafts/[topic]_YYYYMMDD/` using today's date. Use Bash: `mkdir -p drafts/[topic]_YYYYMMDD`

3. **Set as active draft**: Write the new folder as the active draft:
   ```bash
   echo "drafts/[topic]_YYYYMMDD" > .current_draft
   ```

4. **Update TOPICS.md**: Find the matching entry in the Backlog section of `TOPICS.md` (match on topic name or working title). Move it to the **In Progress** section and add the draft folder path. If no matching entry exists, add a new In Progress entry with:
   - **Status**: In Progress
   - **Draft folder**: `drafts/[topic]_YYYYMMDD/`
   - **Started**: today's date

5. **Confirm and suggest next step**: Report the folder path created and confirm it is now the active draft. Ask whether to start with the Interviewer agent or go straight to Research.

## Notes

- Today's date is available in the system context.
- Do not create any files inside the draft folder — the pipeline agents create their own files.
- If the user passes a topic slug as an argument, use it directly without asking.
