#!/bin/bash
# Helper script to check which library files need Stylist analysis
# Usage: ./check_library_updates.sh

LIBRARY_DIR="../../library"
SKILL_FILE="../skills/personal-voice/skill.md"

echo "=== Library Update Check ==="
echo ""

# Check if library directory exists
if [ ! -d "$LIBRARY_DIR" ]; then
    echo "Error: Library directory not found at $LIBRARY_DIR"
    exit 1
fi

# Get list of all .md files in library
echo "Files in library:"
ls -lh "$LIBRARY_DIR"/*.md 2>/dev/null | awk '{print $9, "- Modified:", $6, $7, $8}'
echo ""

# Check if skill file exists and extract last analysis date
if [ -f "$SKILL_FILE" ]; then
    echo "Last Stylist Analysis:"
    grep "Last Updated by Stylist" "$SKILL_FILE" || echo "Not found in skill file"
    echo ""

    echo "Analyzed Files Registry:"
    # Extract the table from the skill file (between the header and the next section)
    awk '/\| Filename \| Last Modified/,/^$/' "$SKILL_FILE" | grep -v "^$"
else
    echo "Warning: personal-voice skill file not found"
fi

echo ""
echo "=== End of Report ==="
