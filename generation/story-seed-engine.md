---
id: story-seed-engine
type: system
title: "The Story Seed Engine"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - narrative
  - seeds
  - procedural
  - quests
  - design
links:
  related:
    - narrative-engine
    - procedural-storytelling
    - mythic-vector-system
    - virtue-vice-system
    - npc-memory-system
---

# The Story Seed Engine

## Mythic Introduction

Deluvia is full of half-formed stories.

Not every tale arrives as a fully scripted quest.  
Most begin as **seeds** — a rumor, a strange bloom by the roadside,  
a beetlefolk caravan arriving out of season, a shrine light that won’t stay lit.

I don’t want a world filled with pre-written questlines alone.  
I want a world where **the state of the world itself** keeps generating new threads.

The Story Seed Engine is how I turn shifting world-state into countless, small, living hooks.

---

# Design Intent

I use the Story Seed Engine to:

- transform **raw world data** into narrative hooks  
- keep the world feeling **fertile**, not empty  
- avoid writing every quest by hand  
- tie procedural quests to the **Mythic Vector System** and **Virtue–Vice** drift  
- let NPC memory, dungeon states, and regional vectors all co-author story opportunities  
- support both AI-assisted and hand-authored quest content  

A “story seed” is lighter than a quest: it’s a **prompt in the world**, not a script.

---

# What is a Story Seed?

A **Story Seed** is:

- a localized cluster of:
  - world conditions
  - tensions
  - needs
  - symbols

- expressed as:
  - a short premise  
  - an initial hook  
  - a few possible directions  

It is **not**:
- a fully branched narrative  
- a guarantee of resolution  
- a forced marker on the player’s map  

It is an invitation.

---

# Seed Structure

I encode seeds in a simple YAML-based structure:

~~~~yaml
story_seed:
  id: seed-rothigport-fog-beggars
  region: rothigport
  source: system | hand-authored | ai-assisted

  triggers:
    virtue_thresholds:
      humility: "> 2"
      vanity: "< -1"
    elements:
      water: "> 1.0"
      soil: "> 0.5"
    dungeon_states:
      - vanitas: "corruption_level > 0.7"
    npc_flags:
      - meek_has_been_met
    world_flags:
      - severing_omens_visible

  hook: >
    Beggars in Rothigport begin speaking in the same eerie, borrowed voice,
    warning of a tide that will not recede.

  tensions:
    - the sea remembers a broken promise
    - the poor feel the first pressure of the coming storm
    - Vanitas leaks poison-dreams into waking minds

  outcomes_hint:
    - appease the sea through humble rites
    - ignore the warnings, accelerating corruption
    - seek Meeks to translate the beggars’ speech
~~~~

Seeds are **lightweight**, but densely connected.

---

# Inputs to the Seed Engine

The Story Seed Engine draws from:

- **Narrative Engine** (story_thread, story_signals)  
- **Mythic Vector System** (regional elemental mood)  
- **Virtue–Vice State** (civic moral weather)  
- **Dungeon State and Mutation Engine** (open wings, corruption levels)  
- **NPC Memory** (aggregated relationship and event patterns)  
- **Global Canon Events** (large mythic shifts)  

It scans this data and looks for **interesting tensions**.

---

# Core Idea: Tension → Seed

Seeds emerge where tension is high:

- a virtue and vice are both strong  
- contrasting elements spike simultaneously  
- a dungeon and town pull in opposite directions  
- NPCs share a common fear or hope  
- canon echoes meet current instability  

I don’t want a seed for every tiny fluctuation —  
I want seeds where the world is clearly *trying to say something*.

---

# Seed Generation Flow

I imagine the engine in three conceptual steps:

## 1. Sensing

- read:
  - regional mythic_vector  
  - virtue_vice_state  
  - dungeon_state snapshots  
  - NPC memory summaries  

- compute:
  - “pressure” metrics:
    - moral tension
    - elemental tension
    - dungeon–town conflict
    - godly attention
    - unresolved canon echoes  

## 2. Pattern Matching

Match high-pressure zones against **seed templates**:

- “Town virtue rising, related dungeon vice spiking”  
- “Elemental opposition at peak: Water vs Fire”  
- “NPC cluster in fear, dungeon instability rising”  
- “Canon echo unresolved in this region”  

Each template corresponds to a category like:
- omen  
- pilgrimage  
- lost relic  
- civic dispute  
- godly messenger  
- corruption outbreak  
- strange weather  

## 3. Seed Creation

For each match:

- instantiate a seed with:
  - concrete region
  - implicated NPCs or factions
  - specific symbols (from element + virtue palette)
  - 1–3 possible directions  

Seeds can be:

- entirely hand-authored and just “unlocked”  
- parameterized with AI assistance  
- semi-randomized within constraints  

---

# Seed Categories

Some initial categories I want:

1. **Omen Seeds**  
   - unusual weather, dreams, apparitions, flock movements  

2. **Civic Seeds**  
   - arguments in markets, guild tensions, shrine disputes  

3. **Dungeon Seeds**  
   - new openings, changed hazards, whispers about vanished delvers  

4. **Relic Seeds**  
   - rumors of lost or awakening artifacts  

5. **Memory Seeds**  
   - NPCs recalling past deeds of the player  
   - old stories resurfacing  

6. **Divine Seeds**  
   - blessings or curses shifting  
   - god-signs in town, sea, forest, or fungus  

Each category has a few generic template patterns plus hand-crafted specials.

---

# Example Seed: Dirt Kingdom / Rothigport Humility Tension

~~~~yaml
story_seed:
  id: seed-dirt-kingdom-clodhaught-whispers
  region: rothigport
  source: hand-authored

  triggers:
    virtue_thresholds:
      humility: "< 1"
      vanity: "< -1.5"
    elements:
      soil: "> 0.8"
      poison: "> 0.4"
    dungeon_states:
      - dirt_kingdom: "corruption_level > 0.6"

  hook: >
    Children in Rothigport wake covered in fine dust, having dreamt
    of a voice beneath the streets saying, "Remember what you're made of."

  tensions:
    - Clodhaught grows restless
    - the city forgets its humble founding
    - beetlefolk prayers go unheard

  outcomes_hint:
    - follow the dust-trail into the Fungal Underground
    - perform a street-level rite of humility
    - ignore it, deepening the rift with the soil spirits
~~~~

This doesn’t force a questline —  
it plants a living situation the player can lean into or walk away from.

---

# Seed Lifecycle

Seeds can be:

- **potential** (dormant template)  
- **emergent** (conditions met, visible in world)  
- **engaged** (player has interacted)  
- **resolved** (some outcome reached)  
- **faded** (time moved on; seed dissolved)  

I do not want every seed to resolve perfectly.  
Some should fade, leaving only a story fragment.

---

# Integration with Quests and Story Looms

Seeds are not always “quests,” but:

- some seeds **promote into full quests**  
- some merge into **Story Looms** as threads  
- some stay atmospheric: only flavor, no explicit objectives  

Workflow:

- Seed emerges →  
- Player engages →  
- Engine checks for:
  - applicable quest templates
  - relevant story-loom structures
  - canon hooks  

If something fits, the seed “blooms” into a richer structure.

---

# Hand-Authored vs Procedural Seeds

I want both:

### Hand-Authored

- highly specific, lore-deep, named NPCs  
- used for major arcs, pantheon crises, key regions  

### Procedural

- generated from patterns, palettes, and templates  
- used for daily life, small mysteries, local color  

### Hybrid

- hand-authored frames with procedural details  
- AI-assisted variations on familiar seed types  

All three share the same **seed structure**, so tools can treat them uniformly.

---

# Seed Density & Pacing

Guidelines I follow:

- A region should *always* have a few active seeds, but never so many that nothing stands out.  
- Dungeon-connected seeds should spike after major runs.  
- Civic seeds should pulse in towns experiencing virtue/vice thresholds.  
- Omen seeds should herald large canon shifts ahead of time.  

Pacing should feel like waves, not a constant blizzard.

---

# Best Practices I Follow

- Seeds should arise from **real tensions**, not randomness.  
- Each seed should be understandable without reading a wiki.  
- Seeds should invite curiosity, not give orders.  
- Not all seeds need resolution — some are atmospheric echoes.  
- Seeds should connect back to:
  - virtue/vice  
  - elements  
  - dungeons  
  - NPC memory  
  - canon  

Whenever possible, seeds should be **story compost**:
they enrich the soil even if nothing “big” happens.

---

# Canonical Truths

- Deluvia constantly generates potential stories as seeds.  
- Story seeds are small, localized, tension-rich invitations.  
- Seeds emerge from the interplay of elements, virtue/vice, dungeons, NPCs, and canon.  
- Some seeds bloom into quests; others remain omens or fragments.  
- The Story Seed Engine keeps the world feeling alive, even when no scripted quest is active.

