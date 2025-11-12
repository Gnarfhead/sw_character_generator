from sw_character_generator.functions.role_dice import wuerfle_1d6

def apply_cleric_dependent_modifiers(character):
    """Apply cleric-specific modifiers to the character."""
    character.profession = "cleric"
    character.tp_dice = 6
    character.main_stats = ("wisdom",)
    character.allowed_alignment = ("good", "evil")
    character.allowed_races = ("human", "halfelf")
    character.allowed_weapon = ("blunt weapons",)
    character.allowed_armor = ("all",)
    character.tp = wuerfle_1d6("TP", 1) + character.tp_mod
    character.save_throw = 15

    """Clerics receive an experience bonus based on their wisdom."""
    if character.stat_wis >= 13:
        character.xp_bonus += 5
