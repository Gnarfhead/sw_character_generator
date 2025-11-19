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
    character.save_bonuses = ()
    character.immunity = ()
    character.special_abilities = (
        "multiple attacks: against creatures with 1 tp or less, fighters strike one attack per level per round",
        "fortress (Level 9): fighters can create a stronghold to gather followers and protect themselves",
    )
    character.xp_bonus = 0
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
    if character.stat_dex == 14:
        character.parry += -1
    elif character.stat_dex == 15:
        character.parry += -2
    elif character.stat_dex == 16:
        character.parry += -3
    elif character.stat_dex == 17:
        character.parry += -4
    elif character.stat_dex == 18:
        character.parry += -5

    # Calculate total HP
    character.hp = wuerfle_1d10(1) + character.hp_mod
    if character.hp < 1:
        character.hp = 1

    # Calculate XP bonus
    if character.stat_str >= 13:
        character.xp_bonus += 5

    # Analyze stat modifiers and apply to character (fighter specific Bonus to STR)
    analyze_mod_str(character)
