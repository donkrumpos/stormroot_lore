---
id: npc-memory-system
type: system
title: "The NPC Memory System"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - npc
  - memory
  - procedural
  - story
  - ai
links:
  related:
    - narrative-engine
    - procedural-storytelling
    - mythic-vector-system
    - chronicle-of-deeds
---

# The NPC Memory System

## Mythic Introduction

Every person in Deluvia — from beetlefolk to seafarers to dusk-eyed moon-priests — carries a memory that is not merely individual but **entangled** with the Weave of the world.

When a mortal meets another, something subtle lingers:
a tone, a gesture, a deed, a kindness, a wound.

NPCs in Deluvia do not “reset.”  
They **remember**, in ways small or mythic.

This system defines how those memories form, shift, and are expressed.

---

# Purpose of This System

The NPC Memory System allows me to:

- store player actions in NPC-specific memory banks  
- drive reactive dialogue  
- influence mood, trust, fear, reverence, suspicion  
- generate emergent quests  
- modify settlement tone over time  
- maintain continuity across months or years of play  

NPCs feel alive when their responses are shaped by a real accumulation of story.

---

# Structure of NPC Memory

NPC memory is divided into four layers:

1. **Impression Layer**  
   Emotional residue from encounters.  
2. **Event Layer**  
   Structured story signals involving that NPC.  
3. **Relationship Layer**  
   Trust, fear, gratitude, obligation, mythic resonance.  
4. **Mythic Layer**  
   Elemental memory echo shaped by the Twelvefold Wheel.

Each layer interacts with the others.

---

# 1. Impression Layer  
Small emotional weights that form automatically from interactions.

~~~~yaml
impression:
  mood_shift: +0.2
  trust_shift: +0.1
  fear_shift: -0.1
  tone_signature:
    water: 0.3
    storm: -0.2
    moon: +0.1
~~~~

Impressions fade slowly unless reinforced.

These give NPCs micro-responses such as:

- tone change  
- body language variations  
- greeting style  
- mood shifts  

---

# 2. Event Layer  
Structured memory of notable player actions.

~~~~yaml
event_memory:
  - id: uuid
    type: rescue | betrayal | gift | combat | ritual | discovery
    intensity: 0.0-1.0
    timestamp: ISO8601
    tags:
      - moral
      - mythic
      - social
~~~~

Examples:

- the player saved them from monsters  
- the player stole from their home  
- the player sacrificed an item at a shrine  
- the player spoke a forbidden name  

Events do not fade.  
They accumulate into the Relationship Layer.

---

# 3. Relationship Layer  

The beating heart of NPC memory.

~~~~yaml
relationship:
  trust:     -1.0 to +1.0
  fear:      -1.0 to +1.0
  respect:   -1.0 to +1.0
  affection: -1.0 to +1.0
  awe:       -1.0 to +1.0
  obligation:
    owed_by_player: 0.0 to 1.0
    owed_to_player: 0.0 to 1.0
~~~~

The Relationship Layer modifies:

- dialogue pools  
- quest eligibility  
- trade prices  
- willingness to reveal secrets  
- whether they shelter or abandon the player  
- whether they mislead or guide  

NPC relationships are **glacial** — they shift slowly, meaningfully.

---

# 4. Mythic Layer  
Each NPC is attuned to specific elemental moods.

~~~~yaml
mythic_signature:
  water: +0.8
  moon:  +0.5
  soil:  -0.3
~~~~

This signature:

- colors their dreams  
- biases their reactions  
- influences procedural dialogue themes  
- makes them resonate more with certain dungeons or gods  

Mythic signatures evolve alongside the Narrative Engine’s world-level vectors.

---

# Memory Encoding Format (Unified)

NPC memory is stored as:

~~~~yaml
npc_memory:
  npc_id: string
  impression: {...}
  event_memory: [...list...]
  relationship: {...}
  mythic_signature: {...}
~~~~

This structure is compact and easily serialized.

---

# How Memory Influences NPC Behavior

NPC reactions flow from memory through four major outputs:

## 1. Dialogue Shifts
NPCs unlock or restrict:

- secrets  
- rumors  
- warnings  
- confessions  
- symbolic commentary related to their mythic signature  

## 2. Behavioral Routines
NPCs may:

- hide indoors  
- confront the player  
- change trade prices  
- avoid eye contact  
- follow the player  
- pray more often  
- wander at night  
- craft special items  

## 3. Emergent Quests
NPC memory drives:

- requests for aid  
- invitations to rituals  
- warnings about dungeon drift  
- personal story arcs  

## 4. Civic Influence
A cluster of NPC memories can shift:

- town virtue meters  
- civic events  
- shrine favor  
- festival tone  

NPC memory is the atomic unit that ripples into settlement-level story.

---

# Memory Drift

NPC memories drift over time:

### **Decay**  
Minor impressions fade after X days.

### **Consolidation**  
Repeated events merge into a stable relationship change.

### **Distortion**  
Moon-aligned NPCs may misremember.

### **Mythic Absorption**  
NPCs close to dungeons absorb elemental influence.

### **Echo Spread**  
When an iconic event is witnessed by many NPCs, subtle echoes propagate.

This creates a living anthropology.

---

# Memory & the Chronicle of Deeds

When memory-event ties are strong enough, entries are pushed to the **Chronicle of Deeds**, giving them mythic permanence.

NPCs react differently to deeds stored in the Chronicle:

- deeper reverence  
- ancestral memory triggers  
- intergenerational storytelling  
- shrine offerings changing tone  

Chronicle entries are “loud” in the Weave.

---

# Best Practices I Follow

- Memory should feel inevitable, not punitive.  
- NPCs never “forgive instantly” or “hate instantly” — drift matters.  
- Mythic Layer is gentle but transformative.  
- Relationship Layer is slow but powerful.  
- Events should be rare enough to matter.  
- NPC behavior should tell the player who remembers what.  

---

# Canonical Truths

- NPCs in Deluvia remember the player over months and years.  
- Memories shape dialogue, behavior, quests, and civic drift.  
- Mythic signatures bind NPCs to the elemental Weave.  
- All memory ultimately contributes to the living narrative ecology.  
- The world is made of stories, and NPCs are vessels for these stories.

