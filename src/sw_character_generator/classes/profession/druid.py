

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
    character.magic_user_class = True
    character.thief_class = False


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

# Delicate tasks thief skills progression
    character.delicate_tasks_profession = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 0,
    }

    # Climb walls thief skills progression
    character.climb_walls_profession = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 0,
    }

    # Hear sounds thief skills progression
    character.hear_sounds_profession = {
        1: "0:6",
        2: "0:6",
        3: "0:6",
        4: "0:6",
        5: "0:6",
        6: "0:6",
        7: "0:6",
        8: "0:6",
        9: "0:6",
        10: "0:6",
        11: "0:6",
        12: "0:6",
        13: "0:6",
        14: "0:6",
        15: "0:6",
        16: "0:6",
        17: "0:6",
        18: "0:6",
        19: "0:6",
        20: "0:6",
    }

    # Hide in shadows thief skills progression
    character.hide_in_shadows_profession = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 0,
    }

    # Move silently thief skills progression
    character.move_silently_profession = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 0,
    
    }

    # Open locks thief skills progression
    character.open_locks_profession = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 0,
        17: 0,
        18: 0,
        19: 0,
        20: 0,
    }


    character.spell_table = {
        1: {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        2: {1: 2, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        3: {1: 3, 2: 1, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        4: {1: 3, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        5: {1: 3, 2: 2, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        6: {1: 3, 2: 2, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        7: {1: 4, 2: 2, 3: 2, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        8: {1: 4, 2: 3, 3: 2, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        9: {1: 4, 2: 3, 3: 3, 4: 2, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        10: {1: 5, 2: 3, 3: 3, 4: 2, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0},
        11: {1: 5, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1, 7: 0, 8: 0, 9: 0},
        12: {1: 5, 2: 4, 3: 4, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0, 9: 0},
        13: {1: 6, 2: 5, 3: 5, 4: 4, 5: 4, 6: 3, 7: 2, 8: 0, 9: 0},
        14: {1: 7, 2: 5, 3: 5, 4: 4, 5: 4, 6: 3, 7: 2, 8: 0, 9: 0},
        15: {1: 7, 2: 6, 3: 5, 4: 4, 5: 4, 6: 3, 7: 2, 8: 0, 9: 0},
        16: {1: 7, 2: 6, 3: 6, 4: 4, 5: 4, 6: 3, 7: 2, 8: 0, 9: 0},
        17: {1: 8, 2: 6, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 0, 9: 0},
        18: {1: 8, 2: 7, 3: 6, 4: 5, 5: 5, 6: 3, 7: 2, 8: 0, 9: 0},
        19: {1: 9, 2: 8, 3: 6, 4: 5, 5: 5, 6: 3, 7: 2, 8: 0, 9: 0},
        20: {1: 9, 2: 8, 3: 7, 4: 5, 5: 5, 6: 3, 7: 2, 8: 0, 9: 0},
    }
