#!/usr/bin/env python3
"""
Lore fragment generation pipeline for Deluvia.

- Reads system prompt from: generation/prompts/system/lore-fragment-generator.md
- Calls an LLM to generate one or more lore fragments following lore-fragment-template.md
- Writes them into: generation/staging/lore/<timestamp>/fragment-###.md

Example usage:

    python3 generation/pipelines/generate-lore-fragments.py \
        --region rothigport \
        --element soil \
        --count 5 \
        --theme "dockworkers, beetlefolk sayings, poison mine rumors"

Requirements:
    - Python 3.9+
    - openai >= 1.0.0 (or adapt call_llm() for your provider)
    - OPENAI_API_KEY set in your environment (if using OpenAI)
"""

import argparse
import datetime as dt
from pathlib import Path
from textwrap import dedent

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


# --- Paths -------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]  # repo root = stormroot/
PROMPT_PATH = ROOT / "generation" / "prompts" / "system" / "lore-fragment-generator.md"
STAGING_ROOT = ROOT / "generation" / "staging" / "lore"


# --- LLM Wrapper -------------------------------------------------------

def call_llm(system_prompt: str, user_prompt: str) -> str:
    """
    Call the LLM and return raw markdown text.

    You can swap this implementation for Anthropic, Kagi, etc.
    The important contract is: return a single markdown string.
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
        temperature=0.8,
        top_p=0.95,
    )

    return response.choices[0].message.content.strip()


# --- Helpers -----------------------------------------------------------

def load_system_prompt() -> str:
    if not PROMPT_PATH.exists():
        raise FileNotFoundError(f"System prompt not found: {PROMPT_PATH}")
    return PROMPT_PATH.read_text(encoding="utf-8")


def build_user_prompt(region: str, element: str, theme: str, count: int) -> str:
    """
    Build a clear, structured user prompt for the lore fragment generator.

    The system prompt already encodes:
      - Deluvia tone/voice
      - lore-fragment-template structure
      - integration expectations

    Here we just specify context + count.
    """
    text = f"""
    I want you to generate {count} lore fragments for my world Deluvia.

    Constraints:

    - Region: {region or "unspecified"}
    - Dominant element: {element or "unspecified"}
    - Overall theme / mood: {theme or "unspecified"}

    For EACH FRAGMENT:

    - Use the lore-fragment-template.md structure exactly.
    - Begin with YAML frontmatter.
    - Use a stable kebab-case id.
    - Include source: ai-generated and status: draft in metadata.
    - Write in my mythic/whimsical, folkloric Deluvia tone.
    - Make the fragment clearly in-world: inscriptions, prayers, gossip, notes, field reports, etc.
    - Anchor each fragment to at least one:
        - region or town,
        - element,
        - virtue–vice tension,
        - and potential story hook (quest, shrine, dungeon, NPC memory, omen).

    VERY IMPORTANT OUTPUT FORM:

    - Output the fragments one after another.
    - Separate them with a line containing exactly: '---FRAGMENT-END---'
      (without quotes) on its own line.
    - Do not add any explanation before, between, or after fragments.
    - Do not wrap the output in code blocks.

    Now generate the lore fragments.
    """
    return dedent(text).strip()


def make_batch_dir() -> Path:
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    batch_dir = STAGING_ROOT / timestamp
    batch_dir.mkdir(parents=True, exist_ok=True)
    return batch_dir


def split_fragments(raw: str) -> list[str]:
    """
    Split the LLM output into individual lore fragment documents.

    We expect fragments to be separated by a line:

        ---FRAGMENT-END---

    Returns a list of markdown strings.
    """
    parts = []
    current_lines = []

    for line in raw.splitlines():
        if line.strip() == "---FRAGMENT-END---":
            if current_lines:
                parts.append("\n".join(current_lines).strip() + "\n")
                current_lines = []
        else:
            current_lines.append(line)

    # Catch last fragment if no trailing separator
    if current_lines:
        parts.append("\n".join(current_lines).strip() + "\n")

    return [p for p in parts if p.strip()]


def write_fragment_files(batch_dir: Path, fragments: list[str]) -> list[Path]:
    paths = []
    for idx, frag_md in enumerate(fragments, start=1):
        filename = f"fragment-{idx:03d}.md"
        out_path = batch_dir / filename
        out_path.write_text(frag_md, encoding="utf-8")
        paths.append(out_path)
    return paths


# --- CLI ---------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate lore fragments into generation/staging/lore/<timestamp>/"
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
        help="Free-form theme/mood, e.g. 'dockworkers, beetlefolk, fungal omens, poison mine collapse'.",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=5,
        help="Number of lore fragments to generate in this batch.",
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

    print(f"[generate-lore-fragments] Using system prompt: {PROMPT_PATH}")
    print(f"[generate-lore-fragments] Region={args.region} Element={args.element} Count={args.count}")
    print(f"[generate-lore-fragments] Calling LLM...")

    raw_output = call_llm(system_prompt, user_prompt)

    print(f"[generate-lore-fragments] LLM output length: {len(raw_output)} characters")

    fragments = split_fragments(raw_output)
    if not fragments:
        raise RuntimeError("No lore fragment documents found in LLM output. Check separators and prompt.")

    batch_dir = make_batch_dir()
    paths = write_fragment_files(batch_dir, fragments)

    print(f"[generate-lore-fragments] Wrote {len(paths)} lore fragment files to:")
    for p in paths:
        print(f"  - {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()