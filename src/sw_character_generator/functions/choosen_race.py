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
        print("DEBUG choosen_race_modifiers: Choosing Halfelf race - race parameter:", race)
        apply_halfelf_dependent_modifiers(player_class)
        player_class.race = "Halfelf"
    elif race.lower() == "dwarf" and "dwarf" in player_class.allowed_races:
        print("DEBUG choosen_race_modifiers: Choosing Dwarf race - race parameter:", race)
        apply_dwarf_dependent_modifiers(player_class)
        player_class.race = "Dwarf"
    elif race.lower() == "elf" and "elf" in player_class.allowed_races:
        print("DEBUG choosen_race_modifiers: Choosing Elf race - race parameter:", race)
        apply_elf_dependent_modifiers(player_class)
        player_class.race = "Elf"
    elif race.lower() == "halfling" and "halfling" in player_class.allowed_races:
        print("DEBUG choosen_race_modifiers: Choosing Halfling race - race parameter:", race)
        apply_halfling_dependent_modifiers(player_class)
        player_class.race = "Halfling"
    elif race.lower() == "human" and "human" in player_class.allowed_races:
        print("DEBUG choosen_race_modifiers: Choosing Human race - race parameter:", race)
        apply_human_dependent_modifiers(player_class)
        player_class.race = "Human"
    else:
        raise ValueError("ERROR choosen_race_modifiers: Unknown or not allowed race:", race)
