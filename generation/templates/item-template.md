---
id: item-template
type: template
title: "Item Template"
scope: internal
visibility: internal
status: active
confidence: high
tags:
  - template
  - item
  - relic
---

# Item Template

I use this template for relics, enchanted items, cursed objects, humble tools with stories, and other tangible artifacts in Deluvia.

Items are not just stats.  
They are condensed stories — little islands of history, virtue, vice, and elemental mood.

---

## Frontmatter (Required)

```yaml
id: item-unique-id
type: item
title: "Item Name"
scope: canon                 # canon | internal | mechanical | meta | apocrypha
visibility: public           # public | internal | secret
status: draft                # draft | active | deprecated
confidence: medium           # high | medium | low | speculative | apocryphal
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD

tags: []                     # e.g. [soil, humility, beetlefolk, relic]
item_type: null              # weapon | armor | tool | trinket | relic | consumable | charm | focus | tome | key
rarity: common | uncommon | rare | legendary | mythic | cursed

associated_element: null     # one of the Twelve Elements
associated_virtue: null      # e.g. humility
associated_vice: null        # e.g. vanity
associated_god: null         # deity id, if any
associated_region: null
associated_town: null
associated_dungeon: null

links:
  related: []                # related items, quests, dungeons, npcs
  origin_quest: null         # quest id, if obtained via quest
  bound_to_npc: null         # npc id, if story-bound
  tied_rituals: []           # ritual ids that use or awaken this item

story_weight: medium         # low | medium | high | canonical-candidate
implementation_path: null    # where Denizen / data live
source: human | ai-generated
```

---

# {Item Name}

## Mythic Description

A short, atmospheric description of the item as it would be spoken of in taverns, shrines, or nightmares.

- what does it *feel* like to carry or wield this?  
- what images, sounds, or smells accompany it?  
- what rumors cling to it?  

---

## Physical Description

Concrete details:

- materials  
- size, weight, texture  
- symbols, engravings, fungi, etchings, stains  
- light effects (glow, shadow, shimmer)  

This is what a player would see if I held it up to the camera.

---

## Origin & History

How did this item come to be?

- forged, grown, shed, unearthed, woven, summoned, or gifted?  
- who made it or called it into being?  
- what event, god, or dungeon is tied to its birth?  

Include at least one **uncertain** or contested detail to leave room for future lore fragments.

---

## Properties & Behavior

### Mundane Properties

Even a relic is still an object:

- durability  
- quirks in daily use  
- who can use it without backlash (if anyone)  

### Magical / Special Properties

High-level behavior, not code:

- what it does (mechanically and narratively)  
- how it interacts with the Twelve Elements  
- how it affects virtue/vice (if at all)  
- any ongoing auras or effects  

Keep this implementation-agnostic but clear enough that I can map it to real stats later.

---

## Costs, Risks, and Curses

What does it demand?

- fatigue, corruption, attention from a god  
- loss of reputation, memory, or time  
- side effects that slowly grow over use  

Items that matter should change the wielder or the world in some way.

---

## Usage in the World

How does this item show up in play?

- quest reward  
- dungeon heart artifact  
- heirloom of a specific NPC or clan  
- rare shop item  
- ritual focus in certain shrines  
- rumor magnet  

If it is meant to be unique, say so.  
If multiples exist as a “pattern” (e.g. beetlefolk tools), note that too.

---

## Integration with Systems

### Narrative Engine

Does using or obtaining this item generate Story Signals?

Examples:
- stealing a sacred relic → corruption / vice spike  
- returning a lost item → humility / truth / closure  

### Virtue–Vice System

Which virtues or vices does this item lean toward?

- humility vs vanity  
- courage vs cowardice  
- truth vs deception  

### Town State System

Does this item affect:

- prices  
- security  
- festivals  
- omens  
- general mood in a town?  

### Dungeon Mutation Engine

Is this item tied to:

- a dungeon’s heart  
- corruption levels  
- boss forms  
- hidden paths?  

### Pantheon Attention System

Does this item:

- attract a god’s gaze  
- mask the wielder from divinity  
- channel worship unintentionally?  

---

## Procedural Hooks

For AI and generation:

- keywords for story-seed-engine  
- which story_looms this item might touch  
- whether this item should spawn:
  - rarely  
  - in specific biomes  
  - only under certain narrative conditions  

This helps automatic content-generation place the item with taste.

---

## Notes

Design notes for myself:

- inspirations (other media, dreams, real-world artifacts)  
- balance concerns  
- gut feeling: “this is a key relic” vs “this is flavor”  
- future ideas (upgrades, corrupted variants, echoes)  

