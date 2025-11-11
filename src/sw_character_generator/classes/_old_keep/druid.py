"""Druid profession module."""
from sw_character_generator.classes.profession.profession import ProfessionBase
from sw_character_generator.functions.role_dice import wuerfle_1d6

class Druid(ProfessionBase):
    """Druid profession class."""
    def __init__(self):
        self.name = "Druid"

    def apply_profession_dependent_modifiers(self, character):
        """Apply druid-specific modifiers to the character."""
        character.tp_dice = 6
        character.main_stats = ("Wisdom", "Charisma")
        character.allowed_alignment = ("Neutral", "Evil", "Good")
        character.allowed_races = ("Human")
        character.allowed_weapon = ("daggers", "sickles", "spears", "slings", "oil flasks")
        character.allowed_armor = ("leather", "wooden shield")
    
    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Druid."""
        character.tp = wuerfle_1d6("TP", 1) + character.tp_mod
