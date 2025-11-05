"""Thief profession module."""
from classes.professions import Profession


class Thief(Profession):
    """Thief profession class."""
    def __init__(self):
        self.name = "Thief"

    def apply_class_modifiers(self, character):
        """Apply thief-specific modifiers to the character."""
        character.tp_dice = 6
        character.main_stat = "dexterity"
        character.allowed_weapon = "light weapons"
        character.allowed_armor = "light"