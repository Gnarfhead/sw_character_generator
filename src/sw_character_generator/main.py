from functions.save_character import save_character
from classes.playerclass import PlayerClass
from classes.fighter import Fighter
from classes.wizard import Wizard
from classes.thief import Thief
from classes.assassin import Assassin
from classes.player_enums import Races

if __name__ == "__main__":

    # Example character creation
    Blubb = PlayerClass(
        player_name="Bert",
        character_name="Hiob the Bold",
        race=Races.HALFLING,
        profession=Thief(),
    )
    # Print the character details
    print(Blubb)

    Blubb2 = PlayerClass(
        player_name="Anna",
        character_name="Luna the Wise",
        race=Races.ELF,
        profession=Wizard()     
    )
    print(Blubb2)

    Blubb3 = PlayerClass(
        player_name="Eddy",
        character_name="Gilbert the Swift",
        race=Races.HUMAN,
        profession=Fighter()
    )
    print(Blubb3)

    # Save the final character data to a JSON file
    save_character(Blubb)
    save_character(Blubb2)
    save_character(Blubb3)
