---
id: lore-fragment-template
type: template
title: "Lore Fragment Template"
scope: internal
visibility: internal
status: active
confidence: high
tags:
  - template
  - lore
  - fragment
---

# Lore Fragment Template

I use this template for books, inscriptions, rumors, myths, poems, riddles, murals, field notes, and any other small narrative artifacts that enrich Deluvia’s world.

Lore fragments are intentionally brief, evocative, and slightly unreliable—they are the spores of story that drift through the setting.

---

## Frontmatter (Required)

```yaml
id: lore-fragment-unique-id
type: lore-fragment
title: "Fragment Title"
scope: canon                # canon | internal | mechanical | meta | apocrypha
visibility: public          # public | internal | secret
status: draft               # draft | active | deprecated
confidence: low             # high | medium | low | speculative | apocryphal
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD

tags: []                    # e.g. [soil, humility, rothigport, beetlefolk]
fragment_type: null         # book-page | inscription | rumor | poem | hymn | myth | mural | dream | riddle | chant | field-note
origin_region: null
associated_elements: []     # e.g. [soil, moon]
associated_virtue: null     # e.g. humility
associated_vice: null       # e.g. vanity

links:
  related: []               # other lore fragments or events
  referenced_entities: []   # gods, towns, dungeons, npcs
  connected_looms: []       # story_looms this might feed

story_weight: low           # low | medium | high | canonical-candidate
implementation_path: null   # optional
source: ai-generated | human
```

---

# {Fragment Title}

## Fragment Content

A short, self-contained piece of lore.  
Choose *one* voice or style appropriate to the fragment type:

- a priest’s chant  
- a sailor’s superstition  
- a fungal spore-riddle  
- a child’s playground rhyme  
- a scholar’s marginalia  
- a dream whisper  
- a cryptic mural description  
- a forgotten journal page  
- a corrupted transmission from a dungeon  

Keep it atmospheric and open to multiple interpretations.

---

## Provenance

Where did this fragment come from?

- found in a ruin  
- overheard in a tavern  
- carved into a shrine stone  
- scrawled in a fever journal  
- spoken by a dying NPC  
- glimpsed during a moon-aligned dream  
- manifested after a pantheon attention spike  

This helps future systems determine how fragments surface in-game.

---

## Interpretations (Optional but Encouraged)

Short list of possible meanings:

- literal  
- symbolic  
- misunderstood  
- twisted by vice  
- crafted as propaganda  
- hinting at deeper story arcs  

Lore fragments should be meaning-dense and meaning-flexible.

---

## System Hooks

### Narrative Engine
Does this fragment:

- seed a story signal?
- hint at a domain shift?
- connect to regional tone?

### Story Looms
Which arcs might it drift toward?

### Town State
Does it strengthen or weaken a virtue/vice?

### Dungeon Mutation
Could this foreshadow a change?

### Pantheon Attention
Is this fragment the god’s whisper or warning?

AI generation can auto-fill these fields based on tags.

---

## Notes

Design reminders:

- What inspired this fragment?
- Should it be canonical or apocryphal?
- Should it be rare, common, or hidden?
- Any concerns for future revisions?

