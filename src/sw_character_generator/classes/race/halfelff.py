from sw_character_generator.classes.race.race import Race

class Halfelf(Race):
    """Define Halfelf race class."""
    def __init__(self):
        super().__init__(name="Halfelf")

    # Implement race-specific modifiers
    def apply_race_dependent_modifiers(self, character):
        """Apply Halfelf-specific modifiers to the character."""
        character.darkvision = True
        character.special_abilities += ("Geheimtüren finden: Aktiv 4:6",)
        character.add_langs += ("Halbelfisch",)
