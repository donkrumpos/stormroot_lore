#!/usr/bin/env python3
# Generates the story-looms.md file safely and cleanly

import os

content = """\
---
id: story-looms
type: system
title: "Story Looms of Deluvia"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - narrative
  - systems
  - storytelling
  - looms
links:
  related:
    - narrative-engine
    - procedural-storytelling
    - narrative-ecology
---

# Story Looms of Deluvia

## Mythic Introduction

When I look at Deluvia as a living myth, I don't see quests or branches or dialogue trees.  
I see **patterns** — the ancient shapes that every story secretly curls itself around.

In Deluvia, these patterns aren’t templates for quests.  
They are **Story Looms**: the great weaving frames beneath the soil where stories knot, fray, echo, and return.

A Loom isn’t a plot.  
It’s the **shape of a story’s becoming** — the emotional contour, the mood pressure, the mythic gravity that pulls events toward meaning.

Players don’t follow Looms.  
They **activate** them simply by being in the world.

This document defines the Looms I rely on to grow emergent stories in Deluvia.

---

# Purpose of This Document

I use Story Looms as *reusable narrative structures* that:

- guide procedural storytelling  
- shape the tone of generated quests  
- constrain AI output into coherent mythic arcs  
- help me maintain narrative cohesion across the world  
- let stories emerge dynamically without becoming formless  

Looms are my **story skeletons**.  
Seeds fill them.  
The Narrative Engine animates them.  
Players bring them to life.

---

# What a Story Loom Is (My Definition)

A Story Loom is:

- **a metaphoric shape**
- **a sequence of emotional beats**
- **a set of narrative roles**
- **a mythic arc**
- **a reusable structure** that can hold countless specific stories

A Loom doesn’t tell me *what* happens — it tells me *how* a story wants to move.

I never lock Looms to one region or one dungeon.  
They travel. They echo. They mutate.  
They are ancient and migratory.

---

# Loom Format (My SSOT Schema)

Each Loom follows a consistent internal format:

~~~~yaml
story_loom:
  id: loom-lost-and-found
  title: "Lost and Found"
  scope: internal
  visibility: internal
  status: active
  confidence: high

  emotional_arc: longing → uncertainty → revelation → bittersweet_return

  roles:
    seeker: character
    lost_thing: object | person | memory
    witness: character | location
    hidden_force: god | curse | environmental

  beats:
    - id: call
      description: "Something cherished has vanished or strayed."
    - id: descent
      description: "The search leads into danger, memory, or illusion."
    - id: encounter
      description: "The truth reveals itself — partially, painfully, or beautifully."
    - id: return
      description: "What is found returns changed, or the seeker returns changed."

  suitable_domains:
    - water
    - moon
    - death

  notes: |
    Works beautifully in Rothigport, Fecundia, Gloam regions.
~~~~

Every Loom in my SSOT follows this shape.

---

# The Core Looms I Use in Deluvia

Below are the **twelve primary Looms** I rely on — one for each elemental domain.  
These aren’t quests. They’re **mythic gravitational fields.**

---

## 1. **Loom of the Drowned Memory** (Water)

**Arc:** memory → resurfacing → confrontation → release  
**Themes:** grief, nostalgia, retrieval  
**Typical beats:**  
- something calls from the past  
- something returns wrong or incomplete  
- a truth drowns unless remembered  
- a choice must be made between past and present

---

## 2. **Loom of Molten Change** (Fire)

**Arc:** destruction → revelation → transformation → cost  
**Themes:** rebirth, sacrifice, volatility  
**Typical beats:**  
- something burns that cannot be unburned  
- a truth emerges in firelight  
- someone changes form  
- the transformation demands a price

---

## 3. **Loom of Burdened Soil** (Soil)

**Arc:** humility → labor → endurance → earned grace  
**Themes:** work, patience, grounded truth  
**Typical beats:**  
- the world grows heavy  
- someone must carry a literal or spiritual burden  
- the ground reveals its quiet wisdom  
- a small, humble reward becomes significant

---

## 4. **Loom of the Quiet Rot** (Poison)

**Arc:** temptation → corruption → blooming ruin → reckoning  
**Themes:** decay, beauty, allure of wrongdoing  
**Typical beats:**  
- a subtle taint creeps in  
- someone enjoys the benefits of a curse  
- corruption blooms beautifully  
- a reckoning comes, gentle or catastrophic

---

## 5. **Loom of the Breaking Sky** (Storm)

**Arc:** upheaval → valor → chaotic test → storm’s mercy  
**Themes:** bravery, chaos, adrenaline  
**Typical beats:**  
- the storm arrives  
- someone must stand against it  
- lightning reveals a hidden truth  
- survivors earn a brief moment of stillness

---

## 6. **Loom of the Mirror Moon** (Moon)

**Arc:** illusion → doubling → distortion → revelation  
**Themes:** dreams, secrets, duality  
**Typical beats:**  
- something appears in doubled form  
- shadows behave strangely  
- truth comes through reflection  
- someone meets a version of themselves

---

## 7. **Loom of the Revealing Dawn** (Sun)

**Arc:** ignorance → revelation → clarity → mercy or judgment  
**Themes:** truth, illumination, harsh honesty  
**Typical beats:**  
- light falls where it wasn’t meant to  
- a lie is exposed  
- someone must face what is  
- truth heals or destroys

---

## 8. **Loom of the Hammered Dream** (Ore)

**Arc:** craft → obsession → breakthrough → complication  
**Themes:** invention, making, dangerous inspiration  
**Typical beats:**  
- someone begins a work  
- the work consumes them  
- the work reveals something unexpected  
- the result creates its own trouble

---

## 9. **Loom of the Fractured Path** (Chaos)

**Arc:** coincidence → anomaly → collapse → strange harmony  
**Themes:** chance, randomness, fate fractures  
**Typical beats:**  
- things go wrong or right by luck  
- patterns break  
- absurdity spikes  
- the world settles into a new, crooked rhythm

---

## 10. **Loom of the Wandering Wind** (Wind)

**Arc:** desire → seeking → redirection → chosen course  
**Themes:** purpose, travel, shifting intentions  
**Typical beats:**  
- a desire stirs  
- the wind offers mixed guidance  
- someone must choose a direction  
- journey becomes destiny

---

## 11. **Loom of Verdant Becoming** (Life)

**Arc:** seed → growth → flourishing → entanglement  
**Themes:** fertility, renewal, entanglement  
**Typical beats:**  
- something small begins  
- it grows beyond control  
- abundance becomes problem or gift  
- pruning or harvest must follow

---

## 12. **Loom of Quiet Finality** (Death)

**Arc:** ending → stillness → echo → closure  
**Themes:** loss, inevitability, peace  
**Typical beats:**  
- a door closes  
- silence stretches  
- an echo remains  
- someone accepts the ending  

---

# How I Use Looms in Procedural Storytelling

When I generate or structure emergent content, I:

1. Identify the region’s dominant **elemental vectors**  
2. Select Looms that match that tonal pressure  
3. Bind Seeds to Loom roles  
4. Let the Narrative Engine adjust beats based on:
   - virtue/vice drift  
   - regional story_thread  
   - Chronicle entries  
5. Generate dialogue, rumors, events using **Loom-shaped constraints**  
6. Always allow the Loom to “bend” in response to players  

Looms keep my stories from becoming noise.  
They are the *bones of mythic coherence.*

---

# Canonical Truths

- Deluvia’s stories follow ancient shapes I call **Story Looms**.  
- Each Loom is a reusable mythic pattern, not a plot.  
- Looms shape emergent narrative without dictating outcomes.  
- Players activate Looms naturally by moving through the world.  
- Seeds, Looms, and the Narrative Engine form Deluvia’s story ecology.  
"""

# Ensure the output directory exists
os.makedirs("generation", exist_ok=True)

# Write the file
output_path = "generation/story-looms.md"
with open(output_path, "w") as f:
    f.write(content)

print(f"Generated: {output_path}")