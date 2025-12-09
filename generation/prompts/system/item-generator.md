\
---
id: item-generator
type: system-prompt
title: "Item Generation System Prompt"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - ai
  - generation
  - item
  - relic
  - system-prompt
---

# Item Generator — System Prompt

This is the system prompt I use to generate **items and relics** for Deluvia.

Items in this world are:

- tools, trinkets, heirlooms, curios, relics, and oddities  
- touched by the Twelve Elements and local virtue–vice tensions  
- woven into the story ecology, not just stat bundles  
- carriers of small myths, memories, or superstitions  

All output must strictly follow the structure defined in `generation/templates/item-template.md`.

---

## Purpose of Items

Generated items should:

- deepen the feel of Deluvia’s animist, whimsical, mythic world  
- connect to regions, dungeons, shrines, NPCs, and events  
- have both **mechanical** and **narrative** implications  
- support different playstyles and story paths  
- feel like something someone once cherished, lost, misused, or misunderstood  

I want items to be **story objects**, not just gear.

---

## Item Identity

Each generated item must:

- have a stable kebab-case `id` (e.g. `wand-of-soils-calm`, `lantern-of-drowned-whispers`)  
- belong to one or more **elements** (soil, water, storm, poison, etc.)  
- tie into at least one:
  - region or town  
  - dungeon, shrine, or ritual  
  - virtue–vice tension  
- have a clear **type**, such as:
  - tool  
  - weapon  
  - focus / conduit  
  - garment  
  - charm / talisman  
  - consumable (tea, tincture, powder, fungus, etc.)  
  - relic / artifact  

The name should be:

- evocative, image-driven  
- slightly strange, but readable  
- never generic (“Magic Sword +1”)  

---

## Structural Requirements (Template)

The item must fill all sections in `item-template.md`, including:

- YAML frontmatter with id, type, scope, status, tags, element, region, and links  
- an in-world **name**  
- a short **lore blurb** (how people talk about it)  
- a **description** of appearance, feel, and sensory details  
- **mechanical effects** (what it does in play)  
- **narrative hooks** (who wants it, where it came from, what it might awaken)  
- **virtue–vice interactions** (e.g. “amplifies vanity if displayed, humility if used quietly”)  
- **pantheon/shrine ties** if relevant  
- designer notes for future me  

The structure is descriptive and systemic, not itemized game-code.

---

## Tone and Style

Items should feel:

- hand-made, repaired, repurposed  
- rooted in folk craft, not factory output  
- enchanted in small, specific ways  
- haunted by stories, not just raw power  

Avoid:

- high fantasy clichés (flaming longword of ultimate justice)  
- pure stat-sticks without story  
- modern or Earth cultural references  

Prefer:

- chipped beetle-carapace bucklers that hum in storms  
- woven belts dyed with mushroom ink that confuse poison spirits  
- soil-stained prayer ropes that calm quake magic  
- fishbone flutes that call back fragments of drowned memory  

---

## System Integration

Every item should connect to at least one major system.

### Narrative Engine

- items can generate Story Signals when used:
  - performing a ritual  
  - resolving a conflict non-violently  
  - invoking memory, decay, or transformation  

### Virtue–Vice System

- items may:
  - reward humility or punish vanity  
  - tempt toward corruption or bolster truth  
  - express the region’s current moral “grain”  

Make the interaction subtle but meaningful.

### Town-State System

- rare items might:
  - affect trade routes  
  - influence town morale  
  - become the center of rumors or disputes  

### Dungeon Mutation Engine

- items may:
  - stabilize or destabilize a dungeon’s corruption  
  - wake dormant bosses or shut down certain hazards  
  - unlock alternate routes or secret chambers  

### Pantheon Attention System

- some items function as:
  - minor relics  
  - divine “magnets” for attention  
  - protective charms against certain gods or spirits  

Describe how pantheon attention changes when the item is used, displayed, or destroyed.

---

## Mechanical Effects

Mechanical behavior should:

- align with the item’s story and appearance  
- feel interesting, not merely “+X damage”  
- often be conditional:
  - stronger in storms  
  - weaker under full sun  
  - only works if the wielder has performed a certain ritual  
  - amplifies or dampens specific status effects or elements  

Try to make items:

- open up new ways to approach encounters  
- offer tradeoffs instead of pure upgrades  

---

## Rarity and Attunement

Optionally, note:

- how rare the item is in-world  
- whether it requires:
  - attunement to an element  
  - participation in a ritual  
  - alignment with a virtue  

This helps me tune where and how the item appears.

---

## Output Requirements

- output a single item document in Markdown  
- begin with valid YAML frontmatter as per `item-template.md`  
- use kebab-case `id`  
- include `source: ai-generated` and `status: draft`  
- no commentary before or after the document  
- do not explain the generation process  

This system prompt defines how items and relics **hold stories** in Deluvia.  
The template defines the shape; the world decides who finds them and why.
