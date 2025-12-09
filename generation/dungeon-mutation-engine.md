---
id: dungeon-mutation-engine
type: system
title: "Dungeon Mutation Engine"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - dungeons
  - procedural
  - mutation
  - narrative
  - systems
links:
  related:
    - narrative-engine
    - mythic-vector-system
    - procedural-storytelling
    - player-action-canon-engine
---

# Dungeon Mutation Engine

## Mythic Introduction

Dungeons in Deluvia are not static blueprints.  
They are **wounds**, **organs**, and **dream-chambers** inside the body of the world.

When mortals enter them, they are not exploring a fixed structure.  
They are disturbing something that is still trying to heal, fester, or change.

I don’t want dungeons that reset like clockwork.  
I want dungeons that **remember**, drift, and respond.

The Dungeon Mutation Engine is how I let each dungeon slowly become its own creature.

---

# Purpose of This System

The Dungeon Mutation Engine allows me to:

- make dungeons evolve over time  
- tie their changes to player actions and canon events  
- express the Mythic Vector System in spatial form  
- keep runs familiar but never identical  
- let corruption, cleansing, and divine attention leave visible marks  
- align dungeons with Story Looms and regional narrative ecology  

Each dungeon becomes a slowly-shifting mythic organism.

---

# Core Principles

These are the rules I hold while designing this system:

1. **Identity First, Layout Second**  
   Each dungeon has a stable identity (theme, element, mythic role) even as its rooms shift.

2. **Change as Consequence, Not Noise**  
   Mutations should arise from:
   - player behavior
   - narrative vectors
   - canon events
   - divine or elemental pressure

3. **Readable Evolution**  
   Players should be able to *sense* why a dungeon has changed, not feel like it’s random soup.

4. **Loops, Not Lines**  
   Dungeons favor looping layouts with variations, not purely linear paths.

5. **Visible Mythic Drift**  
   Changes should reveal the movement of elements, gods, and virtues.

---

# Dungeon State Model

Each dungeon has a state object that the engine reads and updates:

~~~~yaml
dungeon_state:
  dungeon_id: string

  # Identity
  core_element: poison
  secondary_elements:
    - moon
    - death
  associated_virtue: humility
  associated_vice: vanity

  # Progression
  corruption_level: 0.0-1.0
  cleansing_level: 0.0-1.0
  instability: 0.0-1.0

  # Structural
  variant_seed: integer
  unlocked_wings:
    - fungal-upper
    - forgotten-mineshaft

  # Narrative
  mythic_vector: {...}          # see mythic-vector-system
  story_thread_snapshot: {...}  # see narrative-engine
  last_run_summary: {...}
~~~~

This `dungeon_state` is the soil the mutation system grows from.

---

# Inputs to the Mutation Engine

The engine consumes:

- **Story Signals** that involve the dungeon  
- **Canon Events** tied to the dungeon  
- **Regional Mythic Vectors** (narrative-ecology + mythic-vector-system)  
- **Virtue/Vice drift** in associated town(s)  
- **Dungeon run summaries**:
  - how many times cleared
  - which bosses slain
  - which shrines desecrated or cleansed
  - how many deaths inside  

These inputs drive numeric changes in:

- `corruption_level`
- `cleansing_level`
- `instability`
- `mythic_vector`

---

# Mutation Axes

I mutate dungeons along several axes:

1. **Layout Variation**  
   - room connections  
   - secret paths  
   - dead ends  
   - shortcut unlocks  

2. **Environmental Dressing**  
   - fungal growths  
   - crystals, roots, bones  
   - light color, fog, water level  

3. **Enemy Ecology**  
   - types of mobs  
   - density  
   - elemental affinities  
   - special variants  

4. **Mechanic Layers**  
   - traps  
   - puzzles  
   - environmental hazards  

5. **Mythic Presence**  
   - godly symbols  
   - omens  
   - whispers, chants, hallucinations  

6. **Reward Patterns**  
   - type of loot  
   - frequency of relics  
   - quality of resource veins  

Mutation is not just spatial — it is also *symbolic*.

---

# Mutation Triggers

I think of mutations in three categories:

## 1. Slow Drift (Tick-Based)

On a schedule (e.g., once per in-world week):

- read regional vectors  
- adjust dungeon_state slightly  
- update:
  - minor layout variation
  - environmental dressing
  - mob distribution  

This is the “weather” of the dungeon.

---

## 2. Shock Events (Run-Based)

After a player run, I apply shock adjustments:

- if the boss is killed:
  - corruption may drop or spike, depending on lore  
- if shrines are desecrated:
  - divine presence may withdraw or intensify  
- if many deaths occur:
  - death element rises  
- if players rush and loot everything:
  - greed-aligned vices wake  

These shocks cause:

- a new wing to open  
- a passage to collapse  
- a rare variant to appear next time  
- a god to mark the walls  

---

## 3. Canon Mutations (Lore-Based)

When a Canon Event explicitly involves a dungeon:

- the dungeon may undergo a **phase change**:
  - once-living area becomes fossilized  
  - fire areas become ashfields  
  - poison chambers bloom with new, grotesque flora  

Canon mutations are rare but profound.

---

# Example: Vanitas Mutation Logic (Poison Dungeon)

Baseline:

- core_element: poison  
- secondary_elements: moon, death  
- associated_virtue: humility  
- associated_vice: vanity  

If:

- Rothigport’s vanity rises  
- players repeatedly throw knowledge into the bonfire  
- the Wand of Soil’s Ire is used to profit from the mine’s remains  

Then:

- `corruption_level` increases  
- `poison` vector spikes  
- `soil` vector decreases  
- new poison types spawn (Blightox, Mephinox, Amanitox…)  
- boss variants of Ratatoskel emerge:
  - one more skeletal
  - one more fungal
  - one more crowned in acorn-fire  

Visible changes might include:

- more skulls and wilted flowers  
- more distorted fungal growth  
- new toxic vents  
- changed routes that favor ambush predators  

---

# Example: Dirt Kingdom Mutation (Humility Dungeon)

If:

- players repeatedly complete humility rituals  
- beggars receive alms  
- the Wand of Soil’s Calm is used mercifully  

Then:

- `corruption_level` drops  
- `soil` and `life` vectors rise  
- `poison` recedes  
- collapsed tunnels gently re-open  
- draggleflaps become less aggressive  
- Meeks offers new, gentle mushroom boons  

If:

- players exploit the dungeon purely for profit  
- ignore Meeks’s requests  
- seek the Wand of Soil’s Ire  

Then:

- vanity seeps into the soil  
- Clodhaught becomes harsher  
- tunnels grow more jagged  
- new husk-beasts crawl in  

---

# Mutation Output Types

When the engine runs, it outputs:

~~~~yaml
dungeon_mutation:
  dungeon_id: dung-vanitas
  new_variant_seed: 4312
  layout_changes:
    - opened: "toxic-overlook"
    - collapsed: "old-mine-lift"
  environmental_changes:
    - add: "fungal-spires"
    - intensify: "spore-fog"
  enemy_changes:
    - add_variant: "blightox-ooze"
  mythic_changes:
    - symbol: "skull-hourglass"
    - omen: "poisoned-moonlight"
~~~~

These outputs inform concrete generation logic.

---

# How This Connects to Other Systems

- **Narrative Engine**  
  Dungeon mutations reflect regional story_thread and Story Signals.

- **Mythic Vector System**  
  Dungeon vector drift expresses the elemental mood.

- **Player Action → Canon Engine**  
  Canon Events can crystallize dungeon phase shifts.

- **NPC Memory System**  
  NPCs near the dungeon respond to changes in mood, danger, and symbolism.

- **Procedural Storytelling**  
  New Seeds unlock; Looms adapt to mutated dungeon states.

Everything stays knitted together.

---

# Best Practices I Follow

- I change dungeons in **visible, meaningful steps** — not constant noise.  
- I let players recognize patterns and feel responsible.  
- I ensure each dungeon has:
  - a clear archetype
  - a few known possible phases
  - recognizable symbolic stages  

- Mutation should feel:
  - earned  
  - coherent  
  - mythically appropriate  

---

# Canonical Truths

- Dungeons in Deluvia are living mythic organs, not static mazes.  
- They mutate over time in response to player actions, regional ecology, and canon events.  
- The Dungeon Mutation Engine ensures these changes remain coherent, symbolic, and readable.  
- Dungeon evolution is one of the main ways Deluvia shows that it is **watching** and **remembering**.

