"""Profession base class module."""
class ProfessionBase:
    """Base class for all professions."""
    def __init__(self, name: str):
        self.name = name

    def apply_profession_dependent_modifiers(self, character):
        """Apply profession-specific modifiers to the character."""
        pass  # will be overridden in subclasses

    def apply_stat_dependent_modifiers(self, character):
        """Apply stat-dependent modifiers to the character."""
        pass  # will be overridden in subclasses

    #def char_ability_wave_hand(self, character):
    #    """Implement the 'Wave Hand' ability for the profession."""
    #    echo_message = f"{character.character_name} waves their hand mysteriously."
    #    print(echo_message) # Placeholder for actual ability implementation
        
