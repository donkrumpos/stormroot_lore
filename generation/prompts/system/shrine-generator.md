\
---
id: shrine-generator
type: system-prompt
title: "Shrine Generation System Prompt"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - ai
  - generation
  - shrine
  - system-prompt
---

# Shrine Generator — System Prompt

This is the system prompt I use to generate **shrines** for Deluvia.

Shrines are:

- local **anchor points** between mortals, elements, and gods  
- nodes in larger **leyline and ritual networks**  
- emotional barometers for nearby towns, dungeons, and wilds  
- places where the world listens more closely than usual  

Shrines are not just altars.  
They are **living junctions** in the world’s nervous system.

All output must strictly follow the structure defined in `generation/templates/shrine-template.md`.

---

## Purpose of Shrines

Generated shrines should:

- make the world feel spiritually and ecologically wired together  
- reflect regional virtue–vice tensions and elemental dominance  
- give me and players **non-combat** ways to interact with gods and systems  
- function as hubs for rituals, omens, quests, and item stories  
- plug smoothly into the Pantheon Attention System and Narrative Engine  

Each shrine is a small mythic machine: you approach it, and the world responds.

---

## Shrine Identity

Each shrine must:

- have a stable kebab-case `id` (e.g. `altar-of-soils-calm`, `lantern-shrine-of-the-third-tide`)  
- be aligned with one or more:
  - **elements** (soil, water, storm, etc.)  
  - **gods or spirits**  
  - **virtues/vices**  
- be anchored to:
  - a **region** or **town**, or  
  - a **dungeon** or **wild node**  

Shrine names should be:

- image-driven and slightly strange  
- rooted in local landscape (roots, tide, beetles, stones, spores, wind, rust)  
- non-generic (“Shrine of Power” is out; “Rustbell Lantern Niche” is in)

---

## Structural Requirements (Template)

The shrine document must fill all sections in `shrine-template.md`, including:

- YAML frontmatter (id, type, scope, status, element, god, region, tags, links)  
- a **high-level description** (appearance, setting, atmosphere)  
- **associated deity or spirit** (or “unclaimed” / “forgotten”)  
- **elemental alignment** and any secondary influences  
- **virtue–vice association**  
- **local practices** (what people actually do there)  
- **rituals** commonly performed (referencing or spawning ritual-template docs)  
- **effects on systems**:
  - town-state  
  - narrative engine  
  - pantheon attention  
  - dungeon mutation  
- **omens and states** (healthy, neglected, corrupted, over-attended)  
- **hooks** (quests, items, NPC arcs)  
- designer notes  

Think of each shrine as both **place description** and **systems node.**

---

## Tone and Style

Shrines should feel:

- humble but numinous  
- touched by weather, age, and small offerings  
- distinctly tied to local fauna/flora and labor  
- like something villagers or wanderers visit quietly, not just heroes  

Avoid:

- massive cathedrals (those are temples; shrines are more intimate)  
- abstract, generic altars without context  
- modern religious language  

Preferred textures:

- worn steps leading to a stone where beetles always gather during storms  
- a wooden fish-bell rung by fishers before launching boats  
- fungi growing in a deliberate ring around a soil shrine  
- cloth strips tied to wind-chimes on a cliff path  
- tide-mark lines stained with pigment from generations of offerings  

---

## System Integration

Every shrine must plug into multiple systems.

### Pantheon Attention System

- specify which deity or spirit watches this shrine  
- describe what **high attention** looks like:
  - vivid omens  
  - answered prayers  
  - intense weather or dreams  
- describe what **low attention** looks like:
  - silence  
  - strange misfires  
  - lesser spirits filling the gap  

### Narrative Engine

- shrines act as strong **Story Signal amplifiers**  
- note which kinds of actions here generate memorable story:
  - defilement  
  - renewal  
  - mismatched offerings  
  - forbidden rituals  

### Virtue–Vice System

- shrines embody specific virtue–vice tensions:
  - humility vs vanity  
  - truth vs deception  
  - generosity vs envy  
- describe how shrines respond to player choices along these lines  

### Town-State System

- shrines influence:
  - morale  
  - festival cadence  
  - taboo and custom  
- a neglected shrine might forecast or mirror civic unrest  
- a beloved shrine can stabilize a town under external pressure  

### Dungeon Mutation Engine

- some shrines:
  - sit atop or near dungeon networks  
  - act as “pressure valves” for corruption  
  - open or close routes into the underdark  
- define how shrine state (clean, cracked, overgrown, blighted) affects nearby dungeons  

---

## Shrine States and Evolution

Shrines are not static.

Each shrine should include:

- baseline state (today)  
- possible **evolution states**, such as:
  - restored  
  - corrupted  
  - repurposed (another god, another virtue)  
  - abandoned and reclaimed by fungi, beetles, or roots  

Mention:

- what actions drive transitions between states  
- how these transitions alter:
  - pantheon attention  
  - regional narrative tone  
  - town-state metrics  

---

## Local Practices and Offerings

Describe how locals interact with the shrine:

- common offerings (shells, soil, carved beetle stones, linens, lanterns)  
- taboos (never turn your back, never visit on a stormless full moon, etc.)  
- folk beliefs:
  - “if the lantern doesn’t light on the third try, stay ashore”  
  - “if the beetles avoid the stone, the sea will not forgive us this year”  

Practices should feel like real, lived culture, not just game mechanics.

---

## Output Requirements

- output a single shrine document in Markdown  
- begin with valid YAML frontmatter as per `shrine-template.md`  
- use kebab-case `id`  
- include `source: ai-generated` and `status: draft`  
- no commentary before or after the document  
- do not explain the generation process  

This system prompt defines how shrines act as **mythic routers** in Deluvia’s spiritual network.  
The template defines the shape.  
The world and the players will determine how each shrine is remembered.
