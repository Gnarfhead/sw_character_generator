from sw_character_generator.classes.race.race import Race

class Human(Race):
    """Define Human race class."""
    def __init__(self):
        super().__init__(name="Human")

    # Implement race-specific modifiers
    def apply_race_dependent_modifiers(self, character):
        """Apply Human-specific modifiers to the character."""
        character.darkvision = False
        character.add_langs += ("Menschen",)
