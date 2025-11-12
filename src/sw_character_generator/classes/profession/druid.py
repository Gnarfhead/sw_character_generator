from src.sw_character_generator.functions.role_dice import wuerfle_1d6

def apply_druid_dependent_modifiers(character):
    """Apply druid-specific modifiers to the character."""

    # Set profession attributes
    character.profession = "druid"
    character.tp_dice = 6
    character.main_stats = ("wisdom", "charisma")
    character.allowed_alignment = ("neutral", "evil", "good")
    character.allowed_races = ("human",)
    character.allowed_weapon = ("daggers", "sickles", "spears", "slings", "oil flasks")
    character.allowed_armor = ("leather", "wooden shield")
    character.save_throw = 15
    character.save_bonuses += (
        "+2 against fire",
    )
    character.immunity += (
        "Immunity against fay spells and magical effects (Level 5)",
    )
    character.special_abilities += (
        "secret language: druids know a secret language understood only by other druids of neutral alignment",
        "magic items: druids can use magic items that are usable by clerics, except scrolls with cleric-spells",
        "first mysteries (Level 2): ",
        "shape change (Level 5): druids can change their shape into that of a small or medium-sized animal three times per day",
        "Druid fortress (Level 9): druids can create a sanctuary",
    )

    # Calculate total TP
    character.tp = wuerfle_1d6("TP", 1) + character.tp_mod
    if character.tp < 1:
        character.tp = 1

    # Calculate XP bonus
    if character.stat_wis >= 13:
        character.xp_bonus += 5
    if character.stat_cha >= 13:
        character.xp_bonus += 5
