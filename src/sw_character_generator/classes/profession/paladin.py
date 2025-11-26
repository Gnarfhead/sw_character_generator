

def apply_paladin_dependent_modifiers(character):
    """Apply paladin-specific modifiers to the character."""
    
    # Set profession attributes
    character.profession = "paladin"
    character.hp_dice = 8
    character.main_stats = ("strength",)
    character.allowed_alignment = ("good",)
    character.allowed_races = ("human",)
    character.allowed_weapon = ("all",)
    character.allowed_armor = ("all",)
    character.save_throw = 12
    character.delicate_tasks = 0
    character.hide_in_shadows = 0
    character.hear_sounds = 0
    character.move_silently = 0
    character.open_locks = 0
    character.climb_walls = 0
    
    # Ensure save_bonuses is a set
    character.save_bonuses.clear()  # Clear existing bonuses
    if not isinstance(character.save_bonuses, set): # Ensure it's a set
        print("DEBUG apply_paladin_dependent_modifiers: Converting character.save_bonuses to set from", type(character.save_bonuses))
        if isinstance(character.save_bonuses, str): # Single string
            character.save_bonuses = {character.save_bonuses} if character.save_bonuses else set() # single ability to set
        elif isinstance(character.save_bonuses, (list, tuple)): # Multiple abilities
            character.save_bonuses = set(character.save_bonuses) # convert list/tuple to set
        else:
            character.save_bonuses = set() # default to empty set

    # Ensure immunities is a set
    character.immunities.clear()  # Clear existing immunities
    if not isinstance(character.immunities, set): # Ensure it's a set
        print("DEBUG apply_paladin_dependent_modifiers: Converting character.immunities to set from", type(character.immunities))
        if isinstance(character.immunities, str): # Single string
            character.immunities = {character.immunities} if character.immunities else set() # single ability to set
        elif isinstance(character.immunities, (list, tuple)): # Multiple abilities
            character.immunities = set(character.immunities) # convert list/tuple to set
        else:
            character.immunities = set() # default to empty set
    character.immunities.add("immunity against disease")
    
    # Ensure special_abilities is a set
    character.special_abilities.clear()  # Clear existing special abilities
    if not isinstance(character.special_abilities, set): # Ensure it's a set
        print("DEBUG apply_paladin_dependent_modifiers: Converting character.special_abilities to set from", type(character.special_abilities))
        if isinstance(character.special_abilities, str): # Single string
            character.special_abilities = {character.special_abilities} if character.special_abilities else set() # single ability to set
        elif isinstance(character.special_abilities, (list, tuple)): # Multiple abilities
            character.special_abilities = set(character.special_abilities) # convert list/tuple to set
        else:
            character.special_abilities = set() # default to empty set
    character.special_abilities.add("lay on hands: paladins can heal 2 HP by laying on hands or cure a disease once per day")
    character.special_abilities.add("magic items: paladins can use magic items that are usable by fighters. A total of 4 magic items, including max 3 weapons, 1 armor and 1 shield")
    character.special_abilities.add("warhorse: paladins can summon a warhorse which is very intelligent and strong (5 HP dice)")
    character.special_abilities.add("banish evil (Level 8): like the cleric spell")
    character.special_abilities.add("detect evil (Level 8): like the cleric spell")
    character.special_abilities.add("fortress (Level 9): paladins can create a stronghold to gather followers")

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

    # Spells per level
    character.spells_lvl1 = 0
    character.spells_lvl2 = 0
    character.spells_lvl3 = 0
    character.spells_lvl4 = 0
    character.spells_lvl5 = 0
    character.spells_lvl6 = 0
    character.spells_lvl7 = 0
    character.spells_lvl8 = 0
    character.spells_lvl9 = 0
