#!/bin/bash
# publish.sh — Publish the framework to the public GitHub repo.
#
# What gets excluded is controlled by .gitignore-public — edit that file
# when adding new private content. No need to touch this script.

set -e

PUBLIC_REMOTE="public"
PRIVATE_BRANCH=$(git rev-parse --abbrev-ref HEAD)
PUBLISH_BRANCH="publish-temp-$(date +%s)"

# Verify prerequisites
if [ ! -f ".gitignore-public" ]; then
  echo "Error: .gitignore-public not found."
  exit 1
fi

if [ ! -f "public-docs/README.md" ] || [ ! -f "public-docs/CLAUDE.md" ]; then
  echo "Error: public-docs/README.md and public-docs/CLAUDE.md must exist."
  exit 1
fi

if ! git remote get-url "$PUBLIC_REMOTE" &>/dev/null; then
  echo "Error: '$PUBLIC_REMOTE' remote not configured."
  echo "Run: git remote add public https://github.com/yourname/agentic-writer-framework.git"
  exit 1
fi

echo "Publishing framework to public repo..."
echo "Source branch: $PRIVATE_BRANCH"

# Stash any uncommitted changes
STASHED=false
if ! git diff --quiet || ! git diff --staged --quiet; then
  git stash
  STASHED=true
fi

# Create a temporary branch from current state
git checkout -b "$PUBLISH_BRANCH"

# ── Replace docs with public versions ────────────────────────────────────────

cp public-docs/README.md README.md
cp public-docs/CLAUDE.md CLAUDE.md

# ── Strip private content using .gitignore-public ────────────────────────────

while IFS= read -r pattern; do
  # Skip comments and blank lines
  [[ "$pattern" =~ ^[[:space:]]*# ]] && continue
  [[ -z "${pattern// }" ]] && continue

  # Remove matching files/dirs
  git rm -rf --ignore-unmatch "$pattern" > /dev/null 2>&1 || true
  rm -rf "$pattern" 2>/dev/null || true
done < .gitignore-public

# ── Add placeholder .gitkeep files for emptied dirs ─────────────────────────

for dir in library external_library drafts; do
  mkdir -p "$dir"
  touch "$dir/.gitkeep"
  git add "$dir/.gitkeep"
done

# ── Commit and push ──────────────────────────────────────────────────────────

git add -A
git commit -m "chore: publish framework snapshot $(date +%Y-%m-%d)"

git push "$PUBLIC_REMOTE" "$PUBLISH_BRANCH:main" --force

# ── Clean up ─────────────────────────────────────────────────────────────────

git checkout "$PRIVATE_BRANCH"
git branch -D "$PUBLISH_BRANCH"

if [ "$STASHED" = true ]; then
  git stash pop
fi

echo ""
echo "Done. Framework published to public repo."
