from sw_character_generator.functions.role_dice import wuerfle_1d6

def apply_thief_dependent_modifiers(character):
    """Apply thief-specific modifiers to the character."""

    # Set profession attributes
    character.profession = "thief"
    character.tp_dice = 6
    character.main_stats = ("dexterity",)
    character.allowed_alignment = ("neutral", "evil")
    character.allowed_races = ("human", "halfling", "elf", "dwarf")
    character.allowed_weapon = ("light weapons",)
    character.allowed_armor = ("light",)
    character.save_throw = 15
    character.delicate_tasks = 15
    character.hide_in_shadows = 10
    character.hear_sounds = 3
    character.move_silently = 20
    character.open_locks = 10
    character.climb_walls = 85

    # Calculate total TP
    character.tp = wuerfle_1d6("TP", 1) + character.tp_mod
    if character.tp < 1:
        character.tp = 1

    # Calculate XP bonus
    if character.stat_dex >= 13:
        character.xp_bonus += 5