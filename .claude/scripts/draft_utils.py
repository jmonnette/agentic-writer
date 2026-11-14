#!/usr/bin/env python3
"""Shared utilities for agentic_writer scripts."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
CURRENT_DRAFT_FILE = ROOT / ".current_draft"


def get_current_folder() -> Path | None:
    """Return the active draft folder from .current_draft, or None if not set."""
    if CURRENT_DRAFT_FILE.exists():
        raw = CURRENT_DRAFT_FILE.read_text().strip()
        if raw:
            p = Path(raw)
            folder = p if p.is_absolute() else ROOT / p
            if folder.exists():
                return folder
    return None


def set_current_folder(folder: Path) -> None:
    """Write the active draft folder to .current_draft (relative path)."""
    try:
        rel = folder.relative_to(ROOT)
        CURRENT_DRAFT_FILE.write_text(str(rel) + "\n")
    except ValueError:
        CURRENT_DRAFT_FILE.write_text(str(folder) + "\n")


def list_draft_folders() -> list[Path]:
    """Return all draft folders sorted newest first."""
    drafts = ROOT / "drafts"
    if not drafts.exists():
        return []
    return sorted([f for f in drafts.iterdir() if f.is_dir()], reverse=True)


def resolve_folder(arg: str) -> Path:
    """Resolve a folder argument: absolute path, relative path, or name fragment."""
    p = Path(arg)
    if p.is_absolute() and p.exists():
        return p
    full = ROOT / arg
    if full.exists():
        return full
    # Name fragment match
    drafts = ROOT / "drafts"
    matches = [f for f in drafts.iterdir() if f.is_dir() and arg in f.name]
    if matches:
        return sorted(matches, reverse=True)[0]
    return full


def find_current_draft_file(folder: Path) -> Path | None:
    """Return FINAL.md if present, else highest vN.md, else None."""
    final = folder / "FINAL.md"
    if final.exists():
        return final
    versions = sorted(
        [f for f in folder.glob("v*.md") if re.match(r"v\d+\.md", f.name)],
        key=lambda p: int(re.search(r"\d+", p.stem).group()),
        reverse=True,
    )
    return versions[0] if versions else None


def resolve_draft_file(args: list[str]) -> Path:
    """
    Resolve the target draft file from CLI args using this priority:
      1. Explicit file path argument (if arg ends in .md)
      2. Explicit folder argument (use best file within)
      3. .current_draft folder (use best file within)
      4. Error — no active draft set

    Prints an error and exits if nothing can be resolved.
    """
    if args:
        arg = args[0]
        p = Path(arg)
        candidate = p if p.is_absolute() else ROOT / arg
        if candidate.is_file():
            return candidate
        if candidate.is_dir():
            f = find_current_draft_file(candidate)
            if f:
                return f
            print(f"No draft file found in {candidate}", file=sys.stderr)
            sys.exit(1)
        # Try as folder fragment
        folder = resolve_folder(arg)
        if folder.exists():
            f = find_current_draft_file(folder)
            if f:
                return f
        print(f"Cannot resolve: {arg}", file=sys.stderr)
        sys.exit(1)

    # No arg — use .current_draft
    folder = get_current_folder()
    if not folder:
        folders = list_draft_folders()
        if not folders:
            print("No draft folders found and .current_draft is not set.", file=sys.stderr)
            print("Run /new to start an article or /switch to select one.", file=sys.stderr)
            sys.exit(1)
        # Helpful error listing options
        print("No active draft set. Run /switch to select one. Available drafts:", file=sys.stderr)
        for f in folders[:10]:
            print(f"  {f.name}", file=sys.stderr)
        sys.exit(1)

    f = find_current_draft_file(folder)
    if not f:
        print(f"No draft file found in {folder}", file=sys.stderr)
        sys.exit(1)
    return f


def resolve_draft_folder(args: list[str]) -> Path:
    """
    Like resolve_draft_file but returns the folder.
    Uses .current_draft if no arg provided.
    """
    if args:
        arg = args[0]
        p = Path(arg)
        candidate = p if p.is_absolute() else ROOT / arg
        if candidate.is_file():
            return candidate.parent
        if candidate.is_dir():
            return candidate
        folder = resolve_folder(arg)
        if folder.exists():
            return folder
        print(f"Cannot resolve: {arg}", file=sys.stderr)
        sys.exit(1)

    folder = get_current_folder()
    if not folder:
        folders = list_draft_folders()
        if not folders:
            print("No draft folders found and .current_draft is not set.", file=sys.stderr)
            sys.exit(1)
        print("No active draft set. Run /switch to select one. Available drafts:", file=sys.stderr)
        for f in folders[:10]:
            print(f"  {f.name}", file=sys.stderr)
        sys.exit(1)
    return folder
