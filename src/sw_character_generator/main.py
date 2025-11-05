from functions.save_character import save_character
from classes.playerclass import Character
from classes.fighter import Fighter
from classes.wizard import Wizard
from classes.thief import Thief


if __name__ == "__main__":

    Blubb = Character(
        player_name="Bert",
        character_name="Mauser the Sneaky",
        profession=Thief()
    )


    print(Blubb)

    # Save the final character data to a JSON file
    save_character(Blubb)
