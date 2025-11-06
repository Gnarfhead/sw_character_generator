"""Fighter profession module."""
from classes.professions import Profession
from functions.role_dice import wuerfle_1d10
from classes.player_enums import AllowedAlignments, AllowedRaces, MainStat



class Fighter(Profession):
    """Fighter profession class."""
    def __init__(self):
        self.name = "Fighter"

    def apply_profession_modifiers(self, character):
        """Apply fighter-specific modifiers to the character."""
        character.tp_dice = 10
        character.main_stats = [MainStat.STRENGTH]
        character.allowed_alignment = [AllowedAlignments.NEUTRAL, AllowedAlignments.EVIL, AllowedAlignments.GOOD]
        character.alowed_races = [AllowedRaces.HUMAN, AllowedRaces.HALFLING, AllowedRaces.ELF, AllowedRaces.DWARF, AllowedRaces.HALFELF ]
        character.allowed_weapon = "all"
        character.allowed_armor = "heavy"
    
    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Fighter."""
        character.tp = wuerfle_1d10(1) + character.tp_mod
