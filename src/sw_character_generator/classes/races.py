"""Race base class module."""
class Race:
    """Base class for all races."""
    def __init__(self, name: str):
        self.name = name

    """Apply race-specific modifiers to the character."""
    def apply_race_dependent_modifiers(self, character):
        pass  # will be overridden in subclasses

