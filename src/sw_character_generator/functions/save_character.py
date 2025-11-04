import json, os

def save_character(character_data: dict):
    
    filename = f"{character_data['character_name']}.json"
    path = os.path.join("saved_data", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(character_data, f, indent=4)
    print(f"File saved at: {path}")
