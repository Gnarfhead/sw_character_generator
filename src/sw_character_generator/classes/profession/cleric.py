from sw_character_generator.functions.role_dice import wuerfle_1d6

def apply_cleric_dependent_modifiers(character):
    """Apply cleric-specific modifiers to the character."""
    character.tp_dice = 6
    character.main_stats = ("Wisdom")
    character.allowed_alignment = ("Good", "Evil")
    character.allowed_races = ("Human", "Halfelf")
    character.allowed_weapon = ("blunt weapons")
    character.allowed_armor = ("all")
    character.tp = wuerfle_1d6("TP", 1) + character.tp_mod
