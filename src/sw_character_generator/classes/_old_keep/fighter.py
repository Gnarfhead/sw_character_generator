"""Fighter profession module."""
from sw_character_generator.classes.profession.profession import ProfessionBase
from sw_character_generator.functions.role_dice import wuerfle_1d10

class Fighter(ProfessionBase):
    """Fighter profession class."""
    def __init__(self):
        self.name = "Fighter"

    def apply_profession_dependent_modifiers(self, character):
        """Apply fighter-specific modifiers to the character."""
        character.tp_dice = 10
        character.main_stats = ("Strength",)
        character.allowed_alignment = ("Neutral", "Evil", "Good")
        character.allowed_races = ("Human", "Halfling", "Elf", "Dwarf", "Halfelf")
        character.allowed_weapon = ("all",)
        character.allowed_armor = ("heavy",)
    
    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers for Fighter."""
        character.tp = wuerfle_1d10("TP", 1) + character.tp_mod
