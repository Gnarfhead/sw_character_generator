import json
import os
from datetime import datetime
from classes.playerclass import PlayerClass


def save_character(character_data: PlayerClass) -> None:
    """Save the Character data to a JSON file."""
    data = character_data.to_dict()
    
    # Zeitstempel erzeugen
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Dateiname zusammensetzen
    filename = f"{data['player_name']}-{data['profession']}-{data['character_name']}-{timestamp}.json"
    filename = filename.replace(" ", "_")  # Leerzeichen vermeiden

    # Pfad vorbereiten
    path = os.path.join("saved_data", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Datei speichern
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        
    print(f"File saved at: {path}")
    