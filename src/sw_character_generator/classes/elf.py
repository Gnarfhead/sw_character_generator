from sw_character_generator.classes.races import Race

class Elf(Race):
    """Define Elf race class."""
    def __init__(self):
        super().__init__(name="Elf")

    # Implement race-specific modifiers
    def apply_race_dependent_modifiers(self, character):
        """Apply Elf-specific modifiers to the character."""
        character.darkvision = True
        character.special_abilities += ("Geheimtüren finden: Aktiv 4:6, Passiv:1:6",)
        character.immunity += ("Ghulische Lähmung",)
        character.add_langs += ("Elbisch",)
