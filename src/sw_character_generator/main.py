from dataclasses import make_dataclass, asdict
from classes.character import Character
from classes.fighter import Fighter
from functions.save_character import save_character

if __name__ == "__main__":

    # Create instances of Character and Fighter
    player_character = Character(player_name="Alice", character_name="Thorin")
    player_class = Fighter(player_class="Fighter")

    # Merging character and class data into a final character representation
    merged_character = asdict(player_character) | asdict(player_class)
    final_player_character = make_dataclass("final_player_character", merged_character.keys())
    final_character_instance = final_player_character(**merged_character)
    print(asdict(final_character_instance))

    # Save the final character data to a JSON file
    save_character(asdict(final_character_instance))



