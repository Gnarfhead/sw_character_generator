"""Fighter profession module."""
from classes.professions import Profession
from functions.role_dice import wuerfle_1d10
from classes.player_enums import Alignments, Races, MainStat



class Fighter(Profession):
    """Fighter profession class."""
    def __init__(self):
        self.name = "Fighter"

    def apply_profession_dependent_modifiers(self, character):
        """Apply fighter-specific modifiers to the character."""
        character.tp_dice = 10
        character.main_stats = [MainStat.STRENGTH]
        character.allowed_alignment = [Alignments.NEUTRAL, Alignments.EVIL, Alignments.GOOD]
        character.allowed_races = [Races.HUMAN, Races.HALFLING, Races.ELF, Races.DWARF, Races.HALFELF]
        character.allowed_weapon = "all"
        character.allowed_armor = "heavy"
    
    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Fighter."""
        character.tp = wuerfle_1d10("TP", 1) + character.tp_mod
