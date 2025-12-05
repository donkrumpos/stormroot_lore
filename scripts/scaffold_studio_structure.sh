#!/usr/bin/env bash
set -e

echo "Scaffolding Stormroot Studio structure..."

# --- WORLD: in-world truth of Deluvia ---
mkdir -p world/{cosmology,history,geography,peoples,factions,characters,bestiary,artifacts}
touch world/_index.md

# --- SYSTEMS: game design (not implementation) ---
mkdir -p systems/{magic,combat,progression,crafting,ecology}
touch systems/_index.md

# --- CONTENT: playable content built from world + systems ---
mkdir -p content/{dungeons,quests,encounters,events,loot-tables}
touch content/_index.md

# --- IMPLEMENTATION: Minecraft / Denizen / configs ---
mkdir -p implementation/denizen/{magic,combat,npcs}
mkdir -p implementation/{data,config}
touch implementation/_index.md

# --- GENERATION: AI & procedural pipelines ---
mkdir -p generation/templates
mkdir -p generation/prompts/{system,examples,constraints}
mkdir -p generation/pipelines
mkdir -p generation/staging/{npcs,quests,lore}
mkdir -p generation/seeds/{name-lists,trait-pools,regional-flavor}
touch generation/_index.md

# --- STUDIO: devlogs, YouTube, social, community ---
mkdir -p studio/devlog/2025
mkdir -p studio/youtube/{scripts,planning}
mkdir -p studio/social/{twitter-threads,discord-announcements,reddit-posts}
mkdir -p studio/press
mkdir -p studio/community
touch studio/devlog/_index.md
touch studio/youtube/_planning.md
touch studio/community/faq.md

# --- RESEARCH: external references & notes ---
mkdir -p research/{inspiration,references,reading-notes,competitors}
touch research/_index.md

# --- META: design, roadmap, todo, meetings, archive ---
mkdir -p meta/{design,roadmap,todo,meetings,archive}
touch meta/design/ARCHITECTURE.md
touch meta/design/DESIGN_DECISIONS.md
touch meta/roadmap/roadmap.md
touch meta/todo/inbox.md

# --- TOOLS: validators, generators, export scripts ---
mkdir -p tools/{validators,generators,export}

# --- ASSETS: non-text resources ---
mkdir -p assets/{maps,images,audio,fonts}

# --- OPTIONAL: registry + templates roots ---
mkdir -p _registry
mkdir -p _templates/{world,systems,content,studio}

echo "Done. No existing files were moved or deleted."