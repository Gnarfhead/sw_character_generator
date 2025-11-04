from dataclasses import asdict, make_dataclass
from classes.character import Character
from classes.fighter import Fighter


def create_character(dict_character_data: dict, dict_class_data: dict) -> dict :
    
    """
    if isinstance(dict_character_data, dict):
        print("dict_character_data ist ein Dictionary.")
    if isinstance(dict_class_data, dict):
        print("dict_class_data ist ein Dictionary.")
    """

    # Create instances of Character and Fighter
    player_character = Character(dict_character_data['player_name'], dict_character_data['character_name'])
    player_class = Fighter(dict_class_data['player_class'])

    # Merging character and class data into a final character representation
    merged_character = asdict(player_character) | asdict(player_class)

    """
    if isinstance(merged_character, dict):
        print("merged_character ist ein Dictionary.")
    """
    return merged_character

    