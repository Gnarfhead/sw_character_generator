from dataclasses import dataclass
from classes.character import Character
from classes.fighter import Fighter


@dataclass
class FullCharacter:
    """A dataclass that combines Character and Fighter data."""
    character: Character
    character_class: Fighter

def create_character(character_data: Character, class_data: Fighter) -> FullCharacter:
    """Create a FullCharacter instance from Character and Fighter data."""
    return FullCharacter(character=character_data, character_class=class_data)
