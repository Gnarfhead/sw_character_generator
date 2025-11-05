from functions.save_character import save_character
from classes.playerclass import PlayerClass
from classes.fighter import Fighter
from classes.wizard import Wizard
from classes.thief import Thief
from classes.assassin import Assassin

if __name__ == "__main__":

    # Example character creation
    Blubb = PlayerClass(
        player_name="Bert",
        character_name="Hiob the Bold",
        profession=Thief(),
    )
    # Print the character details
    print(Blubb)

    Blubb2 = PlayerClass(   
        player_name= "Anna",
        character_name= "Luna the Wise",
        profession=Wizard(),     
    )
    print(Blubb2)

    # Save the final character data to a JSON file
    save_character(Blubb)
    save_character(Blubb2)
