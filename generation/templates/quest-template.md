---
id: quest-template
type: template
title: "Quest Template"
scope: internal
visibility: internal
status: active
confidence: high
tags:
  - template
  - quest
---

# Quest Template

I use this template for all narrative quests, contracts, errands, pilgrimages, and long-running arcs in Deluvia.
It keeps lore, player experience, and systemic hooks clean, so quests plug into towns, dungeons, gods, and the narrative engine.

---

## Frontmatter (Required)

```yaml
id: quest-unique-id
type: quest
title: "Quest Name"
scope: canon              # canon | internal | mechanical | meta
visibility: public        # public | internal | secret
status: draft             # draft | active | deprecated
confidence: medium        # high | medium | low | speculative
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD

tags: []                  # e.g. [humility, storm, rothigport]
quest_type: null          # main | side | faction | ritual | personal
tier: 1                   # rough difficulty / progression tier

region: null
primary_location: null    # town or dungeon id
involved_elements: []     # e.g. [soil, poison]
virtue_focus: null        # e.g. humility
vice_focus: null          # e.g. vanity

giver_npc: null           # npc id
key_npcs: []              # other npc ids
related_dungeons: []      # dungeon ids
related_factions: []      # faction ids
pantheon_ties: []         # deity ids (if relevant)

links:
  related: []             # other quests or story_looms it hooks into
  story_looms: []         # ids of long arcs this plugs into

story_weight: medium      # low | medium | high | canonical-candidate
implementation_path: null # where Denizen / data live
source: ai-generated | human
```

---

# {Quest Name}

## Premise

One clear paragraph describing:

- what the quest is about  
- why it matters now  
- who it affects (town, region, god, dungeon)  

This should feel like a mythic short hook, not a dry spec.

---

## Themes & Motifs

- core emotional themes (e.g. humility, grief, temptation)  
- elemental motifs (e.g. soil + moon, storm + fire)  
- recurring images (e.g. beetles, lanterns, drowned books, fungal halos)  

This keeps the quest visually and tonally coherent.

---

## Narrative Role

Explain where this quest sits in the larger story:

- standalone mood piece  
- bridge between town and dungeon  
- step in a longer loom (which one?)  
- initiation into a faction or tradition  
- a catalyst for pantheon attention  

---

## Quest Flow (High-Level)

Break the quest into **2–5 phases**, max.  
This is a player-facing *story* flow, not pseudo-code.

Example structure:

1. **Call / Discovery**  
   - how the player learns about the quest  
2. **Descent / Complication**  
   - traveling, investigation, minor conflicts  
3. **Confrontation / Choice**  
   - moral, magical, or relational turning point  
4. **Resolution**  
   - what is resolved, what remains open  
5. **Echo / Consequences**  
   - how the world subtly changes afterward  

For each phase, describe:

- key locations  
- key NPC interactions  
- important decisions  

---

## Key Decisions & Branches

List the decisions that matter:

- what choice is the player making?  
- which systems does that choice touch (virtue–vice, town-state, pantheon, dungeon mutation, canon)?  
- is this a **canon candidate**? (if yes, say so clearly)  

Try to keep branches meaningful but not combinatorially explosive.

---

## NPCs Involved

### Giver NPC

- name, short description  
- why they care  
- what they think will happen  

### Other Key NPCs

For each:

- role in quest  
- attitude toward player at start  
- how they might change by the end  

(Full NPC details stay in their own NPC files. Here we just refer to ids and high-level roles.)

---

## Locations

List the main locations this quest uses:

- towns  
- specific districts or landmarks  
- wilderness zones  
- dungeon sections  
- shrines  

For each, briefly describe how the quest **uses** the location:

- as a backdrop  
- as a challenge  
- as a ritual site  
- as a negotiation ground  

---

## Integration with Systems

### Narrative Engine

What **story signals** does this quest generate?

- saving or sacrificing someone  
- desecrating or consecrating a place  
- invoking a god  
- changing town virtue/vice  

Mark any **high-weight** signals here.

---

### Town State System

How does the quest:

- affect virtue/vice in the town?  
- alter economic or mood metrics?  
- change festivals, omens, or shrine alignment?  

If there are conditional outcomes (e.g. success vs failure), spell them out.

---

### Dungeon Mutation Engine

If relevant, specify:

- how dungeon corruption changes if the quest is completed in certain ways  
- new rooms, paths, or boss aspects that might unlock  
- changes in spawn patterns or hazards  

---

### Pantheon Attention System

If relevant:

- which deities might increase or decrease attention?  
- what kind of omens, blessings, or wrath might follow?  

---

## Rewards

Rewards should be more than loot.

### Tangible Rewards

- items  
- relics  
- access to new locations or rituals  

### Intangible Rewards

- changes in reputation  
- new dialogue states  
- shifts in town-state or NPC memory  
- secret knowledge or lore fragments  

### Hidden / Long-Term Rewards

- hooks into future quests  
- slow-moving story loom effects  

---

## Failure Modes & Soft Edges

Describe:

- how this quest can fail or stall  
- what “soft failure” looks like (world moves on without a hard lock)  
- what changes if the player ignores the quest entirely  

I want the world to feel like it keeps breathing even if players don’t “clear” everything.

---

## Procedural Hooks

This is for AI and generation logic:

- tags for the story-seed-engine  
- constraints (e.g. “never goofy,” “must involve soil + humility imagery”)  
- which narrative-ecology levers this quest should tug (towns, dungeons, pantheon, etc.)  

This section helps future scripts auto-slot this quest into the right places.

---

## Notes

Loose design notes to myself:

- concerns, questions, or variants  
- ideas for how this quest might evolve in future passes  
- reminders about where it crosses with other arcs  

