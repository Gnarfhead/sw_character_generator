"""Assassin profession module."""
from sw_character_generator.classes.professions import Profession
from sw_character_generator.functions.role_dice import wuerfle_1d6
from sw_character_generator.classes.player_enums import MainStat, Alignments, Races


class Assassin(Profession):
    """Assassin profession class."""
    def __init__(self):
        self.name = "Assassin"

    def apply_profession_dependent_modifiers(self, character):
        """Apply Assassin-specific modifiers to the character."""
        character.tp_dice = 6
        character.main_stats = [MainStat.STRENGTH, MainStat.DEXTERITY, MainStat.INTELLIGENCE]
        character.allowed_alignment = [Alignments.NEUTRAL, Alignments.EVIL]
        character.allowed_races = [Races.HUMAN]
        character.allowed_weapon = "light weapons"
        character.allowed_armor = "light"

    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Assassin."""
        character.tp = wuerfle_1d6("TP", 1) + character.tp_mod