# Utility Scripts

Helper scripts for the agentic writing system.

## check_library_updates.sh

**Purpose**: Quickly check which library files have been modified since last Stylist analysis.

**Usage**:
```bash
cd .claude/scripts
./check_library_updates.sh
```

**Output**:
- List of all .md files in `/library` with modification dates
- Last Stylist analysis date
- Current Analyzed Files Registry

**Use Case**: Before running Stylist to see what needs analysis.

---

## Future Scripts

Additional utilities could include:
- Word count calculator for library files
- Validation checker for LIBRARY_INDEX.md format
- Draft folder cleanup (archive old drafts)
- Voice profile comparison (track style evolution over time)
