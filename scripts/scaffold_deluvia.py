#!/usr/bin/env python3
"""
Scaffold folders and markdown files for the Deluvia — Age of Storms world bible.

Usage:
    python scaffold_deluvia.py
or:
    python scaffold_deluvia.py /path/to/workspace
"""

import sys
from pathlib import Path

# Optional: pass a base directory as first argument, otherwise use current dir
base_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
base_dir = base_dir.resolve()

FILES = [
    # 0. SYSTEM ROOT (index)
    "index/master_index.md",
    "index/style_guide.md",
    "index/naming_lexicon.md",
    "index/changelog.md",
    "index/to_do_list.md",
    "index/file_map.md",

    # 1. COSMOLOGY
    "cosmology/deluvic_cycle.md",
    "cosmology/creation_myth_variants.md",
    "cosmology/primordials_overview.md",
    "cosmology/twelve_elements.md",
    "cosmology/virtue_vice_matrix.md",
    "cosmology/the_severing.md",
    "cosmology/shadow_dungeons_explained.md",
    "cosmology/omens_and_prophecies.md",
    "cosmology/calendar_and_seasons.md",
    "cosmology/planes_and_realms.md",

    # 2. ELEMENTS & MAGIC
    "elements/twelvefold_wheel.md",
    "elements/elemental_domains.md",
    "elements/gems_runes_materials.md",

    "magic/overview.md",
    "magic/water_school.md",
    "magic/fire_school.md",
    "magic/soil_school.md",
    "magic/life_school.md",
    "magic/death_school.md",
    "magic/moon_school.md",
    "magic/sun_school.md",
    "magic/ore_school.md",
    "magic/poison_school.md",
    "magic/storm_school.md",
    "magic/chaos_school.md",
    "magic/wind_school.md",
    "magic/rituals_and_incantations.md",
    "magic/spell_lists_basic.md",
    "magic/spell_lists_advanced.md",
    "magic/forbidden_magic.md",
    "magic/focuses_and_conduits.md",

    # 3. PANTHEON
    "pantheon/twelve_gods_overview.md",
    "pantheon/nailune.md",
    "pantheon/solkara.md",
    "pantheon/terragorn.md",
    "pantheon/myrathe.md",
    "pantheon/eirundal.md",
    "pantheon/umbryx.md",
    "pantheon/solaraith.md",
    "pantheon/gravorn.md",
    "pantheon/serith_noxbloom.md",
    "pantheon/stormeid.md",
    "pantheon/khel_druun.md",
    "pantheon/aeralune.md",

    "pantheon/minor_gods.md",
    "pantheon/small_gods_sprites.md",
    "pantheon/corrupted_gods.md",
    "pantheon/holy_beasts.md",
    "pantheon/divine_symbols.md",
    "pantheon/mythic_relationships_chart.md",
    "pantheon/major_legends.md",
    "pantheon/prayers_and_offerings.md",

    # 4. PEOPLES & CULTURES
    "peoples/overview.md",
    "peoples/anthorans_water.md",
    "peoples/ashborn_fire.md",
    "peoples/loamkin_soil.md",
    "peoples/greenwanderers_life.md",
    "peoples/mournwalkers_death.md",
    "peoples/gloam_elves_moon.md",
    "peoples/glyphics_sun.md",
    "peoples/dwerrow_smiths_ore.md",
    "peoples/sporeborn_poison.md",
    "peoples/techion_storm.md",
    "peoples/endirians_chaos.md",
    "peoples/kapasian_skyfolk_wind.md",

    "peoples/languages_and_dialects.md",
    "peoples/naming_conventions.md",
    "peoples/religion_practice.md",
    "peoples/festivals_and_holidays.md",
    "peoples/architecture.md",
    "peoples/foods_and_crafts.md",

    # 5. TOWNS & REGIONS
    "towns/overview.md",
    "towns/rothigport_water.md",
    "towns/embersway_fire.md",
    "towns/loamstead_soil.md",
    "towns/greenhallow_life.md",
    "towns/stillgrave_death.md",
    "towns/moondrift_moon.md",
    "towns/sunspire_sun.md",
    "towns/ironwell_ore.md",
    "towns/fenwick_hollow_poison.md",
    "towns/stormrest_storm.md",
    "towns/fraymarch_chaos.md",
    "towns/aerlum_ridge_wind.md",

    "geography/regional_map.md",
    "geography/trade_routes.md",
    "geography/climates_and_biomes.md",
    "geography/fauna_flora.md",

    # 6. DUNGEONS & SHADOW REALMS
    "dungeons/overview.md",
    "dungeons/niv_rath_hollow_water.md",
    "dungeons/ashen_vault_fire.md",
    "dungeons/mirefall_tangle_soil.md",
    "dungeons/thornspire_life.md",
    "dungeons/the_bone_lantern_death.md",
    "dungeons/gloamsorrow_moon.md",
    "dungeons/blazebound_sun.md",
    "dungeons/rustcrown_cradle_ore.md",
    "dungeons/noxspire_poison.md",
    "dungeons/skybreaker_maw_storm.md",
    "dungeons/shatterweft_chasm_chaos.md",
    "dungeons/galehollow_ruin_wind.md",

    "dungeons/bosses_lore.md",
    "dungeons/mechanics_puzzles.md",
    "dungeons/relics_and_loot.md",

    # 7. BESTIARY
    "bestiary/overview.md",
    "bestiary/elemental_creatures.md",
    "bestiary/spirit_courts_whimsy.md",
    "bestiary/divine_beasts.md",
    "bestiary/corrupted_monstrosities.md",
    "bestiary/fauna_of_deluvia.md",
    "bestiary/flora_of_deluvia.md",
    "bestiary/golems_constructs.md",
    "bestiary/tideborn_creatures.md",

    # 8. PROCEDURAL + SYSTEMS
    "procedural/naming_generator.md",
    "procedural/npc_generator.md",
    "procedural/spirit_generator.md",
    "procedural/dungeon_seed_generator.md",
    "procedural/quest_templates.md",
    "procedural/myth_fragments.md",
    "procedural/player_origin_tables.md",
    "procedural/artifact_generator.md",
    "procedural/prophecy_engine.md",
    "procedural/story_looms.md",

    # 9. DEVELOPER RESOURCES
    "dev/roadmap.md",
    "dev/design_principles.md",
    "dev/data_structures.md",
    "dev/integration_for_api_apps.md",
    "dev/minecraft_engine_notes.md",
    "dev/automations_ai_tasks.md",
    "dev/world_style_reference.md",
]


def main() -> None:
    print(f"Scaffolding Deluvia world files in: {base_dir}")
    created_dirs = set()
    created_files = 0

    for rel_path in FILES:
        target_path = base_dir / rel_path
        target_dir = target_path.parent

        if target_dir not in created_dirs:
            target_dir.mkdir(parents=True, exist_ok=True)
            created_dirs.add(target_dir)

        if not target_path.exists():
            target_path.touch()
            created_files += 1

    print(f"Created {len(created_dirs)} directories.")
    print(f"Created {created_files} new files.")
    print("Done. Existing files were left untouched.")


if __name__ == "__main__":
    main()