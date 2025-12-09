#!/usr/bin/env python3
"""
Promote a staged, AI-generated file into canon.

This script:
- Reads a markdown file from generation/staging/...
- Parses YAML frontmatter
- Updates metadata to mark it as canon
- Chooses a target directory based on `type`
- Writes a new file into the world/ or content/ trees using `id` as filename

Example usage:

    python3 tools/promote-to-canon.py \
        generation/staging/npcs/20251206-053210/npc-001.md

Optional override:

    python3 tools/promote-to-canon.py \
        generation/staging/quests/20251206-053210/quest-001.md \
        --target-dir world/lore

Requirements:
    - Python 3.9+
    - pyyaml (install with `pip install pyyaml`)
"""

import argparse
import datetime as dt
from pathlib import Path
from typing import Tuple, Dict, Any

import yaml  # type: ignore


# --- Repo Root ---------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]  # assumes tools/ at repo root


# --- Type → Target Directory Mapping -----------------------------------

# You can adjust this mapping to match your actual repo layout.
TYPE_TO_DIR = {
    # world-facing lore
    "character": "world/characters",
    "npc": "world/characters",
    "location": "world/locations",
    "faction": "world/factions",
    "culture": "world/cultures",
    "species": "world/species",
    "deity": "world/deities",
    "artifact": "world/artifacts",
    "item": "world/artifacts",
    "event": "world/events",
    "ritual": "world/rituals",
    "shrine": "world/shrines",
    "lore-fragment": "world/lore",

    # playable content
    "quest": "content/quests",
    "dungeon": "content/dungeons",
    "encounter": "content/encounters",
    "loot-table": "content/loot-tables",
}


# --- Frontmatter Helpers -----------------------------------------------

def parse_frontmatter(text: str) -> Tuple[Dict[str, Any], str]:
    """
    Split markdown into (frontmatter_dict, body_text).

    If no frontmatter is present, returns ({}, original_text).
    """
    if not text.lstrip().startswith("---"):
        return {}, text

    lines = text.splitlines()
    if lines[0].strip() != "---":
        return {}, text

    # Find closing ---
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        return {}, text  # malformed; treat whole thing as body

    fm_str = "\n".join(lines[1:end_idx])
    body = "\n".join(lines[end_idx + 1:]).lstrip("\n")

    try:
        meta = yaml.safe_load(fm_str) or {}
        if not isinstance(meta, dict):
            meta = {}
    except yaml.YAMLError:
        meta = {}

    return meta, body


def render_frontmatter(meta: Dict[str, Any]) -> str:
    """
    Render a metadata dict back into YAML frontmatter.
    """
    dumped = yaml.safe_dump(meta, sort_keys=False).strip()
    return f"---\n{dumped}\n---\n\n"


# --- Core Logic --------------------------------------------------------

def infer_target_dir(meta: Dict[str, Any], override: str | None) -> Path:
    """
    Decide where this file should live in canon.

    Preference:
    1. --target-dir override from CLI
    2. TYPE_TO_DIR based on meta['type']
    """
    if override:
        return ROOT / override

    entity_type = meta.get("type")
    if not entity_type:
        raise ValueError("Frontmatter is missing 'type'; cannot infer target directory.")

    target_rel = TYPE_TO_DIR.get(entity_type)
    if not target_rel:
        raise ValueError(
            f"Unknown type '{entity_type}' and no --target-dir override provided.\n"
            f"Add it to TYPE_TO_DIR or pass --target-dir explicitly."
        )

    return ROOT / target_rel


def update_metadata_for_canon(
    meta: Dict[str, Any],
    source_path: Path,
) -> Dict[str, Any]:
    """
    Mutate metadata to reflect canonical status.
    """
    meta = dict(meta)  # shallow copy
    today = dt.date.today().isoformat()
    now = dt.datetime.now().isoformat(timespec="seconds")

    # Identity fields should already be there: id, type, title...
    # We just normalize canonical status.
    meta.setdefault("scope", "canon")
    meta.setdefault("visibility", "public")
    meta["status"] = "active"
    meta["confidence"] = meta.get("confidence", "medium")
    meta["last_reviewed"] = today

    # Provenance
    meta.setdefault("source", "ai-generated")
    meta["promoted_at"] = now
    meta["promoted_from"] = str(source_path.relative_to(ROOT))

    return meta


def promote_file(
    source_path: Path,
    target_dir_override: str | None = None,
    dry_run: bool = False,
) -> Path:
    """
    Read a staged file, update frontmatter, and write into canon.

    Returns the path of the new canonical file.
    """
    if not source_path.exists():
        raise FileNotFoundError(f"Source file not found: {source_path}")

    raw = source_path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(raw)

    if not meta:
        raise ValueError("No valid YAML frontmatter found in source file.")

    if "id" not in meta:
        raise ValueError("Frontmatter is missing required field 'id'.")

    # Update metadata for canon
    meta = update_metadata_for_canon(meta, source_path)

    # Decide target directory and filename
    target_dir = infer_target_dir(meta, target_dir_override)
    target_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{meta['id']}.md"
    target_path = target_dir / filename

    # Combine frontmatter + body
    new_text = render_frontmatter(meta) + body

    if dry_run:
        print("[DRY RUN] Would write canon file to:", target_path)
    else:
        target_path.write_text(new_text, encoding="utf-8")
        print("[promote-to-canon] Wrote canon file to:", target_path.relative_to(ROOT))

    return target_path


# --- CLI ---------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Promote a staged markdown file into the canonical world/content trees."
    )
    parser.add_argument(
        "source",
        type=str,
        help="Path to staged markdown file (e.g. generation/staging/quests/2025.../quest-001.md).",
    )
    parser.add_argument(
        "--target-dir",
        type=str,
        default=None,
        help="Optional override for canonical target directory (relative to repo root). "
             "Example: 'world/lore' or 'content/quests'.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not write anything; just show what would happen.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source_path = (ROOT / args.source).resolve()

    print(f"[promote-to-canon] Repo root: {ROOT}")
    print(f"[promote-to-canon] Source: {source_path}")
    if args.target_dir:
        print(f"[promote-to-canon] Target override: {args.target_dir}")
    if args.dry_run:
        print("[promote-to-canon] DRY RUN mode enabled")

    try:
        promote_file(
            source_path=source_path,
            target_dir_override=args.target_dir,
            dry_run=args.dry_run,
        )
    except Exception as e:
        print("[promote-to-canon] ERROR:", e)
        raise SystemExit(1)


if __name__ == "__main__":
    main()