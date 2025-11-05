from functions.create_character import create_character
from functions.save_character import save_character
from classes.playerclass import Character

if __name__ == "__main__":

    Blubb = Character(
        player_name="Bob",
        character_name="Frodo the Brave",
        player_class="Fighter"
    )


    print(Blubb)

    # Save the final character data to a JSON file
    save_character(Blubb)
