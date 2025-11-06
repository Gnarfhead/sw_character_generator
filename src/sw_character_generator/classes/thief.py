"""Thief profession module."""
from classes.professions import Profession
from functions.role_dice import wuerfle_1d6
from classes.player_enums import Alignments, Races, MainStat


class Thief(Profession):
    """Thief profession class."""
    def __init__(self):
        self.name = "Thief"

    def apply_profession_dependent_modifiers(self, character):
        """Apply thief-specific modifiers to the character."""
        character.tp_dice = 6
        character.main_stats = [MainStat.DEXTERITY]
        character.allowed_alignment = [Alignments.NEUTRAL, Alignments.EVIL]
        character.allowed_races = [Races.HUMAN, Races.HALFLING, Races.ELF, Races.DWARF]
        character.allowed_weapon = "light weapons"
        character.allowed_armor = "light"

    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Thief."""
        character.tp = wuerfle_1d6("TP", 1) + character.tp_mod