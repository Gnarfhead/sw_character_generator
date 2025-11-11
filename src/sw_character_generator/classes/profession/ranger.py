from sw_character_generator.functions.role_dice import wuerfle_1d8

def apply_ranger_dependent_modifiers(character):
    """Apply ranger-specific modifiers to the character."""
    character.tp_dice = 8
    character.main_stats = ("Strength",)
    character.allowed_alignment = ("Good",)
    character.allowed_races = ("Human",)
    character.allowed_weapon = ("all",)
    character.allowed_armor = ("all",)
    character.tp = wuerfle_1d8("TP", 2) + character.tp_mod
