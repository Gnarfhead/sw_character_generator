

def apply_thief_dependent_modifiers(character):
    """Apply thief-specific modifiers to the character."""

    # Set profession attributes
    character.profession = "thief"
    character.hp_dice = 6
    character.main_stats = ("dexterity",)
    character.allowed_alignment = ("neutral", "evil")
    character.allowed_races = ("human", "halfling", "elf", "dwarf")
    character.allowed_weapon = ("light weapons",)
    character.allowed_armor = ("light",)
    character.thief_user_class = True
    character.magic_user_class = False

    # Ensure save_bonuses is a set
    if not isinstance(character.save_bonuses_profession, set): # Ensure it's a set
        print("DEBUG apply_thief_dependent_modifiers: Converting character.save_bonuses to set from", type(character.save_bonuses_profession))
        if isinstance(character.save_bonuses_profession, str): # Single string
            character.save_bonuses_profession = {character.save_bonuses_profession} if character.save_bonuses_profession else set() # single ability to set
        elif isinstance(character.save_bonuses_profession, (list, tuple)): # Multiple abilities
            character.save_bonuses_profession = set(character.save_bonuses_profession) # convert list/tuple to set
        else:
            character.save_bonuses_profession = set() # default to empty set
    character.save_bonuses_profession.clear()  # Clear existing bonuses
    character.save_bonuses_profession.add("- Bonus +2 against traps and mechanical devices: Include traps, wands and magical devices")

   # Ensure immunities is a set
    if not isinstance(character.immunities_profession, set): # Ensure it's a set
        print("DEBUG apply_thief_dependent_modifiers: Converting character.immunities to set from", type(character.immunities_profession))
        if isinstance(character.immunities_profession, str): # Single string
            character.immunities_profession = {character.immunities_profession} if character.immunities_profession else set() # single ability to set
        elif isinstance(character.immunities_profession, (list, tuple)): # Multiple abilities
            character.immunities_profession = set(character.immunities_profession) # convert list/tuple to set
        else:
            character.immunities_profession = set() # default to empty set
    character.immunities_profession.clear()  # Clear existing immunities
    character.immunities_profession.add("- Immunity against disease")

    # Ensure special_abilities is a set
    if not isinstance(character.special_abilities_profession, set): # Ensure it's a set
        print("DEBUG apply_thief_dependent_modifiers: Converting character.special_abilities to set from", type(character.special_abilities_profession))
        if isinstance(character.special_abilities_profession, str): # Single string
            character.special_abilities_profession = {character.special_abilities_profession} if character.special_abilities_profession else set() # single ability to set
        elif isinstance(character.special_abilities_profession, (list, tuple)): # Multiple abilities
            character.special_abilities_profession = set(character.special_abilities_profession) # convert list/tuple to set
        else:
            character.special_abilities_profession = set() # default to empty set
    character.special_abilities_profession.clear()  # Clear existing special abilities
    character.special_abilities_profession.add("- Sneak attack: thieves gain a +4 bonus to attack and damage rolls are doubled when attacking opponent from behind")
    character.special_abilities_profession.add("- Read languages  (Level 3): thieves can read all written languages; 80% chance to understand maps and written information")
    character.special_abilities_profession.add("- Read magic language (Level 9): thieves can read magic inscriptions on magical items and scrolls and cast wizard-spells from scrolls")
    character.special_abilities_profession.add("- Create guild (Level 9): thieves can create a thieves' guild to gather followers")

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
        12: 5,
        13: 5,
        14: 5,
        15: 5,
        16: 5,
        17: 5,
        18: 5,
        19: 5,
        20: 5,
    }

    # Delicate tasks thief skills progression
    character.delicate_tasks_profession = {
        1: 15,
        2: 20,
        3: 25,
        4: 30,
        5: 35,
        6: 40,
        7: 45,
        8: 50,
        9: 60,
        10: 70,
        11: 80,
        12: 90,
        13: 100,
        14: 100,
        15: 100,
        16: 100,
        17: 100,
        18: 100,
        19: 100,
        20: 100,
    }

    # Climb walls thief skills progression
    character.climb_walls_profession = {
        1: 85,
        2: 86,
        3: 87,
        4: 88,
        5: 89,
        6: 90,
        7: 91,
        8: 92,
        9: 93,
        10: 94,
        11: 95,
        12: 96,
        13: 97,
        14: 98,
        15: 99,
        16: 99,
        17: 99,
        18: 99,
        19: 99,
        20: 99,
    } 

    # Hear sounds thief skills progression
    character.hear_sounds_profession = {
        1: "3:6",
        2: "3:6",
        3: "4:6",
        4: "4:6",
        5: "4:6",
        6: "4:6",
        7: "5:6",
        8: "5:6",
        9: "5:6",
        10: "5:6",
        11: "6:6",
        12: "6:6",
        13: "6:6",
        14: "6:6",
        15: "6:6",
        16: "6:6",
        17: "6:6",
        18: "6:6",
        19: "6:6",
        20: "6:6",
    }

    # Hide in shadows thief skills progression
    character.hide_in_shadows_profession = {
        1: 10,  
        2: 15,
        3: 20,
        4: 25,
        5: 30,
        6: 35,
        7: 40,
        8: 55,
        9: 65,
        10: 75,
        11: 85,
        12: 95,
        13: 100,
        14: 100,
        15: 100,
        16: 100,
        17: 100,
        18: 100,
        19: 100,
        20: 100,
    }

    # Move silently thief skills progression
    character.move_silently_profession = {
        1: 20,
        2: 25,
        3: 30,
        4: 35,
        5: 40,
        6: 45,
        7: 50,
        8: 60,
        9: 70,
        10: 80,
        11: 90,
        12: 100,
        13: 100,
        14: 100,
        15: 100,
        16: 100,
        17: 100,
        18: 100,
        19: 100,
        20: 100,
    }

    # Open locks thief skills progression
    character.open_locks_profession = {
        1: 10,
        2: 15,
        3: 20,
        4: 25,
        5: 30,
        6: 35,
        7: 40,
        8: 55,
        9: 65,
        10: 75,
        11: 85,
        12: 95,
        13: 100,
        14: 100,
        15: 100,
        16: 100,
        17: 100,
        18: 100,
        19: 100,
        20: 100,
    }

    character.spell_table = {
        1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        2: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        3: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        4: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        5: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        6: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        7: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        8: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        9: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        10: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        11: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        12: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        13: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        14: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        15: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        16: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        17: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        18: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 , 7: 0, 8: 0, 9: 0},
        19: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        20: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
    }