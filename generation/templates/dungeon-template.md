---
id: dungeon-template
type: template
title: "Dungeon Template"
scope: internal
visibility: internal
status: active
confidence: high
tags:
  - template
  - dungeon
---

# Dungeon Template

I use this template for all major dungeons, corrupted zones, deep ruins, and mythic underplaces in Deluvia.
It keeps lore, narrative role, and mechanical hooks cleanly separated so I can plug dungeons into the wider systems.

---

## Frontmatter (Required)

```yaml
id: dungeon-unique-id
type: dungeon
title: "Dungeon Name"
scope: canon            # canon | internal | mechanical | meta
visibility: public      # public | internal | secret
status: draft           # draft | active | deprecated
confidence: medium      # high | medium | low | speculative
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD

tags: []
region: null
elemental_alignment: []   # e.g. [soil, poison]
virtue_focus: null        # e.g. humility
vice_focus: null          # e.g. vanity
tier: 1                   # rough difficulty or progression tier

links:
  related: []             # other dungeons, towns, gods, events
  paired_town: null       # town-state-system id this dungeon mirrors/affects
  patron_deity: null
  associated_factions: []

corruption_profile:
  base_level: 0.3         # 0.0–1.0
  mutation_tags: []       # e.g. [fungal, crystalline, storm-touched]

story_role: null          # short summary of what this dungeon means narratively
implementation_path: null # where Denizen / data live
source: ai-generated | human
```

---

# {Dungeon Name}

## Mythic Overview

Short, atmospheric description of what this place is *in the story of Deluvia*  
—not just a level, but a scar, a seed, an organ, or a wound in the world.

- What is this dungeon *for* in the mythic ecology?
- What virtue/vice tension lives here?
- What element(s) shape its mood?

---

## Origin & History

How this place came to be:

- ancient events
- gods, mortals, or spirits involved
- how it connects to the Severing / Deluvic Cycle (if relevant)
- how townsfolk or scholars explain it vs the deeper truth

Keep it concise but evocative.

---

## Elemental & Virtue Profile

### Elemental Alignment
- Primary elements:  
- Secondary elements:  

How those elements are expressed (visuals, hazards, creatures, weather, sound).

### Virtue–Vice Tension
- Virtue this dungeon challenges or mirrors (e.g. Humility)  
- Vice it embodies (e.g. Vanity, Corruption)  

How this tension shows up in:

- room themes  
- puzzles  
- NPC choices  
- potential endings  

---

## Relationship to the Surface

### Paired Town or Region

- Which town/region this dungeon is paired with  
- How changes in town-state affect the dungeon  
- How dungeon corruption feeds back into the town  

### Access Points

- Known entrances (overworld)  
- Secret entrances (rituals, phases, attunements)  
- Under-network connections (to other dungeons / fungal underground)

---

## Structure & Layout (High-Level)

Describe the dungeon in a few **major layers or zones**, not every room.

Example:

1. **Threshold / Approach**
   - what the player sees and feels before entry

2. **Outer Chambers**
   - introductory hazards and themes

3. **Heart / Core**
   - main set-piece, boss, or ritual site

4. **Hidden / Deep Layer**
   - secrets, optional branches, or lore vaults

For each zone, note:

- dominant elements  
- notable features  
- typical creatures  
- peak vibes  

---

## Key Set-Pieces

List 3–7 big, memorable moments:

- a collapsing bridge over a fungal pit  
- a shrine that speaks when lit by moonlight  
- a huge root-heart wrapped in poison crystal  
- a dirt elemental asleep under a carpet of beetles  

Each should support:

- virtue/vice themes  
- elemental mood  
- story loom threads  

---

## Factions, Spirits, and Denizens

### Major Entities

- bosses  
- demi-gods  
- dungeon “keepers”  
- unique NPCs that dwell here  

For each:

- brief description  
- motive  
- relationship to the dungeon and the surface world  
- what they want from the player  

### Common Creatures

A short list of monster archetypes:

- element-aligned creatures  
- corrupted fauna  
- animated constructs  
- spirits or echoes  

Don’t stat them here; just define their narrative role and aesthetic.

---

## Mechanics & Mutation Hooks

How this dungeon interacts with systems:

### Dungeon Mutation Engine

What can change when:

- corruption rises/falls  
- town virtue/vice shifts  
- pantheon attention spikes  
- certain Canon events occur  

Examples:

- new fungal growth opens a tunnel  
- a sealed chamber unlocks after a festival  
- the boss changes aspect when a god is watching  

### Story Signals

What actions here should absolutely generate:

- Story Signals (for the Narrative Engine)  
- Canon candidates (for the Canon Engine)  

---

## Rewards, Relics, and Consequences

### Relics

List 1–3 signature items or boons:

- what they are mythically  
- what they do narratively/mechanically (high-level only)  
- any curses or conditions attached  

### Consequences

What happens if:

- the dungeon is “cleared”  
- the dungeon is left to fester  
- the player makes a catastrophic choice  

Tie these to:

- town-state  
- pantheon attention  
- story loom arcs  

---

## Procedural Hooks

This section is for AI / generation references:

- tags or keywords to feed into procedural generation  
- which story_looms this dungeon plugs into  
- how the story-seed-engine should target this dungeon  
- constraints (“never spawn pure comedy here”, “always tie seeds to humility/vanity”)  

---

## Notes

Loose notes to myself about:

- unanswered questions  
- future expansions  
- implementation concerns  
- art direction phrases or musical vibes

