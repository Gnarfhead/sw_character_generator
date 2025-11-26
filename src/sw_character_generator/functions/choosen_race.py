"""Functions for applying race-dependent modifiers to player characters."""
from src.sw_character_generator.classes.playerclass import PlayerClass
from src.sw_character_generator.classes.race.dwarf import apply_dwarf_dependent_modifiers
from src.sw_character_generator.classes.race.elf import apply_elf_dependent_modifiers
from src.sw_character_generator.classes.race.halfelff import apply_halfelf_dependent_modifiers
from src.sw_character_generator.classes.race.halfling import apply_halfling_dependent_modifiers
from src.sw_character_generator.classes.race.human import apply_human_dependent_modifiers


def choosen_race_modifiers(player_class: PlayerClass, race: str):
    """Applies race-dependent modifiers to the player character based on the chosen race."""
    print("DEBUG choosen_race_modifiers: ----------------------------------------------------------------")
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

    #print("DEBUG choosen_race_modifiers: player_class.special_abilities after race modifiers:", player_class.special_abilities)
    #print("DEBUG choosen_race_modifiers: type of player_class.special_abilities:", type(player_class.special_abilities))
    #print("DEBUG choosen_race_modifiers: player_class.languages after race modifiers:", player_class.languages)
    #print("DEBUG choosen_race_modifiers: type of player_class.languages:", type(player_class.languages))
    #print("DEBUG choosen_race_modifiers: player_class.save_bonuses after race modifiers:", player_class.save_bonuses)
    #print("DEBUG choosen_race_modifiers: type of player_class.save_bonuses:", type(player_class.save_bonuses))
    #print("DEBUG choosen_race_modifiers: player_class.immunities after race modifiers:", player_class.immunities)
    #print("DEBUG choosen_race_modifiers: type of player_class.immunities:", type(player_class.immunities))
