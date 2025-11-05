"""Assassin profession module."""
from classes.professions import Profession
from functions.role_dice import wuerfle_1d6
from classes.mainstat import MainStat


class Assassin(Profession):

    def __init__(self):
        self.name = "Assassin"

    def apply_class_modifiers(self, character):
        """Apply Assassin-specific modifiers to the character."""
        character.tp_dice = 6
        character.main_stats = [MainStat.STRENGTH, MainStat.DEXTERITY, MainStat.INTELLIGENCE]
        character.allowed_weapon = "light weapons"
        character.allowed_armor = "light"

    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Assassin."""
        character.tp = wuerfle_1d6(1) + character.tp_mod