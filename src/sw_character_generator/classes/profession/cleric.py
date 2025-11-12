from sw_character_generator.functions.role_dice import wuerfle_1d6

def apply_cleric_dependent_modifiers(character):
    """Apply cleric-specific modifiers to the character."""
    
    # Set profession attributes
    character.profession = "cleric"
    character.tp_dice = 6
    character.main_stats = ("wisdom",)
    character.allowed_alignment = ("good", "evil")
    character.allowed_races = ("human", "halfelf")
    character.allowed_weapon = ("blunt weapons",)
    character.allowed_armor = ("all",)
    character.save_throw = 15
    character.save_bonuses += (
        "+2 against paralysis and poison",
    )

    character.special_abilities += (
        "turn undead: clerics can turn undead creatures",
        "religious fortress (Level 9): clerics can create a temple to gather followers",
    )

    # Calculate total TP
    character.tp = wuerfle_1d6("TP", 1) + character.tp_mod
    if character.tp < 1:
        character.tp = 1

    # Calculate XP bonus
    if character.stat_wis >= 13:
        character.xp_bonus += 5
