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
    character.save_throw = 14
    character.delicate_tasks = 0
    character.hide_in_shadows = 0
    character.hear_sounds = 0
    character.move_silently = 0
    character.open_locks = 0
    character.climb_walls = 0

    character.save_bonuses = set()

    character.immunity = set()

    print("DEBUG apply_fighter_dependent_modifiers: type of character.special_abilities before assignment:", type(character.special_abilities))
    character.special_abilities = set()
    character.special_abilities.add("multiple attacks: against creatures with 1 tp or less, fighters strike one attack per level per round")
    character.special_abilities.add("fortress (Level 9): fighters can create a stronghold to gather followers and protect themselves")
    print("DEBUG apply_fighter_dependent_modifiers: type of character.special_abilities after assignment:", type(character.special_abilities))

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
