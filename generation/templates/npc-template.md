---
id: npc-template
type: template
title: "NPC Template"
scope: internal
visibility: internal
status: active
confidence: high
tags:
  - template
  - npc
---

# NPC Template

Use this template for all AI-generated or manually-authored NPCs.  
All fields should be completed unless noted optional.

---

## Frontmatter (Required)
```yaml
id: npc-unique-id
type: npc
title: "NPC Name"
scope: canon          # canon | internal | mechanical | meta
visibility: public    # public | internal | secret
status: draft         # draft | active | deprecated
confidence: medium    # high | medium | low | speculative
created: YYYY-MM-DD
last_reviewed: YYYY-MM-DD

tags: []
region: null
culture: null
elemental_alignment: []
virtue_profile: {}
links:
  related: []
  faction: null
  deity: null
implementation_path: null
source: ai-generated | human
```

---

# {NPC Name}

## Overview
Brief mythic and narrative summary of who this character is and why they matter.

## Personality
- Core traits  
- Contradictions  
- Behaviors under stress  
- Speech patterns  
- Fears, hopes, devotions  

## Appearance
Describe silhouette, color palette, clothing, posture, motifs.

## Backstory
Concise history tied into:
- region  
- culture  
- virtues/vices  
- any significant events  

## Role in the World
How they matter mechanically or narratively:
- merchant  
- ritualist  
- antagonist  
- quest-giver  
- wandering spirit  
- shrine attendant  

## Signature Abilities / Skills (Optional)
Mechanical hooks ONLY, no implementation details.

## Relationships
- factions  
- towns  
- gods  
- rivalries or alliances  

## Story Hooks
Bulleted list of procedural seeds this NPC can generate.

## Notes
Additional meta notes for revision or review.
