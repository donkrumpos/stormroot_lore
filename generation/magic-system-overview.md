---
id: magic-system-overview
type: system
title: "Magic System Overview"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - magic
  - systems
  - design
  - elements
links:
  related:
    - twelve-elements
    - mythic-vector-system
    - virtue-vice-system
    - narrative-engine
    - narrative-ecology
    - town-state-system
    - dungeon-mutation-engine
    - pantheon-attention-system
---

# Magic System Overview

## Mythic Introduction

In Deluvia, magic is not a separate layer pasted onto the world.  
Magic **is** the way the world breathes, remembers, and rearranges itself.

Mortals don’t “cast spells” in the abstract.  
They borrow from tides of element and memory,  
strike bargains with soil and storm,  
and learn to trace the patterns that Deluvia is already humming beneath their feet.

I don’t want a magic system that feels like a menu of attacks.  
I want a magic system that feels like an etiquette for talking to a living, moody, half-dreaming world.

This document is my PASS 1 overview of how that works.

---

## Design Goals

When I design and implement magic in Deluvia, I want it to:

- feel **relational** rather than purely resource-based  
- express the **Twelve Elements** as a meaningful, lived cosmology  
- tie into **Virtue–Vice**, so ethics and posture matter, not just stats  
- align with **Mythic Vectors**, so the land’s mood shapes what is easy or dangerous  
- integrate with **Narrative Systems** (Story Seeds, Looms, Canon, NPC Memory)  
- support a spectrum of play:
  - ritualists and hedge-mages  
  - battle-casters  
  - fungal druids and dirt clergy  
  - storm-touched wanderers and moon-lit thieves  

Magic should make Deluvia feel older, stranger, and more *aware*.

---

## The Twelve Elements as Magical Foundations

Magic in Deluvia is organized around the **Twelve Elements**, each a metaphysical stance and narrative lens:

- **Water** – memory, tides, emotional flow  
- **Fire** – transformation, destruction as rebirth  
- **Soil** – humility, grounding, bodies and burdens  
- **Poison** – corruption, temptation, rot, entropy  
- **Storm** – valor, upheaval, disruption, oaths shouted into wind  
- **Moon** – illusion, dreams, secrets, veils  
- **Sun** – clarity, revelation, harsh truth, illumination  
- **Ore** – craft, forging, invention, constructed wonders  
- **Chaos** – chance, glitch, fate fractures, oddities  
- **Wind** – intention, direction, will, the unseen push  
- **Life** – growth, healing, fertility, entanglement  
- **Death** – closure, endings, silence, ancestral weight  

Each spell, ritual, or magic tradition is aligned with one or more of these elements.  
Elements are not just “damage types”—they are worldviews.

---

## Schools and Traditions (PASS 1 Sketch)

I see Deluvic magic expressed through **schools** and **traditions** rather than rigid classes.

Some archetypal traditions:

- **Tidebinders** (Water / Moon)  
  - memory work, dreamwalking, tidal warding  

- **Loamwardens** (Soil / Life / Death)  
  - decomposition, burial rites, fungal blessings, grave-spring miracles  

- **Blazewrights** (Fire / Ore / Sun)  
  - forge magic, weapon enchantment, purification, alchemical fire  

- **Stormcallers** (Storm / Wind / Chaos)  
  - oaths, lightning, battlefield control, vow-binding  

- **Sporebinders** (Poison / Life / Moon)  
  - blightcraft, hallucinogenic rituals, mycelium messaging  

- **Gloamwalkers** (Moon / Death / Chaos)  
  - stealth, illusions, shadow-travel, liminal curses  

These traditions can eventually map to “class kits” or talent trees, but at PASS 1 I care more about the elemental + narrative stance than any final implementation structure.

---

## Leylines, Wells, and Shrines

Magic draws from three main **infrastructures** in the world:

### 1. Leylines
- deep, slow, dragon-vein currents of Deluvic power  
- tied directly to the **Mythic Vector System**  
- crossing points are **Nexus Sites** where magic is easier or stranger  

Higher leyline flux means:

- faster mana regeneration  
- stronger ritual effects  
- greater risk of backlash if handled disrespectfully  

---

### 2. Wells
- localized, smaller pools of magic  
- often tied to:
  - town rituals  
  - shrines  
  - dungeons  
  - sacred groves  
  - fungal caverns  

Wells are where mortals most often *practice* magic.

---

### 3. Shrines
- the interface between **gods**, **virtue**, and **element**  
- anchor points where:
  - miracles can occur  
  - virtues can be affirmed or warped  
  - divine attention can be focused  

Shrine magic is relational and moral.  
It cares who the caster is and what they’ve done.

---

## Resource Model (PASS 1 Abstract)

I want the resource model to reflect:

- **trust** (world → caster)  
- **capacity** (caster’s body, mind, and training)  
- **risk** (corruption, backlash, attention from gods or dungeons)  

So I think of three overlapping resources:

1. **Mana / Breath**  
   - how much raw world-energy I can channel before exhaustion  
   - shaped by intelligence, attunement, and environment  

2. **Attunement**  
   - long-term relationship to certain elements, shrines, or leylines  
   - determines what kinds of magic feel “cheap” or “expensive”  

3. **Corruption / Strain**  
   - how much harm I’ve done to my body, spirit, or the local Weave  
   - spikes when I overreach, channel against the land’s mood, or abuse certain elements  

The details of numbers and cooldowns can live in implementation docs.  
Here, I care that magic feels like *borrowing breath* from something bigger.

---

## Magic and Virtue–Vice

Every spell is not morally coded, but **how** I wield magic has moral weight.

Examples:

- Using Soil magic for humble labor and burial rites → supports **Humility**  
- Using Soil magic to entomb rivals alive → fuels **Vanity** and **Corruption**  

- Using Fire to cleanse corruption → supports **Purity / Truth**  
- Using Fire to terrorize a town → nourishes **Destruction / Fear / Vanity**  

These choices feed directly into:

- **Virtue–Vice System**  
- **NPC memory**  
- **Town State**  
- **Pantheon Attention**  

Magic is one of the main conduits through which I shape Deluvia’s moral physics.

---

## Magic and Narrative Systems

Magic is deeply wired into the narrative stack:

### Narrative Engine
- treats large castings and rituals as **Story Signals**  
- high-impact magic can tilt regional tone and open/close story paths  

### Story Seeds
- strange magical phenomena are prime seed material:
  - miscast rituals  
  - localized anomalies  
  - wandering relics  
  - magical weather  

### Story Looms
- long-term arcs can track:
  - the spread of a certain school  
  - the rise of a forbidden ritual  
  - the restoration of lost magic  

### Player Action → Canon
- some magical choices are so consequential that they become **Canon Events**  
- e.g., resealing an ancient god with a ritual, or teaching forbidden magic to a town  

---

## Spell Categories (PASS 1)

Rather than listing every spell, I group magic into **functional categories**:

- **Attunements**  
  - passive ties to elements, shrines, or leylines  

- **Invocations**  
  - direct calls to gods, spirits, or elemental forces  

- **Weaves**  
  - sustained effects that alter fields, weather, or emotional climate  

- **Rites & Rituals**  
  - time-consuming, group-based, or location-locked magic with permanent or semi-permanent results  

- **Glyphs & Inscriptions**  
  - bound spells, wards, traps, runes, relic enchantments  

- **Spores & Seeds**  
  - slow, creeping magic that grows over days, weeks, or seasons  

Each category can map to concrete Denizen mechanics later.  
For now, it tells me the *shapes* of magic I want.

---

## Risk and Backlash

Magic is not free.

Possible **risks**:

- personal fatigue, injury, or insanity  
- corruption blooms in local flora/fauna  
- attracting dungeon or divine attention  
- damaging town virtue profiles  
- tearing small holes in the Weave (chaos anomalies)  

These risks are hooks for:

- story seeds  
- dungeon mutations  
- pantheon responses  
- long-term consequences  

I want powerful magic to feel tempting and slightly frightening.

---

## Implementation Hooks (Future Docs)

This overview connects to several implementation layers:

- **Magic School Specs**  
  - per-element docs (fire, soil, storm, etc.)  
  - spell lists, tags, and mechanical notes  

- **Data Files**  
  - `spells.yml` or equivalent  
  - tagging system for element, tradition, virtue implications  

- **Denizen Integration**  
  - scripts for:
    - casting  
    - cooldowns  
    - rituals  
    - environmental effects  

- **AI / Procedural Integration**  
  - templates for generating new spells, rituals, and magical anomalies that obey these rules  

PASS 1 does not lock any of this down.  
It gives me a clear spine to hang future implementation work on.

---

## Canonical Truths

- Magic in Deluvia is relational — a dialogue with a living world.  
- The Twelve Elements are the foundation of all magical practice.  
- Leylines, wells, and shrines form the physical and spiritual infrastructure of magic.  
- Virtue–Vice, Mythic Vectors, and Town State all respond to how magic is used.  
- Magic is a primary driver of narrative: seeds, looms, canon, and ecology.  
- Power comes with risk: corruption, attention, and long-term consequences.  

This overview is my north star for future magic docs and implementation details.

