---
id: generation-index
type: index
title: "Generation Layer Overview"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - generation
  - narrative
  - systems
  - ai
---

# Generation Layer Overview

This directory is the **procedural and AI heart** of Deluvia.  
It does **not** store lore directly and it is **not** implementation code.

Instead, it defines:

- how I generate NPCs, dungeons, quests, items, shrines, and lore fragments  
- how I stage and review AI output before it becomes canon  
- how world systems (virtue–vice, pantheon attention, town-state, dungeon mutation) react to player actions  
- how nightly or periodic jobs can keep the world breathing while I sleep  

If the rest of the project is *what* Deluvia is, this layer is *how* Deluvia keeps telling new stories.

---

## High-Level Flow

Conceptually, the generation layer follows this loop:

1. **Seeds** — I provide structured seeds, name lists, trait pools, regional flavors.
2. **Prompts** — I define strict system prompts that tell AI how to think and how to use my templates.
3. **Templates** — I define the structure of NPCs, dungeons, quests, rituals, items, lore fragments, shrines.
4. **Pipelines** — scripts call the AI, fill templates, and write output into `staging/`.
5. **Staging** — I (or future tools) review, prune, and revise generated content.
6. **Promotion** — approved content is moved into the appropriate `world/`, `systems/`, or `content/` directory and becomes canon, with metadata indicating it was ai-generated.
7. **Feedback** — as players act, world systems (narrative engine, town-state, pantheon attention, dungeon mutation) feed back into seeds and prompts, shaping future generations.

Nothing should go directly from AI into canon.  
`generation/` is the **gardener’s shed**, not the shrine.

---

## Core System Docs (Conceptual Spine)

These files define the main narrative and simulation systems that generation plugs into:

- `narrative-engine.md`  
  - How Story Signals become world reactions, regional tone, and emergent story.

- `narrative-ecology.md`  
  - How towns, dungeons, shrines, gods, and wilderness form a living story-ecosystem.

- `procedural-storytelling.md`  
  - How I use procedural systems (not just randomness) to grow story instead of scripting it.

- `story-looms.md`  
  - The long-running story arcs and “looms” that smaller events and quests weave into.

- `player-action-canon-engine.md`  
  - How player choices are evaluated as candidates for canon, and how they change the world.

- `story-seed-engine.md`  
  - How I generate and manage reusable seeds for NPCs, quests, dungeons, and lore fragments.

---

## System Docs: World-State & Simulation

These files describe how the simulation components behave:

- `npc-memory-system.md`  
  - How NPCs remember player deeds and how those memories matter over time.

- `town-state-system.md`  
  - How each town’s mood, virtue/vice, economy, and events shift in response to story.

- `dungeon-mutation-engine.md`  
  - How dungeons change over time: corruption, layouts, boss aspects, environmental overlays.

- `pantheon-attention-system.md`  
  - How the gods notice or ignore regions and actions, and what that attention does.

- `virtue-vice-system.md`  
  - How virtues and vices are treated as mythic physics rather than simple morality.

- `mythic-vector-system.md`  
  - How I track multi-dimensional “mythic vectors” (elements, virtues, tones) to drive emergent behavior.

- `twelve-elements.md`  
  - The Twelve Elements and how they function as narrative, magical, and ecological axes.

- `magic-system-overview.md`  
  - High-level rules and metaphysics of magic as a lived, systemic practice in Deluvia.

---

## Templates

These are **not** content. They are **shapes** that content must take.

Located in `generation/templates/`:

- `npc-template.md`  
  - Structure for all NPCs: identity, personality, hooks, relationships, system hooks.

- `dungeon-template.md`  
  - Structure for dungeons and deep places: origin, zones, set-pieces, mutations, system integration.

- `quest-template.md`  
  - Structure for quests and arcs: premise, flow, decisions, system hooks, consequences.

- `lore-fragment-template.md`  
  - Structure for lore fragments: myths, inscriptions, gossip, poems, apocrypha.

- `ritual-template.md`  
  - Structure for rituals and rites: requirements, procedure, outcomes, system hooks.

- `item-template.md`  
  - Structure for relics and items: origin, properties, costs, integration into systems.

- `shrine-template.md`  
  - Structure for shrines and altars: alignment, rituals, blessings, curses, system roles.

Future templates (optional, later):

- shrine-network  
- omen  
- seasonal-event  
- faction  

---

## Prompts

`generation/prompts/` is where I teach AI how to behave in this world.

Planned structure:

- `prompts/system/`  
  - System prompts for:
    - npc-generation  
    - dungeon-generation  
    - quest-generation  
    - lore-fragment-generation  
    - ritual-generation  
    - item-generation  
    - shrine-generation  

- `prompts/examples/`  
  - Few-shot examples for each generator.

- `prompts/constraints/`  
  - Tone and style guide (Miyazaki/Froud whimsy, Deluvic mythic voice, no generic fantasy slop).  
  - Hard constraints (no breaking core cosmology, no contradicting canon ids, etc.).

Prompts + templates define the **grammar** of Deluvia for AI collaborators.

---

## Seeds

`generation/seeds/` contains curated inputs for generation:

- `name-lists/`  
  - Names by culture, region, element, creature type.

- `trait-pools/`  
  - Personality traits, flaws, motifs, aesthetics.

- `regional-flavor/`  
  - Descriptive fragments and motifs bound to specific regions or biomes.

Seeds keep procedural content from feeling generic. They tether generation to the soil.

---

## Staging

`generation/staging/` is where AI outputs go **before** becoming canon:

- `staging/npcs/`  
- `staging/quests/`  
- `staging/lore/`  

Everything in `staging/` is:

- marked `status: draft` and `confidence: low`  
- clearly tagged with `source: ai-generated`  
- waiting for review, pruning, or rewriting  

This is where I act as editor, not stenographer.

---

## Pipelines

`generation/pipelines/` will hold scripts that automate flows, for example:

- `generate-npcs.py`  
  - read seeds → call AI with npc system prompt + template → write to `staging/npcs/`.

- `generate-quests.py`  
  - generate quest outlines tied to specific regions, towns, or dungeons.

- `generate-dungeons.py`  
  - propose new dungeon variants or deep layers using dungeon templates.

- `promote-to-canon.py`  
  - move reviewed drafts from `staging/` into `world/` or `content/` with updated metadata.

- `update-world-state.py`  
  - read Chronicle / Story Signals → adjust town-state, dungeon mutation, pantheon attention.

These pipelines turn this directory from philosophy into machinery.

---

## How This Layer Relates to the Rest of the Project

- `world/`  
  - Holds canonical truth: gods, towns, cultures, regions, bestiary.  
  - **Receives** new content from `generation/` after review.

- `systems/`  
  - Describes rules and mechanics (many of which are defined here first).  
  - **Defines** what pipelines and generators are allowed to do.

- `content/`  
  - Holds authored encounters, quests, dialogues, dungeons.  
  - **Grows** partly by hand, partly by promoted generations.

- `implementation/`  
  - Denizen scripts, data files, configs.  
  - **Implements** behaviors specified by systems and fed by canon content.

This `generation/` layer sits between design and implementation:  
it is my **mythic factory**, my **story workshop**, my **automation lab**.

---

## Working Agreements (for Future Me)

- No AI output enters `world/` or `content/` without passing through `staging/`.  
- Every generated entity gets:
  - a stable `id`
  - `source: ai-generated`
  - `confidence: low` or `medium` until I review it.
- Systems docs in this folder define behavior; canonical truth lives elsewhere.
- When in doubt: favor **fewer, stronger systems** over many one-off generators.
- If this file feels out of date, I revise it first before expanding the layer further.

