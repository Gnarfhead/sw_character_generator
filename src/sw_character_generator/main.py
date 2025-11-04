from dataclasses import make_dataclass, asdict
from classes.character import Character
from classes.fighter import Fighter
from functions.save_character import save_character

if __name__ == "__main__":

    # Create instances of Character and Fighter
    player_character = Character(playerName="Alice", characterName="Thorin")
    player_class = Fighter(playerClass="Fighter")

    # Merging character and class data into a final character representation
    merged_character = asdict(player_character) | asdict(player_class)
    FinalPlayerCharacter = make_dataclass("FinalPlayerCharacter", merged_character.keys())
    final_character_instance = FinalPlayerCharacter(**merged_character)
    print(asdict(final_character_instance))

    # Save the final character data to a JSON file
    save_character(asdict(final_character_instance))



