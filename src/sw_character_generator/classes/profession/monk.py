

def apply_monk_dependent_modifiers(character):
    """Apply monk-specific modifiers to the character."""
    
    # Set profession attributes
    character.profession = "monk"
    character.hp_dice = 4
    character.main_stats = ("wisdom",)
    character.allowed_alignment = ("neutral", "evil", "good")
    character.allowed_races = ("human",)
    character.allowed_weapon = ("all",)
    character.allowed_armor = ("none",)
    character.save_throw = 15
    character.delicate_tasks = 15
    character.hide_in_shadows = 10
    character.hear_sounds = "3:6"
    character.move_silently = 20
    character.open_locks = 10
    character.climb_walls = 85

    # Ensure save_bonuses is a set
    character.save_bonuses.clear()  # Clear existing bonuses
    if not isinstance(character.save_bonuses, set): # Ensure it's a set
        print("DEBUG apply_monk_dependent_modifiers: Converting character.save_bonuses to set from", type(character.save_bonuses))
        if isinstance(character.save_bonuses, str): # Single string
            character.save_bonuses = {character.save_bonuses} if character.save_bonuses else set() # single ability to set
        elif isinstance(character.save_bonuses, (list, tuple)): # Multiple abilities
            character.save_bonuses = set(character.save_bonuses) # convert list/tuple to set
        else:
            character.save_bonuses = set() # default to empty set
    character.save_bonuses.add("+2 against paralysis and poison")

    # Ensure immunities is a set
    character.immunities.clear()  # Clear existing immunities
    if not isinstance(character.immunities, set): # Ensure it's a set
        print("DEBUG apply_monk_dependent_modifiers: Converting character.immunities to set from", type(character.immunities))
        if isinstance(character.immunities, str): # Single string
            character.immunities = {character.immunities} if character.immunities else set() # single ability to set
        elif isinstance(character.immunities, (list, tuple)): # Multiple abilities
            character.immunities = set(character.immunities) # convert list/tuple to set
        else:
            character.immunities = set() # default to empty set
    character.immunities.add("mastering self (Level 8): immune against mindcontrol, charm and hypnosis; except the spells 'geas' and 'command'")
    character.immunities.add("be one with your self (Level 9): also immune against spells 'geas' and 'command'")

    # Ensure special_abilities is a set
    character.special_abilities.clear()  # Clear existing special abilities
    if not isinstance(character.special_abilities, set): # Ensure it's a set
        print("DEBUG apply_monk_dependent_modifiers: Converting character.special_abilities to set from", type(character.special_abilities))
        if isinstance(character.special_abilities, str): # Single string
            character.special_abilities = {character.special_abilities} if character.special_abilities else set() # single ability to set
        elif isinstance(character.special_abilities, (list, tuple)): # Multiple abilities
            character.special_abilities = set(character.special_abilities) # convert list/tuple to set
        else:
            character.special_abilities = set() # default to empty set
    character.special_abilities.add("deflect missiles: monks can deflect magic missiles and arrows with a successful save throw")
    character.special_abilities.add("magic items: you can't use magic healing potions. Monks can only use magic weapons and rings")
    character.special_abilities.add("deadly strike: if attack roll is 5 points above opponents AC, chance is 75% to stun opponent for 2d6 rounds; opponents less 1 TP die instantly die by 25% chance")
    character.special_abilities.add("alertness: your group isn't easy to surprise; opponents chance ist 1:6")
    character.special_abilities.add("weapon damage (Level 2): +1 damage when using a weapon")
    character.special_abilities.add("talk to animals (Level 4): monks can communicate with animals")
    character.special_abilities.add("feather fall (Level 5): monks can fall from 6m height without taking damage")
    character.special_abilities.add("mastering silence (Level 5): you can play dead for 1d6 *  monk level * 10 minutes")
    character.special_abilities.add("mastering mind (Level 6): read you thoughts don't work with 90% chance")
    character.special_abilities.add("weaponless combat (Level 6): when fight unarmed, you can strike multiple times")
    character.special_abilities.add("mastering body (Level 7): you can heal yourself 1d6+1 TP per day")
    character.special_abilities.add("create monastery (Level 11): monks can create a monastery to gather followers")
    character.special_abilities.add("harmony touch (Level 13): connect through touch with another living being when TP die is equal or less; stop the heart and kill the being instantly")

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
