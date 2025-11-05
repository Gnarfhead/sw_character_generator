"""Wizard profession module."""
from classes.professions import Profession


class Wizard(Profession):
    """Wizard profession class."""
    def __init__(self):
        self.name = "Wizard"

    def apply_class_modifiers(self, character):
        """Apply wizard-specific modifiers to the character."""
        character.tp_dice = 4
        character.main_stat = "intelligence"
        character.allowed_weapon = "staff, dagger"
        character.allowed_armor = "none"