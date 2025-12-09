---
id: mythic-vector-system
type: system
title: "The Mythic Vector System"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - metaphysics
  - elements
  - narrative-system
  - design
links:
  related:
    - narrative-engine
    - procedural-storytelling
    - narrative-ecology
    - twelve-elements
---

# The Mythic Vector System

## Mythic Introduction

Deluvia is not a world of rigid categories.  
It breathes in **gradients** — shifting moods, elemental tides, emotional textures, and half-forgotten whispers.  
If the Narrative Engine is how I *listen* to the world, the Mythic Vector System is how I *measure its pulse*.

Every entity, from a dungeon to a god to a wandering beetle spirit, expresses itself across the **Twelvefold Wheel**.  
These expressions form a **vector**: a directional signature showing how myth, emotion, and elemental force flow through a thing.

It’s not alignment.  
It’s not morality.  
It’s much closer to *a living fingerprint of story physics*.

---

# Purpose of This System

The Mythic Vector System allows me to:

- model how **dungeons drift** over time  
- define how **towns shift in mood**  
- describe **NPC emotional resonance**  
- determine **godly influence**  
- adjust **procedural story weights**  
- unify lore + mechanics under a single symbolic umbrella

This is a core metaphysical subsystem.  
It stabilizes everything else.

---

# What a Mythic Vector *Is*

At its core:

A **Mythic Vector** is a 12-value elemental signature, one value per element of Deluvia’s wheel.

Each value ranges from **-2.0 to +2.0**, where:

- **negative** = receding, suppressed, suppressed-aspect, shadow-mode  
- **zero** = neutral, dormant  
- **positive** = active, expressive, dominant  

A typical vector is NOT balanced. It leans.

That lean is the story.

---

# The Twelve Elements (Vector Axes)

These are the twelve axes your world expresses through:

| Element | Vector Meaning |
|---------|----------------|
| **Water** | memory, emotion, reflection, ancestral pull |
| **Fire** | transformation, volatility, hunger, change |
| **Soil** | grounding, humility, burden, patience |
| **Poison** | corruption, temptation, rot, subversion |
| **Storm** | upheaval, courage, conflict, boldness |
| **Moon** | illusion, secrets, dreams, liminality |
| **Sun** | clarity, revelation, truth, direction |
| **Ore** | craft, forging, innovation, material will |
| **Chaos** | randomness, fate fracture, oddity, chance |
| **Wind** | intention, choices, freedom, directionality |
| **Life** | growth, abundance, healing, flux |
| **Death** | closure, endings, entropy, inevitability |

Every place, entity, faction, spell, dungeon, or moment expresses itself across these axes.

---

# Vector Encoding Format

I encode Mythic Vectors in YAML for clarity and machine-readability:

~~~~yaml
mythic_vector:
  water:  +0.6
  fire:   -0.2
  soil:   +1.1
  poison: +0.3
  storm:  +0.0
  moon:   -0.4
  sun:    +1.3
  ore:    +0.2
  chaos:  +0.8
  wind:   -0.1
  life:   +0.5
  death:  -0.7
~~~~

A vector like this says:

- The place/entity resonates strongly with **Sun** and **Soil**.  
- Its **Chaos** aspect is active.  
- Its **Death** and **Moon** aspects are in recession.  
- **Wind** is indecisive, minimal.  

This becomes a universal descriptive tool.

---

# What Vectors Apply To

Vectors exist for:

### **Regions**
Their emotional and mythic climate.

### **Towns**
Their cultural drift, civic virtue/vice, elemental mood.

### **Dungeons**
Their instability, corruption, alignment shifts, boss variants.

### **NPCs**
Their internal emotional resonance, magical attunement, factional drift.

### **Factions**
Their ideology, motives, elemental philosophy.

### **Gods**
Their full divine signature (usually extreme values).

### **Items & Relics**
Their symbolic power and infused elemental memory.

### **World States**
Seasonal shifts, omens, lunar cycles, calamities.

---

# How Vectors Change Over Time

Vectors are *dynamic*, not fixed.

They change through:

- **player actions** (story signals)
- **canon events** (see canon engine)
- **dungeon mutations**
- **regional ecological shifts**
- **virtue/vice movement**
- **procedural story arcs resolving**
- **divine attention intensifying or fading**

The world is never static, because the vector-space of the world is never static.

---

# Vector Drift Model

I model drift in three ways:

## **1. Soft Drift (World Ecology)**  
Slow, atmospheric changes —  
like Wind creeping upward during a migration season, or Water rising during years of grief.

## **2. Hard Drift (Events)**  
Triggered by major player deeds, global mythic shift, dungeon falls or resurrections.

These kicks can dramatically reshuffle the vector.

## **3. Oscillatory Drift (Cycles)**  
Elements oscillate based on lunar phases, seasonal tides, and mythic cycles like:

- The Severing  
- The Verdant Bloom  
- The Night of Three Moons  
- The Emberfall

Oscillation gives the world rhythm.

---

# Using Vectors in Procedural Systems

Vectors feed directly into:

### **Dungeon Mutation Tables**
A dungeon with high Moon + Poison becomes:
- foggier  
- dreamlier  
- more riddled with toxin, shadow, deception  

### **NPC Memory & Personality**
NPCs with:
- high Wind → impulsive  
- high Soil → patient  
- high Sun → bluntly honest  
- high Moon → evasive, mystical  

### **Story Loom Weighting**
Certain arcs unfold more often when vectors lean toward certain domains.

### **Loot Tables**
High Ore + Fire increases:
- forged relics  
- volatile enchantments  
- explosive affixes  

### **Weather & Overworld Effects**
Storm vector + Chaos vector → wild, reality-warp storms.

---

# Example: Rothigport’s Baseline Vector

~~~~yaml
mythic_vector:
  water:  +1.4    # memory + sea-bound grief + fishing heritage
  soil:   +0.9    # humility, work ethic
  sun:    +0.3    # some clarity in civic rituals
  wind:   +0.2    # faint but steady seafaring intention
  life:   +0.1    # mild fertility from coastal flora

  poison: -0.3    # dormant corruption
  moon:   -0.2    # low dream-influence
  chaos:  -0.1    # mild unpredictability
  fire:   -0.1    # conservative, little appetite for change
  ore:    +0.0    # neutral crafting influence
  storm:  +0.0
  death:  -0.4    # death energy in remission (for now)
~~~~

When the Vanitas dungeon awakens, Poison and Moon rise — Soil may fall — and Humility may be tested.

---

# Example: Dungeon Vector (Vanitas)

~~~~yaml
mythic_vector:
  poison: +1.9
  moon:   +1.1
  death:  +0.7
  chaos:  +0.4

  life:   -0.9
  soil:   -0.6
  sun:    -0.5
~~~~

This is why Vanitas feels sick, dreamlike, and unmoored.

---

# Best Practices I Follow

- Vectors should **lean**, not balance.  
- Neutral vectors are boring — imbalance creates myth.  
- Vectors should change over time — the world is alive.  
- Vectors should influence mechanics — not just flavor.  
- Vectors should act as **inputs** for procedural systems to avoid hard-coded narrative.  

---

# Canonical Truths

- Everything in Deluvia expresses itself across the Twelvefold Wheel.  
- Mythic Vectors describe the elemental, emotional, and narrative signature of entities.  
- Vectors drift through ecology, player action, and mythic tides.  
- Procedural systems become richer and more coherent when powered by vectors.  
- The Mythic Vector System is foundational to how I keep the world breathing.

