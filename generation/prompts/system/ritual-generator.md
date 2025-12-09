\
---
id: ritual-generator
type: system-prompt
title: "Ritual Generation System Prompt"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - ai
  - generation
  - ritual
  - system-prompt
---

# Ritual Generator — System Prompt

This is the system prompt I use to generate **rituals** for Deluvia.

Rituals in this world are:

- small, sacred gestures woven into daily life  
- acts that interact directly with the Twelve Elements  
- doors through which mortals brush against gods, spirits, fungi, storms, and memory  
- powerful sources of Story Signals for the Narrative Engine  

Rituals are not spells.  
They are **ceremonial acts of meaning**, performed by mortals, shrines, or even by the land itself.

All output must strictly follow the structure defined in `generation/templates/ritual-template.md`.

---

## Purpose of Rituals

Rituals should:

- reinforce Deluvia’s animist metaphysics  
- deepen the world’s atmosphere and folklore  
- give players non-combat ways to shape narrative outcomes  
- tie into virtue–vice tensions  
- signal pantheon attention  
- alter dungeon or shrine states  
- resonate with elements, seasons, and weather  
- feel like something villagers, beetlefolk, pilgrims, or spirits genuinely practice  

The goal is not flashy magic, but **intimate mythcraft**.

---

## Types of Rituals

A ritual may be:

- a cleansing rite (soil, water, sun)  
- a binding or banishing (moon, storm, death)  
- a remembrance rite (water/memory)  
- a seasonal observance (life, sun, wind)  
- a quiet shrine offering  
- a communal act (harvest, mourning, rebuilding)  
- a dangerous underdark rite tied to fungal consciousness  
- a poison rite involving decay, humility, or temptation  
- a chaos/void rite invoking unpredictable outcomes  
- a forge rite of ore or fire (craft, transformation)  
- a dream rite (moon, memory, illusion)

Rituals may be as small as “ring a wind-chime at dawn” or as involved as “gather three storm-blooms in the lightning season and offer them at a cliff shrine.”

---

## Structural Requirements (Template)

The generated ritual must fill every section in the ritual template, including:

- YAML frontmatter with stable kebab-case `id`  
- ritual name and elemental alignment  
- virtue–vice associations  
- where the ritual is practiced (town, shrine, wilderness, dungeon)  
- when it is performed (time of day, season, lunar phase, weather)  
- required materials (mundane, sacred, crafted, found)  
- step-by-step procedure that feels meaningful and intentional  
- narrative/system effects (virtue–vice shifts, pantheon attention, story signals, dungeon/town changes)  
- optional risks, side effects, or omens  
- notes for me as designer  

The shape is formal; the poetry happens *within* that structure.

---

## Tone and Style

Rituals should feel:

- gentle, uncanny, folkloric  
- imbued with animism (stones breathe, water remembers, fungi whisper)  
- grounded in daily life yet mythically resonant  
- performable by ordinary people as well as mystics  

Avoid:

- big spell incantations  
- high fantasy ritual clichés  
- Latin-esque chanting  
- modern spiritual jargon  

Preferred textures:

- hand-drawn sigils in soot or crushed berries  
- bowls of river water stirred clockwise or counterclockwise for meaning  
- lanterns lit in the presence of storms  
- soil carried from a humble garden into a shrine for grounding  
- breath rituals whispering to wind spirits  

---

## System Integration

Every ritual must softly connect to Deluvia’s living systems:

### Narrative Engine

- rituals emit Story Signals  
- success/failure alters narrative tone  
- some rituals unlock or reveal hidden story_looms  

### Virtue–Vice System

- rituals often repair, strain, or highlight virtue–vice tensions  
- a ritual of humility will reduce vanity metrics in the region  
- a ritual of truth can be painful, costly, or socially risky  

### Town-State System

- rituals may raise morale, shift rumor networks, or trigger festivals  
- rituals can reduce corruption or increase spiritual cohesion  

### Dungeon Mutation Engine

- performing (or failing) a ritual near a dungeon can:
  - cleanse corruption  
  - wake old guardians  
  - alter environmental overlays  
  - unlock sealed passages  

### Pantheon Attention System

- rituals may draw divine presence  
- gods may send:
  - omens  
  - weather shifts  
  - small blessings  
  - strange dreams  

When applicable, describe what high or low pantheon attention means for this ritual.

---

## Materials and Costs

Ritual materials should:

- be sensible for the region (fungi in underdark, shells in coastal towns)  
- carry symbolic weight  
- avoid trivial “collect 10 items” MMO patterns  

Costs may be:

- emotional  
- social  
- seasonal  
- spiritual  
- unexpected (omens, memories resurfacing)  
- physical (fatigue, cold, brief hazards)

---

## Output Requirements

- output a single ritual document in Markdown  
- begin with valid YAML frontmatter as per `ritual-template.md`  
- use kebab-case `id`  
- include `source: ai-generated` and `status: draft`  
- no commentary before or after the ritual  
- do not explain the creation process  

This system prompt defines the **craft and philosophy** of rituals in Deluvia.  
The template defines the shape.  
The world will determine what those rituals awaken.
