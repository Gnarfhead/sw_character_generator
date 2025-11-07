"""Paladin profession module."""
from sw_character_generator.classes.profession.profession import ProfessionBase
from sw_character_generator.functions.role_dice import wuerfle_1d8
from sw_character_generator.classes.player_enums import Alignments, Races, MainStats



class Paladin(ProfessionBase):
    """Paladin profession class."""
    def __init__(self):
        self.name = "Paladin"

    def apply_profession_dependent_modifiers(self, character):
        """Apply paladin-specific modifiers to the character."""
        character.tp_dice = 8
        character.main_stats = [MainStats.STRENGTH]
        character.allowed_alignment = [Alignments.GOOD]
        character.allowed_races = [Races.HUMAN]
        character.allowed_weapon = "all"
        character.allowed_armor = "all"
    
    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Paladin."""
        character.tp = wuerfle_1d8("TP", 1) + character.tp_mod
