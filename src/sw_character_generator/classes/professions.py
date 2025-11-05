"""Profession base class module."""
class Profession:
    """Base class for all professions."""
    def __init__(self, name: str):
        self.name = name

    """Apply class-specific modifiers to the character."""
    def apply_class_modifiers(self, character):
        pass  # will be overridden in subclasses

    """Apply stat-dependent modifiers to the character."""
    def apply_stat_dependent_modifiers(self, character):
        pass
