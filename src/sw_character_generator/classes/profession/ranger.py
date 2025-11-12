from sw_character_generator.functions.role_dice import wuerfle_1d8

def apply_ranger_dependent_modifiers(character):
    """Apply ranger-specific modifiers to the character."""
    character.profession = "ranger"
    character.tp_dice = 8
    character.main_stats = ("strength",)
    character.allowed_alignment = ("good",)
    character.allowed_races = ("human",)
    character.allowed_weapon = ("all",)
    character.allowed_armor = ("all",)
    character.tp = wuerfle_1d8("TP", 2) + character.tp_mod
    character.save_throw = 14

    """Rangers receive an experience bonus based on their strength."""
    if character.stat_str >= 13:
        character.xp_bonus += 5
