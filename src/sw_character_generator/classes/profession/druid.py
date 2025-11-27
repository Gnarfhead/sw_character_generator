

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


    # Ensure save_bonuses is a set
    if not isinstance(character.save_bonuses_profession, set): # Ensure it's a set
        print("DEBUG apply_druid_dependent_modifiers: Converting character.save_bonuses to set from", type(character.save_bonuses_profession))
        if isinstance(character.save_bonuses_profession, str): # Single string
            character.save_bonuses_profession = {character.save_bonuses_profession} if character.save_bonuses_profession else set() # single ability to set
        elif isinstance(character.save_bonuses_profession, (list, tuple)): # Multiple abilities
            character.save_bonuses_profession = set(character.save_bonuses_profession) # convert list/tuple to set
        else:
            character.save_bonuses_profession = set() # default to empty set
    character.save_bonuses_profession.clear()  # Clear existing bonuses
    character.save_bonuses_profession.add("- Bonus +2 against fire")

    # Ensure immunities is a set
    if not isinstance(character.immunities_profession, set): # Ensure it's a set
        print("DEBUG apply_druid_dependent_modifiers: Converting character.immunities to set from", type(character.immunities_profession))
        if isinstance(character.immunities_profession, str): # Single string
            character.immunities_profession = {character.immunities_profession} if character.immunities_profession else set() # single ability to set
        elif isinstance(character.immunities_profession, (list, tuple)): # Multiple abilities
            character.immunities_profession = set(character.immunities_profession) # convert list/tuple to set
        else:
            character.immunities_profession = set() # default to empty set
    character.immunities_profession.clear()  # Clear existing immunities
    character.immunities_profession.add("- Immunity against fay spells and magical effects (Level 5)")

    # Ensure special_abilities is a set
    if not isinstance(character.special_abilities_profession, set): # Ensure it's a set
        print("DEBUG apply_druid_dependent_modifiers: Converting character.special_abilities to set from", type(character.special_abilities_profession))
        if isinstance(character.special_abilities_profession, str): # Single string
            character.special_abilities_profession = {character.special_abilities_profession} if character.special_abilities_profession else set() # single ability to set
        elif isinstance(character.special_abilities_profession, (list, tuple)): # Multiple abilities
            character.special_abilities_profession = set(character.special_abilities_profession) # convert list/tuple to set
        else:
            character.special_abilities_profession = set() # default to empty set
    character.special_abilities_profession.clear()  # Clear existing special abilities
    character.special_abilities_profession.add("- Secret language: druids know a secret language understood only by other druids of neutral alignment")
    character.special_abilities_profession.add("- Magic items: druids can use magic items that are usable by clerics; except scrolls with cleric-spells")
    character.special_abilities_profession.add("- First mysteries (Level 2): ")
    character.special_abilities_profession.add("- Shape change (Level 5): druids can change their shape into that of a small or medium-sized animal three times per day")
    character.special_abilities_profession.add("- Druid fortress (Level 9): druids can create a sanctuary")

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
