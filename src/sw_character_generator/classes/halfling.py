from sw_character_generator.classes.races import Race

class Halfling(Race):
    """Define Halfling race class."""
    def __init__(self):
        super().__init__(name="Halfling")

    # Implement race-specific modifiers
    def apply_race_dependent_modifiers(self, character):
        """Apply Halfling-specific modifiers to the character."""
        character.ranged_atck_mod += 1
        character.save_bonuses += ("Rettungswurf +4 gegen Magie",)
        character.add_langs += ("Halflingisch",)
