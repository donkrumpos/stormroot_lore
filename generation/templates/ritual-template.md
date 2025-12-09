---
id: ritual-template
type: template
title: "Ritual Template"
scope: internal
visibility: internal
status: active
confidence: high
tags:
  - ritual
  - template
  - magic
---

# Ritual Template

I use this template to create the rites, observances, ceremonies, offerings, and mythic actions that weave the world of Deluvia together.

A ritual is not a spell.  
It is a **conversation with the world**, performed through gesture, offering, intention, and alignment with elemental or divine forces.

Rituals may be lore-first (for books and shrines), or gameplay-first (for mechanics, buffs, debuffs, unlocks).

---

## Frontmatter (Required)

```yaml
id: ritual-unique-id
type: ritual
title: "Ritual Name"
scope: canon                 # canon | internal | mechanical | meta | apocrypha
visibility: public           # public | internal | secret
status: draft                # draft | active | deprecated
confidence: medium           # high | medium | low | speculative | apocryphal
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD

tags: []                     # e.g. [soil, humility, fungal-rites]
ritual_type: null            # offering | shrine | seasonal | moon-phase | crafting | funerary | oath | curse | blessing | cleansing | communion
tier: common | uncommon | rare | sacred | forbidden

associated_element: null     # one of the Twelve Elements
associated_god: null         # id of deity
associated_region: null
associated_town: null
associated_dungeon: null

virtue_alignment: null       # e.g. humility
vice_alignment: null         # e.g. vanity

difficulty: low | medium | high | perilous
risk_level: none | mild | severe | existential

links:
  related: []                # other rituals, lore fragments, spells
  unlocks: []                # spells, paths, shrines, NPC trust
  required_by: []            # quests or story-looms that depend on this

source: human | ai-generated
```

---

# {Ritual Name}

## Mythic Description

A narrative, poetic framing of the ritual — what it evokes, how it feels, what the practitioners believe it accomplishes.

This is the voice of Deluvia itself, the old world whispering.

Examples of tones:
- reverent  
- secretive  
- earthy and fungal  
- lunar and dreamlike  
- blighted and dangerous  
- fiery and transformative  
- wind-born and wanderer-like  

Keep it evocative, symbolic, atmospheric.

---

## Requirements

### Materials
- physical items  
- rare reagents  
- offerings  
- relics  
- natural objects  

### Place
Where must this occur?
- shrine  
- leyline crossing  
- moonlit clearing  
- fungal cavern  
- mountaintop  
- river’s memory pool  
- dungeon heart  

### Time
- lunar phase  
- season  
- storm alignment  
- “when fog blooms across the fen”  
- after defeating a specific creature  

### Participants
- solo  
- duet  
- coven  
- community  
- NPC involvement  

---

## Procedure

Step-by-step instructions, written from my perspective as designer and ritualist.

Make them:
- clear  
- mystical but unambiguous  
- game-implementable  

Example structure:

1. **Approach** — gesture, posture, spoken line
2. **Offering** — what is given, destroyed, planted, burned, drowned, whispered
3. **Alignment** — how the participant attunes to element, virtue, god, or leyline
4. **Act** — the core transformative action
5. **Seal** — how the ritual concludes, resets, or closes

---

## Outcomes

### Mechanical Effects (if any)
- buffs / debuffs  
- unlock spells  
- change town-state metrics  
- adjust virtue/vice  
- awaken NPC memory  
- mutate dungeon  
- alter regional tone-state  

### Narrative Effects
- visions  
- lore fragments unlocked  
- pantheon attention change  
- omens  
- player reputation shifts  

### Failure States
If the ritual falters:
- backlash  
- curses  
- wandering spirits drawn  
- pantheon displeasure  
- corruption bloom  

---

## Interpretations

Multiple possible readings:
- literal (what happens mechanically)
- symbolic (what the ritual expresses)
- cultural (what different peoples think it means)
- divine (what the gods actually respond to)
- ecological (how it affects the Weave and soil-memory)

This gives rituals nuance and lets them appear in books, dungeons, shrines, NPC dialogue, and mythic visions.

---

## System Hooks

### Narrative Engine
Does this ritual generate Story Signals?
Which domain(s) does it activate?

### Virtue/Vice System
What virtue does it strengthen?
What vice does it risk invoking?

### Dungeon Mutation
Does this ritual alter corruption levels or environmental effects?

### Pantheon Attention System
Which god notices?
How strongly?

### Magic System
Does this ritual deepen attunement?
Change mana behavior?
Unlock new spellcasting routes?

---

## Notes
Any behind-the-scenes designer notes:
- what inspired this ritual  
- concerns for balance  
- where it might appear in-game  
- if it should eventually become rare or forbidden  

