def apply_assassin_dependent_modifiers(character):
    """Apply assassin-specific modifiers to the character."""

    # Set profession attributes
    character.profession = "assassin"
    character.hp_dice = 6
    character.main_stats = ("strength", "dexterity", "intelligence",)
    character.allowed_alignment = ("neutral", "evil")
    character.allowed_races = ("human",)
    character.allowed_weapon = ("light weapons",)
    character.allowed_armor = ("light",)
    character.thief_class = True
    character.magic_user_class = False

    # Ensure save_bonuses is a set
    if not isinstance(character.save_bonuses_profession, set): # Ensure it's a set
        print("DEBUG apply_assassin_dependent_modifiers: Converting character.save_bonuses to set from", type(character.save_bonuses))
        if isinstance(character.save_bonuses_profession, str): # Single string
            character.save_bonuses_profession = {character.save_bonuses_profession} if character.save_bonuses_profession else set() # single ability to set
        elif isinstance(character.save_bonuses_profession, (list, tuple)): # Multiple abilities
            character.save_bonuses_profession = set(character.save_bonuses_profession) # convert list/tuple to set
        else:
            character.save_bonuses_profession = set() # default to empty set
    character.save_bonuses_profession.clear()  # Clear existing bonuses

    # Ensure immunities is a set
    if not isinstance(character.immunities_profession, set): # Ensure it's a set
        print("DEBUG apply_assassin_dependent_modifiers: Converting character.immunities to set from", type(character.immunities_profession))
        if isinstance(character.immunities_profession, str): # Single string
            character.immunities_profession = {character.immunities_profession} if character.immunities_profession else set() # single ability to set
        elif isinstance(character.immunities_profession, (list, tuple)): # Multiple abilities
            character.immunities_profession = set(character.immunities_profession) # convert list/tuple to set
        else:
            character.immunities_profession = set() # default to empty set
    character.immunities_profession.clear()  # Clear existing immunities

    # Ensure special_abilities is a set
    if not isinstance(character.special_abilities_profession, set): # Ensure it's a set
        print("DEBUG apply_assassin_dependent_modifiers: Converting character.special_abilities to set from", type(character.special_abilities_profession))
        if isinstance(character.special_abilities_profession, str): # Single string
            character.special_abilities_profession = {character.special_abilities_profession} if character.special_abilities_profession else set() # single ability to set
        elif isinstance(character.special_abilities_profession, (list, tuple)): # Multiple abilities
            character.special_abilities_profession = set(character.special_abilities_profession) # convert list/tuple to set
        else:
            character.special_abilities_profession = set() # default to empty set
    character.special_abilities_profession.clear()  # Clear existing special abilities
    character.special_abilities_profession.add("- Sneak attack: assassins gain a +4 bonus to attack and damage rolls are doubled when attacking opponent from behind")
    character.special_abilities_profession.add("- Poison use: assassins are skilled in the use of poisoning weapons")
    character.special_abilities_profession.add("- Magic items: assassins can use magic items that are usable by thieves; additionally; they can use magic weapons; leather armor and shields")
    character.special_abilities_profession.add("- Disguise self: assassins can cast disguise self; danger of being discovered 5% -10% based on intelligence/wisdom of opponent")
    character.special_abilities_profession.add("- Create guild (Level 14): assassins can create an assassins' guild to gather followers")

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
        1: 0,
        2: 0,
        3: 15,
        4: 20,
        5: 25,
        6: 30,
        7: 35,
        8: 40,
        9: 45,
        10: 50,
        11: 60,
        12: 70,
        13: 80,
        14: 80,
        15: 80,
        16: 80,
        17: 95,
        18: 80,
        19: 80,
        20: 80,
    }

    # Climb walls thief skills progression
    character.climb_walls_profession = {
        1: 0,
        2: 0,
        3: 85,
        4: 86,
        5: 87,
        6: 88,
        7: 89,
        8: 90,
        9: 91,
        10: 92,
        11: 93,
        12: 94,
        13: 95,
        14: 95,
        15: 95,
        16: 95,
        17: 95,
        18: 95,
        19: 95,
        20: 95,
    } 

    # Hear sounds thief skills progression
    character.hear_sounds_profession = {
        1: "0:6",
        2: "0:6",
        3: "3:6",
        4: "3:6",
        5: "4:6",
        6: "4:6",
        7: "4:6",
        8: "4:6",
        9: "5:6",
        10: "5:6",
        11: "5:6",
        12: "5:6",
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
        1: 0,
        2: 0,
        3: 10,
        4: 15,
        5: 20,
        6: 25,
        7: 30,
        8: 35,
        9: 40,
        10: 55,
        11: 65,
        12: 75,
        13: 85,
        14: 85,
        15: 85,
        16: 85,
        17: 85,
        18: 85,
        19: 85,
        20: 85,
    }

    # Move silently thief skills progression
    character.move_silently_profession = {
        1: 0,
        2: 0,
        3: 20,
        4: 25,
        5: 30,
        6: 35,
        7: 40,
        8: 45,
        9: 50,
        10: 60,
        11: 70,
        12: 80,
        13: 90,
        14: 90,
        15: 90,
        16: 90,
        17: 90,
        18: 90,
        19: 90,
        20: 90,
    
    }

    # Open locks thief skills progression
    character.open_locks_profession = {
        1: 0,
        2: 0,
        3: 10,
        4: 15,
        5: 20,
        6: 25,
        7: 30,
        8: 35,
        9: 40,
        10: 55,
        11: 65,
        12: 75,
        13: 85,
        14: 85,
        15: 85,
        16: 85,
        17: 85,
        18: 85,
        19: 85,
        20: 85,
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