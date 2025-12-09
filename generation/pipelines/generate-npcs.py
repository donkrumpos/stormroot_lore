#!/usr/bin/env python3
"""
Simple NPC generation pipeline for Deluvia.

- Reads system prompt from: generation/prompts/system/npc-generator.md
- Calls an LLM to generate NPCs following npc-template.md
- Writes them into: generation/staging/npcs/<timestamp>/npc-###.md

You can run, for example:

    python3 generation/pipelines/generate-npcs.py \
        --region rothigport \
        --element soil \
        --count 3 \
        --theme "dockworkers, beetlefolk rumors, humble storm-prep"

Requirements:
    - Python 3.9+
    - openai >= 1.0.0 (or swap out the LLM client with your own)
    - OPENAI_API_KEY set in your environment (if using OpenAI)
"""

import argparse
import datetime as dt
import os
from pathlib import Path
from textwrap import dedent

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


# --- Paths -------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]  # repo root = stormroot/
PROMPT_PATH = ROOT / "generation" / "prompts" / "system" / "npc-generator.md"
STAGING_ROOT = ROOT / "generation" / "staging" / "npcs"


# --- LLM Wrapper -------------------------------------------------------

def call_llm(system_prompt: str, user_prompt: str) -> str:
    """
    Call the LLM and return raw markdown text.

    This uses OpenAI's Python client by default, but you can:
      - swap it for Anthropic / Kagi / etc.
      - or plug into your own routing layer.

    IMPORTANT:
        The system prompt should already instruct the model to:
        - follow npc-template.md
        - include YAML frontmatter
        - mark source: ai-generated, status: draft, etc.
    """
    if not OPENAI_AVAILABLE:
        raise RuntimeError(
            "openai package not installed. "
            "Install with `pip install openai` or adapt call_llm() to your provider."
        )

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-5.1-mini",  # or your preferred model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        top_p=0.9,
    )

    return response.choices[0].message.content.strip()


# --- Helpers -----------------------------------------------------------

def load_system_prompt() -> str:
    if not PROMPT_PATH.exists():
        raise FileNotFoundError(f"System prompt not found: {PROMPT_PATH}")
    return PROMPT_PATH.read_text(encoding="utf-8")


def build_user_prompt(region: str, element: str, theme: str, count: int) -> str:
    """
    Build a clear, structured user prompt.

    The system prompt already sets tone and template; this just tells it
    what *kind* of NPCs to grow.
    """
    text = f"""
    I want you to generate {count} NPCs for my world Deluvia.

    Constraints:

    - Region: {region or "unspecified"}
    - Dominant element: {element or "unspecified"}
    - Overall theme / mood: {theme or "unspecified"}

    For EACH NPC:

    - Use the npc-template.md structure exactly.
    - Begin with YAML frontmatter.
    - Use a stable kebab-case id.
    - Include source: ai-generated and status: draft in metadata.
    - Write in my mythic/whimsical, folkloric tone for Deluvia.
    - Make sure the NPC hooks into:
        - the local region,
        - at least one virtue–vice tension,
        - and at least one potential story hook.

    VERY IMPORTANT OUTPUT FORM:

    - Output the NPCs one after another.
    - Separate them with a line containing exactly: '---NPC-END---'
      (without quotes) on its own line.
    - Do not add any explanation before, between, or after NPCs.
    - Do not wrap the output in code blocks.

    Now generate the NPCs.
    """
    return dedent(text).strip()


def make_batch_dir() -> Path:
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    batch_dir = STAGING_ROOT / timestamp
    batch_dir.mkdir(parents=True, exist_ok=True)
    return batch_dir


def split_npcs(raw: str) -> list[str]:
    """
    Split the LLM output into individual NPC documents.

    We expect NPCs to be separated by a line:

        ---NPC-END---

    Returns a list of markdown strings.
    """
    parts = []
    current_lines = []

    for line in raw.splitlines():
        if line.strip() == "---NPC-END---":
            if current_lines:
                parts.append("\n".join(current_lines).strip() + "\n")
                current_lines = []
        else:
            current_lines.append(line)

    # catch last one if no trailing separator
    if current_lines:
        parts.append("\n".join(current_lines).strip() + "\n")

    return [p for p in parts if p.strip()]


def write_npc_files(batch_dir: Path, npcs: list[str]) -> list[Path]:
    paths = []
    for idx, npc_md in enumerate(npcs, start=1):
        filename = f"npc-{idx:03d}.md"
        out_path = batch_dir / filename
        out_path.write_text(npc_md, encoding="utf-8")
        paths.append(out_path)
    return paths


# --- CLI ---------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate NPCs into generation/staging/npcs/<timestamp>/"
    )
    parser.add_argument(
        "--region",
        type=str,
        default="unspecified-region",
        help="Region id or name (e.g. rothigport, loamstead-soil).",
    )
    parser.add_argument(
        "--element",
        type=str,
        default="unspecified-element",
        help="Dominant element (e.g. soil, water, storm, poison).",
    )
    parser.add_argument(
        "--theme",
        type=str,
        default="",
        help="Free-form theme/mood, e.g. 'dockworkers, humble storms, beetlefolk rumors'.",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=3,
        help="Number of NPCs to generate in this batch.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    system_prompt = load_system_prompt()
    user_prompt = build_user_prompt(
        region=args.region,
        element=args.element,
        theme=args.theme,
        count=args.count,
    )

    print(f"[generate-npcs] Using system prompt: {PROMPT_PATH}")
    print(f"[generate-npcs] Region={args.region} Element={args.element} Count={args.count}")
    print(f"[generate-npcs] Calling LLM...")

    raw_output = call_llm(system_prompt, user_prompt)

    print(f"[generate-npcs] LLM output length: {len(raw_output)} characters")

    npcs = split_npcs(raw_output)
    if not npcs:
        raise RuntimeError("No NPC documents found in LLM output. Check separators and prompt.")

    batch_dir = make_batch_dir()
    paths = write_npc_files(batch_dir, npcs)

    print(f"[generate-npcs] Wrote {len(paths)} NPC files to:")
    for p in paths:
        print(f"  - {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()