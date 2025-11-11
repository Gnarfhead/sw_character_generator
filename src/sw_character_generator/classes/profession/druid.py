from sw_character_generator.functions.role_dice import wuerfle_1d6

def apply_profession_dependent_modifiers(self, character):
    """Apply druid-specific modifiers to the character."""
    character.tp_dice = 6
    character.main_stats = ("Wisdom", "Charisma")
    character.allowed_alignment = ("Neutral", "Evil", "Good")
    character.allowed_races = ("Human")
    character.allowed_weapon = ("daggers", "sickles", "spears", "slings", "oil flasks")
    character.allowed_armor = ("leather", "wooden shield")
    character.tp = wuerfle_1d6("TP", 1) + character.tp_mod
