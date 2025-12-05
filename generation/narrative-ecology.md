---
id: narrative-ecology
type: system
title: "Narrative Ecology of Deluvia"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - narrative
  - ecology
  - systems
  - world
links:
  related:
    - narrative-engine
    - procedural-storytelling
    - twelve-elements
    - virtue-vice-matrix
---

# Narrative Ecology of Deluvia

## Mythic Introduction

Deluvia is not a map — it is a **habitat for stories**.

Towns cling to coasts and cliff edges the way barnacles cling to ships.
Dungeons bloom like infections beneath the skin of the world.
Shrines drink in prayers, fears, and bargains, then exhale omens into the wind.
Gods are not distant; they are **pressure systems** in the mythic weather.

Every choice a mortal makes falls into this living web:
it disturbs soil, wakes sleeping spores, bends leylines, angers or soothes small gods.
The result is not a linear plot, but an **ecology** — a system of dependencies, feedback loops, and niches where certain stories thrive.

This document explains how that ecology is structured.

---

# Purpose of This Document

The **Narrative Ecology** describes how:

- elements, virtues, vices, and domains shape regional behavior
- towns, shrines, dungeons, factions, and creatures interact
- the Narrative Engine and procedural storytelling draw from this web
- local actions can have non-local mythic consequences

It is the **conceptual backbone** behind:

- `narrative_engine.md` (how signals move through the system)
- `procedural_storytelling.md` (how seeds + looms are selected)
- future content (towns, dungeons, NPC behaviors, events)

This document stays **engine-agnostic** — it describes *what is true in Deluvia*, not how code is written.

---

# Core Idea: Regions as Narrative Biomes

Each region in Deluvia is a **narrative biome**:
a place where certain stories are more likely to appear, flourish, and return.

A region is defined by:

- **Elemental Profile** — which of the 12 domains dominate
- **Virtue/Vice Dyad** — its moral-mythic tension (e.g., Humility / Vanity)
- **Primary Structures** — towns, shrines, dungeons, landmarks
- **Inhabitants** — cultures, factions, creatures
- **Mythic Pressure** — which gods, spirits, or forces lean on it

In data form:

~~~~yaml
narrative_biome:
  id: region-rothigport-bay
  title: "Rothigport & the Bay of Low Lanterns"

  elements:
    water: 1.4
    soil: 0.9
    storm: 0.3
    moon: 0.2
    # other elements near 0.0–0.2 baseline

  virtue_vice:
    virtue: humility
    vice: vanity

  primary_structures:
    towns:
      - town-rothigport
    dungeons:
      - dung-vanitas
      - dung-pool-of-haught
    shrines:
      - shrine-humility
      - shrine-purity
    landmarks:
      - landmark-drowned-lantern
      - landmark-kelp-grave

  mythic_pressure:
    patron_gods:
      - god-sifaneus        # soil / humility
      - god-kelvora         # water / purity
    meddling_forces:
      - demi-perf           # filth / decay
      - demon-ratatoskel    # poison / vanity

  ecological_notes: |
    Stories about work, shame, penitent journeys, and memory of the drowned thrive here.
~~~~

The Narrative Engine and procedural systems use these biomes to:

- weigh seed selection
- modify Loom expression
- control dungeon mutations
- guide NPC attitudes and rumors

---

# The Four Layers of Narrative Ecology

We can think of Deluvia’s narrative ecology in **four interacting layers**:

1. **Elemental Layer** — the 12 Elements as narrative forces  
2. **Virtue/Vice Layer** — moral-mythic tensions per region  
3. **Structure Layer** — towns, shrines, dungeons, landmarks  
4. **Living Layer** — NPCs, factions, creatures, and players

Each layer influences and constrains the others.

---

## 1. Elemental Layer

The 12 Elements are not just spell schools — they are **story gradients**:

- **Water (Memory)** — nostalgia, loss, things returning or refusing to
- **Fire (Transformation)** — radical change, destruction as threshold
- **Soil (Humility)** — burden, labor, smallness, grounded truth
- **Poison (Corruption)** — temptation, slow ruin, beautiful rot
- **Storm (Valor)** — upheaval, bravery, sudden breaks in the sky
- **Moon (Illusion)** — secrets, half-truths, dreams, masks
- **Sun (Clarity)** — revelation, harsh truth, mercy by exposure
- **Ore (Craft)** — invention, forging, obsession with making
- **Chaos (Chance)** — coincidences, luck, strange attractors
- **Wind (Intention)** — direction, vows, changing course mid-air
- **Life (Growth)** — exuberance, fecundity, resilience
- **Death (Closure)** — endings, stillness, grief that seals

Each region has a **weight vector** over these elements (see `twelve-elements` doc).
That vector influences:

- which seeds are available
- how dungeons express themselves
- how gods and spirits manifest
- which Story Looms are favored

If Storm is high and Soil is low, you get explosive, courageous stories with little patience.
If Soil is high and Water is high, you get slow, memory-heavy tales of work and regret.

---

## 2. Virtue / Vice Layer

Each major region has a **Virtue/Vice Dyad**, a mythic tension line.

Examples (illustrative, not final):

- Rothigport — **Humility / Vanity**
- Kapasia — **Honor / Greed**
- Druvvenrog — **Transformation / Destruction**
- Fecundia — **Generosity / Envy**

Virtue/Vice is tracked as:

- a **regional meter** (long-term drift)
- short-term **story pressure** (recent deeds)

~~~~yaml
virtue_vice_state:
  region: rothigport
  virtue: humility
  vice: vanity
  virtue_score: +3     # higher = stronger virtue presence
  vice_score: -1       # lower = not currently dominant
~~~~

This layer affects:

- which NPCs gain or lose influence
- how shrines respond
- dungeon hostility or mercy
- which stories feel “cheap” vs “earned”

It also ties into:

- `virtue_vice_matrix.md` (mapping elemental links)
- the long-term **Deluvic Cycle** (balance vs imbalance across the map)

---

## 3. Structure Layer (Towns, Shrines, Dungeons, Landmarks)

These are the **organs** of Deluvia’s narrative body.

### Towns

Towns are:

- social centers
- virtue/vice amplifiers
- rumor hubs
- economic nodes
- staging grounds for quests

Each town file (in your `world/towns` or equivalent) should carry:

- elemental profile
- virtue/vice context
- key NPCs
- primary shrines
- nearby dungeons

Towns answer:  
**“Where do stories begin and return?”**

---

### Shrines

Shrines are:

- local proxies for gods, spirits, concepts
- narrative valves: they bless, curse, redirect
- key anchors for rituals and story beats

Each shrine has:

- patron force (god, concept, elemental mixture)
- required offerings or behaviors
- preferred virtues
- ways it reacts to regional state

Shrines answer:  
**“Who or what is listening here?”**

---

### Dungeons

Dungeons are:

- concentrated story biomes
- crystallized vice or unresolved myth
- places where narrative pressure becomes tangible (mobs, hazards, bosses)

Your earlier ideas (fungal underground, poison mines, vanity caverns, etc.) all belong here.

Each dungeon has:

- elemental alignment(s)
- vice focus
- relationship to nearby towns/shrines
- long-term behavior under the Narrative Engine

Dungeons answer:  
**“What happens if this imbalance is left to fester?”**

---

### Landmarks & Features

These are:

- recurring visual myths (the same burned tree, the same tide-bent statue)
- geographic memory points
- often used as anchors for Story Seeds

Landmarks answer:  
**“What does this place remember?”**

---

## 4. Living Layer (NPCs, Factions, Creatures, Players)

This is where the ecology moves.

### NPCs

NPCs are:

- carriers of local mood
- mirrors for player choices
- interpreters of the gods’ silence

Their behavior is shaped by:

- regional element and virtue/vice
- faction ties
- personal arcs (small Looms)
- memories (from Chronicle entries)

---

### Factions

Factions are slow-moving story vectors:

- cults
- guilds
- caravans
- knightly orders
- secret societies
- beetle colonies

They:

- form alliances or rivalries across regions
- magnify or resist regional drift
- provide mid- to long-term arcs for players

---

### Creatures & Spirits

Creatures and spirits express the **land’s subconscious**:

- fungal beasts in places of hidden rot
- storm eels where valor and danger meet
- bonewalkers where Death and Memory intertwine

Their spawn logic is linked to:

- elements
- regional tone
- dungeon state
- recent Story Signals (from the Narrative Engine)

---

### Players

Players are not outside the ecology.

They are:

- invasive species
- pollinators
- heralds of change
- sometimes antibodies

Their actions:

- perturb balances
- awaken dormant seeds
- introduce new myths into old soil

The Narrative Engine treats them as **active agents** in this web, not passive consumers.

---

# Flows in the Narrative Ecology

At a high level, we model flows between layers:

1. **Local Action → Story Signal**  
   - Player defeats a corrupted mine boss, performs a ritual, makes a major choice.

2. **Story Signal → Thread & Biome Update**  
   - Narrative Engine updates the regional story_thread and virtue/vice meters.

3. **Biome State → Procedural Choice**  
   - Procedural Storytelling favors certain seeds, Looms, and tone based on current ecology.

4. **Procedural Output → Structures & Living Layer**  
   - New quests, dungeon states, NPC behaviors, and shrines shift in response.

5. **Structures & Living Layer → More Local Action**  
   - Players experience new situations, act again, and the cycle continues.

In short:

> **Ecology is the backdrop; Engine is the motion; Story is the trace.**

---

# Practical Design Rules

To keep the narrative ecology from becoming hand-wavy, we adopt some practical rules:

1. **Every region has:**
   - a clear elemental vector
   - a virtue/vice dyad
   - at least one town, shrine, dungeon

2. **Every dungeon is tied to:**
   - one or more nearby towns
   - at least one shrine or god
   - a specific vice and element

3. **Every major NPC is anchored to:**
   - a region
   - a faction or shrine or town role
   - a small personal Loom (micro-arc)

4. **No story exists without at least one ecological hook:**
   - region
   - element
   - virtue/vice
   - structure
   - living entity (NPC/faction/creature)

If a story seed has none of these, it doesn’t belong in Deluvia — it’s driftwood from another world.

---

# Relationship to Other System Docs

- **`narrative_engine.md`**  
  Describes how Story Signals move through this ecology and update it.

- **`procedural_storytelling.md`**  
  Describes how Seeds + Looms draw on ecological state to grow stories.

- **`twelve-elements.md`**  
  Defines elemental meanings, which feed directly into region profiles.

- **`virtue_vice_matrix.md`**  
  Maps virtues/vices to elements and informs regional dyads and dungeon roles.

---

# Canonical Truths

- Deluvia is a **narrative ecology**, not a static map.
- Regions are narrative biomes with elemental, virtue/vice, structural, and living components.
- Towns, shrines, dungeons, and landmarks are the organs through which stories circulate.
- NPCs, factions, creatures, and players are all actors within this ecology.
- The Narrative Engine and procedural storytelling systems operate on top of this web, not apart from it.
