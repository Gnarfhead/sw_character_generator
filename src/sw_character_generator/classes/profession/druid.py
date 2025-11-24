from src.sw_character_generator.functions.role_dice import wuerfle_1d6

def apply_druid_dependent_modifiers(character):
    """Apply druid-specific modifiers to the character."""

    # Set profession attributes
    character.profession = "druid"
    character.hp_dice = 6
    character.main_stats = ("wisdom", "charisma",)
    character.allowed_alignment = ("neutral", "evil", "good")
    character.allowed_races = ("human",)
    character.allowed_weapon = ("daggers", "sickles", "spears", "slings", "oil flasks")
    character.allowed_armor = ("leather", "wooden shield")
    character.save_throw = 15
    character.delicate_tasks = 0
    character.hide_in_shadows = 0
    character.hear_sounds = 0
    character.move_silently = 0
    character.open_locks = 0
    character.climb_walls = 0
    character.save_bonuses = (
        "+2 against fire",
    )
    character.immunity = (
        "Immunity against fay spells and magical effects (Level 5)",
    )
    character.special_abilities = (
        "secret language: druids know a secret language understood only by other druids of neutral alignment",
        "magic items: druids can use magic items that are usable by clerics, except scrolls with cleric-spells",
        "first mysteries (Level 2): ",
        "shape change (Level 5): druids can change their shape into that of a small or medium-sized animal three times per day",
        "Druid fortress (Level 9): druids can create a sanctuary",
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
    #if character.stat_char >= 13:
    #    character.xp_bonus += 5
