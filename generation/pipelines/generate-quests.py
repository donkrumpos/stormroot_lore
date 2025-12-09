#!/usr/bin/env python3
"""
Quest generation pipeline for Deluvia.

- Reads system prompt from: generation/prompts/system/quest-generator.md
- Calls an LLM to generate one or more quests following quest-template.md
- Writes them into: generation/staging/quests/<timestamp>/quest-###.md

Example usage:

    python3 generation/pipelines/generate-quests.py \
        --region rothigport \
        --element soil \
        --count 2 \
        --theme "dockworkers, humility vs vanity, poison mine rumors"

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
PROMPT_PATH = ROOT / "generation" / "prompts" / "system" / "quest-generator.md"
STAGING_ROOT = ROOT / "generation" / "staging" / "quests"


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
        model="gpt-4o-mini",  # adjust to your preferred/cheaper model
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
    Build a clear, structured user prompt for the quest generator.

    The system prompt already encodes:
      - Deluvia tone/voice
      - quest-template structure
      - system integration expectations

    Here we just specify context and count.
    """
    text = f"""
    I want you to generate {count} quests for my world Deluvia.

    Constraints:

    - Region: {region or "unspecified"}
    - Dominant element: {element or "unspecified"}
    - Overall theme / mood: {theme or "unspecified"}

    For EACH QUEST:

    - Use the quest-template.md structure exactly.
    - Begin with YAML frontmatter.
    - Use a stable kebab-case id.
    - Include source: ai-generated and status: draft in metadata.
    - Write in my mythic/whimsical, folkloric Deluvia tone.
    - Make sure the quest:
        - arises naturally from local conditions,
        - touches at least one virtue–vice tension,
        - hooks into at least one of: town-state, dungeon mutation, pantheon attention, or narrative engine.

    VERY IMPORTANT OUTPUT FORM:

    - Output the quests one after another.
    - Separate them with a line containing exactly: '---QUEST-END---'
      (without quotes) on its own line.
    - Do not add any explanation before, between, or after quests.
    - Do not wrap the output in code blocks.

    Now generate the quests.
    """
    return dedent(text).strip()


def make_batch_dir() -> Path:
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    batch_dir = STAGING_ROOT / timestamp
    batch_dir.mkdir(parents=True, exist_ok=True)
    return batch_dir


def split_quests(raw: str) -> list[str]:
    """
    Split the LLM output into individual quest documents.

    We expect quests to be separated by a line:

        ---QUEST-END---

    Returns a list of markdown strings.
    """
    parts = []
    current_lines = []

    for line in raw.splitlines():
        if line.strip() == "---QUEST-END---":
            if current_lines:
                parts.append("\n".join(current_lines).strip() + "\n")
                current_lines = []
        else:
            current_lines.append(line)

    # Catch last quest if no trailing separator
    if current_lines:
        parts.append("\n".join(current_lines).strip() + "\n")

    return [p for p in parts if p.strip()]


def write_quest_files(batch_dir: Path, quests: list[str]) -> list[Path]:
    paths = []
    for idx, quest_md in enumerate(quests, start=1):
        filename = f"quest-{idx:03d}.md"
        out_path = batch_dir / filename
        out_path.write_text(quest_md, encoding="utf-8")
        paths.append(out_path)
    return paths


# --- CLI ---------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate quests into generation/staging/quests/<timestamp>/"
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
        help="Free-form theme/mood, e.g. 'poison mine rumors, humble dockworkers, fungal omens'.",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=2,
        help="Number of quests to generate in this batch.",
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

    print(f"[generate-quests] Using system prompt: {PROMPT_PATH}")
    print(f"[generate-quests] Region={args.region} Element={args.element} Count={args.count}")
    print(f"[generate-quests] Calling LLM...")

    raw_output = call_llm(system_prompt, user_prompt)

    print(f"[generate-quests] LLM output length: {len(raw_output)} characters")

    quests = split_quests(raw_output)
    if not quests:
        raise RuntimeError("No quest documents found in LLM output. Check separators and prompt.")

    batch_dir = make_batch_dir()
    paths = write_quest_files(batch_dir, quests)

    print(f"[generate-quests] Wrote {len(paths)} quest files to:")
    for p in paths:
        print(f"  - {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()