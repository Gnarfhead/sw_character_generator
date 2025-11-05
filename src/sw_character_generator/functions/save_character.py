import json
import os
from dataclasses import asdict
from functions.create_character import FullCharacter


def save_character(character_data: FullCharacter) -> None:
    """Save the FullCharacter data to a JSON file."""
    print("debug save: ", character_data.character.character_name)
    hero_name = character_data.character.character_name
    #print(f"Saving character: {hero_name}")
    filename = f"{hero_name}.json"
    #print(f"Filename: {filename}")
    path = os.path.join("saved_data", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(asdict(character_data), f, indent=4)
    print(f"File saved at: {path}")
