---
id: town-state-system
type: system
title: "Town State System"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - towns
  - systems
  - narrative
  - civic-ecology
links:
  related:
    - narrative-engine
    - virtue-vice-system
    - mythic-vector-system
    - npc-memory-system
    - story-seed-engine
---

# Town State System

## Mythic Introduction

Towns in Deluvia are not static clusters of buildings.  
They are **breathing civic organisms**—rooted in landscape, shaped by elemental drift, and stirred awake by the choices I and other players make.

A town’s spirit is made of:

- the virtues its founders held  
- the vices creeping in through time  
- the elemental weather of the region  
- the collective memory of its people  
- the stories that have settled in its stones  

In Deluvia, a town is a *microcosm* of the world’s dreaming mind.  
When its virtues rise, shrines glow, markets flourish, and festivals bloom.  
When vice takes root, shadows lengthen, tempers fray, and the world whispers warnings in fungi, tides, and flickering lanterns.

The Town State System captures this living civic ecology.

---

# System Overview

Each town in Deluvia maintains a **TownState** object—an evolving snapshot of its mood, economy, culture, spiritual energy, and mythic drift.

A simplified representation:

```yaml
town_state:
  id: rothigport
  virtue_profile:
    humility: 7
    truth: 2
    generosity: 1
    vanity: -4
    corruption: -2
  elemental_tone:
    water: 1.4
    soil: 1.1
    moon: 0.2
    poison: -0.4
  npc_memory_cloud:
    trust: 0.6
    fear: 0.2
    reverence: 0.1
    resentment: 0.1
  economic_state:
    prosperity: 0.4
    scarcity: 0.3
    imports: [ore, lumber]
    exports: [fish, clay]
  civic_events:
    active_festivals: []
    active_omens: []
  shrine_alignment:
    favored_by: ["Sifaneus"]
    spurned_by: []
  corruption_index: 0.1
```

Each field is influenced by:

- player actions  
- regional story signals  
- dungeon proximity and corruption blooms  
- mythic vectors  
- virtue/vice drift  
- shrine activity  
- elemental dominance in the region  
- pantheon attention  

---

# 1. Virtue–Vice Profile

Every town has a **virtue it aspires to** and a **vice that threatens it**.

Example: **Rothigport**
- Virtue: Humility  
- Vice: Vanity  

Virtue/Vice shifts when:

- players help or harm townsfolk  
- quests succeed or fail  
- corruption from nearby dungeons bleeds in  
- festivals are held or canceled  
- civic rituals are performed  
- dangerous omens are ignored  

A town leaning toward virtue feels:

- calmer ambient music  
- NPCs more trusting  
- festivals occurring more often  
- shrines responding positively  
- trade more consistent  

A vice-drifting town feels:

- tense NPC dialogue  
- unlucky events  
- darker weather patterns  
- shrines dimming  
- corruption vines appearing on architecture  

---

# 2. Elemental Tone (Mythic Vector Influence)

Each town inherits **regional elemental tone** from the Mythic Vector System.

But towns also *modify it* through:

- civic rituals  
- festivals  
- mythic events  
- shrine activity  
- player deeds  

Example shifts:

- A fire-aligned festival increases **fire** tone.  
- A terrible storm spreads **storm** for days.  
- A corruption bloom from Vanitas pushes **poison** and **death**.  
- A heroic cleansing ritual boosts **sun** and **life**.  

These tones influence:

- ambient soundscapes  
- environmental FX  
- NPC temperament  
- dungeon behaviors nearby  
- random events  
- story seed generation  

---

# 3. NPC Memory Cloud

Instead of tracking each NPC separately at all times, town-level sentiment is aggregated into a **memory cloud**:

- trust  
- fear  
- reverence  
- resentment  

Player actions contribute weighted values, creating a civic mood.

This mood determines:

- dialogue variations  
- trade prices  
- civic quests offered  
- how mobs in nearby wilderness react  
- whether townsfolk aid the player in emergencies  
- the tone of festivals  

---

# 4. Economic State

Towns rise and fall economically based on:

- trade routes  
- storms  
- dungeon influence  
- quests performed  
- supply/demand shifts  
- corruption blooms  
- famine, drought, or fungal infestations  

Economic change is represented by:

- **prosperity metric**  
- **scarcity metric**  
- import/export arrays  
- special conditions (“fish scarcity,” “fungal blight,” “ore surplus”)  

This creates a dynamic sense of place—markets change, goods appear or vanish, and towns feel alive.

---

# 5. Civic Events: Festivals & Omens

Festivals occur when:

- virtue is high  
- shrine alignment is favorable  
- elemental tone is balanced  
- seasonal triggers align  

Omens occur when:

- vice grows  
- corruption indices spike  
- moon element surges  
- death element whispers  

Examples:

**Festivals**
- Lantern Tide (Rothigport, high humility)  
- Blazeborn Revel (Embersway, fire tone high)  
- Skywright Concord (Stormrest, storm tone)  

**Omens**
- Hollow-Moon Shadows  
- Bloom of Black Spores  
- Screaming Gulls of the Stormfather  

These events propagate story seeds.

---

# 6. Shrine Alignment

Shrines monitor:

- civic virtue  
- elemental tone  
- canonical deeds  
- corruption threshold  

A shrine may:

- bless the town  
- withdraw favor  
- send a minor avatar  
- warn via omens  
- empower or punish the player  

Shrines act as the spiritual barometers of towns.

---

# 7. Corruption Index

Derived from:

- dungeon corruption  
- poison/miasma levels  
- vices  
- pantheon disfavor  
- unattended omens  

High corruption triggers:

- hostile NPC variants  
- fungal overgrowth  
- closed markets  
- curfews  
- elemental anomalies  

---

# 8. How Town State Feeds Other Systems

Towns influence:

- **story seeds**  
- **NPC memory**  
- **regional mythic vectors**  
- **dungeon mutation logic**  
- **pantheon attention**  
- **procedural storytelling pacing**  

Town State is the civic nervous system of Deluvia.

---

# Canonical Truths

- A town is a living mythic organism.  
- Virtues and vices shape civic fate.  
- Elemental tone governs mood and event generation.  
- NPC memory is a collective field.  
- Festivals and omens are narrative signals.  
- Corruption and shrine favor ebb and flow like tides.  
- Towns respond to players like stones respond to storms: slowly, inevitably, with deep memory.

