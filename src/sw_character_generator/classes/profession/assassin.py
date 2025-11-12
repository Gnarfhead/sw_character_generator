from sw_character_generator.functions.role_dice import wuerfle_1d6

def apply_assassin_dependent_modifiers(character):
    """Apply assassin-specific modifiers to the character."""
    character.profession = "assassin"
    character.tp_dice = 6
    character.main_stats = ("strength", "dexterity", "intelligence")
    character.allowed_alignment = ("neutral", "evil")
    character.allowed_races = ("human",)
    character.allowed_weapon = ("light weapons",)
    character.allowed_armor = ("light",)
    character.tp = wuerfle_1d6("TP", 1) + character.tp_mod
    character.save_throw = 15
    character.delicate_tasks = 0
    character.hide_in_shadows = 0
    character.hear_sounds = 0
    character.move_silently = 0
    character.open_locks = 0
    character.climb_walls = 0

    """Assassins receive an experience bonus based on their main stats."""
    if character.stat_str >= 13:
        character.xp_bonus += 5
    if character.stat_dex >= 13:
        character.xp_bonus += 5
    if character.stat_int >= 13:
        character.xp_bonus += 5


