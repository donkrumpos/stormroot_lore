---
id: narrative-engine
type: system
title: "The Narrative Engine of Deluvia"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - narrative
  - procedural
  - ai
  - story
links:
  related:
    - procedural-storytelling
    - story-looms
    - player-action-canon-engine
    - narrative-ecology
---

# The Narrative Engine of Deluvia

## Mythic Introduction
Beneath the loam and stone, deeper than any dungeon and older than the first twelve gods, lies the Weave — the secret memory of Deluvia.
Stories are not written here; they **sprout**. They cling to root and cavern wall, drift as spores through the dreaming soil, and settle in chambers where ancient echoes sleep.

When mortals act, their choices ripple through this underground mind.
Deluvia reshapes itself in answer — not out of morality or judgment, but out of **instinct**, like a great hakoniwa-creature shifting in its slumber.

The Narrative Engine is the quiet mechanism beneath that dream, translating mortal actions into mythic consequence.

---

# System Overview
The Narrative Engine converts **player actions** into:

- world changes
- story fragments
- dungeon mutations
- NPC memory updates
- virtue/vice adjustments for towns and dungeons
- mythic consequences that persist across eras

Its structure contains six major pillars:

1. Story Signal Capture
2. Domain Encoding
3. Virtue/Vice Modifiers
4. Thread Binding
5. Emergence & Mutation (World Reaction)
6. Archival via the Chronicle of Deeds

---

# 1. Story Signal Capture

A **Story Signal** is any action that carries narrative weight.

### Examples
- defeating a dungeon mini-boss
- consecrating or desecrating a shrine
- burning a book in the Vanitas chamber
- rescuing (or betraying) an NPC
- killing a sacred creature
- discovering a hidden chamber
- performing a ritual incorrectly
- entering a mythic area during a lunar phase
- building major structures visible across a region

### Structured Format
Every Story Signal is encoded with stable fields:

~~~~yaml
story_signal:
  id: uuid
  type: combat | ritual | social | discovery | transgression | creation
  actor: player_id
  location: region_id
  domain: elemental_domain
  virtue_impact:
    humility: -1
    truth: +2
  intensity: 0.0-1.0
  timestamp: ISO8601
~~~~

Signals accumulate in **regional buffers**, forming the substrate of emergent story.

---

# 2. Domain Encoding

Each Story Signal belongs to one of Deluvia’s Twelve Narrative Domains:

| Element | Narrative Domain | Interpretation |
|--------|------------------|----------------|
| Water | Memory | emotional resonance, resurfacing pasts |
| Fire | Transformation | destruction as rebirth, heat of change |
| Soil | Humility | grounding, burden, truth, patience |
| Poison | Corruption | entropy, rot, temptation, blight |
| Storm | Valor | upheaval, courage, disruption |
| Moon | Illusion | dreams, secrets, hidden paths |
| Sun | Clarity | revelation, illumination, insight |
| Ore | Craft | forging, invention, shaping matter |
| Chaos | Chance | randomness, fate fractures, oddity |
| Wind | Intention | direction, will, choice |
| Life | Growth | emergence, healing, fertility |
| Death | Closure | endings, silence, inevitability |

Domains determine **how** signals influence the local narrative ecology.

---

# 3. Virtue / Vice Modifiers

Each town and dungeon exist in a **Virtue/Vice Dyad**, shaping regional mythflow.

Example:
- **Rothigport — Humility**
- **Vanitas — Vanity / Poison**

Story Signals adjust these values, influencing:

- corruption density
- dungeon hostility
- town prosperity or unrest
- shrine favor/disfavor
- NPC trust, fear, or reverence
- civic rituals and omens

Virtue/Vice is not morality — it is **mythic physics**.

---

# 4. Thread Binding

A **Story Thread** is a rolling, aggregated state for each region.

~~~~yaml
story_thread:
  region: region_id
  signals:
    - story_signal
  tone_state:
    water: 0.8
    fire: 0.3
    soil: 1.2
    moon: 0.1
    # ... all 12 elements
  virtue_meter:
    humility: 3
    vanity: -1
    truth: 0
    corruption: 1
~~~~

### Components

**Tone State**  
A weighted elemental vector describing mythic “weather”.

**Virtue Meter**  
Tracks long-term spiritual/cultural drift.

**Signal List**  
Buffer of 200–500 recent narrative events.

---

# 5. Emergence & Mutation (World Reaction)

Once thresholds are crossed, the world reacts organically.

## Town-Level Effects

### NPCs
- dialogue changes
- mood shifts
- altered routines or allegiances
- rumors propagate
- trade inventory shifts

### Settlements
- prices fluctuate
- festivals unlock or cancel
- shrine lights brighten or dim
- omens appear (fungal blooms, celestial arcs)

---

## Dungeon-Level Effects

### Mutations
- room layout variations
- corruption bloom or retreat
- elemental overlays (storm, frost, blight, moonlight)
- rare boss variants
- shifting hazards
- fungal growth or crystal accretion

### Spawn Logic Shifts
Based on:

- dominant narrative domain
- recent player deeds
- dungeon’s elemental alignment
- corruption metastability

---

## Wilderness & Overworld Effects
- leyline flux increases or dims
- wandering spirits appear
- weather patterns alter
- hidden paths open (moon/memory dominance)
- environmental catastrophes (storm/fire dominance)

---

## Global Mythic Effects
- gods turn attention toward or away from a region
- cross-regional mythic drift
- ancient cycles reawaken
- omens spread across towns

---

# 6. Chronicle of Deeds

The **immutable archive** of myth-weighted events.

~~~~yaml
chronicle_entry:
  id: uuid
  actor: player_id
  event: string
  region: region_id
  domain: elemental_domain
  timestamp: ISO8601
  consequences:
    - npc_memory_update
    - dungeon_state_shift
    - regional_tone_modification
    - virtue_meter_adjustment
~~~~

Purposes include:

- NPC memory persistence
- multi-era world continuity
- seeding future procedural generation
- mythic recognition (“your deeds echo in the Weave”)
- safeguarding narrative causality across resets

---

# Design Intent
The Narrative Engine must make Deluvia feel:

- **alive**
- **responsive**
- **aware**
- **ancient yet curious**

Players should feel they are walking inside a dreaming hakoniwa realm — a miniature world vast enough to hold myth and memory.

This is not a quest system.  
It is a **story ecology**.

---

# Canonical Truths
- Deluvia remembers.  
- Player choices shape myth and regional destiny.  
- Towns and dungeons exist in shifting harmony and tension.  
- Stories emerge from ecology, not scripting.  
- Every action leaves a trace in the Weave.
