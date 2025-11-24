

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
    character.save_bonuses = ()
    character.immunity = (
        "immunity against disease",
    )
    character.special_abilities = (
        "lay on hands: paladins can heal 2 HP by laying on hands or cure a disease once per day",
        "magic items: paladins can use magic items that are usable by fighters. A total of 4 magic items, including max 3 weapons, 1 armor and 1 shield",
        "warhorse: paladins can summon a warhorse which is very intelligent and strong (5 HP dice)",
        "banish evil (Level 8): like the cleric spell",
        "detect evil (Level 8): like the cleric spell",
        "fortress (Level 9): paladins can create a stronghold to gather followers",
    )
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
