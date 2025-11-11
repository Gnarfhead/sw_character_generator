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
    if profession.lower() == "assassin":    
        apply_assassin_dependent_modifiers(player_class)
    elif profession.lower() == "paladin":
        apply_paladin_dependent_modifiers(player_class)
    elif profession.lower() == "fighter":
        apply_fighter_dependent_modifiers(player_class)
    elif profession.lower() == "wizard":
        apply_wizard_dependent_modifiers(player_class)
    elif profession.lower() == "thief":
        apply_thief_dependent_modifiers(player_class)
    elif profession.lower() == "ranger":
        apply_ranger_dependent_modifiers(player_class)
    elif profession.lower() == "monk":
        apply_monk_dependent_modifiers(player_class)
    elif profession.lower() == "druid":
        apply_druid_dependent_modifiers(player_class)
    elif profession.lower() == "cleric":
        apply_cleric_dependent_modifiers(player_class)
    else:
        raise ValueError(f"Unknown profession: {profession}")
    