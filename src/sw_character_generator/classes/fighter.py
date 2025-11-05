"""Fighter profession module."""
from classes.professions import Profession
from functions.role_dice import wuerfle_1d10


class Fighter(Profession):
    """Fighter profession class."""
    def __init__(self):
        self.name = "Fighter"

    def apply_class_modifiers(self, character):
        """Apply fighter-specific modifiers to the character."""
        character.tp_dice = 10
        character.main_stat = "strength"
        character.allowed_weapon = "all"
        character.allowed_armor = "heavy"
    
    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Fighter."""
        character.tp = wuerfle_1d10(1) + character.tp_mod
