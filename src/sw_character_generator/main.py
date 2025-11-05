from functions.save_character import save_character
from classes.playerclass import PlayerClass
from classes.fighter import Fighter
from classes.wizard import Wizard
from classes.thief import Thief

if __name__ == "__main__":

    # Example character creation
    Blubb = PlayerClass(
        player_name="Bert",
        character_name="Hiob the Bold",
        profession=Fighter(),
        coins=100
    )
    # Print the character details
    print(Blubb)

    # Save the final character data to a JSON file
    save_character(Blubb)
