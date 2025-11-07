"""Ranger profession module."""
from sw_character_generator.classes.profession.profession import ProfessionBase
from sw_character_generator.functions.role_dice import wuerfle_1d8
from sw_character_generator.classes.player_enums import Alignments, Races, MainStats



class Ranger(ProfessionBase):
    """Ranger profession class."""
    def __init__(self):
        self.name = "Ranger"

    def apply_profession_dependent_modifiers(self, character):
        """Apply ranger-specific modifiers to the character."""
        character.tp_dice = 8
        character.main_stats = [MainStats.STRENGTH]
        character.allowed_alignment = [Alignments.GOOD]
        character.allowed_races = [Races.HUMAN]
        character.allowed_weapon = "all"
        character.allowed_armor = "all"
    
    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Ranger."""
        character.tp = wuerfle_1d8("TP", 2) + character.tp_mod
