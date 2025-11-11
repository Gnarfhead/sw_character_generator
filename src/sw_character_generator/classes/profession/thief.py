from sw_character_generator.functions.role_dice import wuerfle_1d6

def apply_thief_dependent_modifiers(character):
    """Apply thief-specific modifiers to the character."""
    character.profession = "Thief"
    character.tp_dice = 6
    character.main_stats = ("Dexterity",)
    character.allowed_alignment = ("Neutral", "Evil")
    character.allowed_races = ("Human", "Halfling", "Elf", "Dwarf")
    character.allowed_weapon = ("light weapons",)
    character.allowed_armor = ("light",)
    character.tp = wuerfle_1d6("TP", 1) + character.tp_mod