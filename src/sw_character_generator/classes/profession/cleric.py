"""Cleric profession module."""
from sw_character_generator.classes.profession.profession import ProfessionBase
from sw_character_generator.functions.role_dice import wuerfle_1d6
from sw_character_generator.classes.player_enums import Alignments, Races, MainStats



class Cleric(ProfessionBase):
    """Cleric profession class."""
    def __init__(self):
        self.name = "Cleric"

    def apply_profession_dependent_modifiers(self, character):
        """Apply cleric-specific modifiers to the character."""
        character.tp_dice = 6
        character.main_stats = [MainStats.WISDOM]
        character.allowed_alignment = [Alignments.GOOD, Alignments.EVIL]
        character.allowed_races = [Races.HUMAN, Races.HALFELF]
        character.allowed_weapon = "blunt weapons"
        character.allowed_armor = "all"
    
    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Cleric."""
        character.tp = wuerfle_1d6("TP", 1) + character.tp_mod
