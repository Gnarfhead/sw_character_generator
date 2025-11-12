from sw_character_generator.functions.role_dice import wuerfle_1d6

def apply_druid_dependent_modifiers(character):
    """Apply druid-specific modifiers to the character."""
    character.profession = "druid"
    character.tp_dice = 6
    character.main_stats = ("wisdom", "charisma")
    character.allowed_alignment = ("neutral", "evil", "good")
    character.allowed_races = ("human",)
    character.allowed_weapon = ("daggers", "sickles", "spears", "slings", "oil flasks")
    character.allowed_armor = ("leather", "wooden shield")
    character.tp = wuerfle_1d6("TP", 1) + character.tp_mod
    character.save_throw = 15

    """Druids receive an experience bonus based on their main stats."""
    if character.stat_wis >= 13:
        character.xp_bonus += 5
    if character.stat_cha >= 13:
        character.xp_bonus += 5
