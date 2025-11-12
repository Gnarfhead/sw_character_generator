"""Functions for applying race-dependent modifiers to player characters."""
from src.sw_character_generator.classes.playerclass import PlayerClass
from src.sw_character_generator.classes.race.dwarf import apply_dwarf_dependent_modifiers
from src.sw_character_generator.classes.race.elf import apply_elf_dependent_modifiers
from src.sw_character_generator.classes.race.halfelff import apply_halfelf_dependent_modifiers
from src.sw_character_generator.classes.race.halfling import apply_halfling_dependent_modifiers
from src.sw_character_generator.classes.race.human import apply_human_dependent_modifiers


def choosen_race_modifiers(player_class: PlayerClass, race: str):
    """Applies race-dependent modifiers to the player character based on the chosen race."""

    if race.lower() == "halfelf" and "halfelf" in player_class.allowed_races:
        print("DEBUG: Choosing Halfelf race - race parameter:", race)
        apply_halfelf_dependent_modifiers(player_class)
        player_class.race = "halfelf"
    elif race.lower() == "dwarf" and "dwarf" in player_class.allowed_races:
        print("DEBUG: Choosing Dwarf race - race parameter:", race)
        apply_dwarf_dependent_modifiers(player_class)
        player_class.race = "dwarf"
    elif race.lower() == "elf" and "elf" in player_class.allowed_races:
        print("DEBUG: Choosing Elf race - race parameter:", race)
        apply_elf_dependent_modifiers(player_class)
        player_class.race = "elf"
    elif race.lower() == "halfling" and "halfling" in player_class.allowed_races:
        print("DEBUG: Choosing Halfling race - race parameter:", race)
        apply_halfling_dependent_modifiers(player_class)
        player_class.race = "halfling"
    elif race.lower() == "human" and "human" in player_class.allowed_races:
        print("DEBUG: Choosing Human race - race parameter:", race)
        apply_human_dependent_modifiers(player_class)
        player_class.race = "human"
    else:
        print("All allowed races:", player_class.allowed_races, "Provided race:", race)
        raise ValueError("Unknown or not allowed race:", race)
