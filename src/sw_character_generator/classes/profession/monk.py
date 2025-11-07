"""Monk profession module."""
from sw_character_generator.classes.profession.profession import ProfessionBase
from sw_character_generator.functions.role_dice import wuerfle_1d4

class Monk(ProfessionBase):
    """Monk profession class."""
    def __init__(self):
        self.name = "Monk"

    def apply_profession_dependent_modifiers(self, character):
        """Apply monk-specific modifiers to the character."""
        character.tp_dice = 4
        character.main_stats = ("Wisdom")
        character.allowed_alignment = ("Neutral", "Evil", "Good")
        character.allowed_races = ("Human")
        character.allowed_weapon = ("all")
        character.allowed_armor = ("none")
    
    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Monk."""
        character.tp = wuerfle_1d4("TP", 1) + character.tp_mod
