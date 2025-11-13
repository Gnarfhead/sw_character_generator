from src.sw_character_generator.functions.role_dice import wuerfle_1d10

def apply_fighter_dependent_modifiers(character):
    """Apply fighter-specific modifiers to the character."""
    
    # Set profession attributes
    character.profession = "fighter"
    character.tp_dice = 10
    character.main_stats = ("strength",)
    character.allowed_alignment = ("neutral", "evil", "good")
    character.allowed_races = ("human", "halfling", "elf", "dwarf", "halfelf")
    character.allowed_weapon = ("all",)
    character.allowed_armor = ("heavy",)
    character.save_throw = 14
    character.special_abilities += (
        "multiple attacks: against creatures with 1 tp or less, fighters strike one attack per level per round",
        "fortress (Level 9): fighters can create a stronghold to gather followers and protect themselves",
    )

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

    # Calculate total TP
    character.tp = wuerfle_1d10(1) + character.tp_mod
    if character.tp < 1:
        character.tp = 1

    # Calculate XP bonus
    if character.stat_str >= 13:
        character.xp_bonus += 5
