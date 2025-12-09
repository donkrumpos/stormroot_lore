---
id: pantheon-attention-system
type: system
title: "Pantheon Attention System"
scope: internal
visibility: internal
status: active
confidence: high
created: 2025-01-17
last_reviewed: 2025-01-17
tags:
  - gods
  - systems
  - narrative
  - mythic-ecology
links:
  related:
    - narrative-engine
    - narrative-ecology
    - virtue-vice-system
    - mythic-vector-system
    - story-seed-engine
    - town-state-system
---

# Pantheon Attention System

## Mythic Introduction

Every god in Deluvia listens.  
But not all listen equally.

Some tilt their heads toward regions where their element is flourishing.  
Others awaken when a vice grows strong.  
And some—ancient and patient—watch only when the Weave itself trembles.

I built the Pantheon Attention System to model this *cosmic listening*,  
a way for the gods to feel present in the living dream of Deluvia without becoming constant overseers.

A god’s attention is **a tide, a beam of awareness, a shifting weight**—  
and when a deity turns its gaze toward a town, dungeon, player, or region, the world changes subtly, meaningfully, mythically.

---

# System Overview

Each deity maintains an evolving **attention profile**:

```yaml
god_attention:
  id: solaraith
  regional_focus:
    rothigport: 0.8
    stormrest: 0.4
  vector_resonance:
    sun: 1.0
    fire: 0.6
    storm: 0.2
  virtue_interest:
    truth: 0.7
    courage: 0.4
  vice_irritants:
    deception: 1.0
    corruption: 0.6
  event_sensitivity:
    shrine_damage: 1.0
    ritual_success: 0.8
    ritual_failure: 0.5
    omens_ignored: 0.7
  attention_level: 0.65
```

A god’s **attention_level** determines:

- whether omens occur  
- whether blessings emerge  
- whether avatars stir  
- whether shrines awaken  
- whether catastrophes or miracles echo through a region  
- whether story seeds with divine flavor are generated  

---

# 1. Drivers of Divine Attention

### 1. Elemental Resonance (Mythic Vectors)
The stronger a region expresses a god’s element, the more that deity leans toward it.

Examples:

- High **sun** vector → Solaraith awakens  
- High **moon** vector → Nailune becomes curious  
- Surging **poison** vector → Serith Noxbloom stirs  
- Equal flux of **chaos** + **wind** → Myrathe listens for oddities  

Elemental resonance is the single greatest baseline driver of godly awareness.

---

### 2. Virtue–Vice Drift
Gods care about spiritual ecology.

- If truth rises → Heegmos pays attention  
- If humility prevails → Sifaneus watches gently  
- If corruption blooms → Terragorn’s patience thins  
- If generosity flourishes → Myrathe brightens  

Virtue and Vice are a mythic navigational system for divine senses.

---

### 3. Civic Events, Festivals, and Rituals

The gods notice:

- lantern festivals (sun, fire, air)  
- harvest rites (soil, life)  
- moonlit vigils (moon, death)  
- purification rituals (water, sun)  
- oath-ceremonies (wind, storm)  

Successful rituals increase attention.  
Failed rituals—especially dramatic ones—draw even more.

---

### 4. Dungeon Disturbance

When a dungeon’s corruption shifts or a boss is defeated:

- chaos stirs Khel Druun  
- death awakens Gravorn  
- poison whispers to Serith Noxbloom  
- storm cracks open Stormeid’s distant ear  

Dungeon mutation is a loud signal in the Weave.

---

### 5. Player Deeds

Some actions are so narratively potent that gods notice immediately.

Examples:

- rescuing a sacred creature  
- sacrificing a relic  
- desecrating a shrine  
- defeating a demi-god  
- rewriting town fate  
- performing an ancient ritual correctly  

Gods notice patterns, not just events.

---

# 2. Divine Attention Curve

Attention is not binary.  
It follows a curve of increasing involvement:

| Level | Name | Meaning |
|-------|-------|---------|
| 0.00 | Dormant | The god is inert, hardly aware. |
| 0.15 | Glancing | Minor omens, faint dreams. |
| 0.30 | Aware | Shrine reactions, subtle blessings. |
| 0.45 | Watching | More frequent omens, rare miracles. |
| 0.60 | Attending | Town-wide effects, altered dungeon behavior. |
| 0.75 | Engaged | Avatars manifest, miracles become real. |
| 0.90 | Intervening | World events occur. |
| 1.00 | Present | A moment of divine historic significance. |

No god stays at 1.00 long.  
The Weave pulls them back to sleep unless continuously fed by events.

---

# 3. Divine Effects

### Blessings (positive attention)
- shrine radiance  
- protection wards  
- increased festival luck  
- NPCs dreaming prophetic dreams  
- increased elemental resources  
- lower corruption in nearby dungeons  
- special story seeds unlock  

### Omens (neutral attention)
- celestial signs  
- fungal patterns  
- anomalous winds  
- glowing stones  
- dream fragments in NPC dialogue  

### Wrath (negative attention, or vice dominance)
- plagues  
- storms  
- nightmares  
- cursed waters  
- dungeon intensification  
- weakened shrines  
- hostile spirit manifestations  

---

# 4. Pantheon Interference Patterns

Some gods reinforce each other.  
Some cancel each other.  
Some fight silently beneath the soil.

Examples:

- **Solaraith & Nailune**  
  Their opposing vectors (sun vs moon) cause interference.  
  When both pay attention, omens become strange and contradictory.

- **Terragorn & Serith Noxbloom**  
  Soil vs poison — corruption blooms become violent.

- **Stormeid & Myrathe**  
  Storm + chaos → unpredictable miracles.

- **Umbryx & Solaraith**  
  Death + sun → rare equilibrium moments (“still-light cycles”).  

Interference creates emergent world phenomena not explicitly scripted.

---

# 5. Attention Decay

Attention decays over time unless reinforced.

Decay rate depends on:

- the deity’s temperament  
- the match between region tone and divine element  
- the density of story signals  
- the presence of shrines  
- dungeon activity  

This keeps the world dynamic—not frozen at a single divine state.

---

# 6. Data Model

```yaml
pantheon_status:
  solaraith:
    attention_level: 0.62
    decay_rate: 0.04
    interference:
      nailune: -0.2
      stormeid: +0.1
    blessing_chance: 0.12
    omen_chance: 0.18
    wrath_chance: 0.03
  nailune:
    attention_level: 0.40
    decay_rate: 0.03
    interference:
      solaraith: -0.2
      umbryx: +0.15
```

Multiple gods may observe the same region simultaneously.  
This creates mythic layering—exactly what I want for Deluvia’s tone.

---

# Canonical Truths

- Gods awaken in response to story, not devotion alone.  
- Divine attention is a tide, shifting with mythic currents.  
- Rituals, corruption, elemental resonance, and player deeds guide divine awareness.  
- Multiple gods can attend at once, causing interference patterns.  
- Divine presence is rare but profound.  
- The Pantheon Attention System ensures Deluvia feels ancient, aware, and deeply reactive.

