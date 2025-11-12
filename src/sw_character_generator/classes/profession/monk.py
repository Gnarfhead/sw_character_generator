from sw_character_generator.functions.role_dice import wuerfle_1d4

def apply_monk_dependent_modifiers(character):
    """Apply monk-specific modifiers to the character."""
    
    # Set profession attributes
    character.profession = "monk"
    character.tp_dice = 4
    character.main_stats = ("wisdom",)
    character.allowed_alignment = ("neutral", "evil", "good")
    character.allowed_races = ("human",)
    character.allowed_weapon = ("all",)
    character.allowed_armor = ("none",)
    character.save_throw = 15

    # Calculate total TP
    character.tp = wuerfle_1d4("TP", 1) + character.tp_mod
    if character.tp < 1:
        character.tp = 1

    # Calculate XP bonus
    if character.stat_wis >= 13:
        character.xp_bonus += 5
