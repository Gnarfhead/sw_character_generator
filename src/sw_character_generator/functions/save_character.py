import json, os

def save_character(character_data: dict):
    
    """"
    if not isinstance(character_data, dict):
        raise TypeError("character_data muss ein Dictionary sein.")
    if isinstance(character_data, dict):
        print("character_data ist ein Dictionary.")
    """


    hero_name = character_data["character_name"]
    #print(f"Saving character: {hero_name}")
    filename = f"{hero_name}.json"
    #print(f"Filename: {filename}")
    path = os.path.join("saved_data", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(character_data, f, indent=4)
    print(f"File saved at: {path}")
