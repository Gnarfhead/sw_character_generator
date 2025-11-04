from dataclasses import dataclass
from classes.character import Character
from classes.fighter import Fighter


@dataclass
class FullCharacter:
    character: Character
    character_class: Fighter

def create_character(character_data: Character, class_data: Fighter) -> FullCharacter:

    #player_character = Character(
    #    character_data['player_name'],
    #    character_data['character_name']
    #)
    
    #player_class = Fighter(class_data['player_class'])

    #return FullCharacter(character=player_character, character_class=player_class)
    return FullCharacter(character=character_data, character_class=class_data)

    