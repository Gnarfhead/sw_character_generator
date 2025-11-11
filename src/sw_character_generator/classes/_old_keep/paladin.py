"""Paladin profession module."""
from sw_character_generator.classes._old_keep.profession import ProfessionBase
from sw_character_generator.functions.role_dice import wuerfle_1d8

class Paladin(ProfessionBase):
    """Paladin profession class."""
    def __init__(self):
        self.name = "Paladin"

    def apply_profession_dependent_modifiers(self, character):
        """Apply paladin-specific modifiers to the character."""
        character.tp_dice = 8
        character.main_stats = ("Strength",)
        character.allowed_alignment = ("Good",)
        character.allowed_races = ("Human",)
        character.allowed_weapon = ("all",)
        character.allowed_armor = ("all",)
    
    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Paladin."""
        character.tp = wuerfle_1d8("TP", 1) + character.tp_mod
