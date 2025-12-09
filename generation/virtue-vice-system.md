---
id: virtue-vice-system
type: system
title: "The Virtue–Vice System"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - metaphysics
  - virtues
  - vices
  - alignment
  - narrative-system
  - design
links:
  related:
    - twelve-elements
    - narrative-engine
    - dungeon-mutation-engine
    - narrative-ecology
---

# The Virtue–Vice System

## Mythic Introduction

Deluvia doesn’t divide the world into good and evil.  
Instead, it breathes through **tensions** — paired moral forces that act like weather.  
Every town, dungeon, god, and mortal carries some version of these currents.

A virtue is a way of *leaning into harmony with the world’s memory*.  
A vice is a way of *leaning into imbalance* — not evil, but drift, distortion, excess.

This system keeps morality mythic rather than moralistic.

---

# Design Intent

I use the Virtue–Vice System to:

- shape town identities  
- define dungeon themes  
- influence procedural storytelling tone  
- anchor NPC behavior and cultural drift  
- tie player choices into regional consequences  
- provide “moral physics” without moral preaching  
- unify lore, mechanics, and metaphysics with the Twelve Elements  

Each virtue–vice pair grows naturally from an element.

---

# The Twelve Pairs

These are not strict opposites but **polar tensions**:

| Element | Virtue | Vice | Notes |
|---------|--------|------|-------|
| Water | Compassion | Despise | empathy vs emotional hardening |
| Fire | Transformation | Destruction | change vs ruin |
| Soil | Humility | Vanity | grounding vs self-inflation |
| Poison | Cunning | Theft | strategy vs exploitation |
| Storm | Valor | Cowardice | courage vs avoidance |
| Moon | Spirituality | Chaos (unmoored) | insight vs unrooted disorder |
| Sun | Courage (truth-speaking) | Fear | revelation vs avoidance |
| Ore | Honor | Greed | craft-with-integrity vs craft-for-power |
| Life | Truth | Deception | growth-through-honesty vs rot-through-lies |
| Death | Justice | Corruption | closure vs decay |
| Wind | Generosity | Envy | giving vs coveting |
| Chaos | Transformation (wild) | Vanity/Destruction hybrid | chaos is its own mirror |

This table is a cleaned and mythically attuned version of your earlier matrix.

Note:  
Some elements have more than one viable “moral expression.”  
This is intentional — it keeps the world from feeling algebraic.

---

# Virtue / Vice Expression in Towns

Towns have virtue–vice meters that shift over time based on:

- player actions  
- NPC memory aggregation  
- Story Signals  
- dungeon drift  
- shrine rituals  

A town leaning far into virtue:

- becomes prosperous or spiritually aligned  
- receives blessings or festival boons  
- unlocks certain story arcs  
- shifts settlement Mythic Vectors  

A town leaning far into vice:

- becomes turbulent, fearful, greedy, paranoid  
- corrupts nearby dungeon ecology  
- manifests omens  
- may trigger new dungeon phases  

This creates a living civic anthropology.

---

# Virtue / Vice Expression in Dungeons

Each dungeon embodies **one vice** fully and **one virtue** partially.

Example:

- **Vanitas (Poison Dungeon)**  
  - Vice: Vanity  
  - Virtue: Humility (buried beneath layers of corrosion)

- **Dirt Kingdom (Soil Dungeon)**  
  - Vice: Vanity (the soil remembering mortal arrogance)  
  - Virtue: Humility (the virtue Deluvia seeks to restore)

Dungeons drift as vices strengthen or weaken:

- new wings open  
- corruption spreads or recedes  
- mythic symbols grow on walls  
- bosses change posture or form  
- hazards shift in response to moral weather  

This is morality as story ecology, not a judgment system.

---

# Virtue / Vice Expression in NPCs

NPCs inherit virtue/vice tendencies based on:

- culture  
- upbringing  
- mythic signature  
- proximity to dungeons  
- historical trauma or pride  

The Relationship Layer (from NPC Memory System) adjusts how vice/virtue is expressed:

- Compassion NPCs give discounts, warnings, and patient dialogue  
- Despise NPCs give clipped remarks and refuse trade  
- Honor NPCs uphold agreements  
- Greed NPCs demand higher prices  
- Transformation NPCs urge quests and experimentation  
- Destruction NPCs push reckless options  

This creates moral diversity without stereotypes.

---

# Virtue / Vice and Elements

Virtue and vice bind directly into the Twelve Elements.

Each virtue is:

- a **stabilized expression** of its element  
- harmonized, constructive, and balanced  

Each vice is:

- an **unbounded expression** of the same element  
- distorted by excess, scarcity, or ego  

### Example:

**Element:** Soil  
**Virtue:** Humility  
**Vice:** Vanity  

Soil wants grounding, patience, honest labor.

When Soil is balanced:
- builders share their craft  
- farmers honor the seasons  
- rulers stay modest  

When Soil is warped:
- ego becomes granite  
- pride mocks the plow  
- power climbs atop its own monuments  

Virtue and vice aren’t opposites — they are **angles** of the same force.

---

# Virtue / Vice Drift Model

Virtue and vice shift through:

### **Soft Drift**
- average NPC mood  
- trade patterns  
- civic rituals  
- regional mythic vector influence  

### **Shock Drift**
Triggered by:
- desecration of shrines  
- killing sacred creatures  
- refusing or betraying moral quests  
- participating in corruption cults  
- completing great works sponsored by the gods  

### **Global Drift**
Caused by:
- the Severing  
- divine attention  
- large Story Loom resolutions  
- regional calamities  

Drift is slow unless catalyzed.

---

# Virtue–Vice Encoding

~~~~yaml
virtue_vice_state:
  region: rothigport
  virtue_scores:
    humility: 3.1
    compassion: 0.4
    truth: 0.7
  vice_scores:
    vanity: -1.2
    envy: -0.3
    corruption: -0.1
  drift_rate: 0.02
  last_update: 2025-01-17
~~~~

Positive = stronger virtue  
Negative = stronger vice

I treat scores more like gravity than morality.

---

# Integration with Other Systems

### Narrative Engine
Virtue/vice adjusts Story Thread tone and regional consequences.

### Mythic Vector System
A region’s virtue alignment subtly pulls its vector.

### Dungeon Mutation Engine
Dungeons mutate based on vice dominance.

### NPC Memory System
NPC behavior reinforces or rebalances regional virtue.

### Procedural Storytelling & Story Looms
Certain narrative arcs trigger only when virtue/vice reaches thresholds.

### Canon Engine
Canon events can permanently alter virtue baselines.

---

# Example: Rothigport (Humility Town)

Virtue: **Humility**  
Vice: **Vanity**

If humility rises:
- the sea is gentler  
- shrines flicker with approval  
- Meeks’ mushroom blessings grow stronger  
- Storm and Soil vectors harmonize  

If vanity rises:
- waves turn rough  
- dungeons deepen  
- dirt elementals awaken  
- poison and moon influences creep inward  

These shifts should feel emotionally intuitive to the player.

---

# Best Practices I Follow

- Virtue should feel like *alignment with the world’s story*, not righteousness.  
- Vice should feel like *imbalance*, not villainy.  
- Neither virtue nor vice should be absolute.  
- Towns should drift slowly; dungeons should drift visibly.  
- NPCs should reveal regional virtue/vice through tone and rumor.  
- Virtue/vice should always feed other systems, not stand alone.  

---

# Canonical Truths

- Every region of Deluvia resonates with a virtue and struggles with a vice.  
- Virtue and vice express each element’s harmonized or distorted form.  
- These tensions shape dungeons, NPCs, towns, rituals, and procedural story.  
- Virtue/vice drift is slow but world-changing.  
- The Virtue–Vice System ties the moral physics of the world into its elemental metaphysics.

