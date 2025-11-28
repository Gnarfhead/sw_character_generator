from src.sw_character_generator.functions.role_dice import wuerfle_1d10
from sw_character_generator.functions.gen_char_stat_mods import analyze_mod_str

def apply_fighter_dependent_modifiers(character):
    """Apply fighter-specific modifiers to the character."""
    
    # Set profession attributes
    character.profession = "fighter"
    character.hp_dice = 10
    character.main_stats = ("strength",)
    character.allowed_alignment = ("neutral", "evil", "good")
    character.allowed_races = ("human", "halfling", "elf", "dwarf", "halfelf")
    character.allowed_weapon = ("all",)
    character.allowed_armor = ("heavy",)
    character.thief_class = False
    character.magic_user_class = False


    # Ensure save_bonuses is a set
    if not isinstance(character.save_bonuses_profession, set): # Ensure it's a set
        print("DEBUG apply_fighter_dependent_modifiers: Converting character.save_bonuses to set from", type(character.save_bonuses_profession))
        if isinstance(character.save_bonuses_profession, str): # Single string
            character.save_bonuses_profession = {character.save_bonuses_profession} if character.save_bonuses_profession else set() # single ability to set
        elif isinstance(character.save_bonuses_profession, (list, tuple)): # Multiple abilities
            character.save_bonuses_profession = set(character.save_bonuses_profession) # convert list/tuple to set
        else:
            character.save_bonuses_profession = set() # default to empty set
    character.save_bonuses_profession.clear()  # Clear existing bonuses

    # Ensure immunities is a set
    if not isinstance(character.immunities_profession, set): # Ensure it's a set
        print("DEBUG apply_fighter_dependent_modifiers: Converting character.immunities to set from", type(character.immunities_profession))
        if isinstance(character.immunities_profession, str): # Single string
            character.immunities_profession = {character.immunities_profession} if character.immunities_profession else set() # single ability to set
        elif isinstance(character.immunities_profession, (list, tuple)): # Multiple abilities
            character.immunities_profession = set(character.immunities_profession) # convert list/tuple to set
        else:
            character.immunities_profession = set() # default to empty set
    character.immunities_profession.clear()  # Clear existing immunities

    # Ensure special_abilities is a set
    if not isinstance(character.special_abilities_profession, set): # Ensure it's a set
        print("DEBUG apply_fighter_dependent_modifiers: Converting character.special_abilities to set from", type(character.special_abilities_profession))
        if isinstance(character.special_abilities_profession, str): # Single string
            character.special_abilities_profession = {character.special_abilities_profession} if character.special_abilities_profession else set() # single ability to set
        elif isinstance(character.special_abilities_profession, (list, tuple)): # Multiple abilities
            character.special_abilities_profession = set(character.special_abilities_profession) # convert list/tuple to set
        else:
            character.special_abilities_profession = set() # default to empty set
    character.special_abilities_profession.clear()  # Clear existing special abilities
    character.special_abilities_profession.add("- Multiple attacks: against creatures with 1 tp or less; fighters strike one attack per level per round")
    character.special_abilities_profession.add("- Fortress (Level 9): fighters can create a stronghold to gather followers and protect themselves")

    character.xp_bonus = 0

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
        1: 14,
        2: 13,
        3: 12,
        4: 11,
        5: 10,
        6: 9,
        7: 8,
        8: 7,
        9: 6,
        10: 5,
        11: 4,
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


    # Calculate parry based on DEX
    character.parry = 0
    if character.stat_dex == 14:
        character.parry = -1
    elif character.stat_dex == 15:
        character.parry = -2
    elif character.stat_dex == 16:
        character.parry = -3
    elif character.stat_dex == 17:
        character.parry = -4
    elif character.stat_dex == 18:
        character.parry = -5


    # Analyze stat modifiers and apply to character (fighter specific Bonus to STR)
    analyze_mod_str(character)
