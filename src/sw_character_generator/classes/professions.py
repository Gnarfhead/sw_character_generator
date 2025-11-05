"""Profession base class module."""
class Profession:
    def __init__(self, name: str):
        self.name = name

    def apply_class_modifiers(self, character):
        pass  # will be overridden in subclasses
