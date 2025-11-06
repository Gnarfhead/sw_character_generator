"""Wizard profession module."""
from classes.professions import Profession
from functions.role_dice import wuerfle_1d4
from classes.player_enums import AllowedAlignments, AllowedRaces, MainStat


class Wizard(Profession):
    """Wizard profession class."""
    def __init__(self):
        self.name = "Wizard"

    def apply_profession_modifiers(self, character):
        """Apply wizard-specific modifiers to the character."""
        character.tp_dice = 4
        character.main_stats = [MainStat.INTELLIGENCE]
        character.allowed_alignment = [AllowedAlignments.NEUTRAL, AllowedAlignments.EVIL]
        character.alowed_races = [AllowedRaces.HUMAN, AllowedRaces.HALFELF, AllowedRaces.ELF]
        character.allowed_weapon = "staff, dagger"
        character.allowed_armor = "none"

    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Wizard."""
        character.tp = wuerfle_1d4(1) + character.tp_mod