import json
import os
from dataclasses import asdict
from classes.playerclass import PlayerClass


def save_character(character_data: PlayerClass) -> None:
    """Save the Character data to a JSON file."""
    data = character_data.to_dict()
    filename = f"{data['character_name']}.json"
    path = os.path.join("saved_data", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        
    print(f"File saved at: {path}")
    