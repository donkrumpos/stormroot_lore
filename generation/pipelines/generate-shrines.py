#!/usr/bin/env python3
"""
Shrine generation pipeline for Deluvia.

- Reads system prompt from: generation/prompts/system/shrine-generator.md
- Calls an LLM to generate one or more shrines following shrine-template.md
- Writes them into: generation/staging/shrines/<timestamp>/shrine-###.md

Example usage:

    python3 generation/pipelines/generate-shrines.py \
        --region rothigport \
        --element soil \
        --count 3 \
        --theme "harbor humility, beetlefolk tunnels, poison mine omens"

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
PROMPT_PATH = ROOT / "generation" / "prompts" / "system" / "shrine-generator.md"
STAGING_ROOT = ROOT / "generation" / "staging" / "shrines"


# --- LLM Wrapper -------------------------------------------------------

def call_llm(system_prompt: str, user_prompt: str) -> str:
    """
    Call the LLM and return raw markdown text.

    Swap this implementation if you prefer Anthropic, Kagi, etc.
    Just keep the contract: return a single markdown string.
    """
    if not OPENAI_AVAILABLE:
        raise RuntimeError(
            "openai package not installed. "
            "Install with `pip install openai` or adapt call_llm() to your provider."
        )

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-5.1-mini",  # adjust to your preferred model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.75,
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
    Build a clear, structured user prompt for the shrine generator.

    The system prompt already encodes:
      - Deluvia tone/voice
      - shrine-template structure
      - system integration expectations

    Here we specify context + count.
    """
    text = f"""
    I want you to generate {count} shrines for my world Deluvia.

    Constraints:

    - Region: {region or "unspecified"}
    - Dominant element: {element or "unspecified"}
    - Overall theme / mood: {theme or "unspecified"}

    For EACH SHRINE:

    - Use the shrine-template.md structure exactly.
    - Begin with YAML frontmatter.
    - Use a stable kebab-case id.
    - Include source: ai-generated and status: draft in metadata.
    - Write in my mythic/whimsical, folkloric Deluvia tone.
    - Make the shrine feel like a real devotional site:
        - who tends it,
        - what offerings look like,
        - what omens appear,
        - how ordinary folk interact with it.
    - Anchor each shrine to at least one:
        - region or town,
        - element,
        - virtue–vice tension,
        - and at least one system hook:
            - pantheon attention system,
            - town-state system,
            - dungeon mutation engine,
            - narrative engine (story signals / domains).

    VERY IMPORTANT OUTPUT FORM:

    - Output the shrines one after another.
    - Separate them with a line containing exactly: '---SHRINE-END---'
      (without quotes) on its own line.
    - Do not add any explanation before, between, or after shrines.
    - Do not wrap the output in code blocks.

    Now generate the shrines.
    """
    return dedent(text).strip()


def make_batch_dir() -> Path:
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    batch_dir = STAGING_ROOT / timestamp
    batch_dir.mkdir(parents=True, exist_ok=True)
    return batch_dir


def split_shrines(raw: str) -> list[str]:
    """
    Split the LLM output into individual shrine documents.

    We expect shrines to be separated by a line:

        ---SHRINE-END---

    Returns a list of markdown strings.
    """
    parts = []
    current_lines = []

    for line in raw.splitlines():
        if line.strip() == "---SHRINE-END---":
            if current_lines:
                parts.append("\n".join(current_lines).strip() + "\n")
                current_lines = []
        else:
            current_lines.append(line)

    # Catch last shrine if no trailing separator
    if current_lines:
        parts.append("\n".join(current_lines).strip() + "\n")

    return [p for p in parts if p.strip()]


def write_shrine_files(batch_dir: Path, shrines: list[str]) -> list[Path]:
    paths = []
    for idx, shrine_md in enumerate(shrines, start=1):
        filename = f"shrine-{idx:03d}.md"
        out_path = batch_dir / filename
        out_path.write_text(shrine_md, encoding="utf-8")
        paths.append(out_path)
    return paths


# --- CLI ---------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate shrines into generation/staging/shrines/<timestamp>/"
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
        help="Free-form theme/mood, e.g. 'harbor humility, beetlefolk tunnels, poison omens'.",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=3,
        help="Number of shrines to generate in this batch.",
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

    print(f"[generate-shrines] Using system prompt: {PROMPT_PATH}")
    print(f"[generate-shrines] Region={args.region} Element={args.element} Count={args.count}")
    print(f"[generate-shrines] Calling LLM...")

    raw_output = call_llm(system_prompt, user_prompt)

    print(f"[generate-shrines] LLM output length: {len(raw_output)} characters")

    shrines = split_shrines(raw_output)
    if not shrines:
        raise RuntimeError("No shrine documents found in LLM output. Check separators and prompt.")

    batch_dir = make_batch_dir()
    paths = write_shrine_files(batch_dir, shrines)

    print(f"[generate-shrines] Wrote {len(paths)} shrine files to:")
    for p in paths:
        print(f"  - {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()