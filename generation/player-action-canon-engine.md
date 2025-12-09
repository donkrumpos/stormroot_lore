---
id: player-action-canon-engine
type: system
title: "Player Action → Canon Engine"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - canon
  - narrative
  - player-agency
  - systems
links:
  related:
    - narrative-engine
    - story-seed-engine
    - npc-memory-system
    - virtue-vice-system
    - mythic-vector-system
---

# Player Action → Canon Engine

## Mythic Introduction

Most things mortals do in Deluvia pass like footprints in the tide.  
They matter for a while, then the world smooths over and continues breathing.

But some deeds do not wash away.

A broken oath at the wrong shrine,  
a mercy shown to the wrong monster,  
a book thrown into the wrong fire —  

these can bend the long spine of the world and become **Canon**:
facts the world will never forget.

This document defines how a single player action sometimes becomes part of the permanent myth of Deluvia.

---

# Design Intent

I use the Player Action → Canon Engine to:

- decide **which** player actions should shape world history  
- keep most actions light while letting some have deep, lasting weight  
- update gods, towns, dungeons, and story systems with irreversible changes  
- provide a sense of **fate** without railroad  
- feed long-term play: returning players see echoes of years-old choices  
- record these changes in the **Chronicle of Deeds** and broader Canon  

I want Canon to feel rare, significant, and slightly dangerous.

---

# Canon vs. Normal Story

I distinguish three layers:

1. **Ephemeral State**  
   - mood, temporary buffs, small dialogue tweaks  
   - fades quickly  
2. **Persistent State**  
   - NPC memory, dungeon drift, virtue–vice scores  
   - changes slowly, but still reversible over time  
3. **Canon State**  
   - one-way valves  
   - world-level facts that, once set, are never fully undone  

Canon State is the backbone the rest of the systems drape themselves over.

---

# Canon Event Structure

I encode Canon Events like this:

~~~~yaml
canon_event:
  id: canon-dirt-kingdom-clodhaught-tested
  title: "Clodhaught Tested by Mortal Hand"
  category: dungeon | town | divine | global | personal
  priority: major | minor

  source:
    actor: player_id
    location: region_id
    related_npcs:
      - meek
    related_dungeons:
      - dirt_kingdom
    related_towns:
      - rothigport

  triggers:
    # The conditions that made this action canon-worthy
    thresholds:
      humility: "> 2"
      vanity: "< -1"
    dungeon_state_requirements:
      dirt_kingdom: "corruption_level > 0.6"

  description: >
    The player accepted Clodhaught's duel as a test, not as conquest,
    and left the chamber with their humility increased rather than their fame.

  consequences:
    mythic_vectors:
      region: rothigport
      adjustments:
        soil: +0.4
        storm: -0.1
    virtue_vice:
      rothigport:
        humility: +0.6
        vanity: +0.1
    flags_set:
      - clodhaught_has_been_tested_by_mortals
    dungeon_state:
      dirt_kingdom:
        corruption_level: "-= 0.1"
        unlocked_wings:
          - "meeks-hidden-garden"
    npc_memory:
      meek:
        relationship:
          respect: "+= 0.4"
          awe: "+= 0.3"
~~~~

Canon Events explicitly update:

- **Mythic Vectors**  
- **Virtue–Vice State**  
- **Dungeon State**  
- **NPC Memory**  
- **World Flags** (rare, global toggles)  

---

# When Does an Action Become Canon?

I don’t want every lever-pull to be canon.

I use three criteria:

## 1. Mythic Pressure

The action happens in a context where:

- regional mythic vectors are high-tension  
- virtue and vice are both active in the same domain  
- a dungeon or town is near a phase threshold  
- a god’s attention is lingering  

Canon should emerge from **pressure points**, not calm water.

---

## 2. Narrative Uniqueness

The action is:

- rare, unusual, or strongly divergent  
- a clear choice between meaningful paths  
- something most players will not do in exactly the same way  

If a behavior is extremely common and repetitive, it usually stays below Canon.

---

## 3. Systemic Reach

The action affects multiple systems at once:

- a dungeon and a town  
- an NPC and a god  
- a relic and a virtue/vice meter  

The more cross-cutting the impact, the more likely it is to crystallize.

---

# Detection Flow

Conceptually, the engine does this:

1. **Observe**  
   - listen for Story Signals flagged `canon_candidate: true`  
   - some actions are pre-marked (e.g., shrine rituals, boss bargains)  

2. **Evaluate Context**  
   - check mythic vectors, virtue/vice, dungeon state, NPC memory  
   - measure pressure and uniqueness  

3. **Roll Canon**  
   - if thresholds are met:
     - construct a `canon_event`
     - push it into the **Chronicle of Deeds**
     - apply consequences  

4. **Broadcast**  
   - notify Narrative Engine, Story Looms, Seed Engine, NPC Memory System  
   - allow them to express the canon change in their own languages  

---

# Canon and the Chronicle of Deeds

Not every Chronicle entry is Canon, but every Canon Event is stored as a **crowned** Chronicle entry.

~~~~yaml
chronicle_entry:
  id: deed-1342
  actor: player_id
  event: "Accepted Clodhaught's duel and chose humility over fame."
  region: rothigport
  domain: soil
  timestamp: ISO8601
  consequences:
    - npc_memory_update
    - dungeon_state_shift
    - regional_tone_modification
    - virtue_meter_adjustment
  is_canon: true
  canon_id: canon-dirt-kingdom-clodhaught-tested
~~~~

This gives me a single pipeline:  
mundane deeds and transcendent deeds share the same story river.

---

# Examples

## Example 1: Vanitas Bonfire

- Player repeatedly throws books into Noxhortes’ bonfire.  
- Town virtue (Truth) drops, Poison and Moon vectors spike.  
- A threshold is reached.

Possible Canon Event:

- “The Night of Unlearning”  
- Books across Rothigport begin rotting.  
- Some NPCs permanently lose memories or skills.  
- Libraries are marked as cursed sites.  

Canon consequence:
- future characters in this save live in a post-Unlearning world.

---

## Example 2: Sparing a Boss

- Player chooses to spare a dungeon boss instead of killing them.  
- This wasn’t expected by local cults or gods.  

Canon Event:

- the boss becomes a wandering mythic figure  
- appears later in towns, helping or testing the player  
- dungeons realign around the absence of a “final boss”  

The story of that mercy becomes a regional legend.

---

## Example 3: Founding a Shrine

- Player repeatedly performs a certain ritual at an unmarked spot.  
- Regional vectors and virtue align with that behavior.  

Canon Event:

- a new minor shrine appears, recognized by the gods  
- NPCs begin to visit it  
- Story Seeds use it as a new locus  

The player’s private habit becomes a permanent part of the world.

---

# Canon Safety & Scope

Canon should feel powerful, not paralyzing.

Guidelines I follow:

- Canon rarely blocks future stories; instead it **bends** them.  
- I prefer “you changed the flavor of what happens” to “you locked content out forever.”  
- When something is permanently blocked, it should be:
  - thematically appropriate  
  - clearly signaled  

Canon is a commitment.  
I want it to feel like lighting a candle in a cathedral, not flipping a random switch.

---

# Integration with Other Systems

### Narrative Engine
- updates story_thread baselines  
- influences emergent story logic  

### Mythic Vector System
- Canon events can spike or permanently shift vector baselines  

### Virtue–Vice System
- Canon moments often lock in virtue/vice changes  

### Dungeon Mutation Engine
- Canon can unlock or retire entire dungeon phases  

### NPC Memory System
- Canon changes become “everyone knows this now” in a region  

### Story Seed and Story Loom Systems
- new seeds and Loom patterns unlock or retire after Canon events  

This ensures Canon is not just a flag — it’s a **chord** across the whole system.

---

# Best Practices I Follow

- Canon moments should be rare, understandable, and emotionally resonant.  
- The player should **feel** when something just became Canon, even without explicit UI.  
- Canon should deepen a save file’s uniqueness.  
- Canon should be talkable: NPCs, songs, and shrines reference it.  
- I only promote to Canon when I am willing to live with that history permanently.  

---

# Canonical Truths

- Not all actions in Deluvia become Canon — only those under mythic pressure, with unique shape and broad impact.  
- Canon events are stored in the Chronicle of Deeds and never erased.  
- Canon reshapes towns, dungeons, NPCs, vectors, virtues, and seeds.  
- Each save becomes its own timeline of Canon, a personal myth-branch of Deluvia.  
- The Player Action → Canon Engine is the bridge between short-term play and long-term world history.

