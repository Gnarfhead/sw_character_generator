from src.sw_character_generator.functions.role_dice import wuerfle_1d4

def apply_wizard_dependent_modifiers(character):
    """Apply wizard-specific modifiers to the character."""

    # Set profession attributes
    character.profession = "wizard"
    character.hp_dice = 4
    character.main_stats = ("intelligence",)
    character.allowed_alignment = ("good", "neutral", "evil")
    character.allowed_races = ("human", "halfelf", "elf")
    character.allowed_weapon = ("staff", "dagger")
    character.allowed_armor = ("none",)
    character.save_throw = 15
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

    # Calculate total HP
    character.hp = wuerfle_1d4(1) + character.hp_mod
    if character.hp < 1:
        character.hp = 1

    # Calculate XP bonus
    if character.stat_int >= 13:
        character.xp_bonus += 5
