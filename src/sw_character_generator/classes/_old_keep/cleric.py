"""Cleric profession module."""
from sw_character_generator.classes._old_keep.profession import ProfessionBase
from sw_character_generator.functions.role_dice import wuerfle_1d6

class Cleric(ProfessionBase):
    """Cleric profession class."""
    def __init__(self):
        self.name = "Cleric"

    def apply_profession_dependent_modifiers(self, character):
        """Apply cleric-specific modifiers to the character."""
        character.tp_dice = 6
        character.main_stats = ("Wisdom")
        character.allowed_alignment = ("Good", "Evil")
        character.allowed_races = ("Human", "Halfelf")
        character.allowed_weapon = ("blunt weapons")
        character.allowed_armor = ("all")
    
    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Cleric."""
        character.tp = wuerfle_1d6("TP", 1) + character.tp_mod
