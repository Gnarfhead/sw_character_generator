

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

    # Ensure save_bonuses is a set
    if not isinstance(character.save_bonuses, set): # Ensure it's a set
        print("DEBUG apply_druid_dependent_modifiers: Converting character.save_bonuses to set from", type(character.save_bonuses))
        if isinstance(character.save_bonuses, str): # Single string
            character.save_bonuses = {character.save_bonuses} if character.save_bonuses else set() # single ability to set
        elif isinstance(character.save_bonuses, (list, tuple)): # Multiple abilities
            character.save_bonuses = set(character.save_bonuses) # convert list/tuple to set
        else:
            character.save_bonuses = set() # default to empty set
    character.save_bonuses.clear()  # Clear existing bonuses
    character.save_bonuses.add("- Bonus +2 against fire")

    # Ensure immunities is a set
    if not isinstance(character.immunities, set): # Ensure it's a set
        print("DEBUG apply_druid_dependent_modifiers: Converting character.immunities to set from", type(character.immunities))
        if isinstance(character.immunities, str): # Single string
            character.immunities = {character.immunities} if character.immunities else set() # single ability to set
        elif isinstance(character.immunities, (list, tuple)): # Multiple abilities
            character.immunities = set(character.immunities) # convert list/tuple to set
        else:
            character.immunities = set() # default to empty set
    character.immunities.clear()  # Clear existing immunities
    character.immunities.add("- Immunity against fay spells and magical effects (Level 5)")

    # Ensure special_abilities is a set
    if not isinstance(character.special_abilities, set): # Ensure it's a set
        print("DEBUG apply_druid_dependent_modifiers: Converting character.special_abilities to set from", type(character.special_abilities))
        if isinstance(character.special_abilities, str): # Single string
            character.special_abilities = {character.special_abilities} if character.special_abilities else set() # single ability to set
        elif isinstance(character.special_abilities, (list, tuple)): # Multiple abilities
            character.special_abilities = set(character.special_abilities) # convert list/tuple to set
        else:
            character.special_abilities = set() # default to empty set
    character.special_abilities.clear()  # Clear existing special abilities
    character.special_abilities.add("- Secret language: druids know a secret language understood only by other druids of neutral alignment")
    character.special_abilities.add("- Magic items: druids can use magic items that are usable by clerics; except scrolls with cleric-spells")
    character.special_abilities.add("- First mysteries (Level 2): ")
    character.special_abilities.add("- Shape change (Level 5): druids can change their shape into that of a small or medium-sized animal three times per day")
    character.special_abilities.add("- Druid fortress (Level 9): druids can create a sanctuary")

    character.xp_bonus = 0
    character.parry = 0

    # XP progression
    character.xp_progression = {
        1: 0,
        2: 1500,
        3: 3000,
        4: 6000,
        5: 12000,
        6: 24000,
        7: 48000,
        8: 96000,
        9: 192000,
        10: 275000,
        11: 400000,
        12: 550000,
        13: 750000,
        14: 850000,
        15: 1000000,
        16: 1150000,
        17: 1300000,
        18: 1450000,
        19: 1600000,
        20: 1750000,
    }

    # Save throw progression
    character.save_throw_progression = {
        1: 15,
        2: 14,
        3: 13,
        4: 12,
        5: 11,
        6: 10,
        7: 9,
        8: 8,
        9: 7,
        10: 6,
        11: 5,
        12: 4,
        13: 4,
        14: 4,
        15: 4,
        16: 4,
        17: 4,
        18: 4,
        19: 4,
        20: 4,
    }

    character.spells_lvl1 = 0
    character.spells_lvl2 = 0
    character.spells_lvl3 = 0
    character.spells_lvl4 = 0
    character.spells_lvl5 = 0
    character.spells_lvl6 = 0
    character.spells_lvl7 = 0
    character.spells_lvl8 = 0
    character.spells_lvl9 = 0
