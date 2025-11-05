"""Fighter profession module."""
from classes.professions import Profession


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
