from sw_character_generator.classes.race.race import Race

class Dwarf(Race):
    """Define Dwarf race class."""
    def __init__(self):
        super().__init__(name="Dwarf")

    # Implement race-specific modifiers
    def apply_race_dependent_modifiers(self, character):
        """Apply Dwarf-specific modifiers to the character."""
        character.darkvision = True
        character.special_abilities += ("Stonecunning", "Saving throw bonus against magic +4",)
        character.add_langs += ("Dwarvish",)
