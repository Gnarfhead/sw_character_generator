"""Profession base class module."""
class Profession:
    """Base class for all professions."""
    def __init__(self, name: str):
        self.name = name

    """Apply profession-specific modifiers to the character."""
    def apply_profession_dependent_modifiers(self, character):
        pass  # will be overridden in subclasses

    """Apply stat-dependent modifiers to the character."""
    def apply_stat_dependent_modifiers(self, character):
        pass
