from src.sw_character_generator.functions.role_dice import wuerfle_1d6

def apply_cleric_dependent_modifiers(character):
    """Apply cleric-specific modifiers to the character."""
    
    # Set profession attributes
    character.profession = "cleric"
    character.hp_dice = 6
    character.main_stats = ("wisdom",)
    character.allowed_alignment = ("good", "evil")
    character.allowed_races = ("human", "halfelf")
    character.allowed_weapon = ("blunt weapons",)
    character.allowed_armor = ("all",)
    character.save_throw = 15
    character.delicate_tasks = 0
    character.hide_in_shadows = 0
    character.hear_sounds = 0
    character.move_silently = 0
    character.open_locks = 0
    character.climb_walls = 0
    character.save_bonuses = (
        "+2 against paralysis and poison",
    )
    character.immunity = ()
    character.special_abilities = (
        "turn undead: clerics can turn undead creatures",
        "religious fortress (Level 9): clerics can create a temple to gather followers",
    )
    character.xp_bonus = 0
    character.parry = 0
    character.spells_lvl1 = 0
    character.spells_lvl2 = 0
    character.spells_lvl3 = 0
    character.spells_lvl4 = 0
    character.spells_lvl5 = 0
    character.spells_lvl6 = 0
    character.spells_lvl7 = 0
    character.spells_lvl8 = 0
    character.spells_lvl9 = 0

    # Calculate XP bonus
    #if character.stat_wis >= 13:
    #    character.xp_bonus += 5

    # Calculate spell-related attributes
    if character.stat_wis >= 15:
        character.spells_lvl1 += 1
