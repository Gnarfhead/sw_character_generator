"""Apply profession-specific modifiers to the character based on chosen profession."""
from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.classes.profession.assassin import apply_assassin_dependent_modifiers
from sw_character_generator.classes.profession.cleric import apply_cleric_dependent_modifiers
from sw_character_generator.classes.profession.druid import apply_druid_dependent_modifiers
from sw_character_generator.classes.profession.fighter import apply_fighter_dependent_modifiers
from sw_character_generator.classes.profession.monk import apply_monk_dependent_modifiers
from sw_character_generator.classes.profession.paladin import apply_paladin_dependent_modifiers
from sw_character_generator.classes.profession.ranger import apply_ranger_dependent_modifiers
from sw_character_generator.classes.profession.thief import apply_thief_dependent_modifiers
from sw_character_generator.classes.profession.wizard import apply_wizard_dependent_modifiers


def choosen_profession_modifiers(player_class: PlayerClass, profession: str):
    """Apply profession-specific modifiers to the character."""
    print("DEBUG choosen_profession_modifiers: ----------------------------------------------------------------")

    profession_lower = profession.lower()

    if profession_lower == "assassin":
        print("DEBUG choosen_profession_modifiers: Choosing Assassin profession - profession parameter:", profession)
        apply_assassin_dependent_modifiers(player_class)
        player_class.profession = "Assassin"
    elif profession_lower == "paladin":
        print("DEBUG choosen_profession_modifiers: Choosing Paladin profession - profession parameter:", profession)
        apply_paladin_dependent_modifiers(player_class)
        player_class.profession = "Paladin"
    elif profession_lower == "fighter":
        print("DEBUG choosen_profession_modifiers: Choosing Fighter profession - profession parameter:", profession)
        apply_fighter_dependent_modifiers(player_class)
        player_class.profession = "Fighter"
    elif profession_lower == "wizard":
        print("DEBUG choosen_profession_modifiers: Choosing Wizard profession - profession parameter:", profession)
        apply_wizard_dependent_modifiers(player_class)
        player_class.profession = "Wizard"
    elif profession_lower == "thief":
        print("DEBUG choosen_profession_modifiers: Choosing Thief profession - profession parameter:", profession)
        apply_thief_dependent_modifiers(player_class)
        player_class.profession = "Thief"
    elif profession_lower == "ranger":
        print("DEBUG choosen_profession_modifiers: Choosing Ranger profession - profession parameter:", profession)
        apply_ranger_dependent_modifiers(player_class)
        player_class.profession = "Ranger"
    elif profession_lower == "monk":
        print("DEBUG choosen_profession_modifiers: Choosing Monk profession - profession parameter:", profession)
        apply_monk_dependent_modifiers(player_class)
        player_class.profession = "Monk"
    elif profession_lower == "druid":
        print("DEBUG choosen_profession_modifiers: Choosing Druid profession - profession parameter:", profession)
        apply_druid_dependent_modifiers(player_class)
        player_class.profession = "Druid"
    elif profession_lower == "cleric":
        print("DEBUG choosen_profession_modifiers: Choosing Cleric profession - profession parameter:", profession)
        apply_cleric_dependent_modifiers(player_class)
        player_class.profession = "Cleric"
    else:
        raise ValueError(f"ERROR choosen_profession_modifiers: Unknown profession: {profession}")
