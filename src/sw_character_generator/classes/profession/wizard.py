"""Wizard profession module."""
from sw_character_generator.classes.profession.profession import ProfessionBase
from sw_character_generator.functions.role_dice import wuerfle_1d4

class Wizard(ProfessionBase):
    """Wizard profession class."""
    def __init__(self):
        self.name = "Wizard"

    def apply_profession_dependent_modifiers(self, character):
        """Apply wizard-specific modifiers to the character."""
        character.tp_dice = 4
        character.main_stats = ("Intelligence",)
        character.allowed_alignment = ("Good", "Neutral", "Evil")
        character.allowed_races = ("Human", "Halfelf", "Elf")
        character.allowed_weapon = ("staff", "dagger")
        character.allowed_armor = ("none",)

    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Wizard."""
        character.tp = wuerfle_1d4("TP", 1) + character.tp_mod