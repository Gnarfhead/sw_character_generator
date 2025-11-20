"""Save character data to a JSON file with a timestamped filename."""
import json
import os
from datetime import datetime
from src.sw_character_generator.classes.playerclass import PlayerClass


def save_character(character_data: PlayerClass) -> None:
    """Save the Character data to a JSON file."""
    data = character_data.to_dict()

    #print("Current working directory:", os.getcwd())

    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Compose filename
    filename = f"{data['player_name']}-{data['profession']}-{data['character_name']}-{timestamp}.json"
    filename = filename.replace(" ", "_")  # Avoid spaces

    # Prepare path
    path = os.path.join("saved_data", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Save file
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"File saved at: {path}")

def load_character(file_path: str) -> PlayerClass:
    """Load character data from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    try:
        character = PlayerClass.from_dict(data)
    except KeyError as e:
        raise ValueError(f"Missing key in character data: {e}")
    return character
