---
id: procedural-storytelling
type: system
title: "Procedural Storytelling in Deluvia"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - narrative
  - procedural
  - storytelling
  - ai
  - systems
links:
  related:
    - narrative-engine
    - story-looms
    - narrative-ecology
    - player-action-canon-engine
---

# Procedural Storytelling in Deluvia

## Mythic Introduction
Deluvia does not write stories in straight lines.  
It grows them — like lichen on stone, fungus under roots, stories braided into the wind.

When a traveler crosses a threshold, the world does not open a pre-written chapter.  
Instead, it **listens**: to where they came from, what they’ve done, which gods are watching, which wounds are unhealed.  
Then, Deluvia reaches into its underworld of memory, pulls a handful of loose threads, and knots them into something new.

Procedural storytelling in Deluvia is not a machine that spits out random quests.  
It is a **garden of half-remembered myths**, constantly reseeded by players, gods, and the land itself.

---

# Purpose of This Document

This document defines how Deluvia:

- takes in **inputs** (player state, regional tone, Chronicle entries)
- uses **templates, seeds, and constraints** to shape narrative output
- stitches stories into the world in a way that feels:
  - coherent
  - contextual
  - mythically resonant
  - replayable without feeling generic

It is the design companion to [`narrative_engine.md`], focused on **how stories are generated**, not just how the world reacts.

---

# Design Goals

Procedural storytelling in Deluvia must:

1. **Honor the World’s Tone**  
   Stories should feel like they grew out of Deluvia’s soil, not dropped in from another game.

2. **Respond to Player History**  
   Two players standing in the same town should not always receive the same story seeds. The Chronicle matters.

3. **Use Reusable Structures, Not Hardcoded Plots**  
   Stories are woven from patterns (Story Looms, seeds, motifs), not hand-authored branches.

4. **Remain Legible to Builders**  
   You (and future collaborators) must be able to:
   - see where stories are coming from
   - debug why a given event appeared
   - adjust knobs without rewriting everything

5. **Be Safe to Delegate to AI**  
   AI generation should:
   - work within strict templates
   - respect canon
   - never overwrite SSOT
   - always stage output for review before promotion

---

# Core Concepts

## Story Seeds

A **Story Seed** is the smallest meaningful narrative unit the system can plant.

- It is not a full quest.
- It is a “why” plus a “where,” wrapped in a mythic mood.
- Multiple seeds can braid together into an arc.

Example seed format:

~~~~yaml
story_seed:
  id: seed-rothigport-missing-fisher
  scope: canon      # canon | internal | experimental
  visibility: internal
  status: active
  confidence: medium

  region: rothigport
  domain: water      # memory / emotional resonance
  virtue_focus: humility
  tone: wistful      # tonal tag for AI + selection

  triggers:
    min_player_level: 3
    required_flags:
      - visited_rothigport_docks
    excluded_flags:
      - resolved-missing-fisher-arc

  prompt_hook: missing-fisher
  summary: >
    A beloved fisher has vanished after sailing into waters touched by the Severing.
    The town worries quietly; the sea remembers loudly.

  escalation_potential:
    - dockside rumors
    - shrine intervention
    - involvement of a minor water god
~~~~

Seeds live in SSOT as **design-time data**, not code.  
Generators pull from these, not from raw free-form prompts.

---

## Story Patterns (Looms)

Story Patterns — or **Story Looms** — are reusable narrative shapes, like:

- “Lost and Found”
- “A Debt Comes Due”
- “The Silence Before the Storm”
- “The Thing Beneath the Shrine”
- “The Broken Oath”

Each Loom defines:

- required roles (seeker, witness, obstacle, hidden force)
- required locations (origin, threshold, unknown, return)
- emotional arc (fear → wonder, shame → humility, hubris → fall → grace)
- mechanical hooks (quests, status flags, events)

Example loom skeleton:

~~~~yaml
story_loom:
  id: loom-lost-and-found
  title: "Lost and Found"
  scope: internal
  status: active

  roles:
    seeker: character
    lost_thing: object | person | memory
    witness: character | location
    hidden_force: god | curse | environmental

  beats:
    - id: call
      description: Someone or something dear is missing.
      emotional_color: longing
    - id: descent
      description: The search leads into a place of risk or revelation.
      emotional_color: uncertainty
    - id: encounter
      description: The truth behind the loss is revealed or partially glimpsed.
      emotional_color: awe | sorrow
    - id: return
      description: Something is brought back, though never in the same form.
      emotional_color: bittersweet

  suitable_domains:
    - water
    - moon
    - death
~~~~

Procedural storytelling selects **Seeds + Looms** and lets the Narrative Engine bind them to the world state.

---

## Story Constraints

Constraints keep generated stories from:

- breaking lore
- ignoring geography
- contradicting current virtue/vice balance
- repeating too often

Common constraints:

- region must match the seed
- element/domain alignment must not wildly conflict with regional tone
- virtue arc must make sense relative to local dyads
- NPC involved must exist (or be generated in a compatible way)
- dungeons used must be accessible and appropriate difficulty

Constraints are applied *before* any AI text generation.

---

# High-Level Flow

Procedural storytelling follows this loop:

1. **Gather Context**
   - Player state (level, flags, virtues touched, Chronicle history)
   - Regional tone (from story_thread)
   - Active or latent seeds in the region
   - Available Looms compatible with the current narrative state

2. **Select Seed(s) + Loom**
   - Filter seeds for:
     - region
     - triggers met
     - not already resolved
   - Filter looms by:
     - domain alignment
     - emotional arc fit
   - Pick 1–3 seeds and a Loom to bind them.

3. **Assemble a Story Skeleton**
   - Map roles (seeker, witness, hidden force, etc.) to:
     - existing NPCs
     - new minor NPCs
     - existing locations/dungeons
   - Assign beats to locations and events.

4. **Generate or Retrieve Text**
   - Use AI **within strict templates** to draft:
     - rumors
     - quest descriptions
     - shrine whispers
     - small flavor scenes
   - All AI output goes to `generation/staging/` for review.

5. **Integrate with Mechanics**
   - Link beats to:
     - quest flags
     - dungeon variants
     - NPC states
     - Chronicle entries

6. **Evolve Over Time**
   - As the player acts:
     - Chronicle updates
     - Narrative Engine shifts tone
     - New seeds become available
     - Looms can resolve, fracture, or echo elsewhere

---

# Data Structures

## Story Template (for AI + Content)

This is the format AI-friendly generators will target.

~~~~yaml
story_template:
  id: tmpl-rothigport-water-mystery
  type: regional-story
  scope: internal
  status: active

  region: rothigport
  domains:
    - water
    - soil
  virtues:
    primary: humility
    secondary: truth

  supported_looms:
    - loom-lost-and-found
    - loom-silence-before-storm

  ai_prompt_profile:
    system_prompt_ref: sys-proc-story-seaside
    max_tokens: 800
    tone: "somber, sea-worn, gently uncanny"

  required_slots:
    - missing_person
    - worried_npc
    - threshold_location
    - deep_place
    - small_god_or_spirit
~~~~

The generator will fill this with concrete entities and then write staged output to markdown.

---

## Generated Story Instance (Staged)

When the system builds a specific story instance, it writes a file like:

~~~~yaml
story_instance:
  id: story-rothigport-missing-fisher-001
  scope: internal
  visibility: internal
  status: draft
  confidence: low
  source: ai-generated

  seed_id: seed-rothigport-missing-fisher
  loom_id: loom-lost-and-found
  template_id: tmpl-rothigport-water-mystery

  region: rothigport
  domains:
    - water
    - soil

  involved_npcs:
    - npc-rosage
    - npc-dockmaster-len
  locations:
    - loc-rothigport-docks
    - loc-seaward-cave
    - loc-hidden-shrine-of-memory

  beats:
    - id: call
      description: "Dockside rumors of a fisher gone missing three nights ago."
      triggered_by: visit_rothigport_docks
    - id: descent
      description: "Following kelp-slick footprints and broken crab traps to a seaward cave."
      triggered_by: investigate-missing-fisher
    - id: encounter
      description: "A tideborn spirit offers a memory in exchange for something forgotten."
      triggered_by: enter-seaward-cave
    - id: return
      description: "Return to Rothigport with either the fisher, their boat, or only a memory."
      triggered_by: exit-cave

  text_blocks:
    intro_rumor: |
      The waves have been oddly quiet about Jorren. Boats return, gulls scream,
      ropes creak, but no one has seen his lantern on the water these last three nights.
      The dockmaster speaks his name softly, as if not to wake the sea.

    shrine_whisper: |
      "The sea does not lose what it loves," murmurs the barnacled stone.
      "It simply hides things until they are remembered properly."

  review_notes: |
    - Check tone against Rothigport canon.
    - Confirm NPC names match SSOT.
    - Ensure dungeon hooks align with Niv Rath Hollow / coastal caves.
~~~~

Only after **human review** does this become canon or get promoted into a quest or encounter definition.

---

# Relationship to the Narrative Engine

Procedural storytelling **feeds** and **is fed by** the Narrative Engine:

- Seeds and Looms are selected based on:
  - current story_thread tone
  - virtue/vice balance
  - Chronicle events

- Generated stories, once acted upon, produce:
  - new Story Signals
  - Chronicle entries
  - shifts in regional tone

This creates a loop:

> Player acts → World shifts → New story seeds → New stories → Player acts again

The goal is for this cycle to feel **inevitable and surprising** at once.

---

# Implementation Notes (High-Level)

- This document lives in SSOT and should stay:
  - human-readable
  - implementation-agnostic (Denizen, YAML, DB schema, etc.)

- Concrete generators will live in:
  - `generation/pipelines/`
  - `generation/templates/`
  - `generation/staging/`

- AI involvement:
  - strictly template-based
  - never writes directly to `world/` or `content/`
  - always tagged `source: ai-generated` with `confidence: low` until reviewed

---

# Canonical Truths

- Stories in Deluvia are **grown**, not randomly rolled.
- Seeds, Looms, and Constraints form the backbone of procedural narrative.
- The Narrative Engine and procedural storytelling are two halves of the same living system.
- AI-generated text is always subordinate to SSOT and requires human review.
- Players are not just consuming stories — they are **co-authoring Deluvia’s mythic compost heap** with every deed.
