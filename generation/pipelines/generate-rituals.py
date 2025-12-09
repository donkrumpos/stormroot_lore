#!/usr/bin/env python3
"""
Ritual generation pipeline for Deluvia.

- Reads system prompt from: generation/prompts/system/ritual-generator.md
- Calls an LLM to generate one or more rituals following ritual-template.md
- Writes them into: generation/staging/rituals/<timestamp>/ritual-###.md

Example usage:

    python3 generation/pipelines/generate-rituals.py \
        --region rothigport \
        --element soil \
        --count 4 \
        --theme "dockworkers, storms, beetlefolk humility, poison mine unease"

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
PROMPT_PATH = ROOT / "generation" / "prompts" / "system" / "ritual-generator.md"
STAGING_ROOT = ROOT / "generation" / "staging" / "rituals"


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
    Build a clear, structured user prompt for the ritual generator.

    The system prompt already encodes:
      - Deluvia tone/voice
      - ritual-template structure
      - system integration expectations

    Here we specify context + count.
    """
    text = f"""
    I want you to generate {count} rituals for my world Deluvia.

    Constraints:

    - Region: {region or "unspecified"}
    - Dominant element: {element or "unspecified"}
    - Overall theme / mood: {theme or "unspecified"}

    For EACH RITUAL:

    - Use the ritual-template.md structure exactly.
    - Begin with YAML frontmatter.
    - Use a stable kebab-case id.
    - Include source: ai-generated and status: draft in metadata.
    - Write in my mythic/whimsical, folkloric Deluvia tone.
    - Make the ritual feel actually performable in-world:
        - by villagers, beetlefolk, pilgrims, or solitary mages,
        - not just by epic heroes.
    - Anchor each ritual to at least one:
        - region or town,
        - element,
        - virtue–vice tension,
        - and at least one system hook:
            - town-state system,
            - narrative engine,
            - pantheon attention,
            - dungeon mutation.

    VERY IMPORTANT OUTPUT FORM:

    - Output the rituals one after another.
    - Separate them with a line containing exactly: '---RITUAL-END---'
      (without quotes) on its own line.
    - Do not add any explanation before, between, or after rituals.
    - Do not wrap the output in code blocks.

    Now generate the rituals.
    """
    return dedent(text).strip()


def make_batch_dir() -> Path:
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    batch_dir = STAGING_ROOT / timestamp
    batch_dir.mkdir(parents=True, exist_ok=True)
    return batch_dir


def split_rituals(raw: str) -> list[str]:
    """
    Split the LLM output into individual ritual documents.

    We expect rituals to be separated by a line:

        ---RITUAL-END---

    Returns a list of markdown strings.
    """
    parts = []
    current_lines = []

    for line in raw.splitlines():
        if line.strip() == "---RITUAL-END---":
            if current_lines:
                parts.append("\n".join(current_lines).strip() + "\n")
                current_lines = []
        else:
            current_lines.append(line)

    # Catch last ritual if no trailing separator
    if current_lines:
        parts.append("\n".join(current_lines).strip() + "\n")

    return [p for p in parts if p.strip()]


def write_ritual_files(batch_dir: Path, rituals: list[str]) -> list[Path]:
    paths = []
    for idx, ritual_md in enumerate(rituals, start=1):
        filename = f"ritual-{idx:03d}.md"
        out_path = batch_dir / filename
        out_path.write_text(ritual_md, encoding="utf-8")
        paths.append(out_path)
    return paths


# --- CLI ---------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate rituals into generation/staging/rituals/<timestamp>/"
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
        help="Free-form theme/mood, e.g. 'dockworkers, storms, beetlefolk, poison omens'.",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=4,
        help="Number of rituals to generate in this batch.",
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

    print(f"[generate-rituals] Using system prompt: {PROMPT_PATH}")
    print(f"[generate-rituals] Region={args.region} Element={args.element} Count={args.count}")
    print(f"[generate-rituals] Calling LLM...")

    raw_output = call_llm(system_prompt, user_prompt)

    print(f"[generate-rituals] LLM output length: {len(raw_output)} characters")

    rituals = split_rituals(raw_output)
    if not rituals:
        raise RuntimeError("No ritual documents found in LLM output. Check separators and prompt.")

    batch_dir = make_batch_dir()
    paths = write_ritual_files(batch_dir, rituals)

    print(f"[generate-rituals] Wrote {len(paths)} ritual files to:")
    for p in paths:
        print(f"  - {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()