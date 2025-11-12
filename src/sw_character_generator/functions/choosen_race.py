from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.classes.race.dwarf import apply_dwarf_dependent_modifiers
from sw_character_generator.classes.race.elf import apply_elf_dependent_modifiers
from sw_character_generator.classes.race.halfelff import apply_halfelf_dependent_modifiers
from sw_character_generator.classes.race.halfling import apply_halfling_dependent_modifiers
from sw_character_generator.classes.race.human import apply_human_dependent_modifiers


def choosen_race_modifiers(player_class: PlayerClass, race: str):

    """Apply race-specific modifiers to the character."""
    if race.lower() == "human":    
        apply_human_dependent_modifiers(player_class)
        #return player_class
    elif race.lower() == "elf":
        apply_elf_dependent_modifiers(player_class)
        #return player_class
    elif race.lower() == "halfelf":
        apply_halfelf_dependent_modifiers(player_class)
        #return player_class
    elif race.lower() == "halfling":
        apply_halfling_dependent_modifiers(player_class)
        #return player_class
    elif race.lower() == "dwarf":
        apply_dwarf_dependent_modifiers(player_class)
        #return player_class
    else:
        raise ValueError(f"Unknown race: {race}")
    