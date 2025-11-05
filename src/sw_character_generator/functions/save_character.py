import json
import os
from dataclasses import asdict
from classes.playerclass import Character


def save_character(character_data: Character) -> None:
    """Save the Character data to a JSON file."""
    #print("debug save: ", character_data.character_name)
    hero_name = character_data.character_name
    #print(f"Saving character: {hero_name}")
    
    filename = f"{hero_name}.json"
    #print(f"Filename: {filename}")
    path = os.path.join("saved_data", filename)
    
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(asdict(character_data), f, indent=4)
    print(f"File saved at: {path}")
    