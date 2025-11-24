from src.sw_character_generator.functions.role_dice import wuerfle_1d8

def apply_ranger_dependent_modifiers(character):
    """Apply ranger-specific modifiers to the character."""

    # Set profession attributes
    character.profession = "ranger"
    character.hp_dice = 8
    character.main_stats = ("strength",)
    character.allowed_alignment = ("good",)
    character.allowed_races = ("human",)
    character.allowed_weapon = ("all",)
    character.allowed_armor = ("all",)
    character.save_throw = 14
    character.delicate_tasks = 0
    character.hide_in_shadows = 0
    character.hear_sounds = 0
    character.move_silently = 0
    character.open_locks = 0
    character.climb_walls = 0
    character.save_bonuses = ()
    character.immunity = ()
    character.special_abilities = ()
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
    #if character.stat_str >= 13:
    #    character.xp_bonus += 5
