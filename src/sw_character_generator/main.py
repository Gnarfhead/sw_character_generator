from functions.save_character import save_character
from classes.playerclass import PlayerClass
from classes.fighter import Fighter
from classes.wizard import Wizard
from classes.thief import Thief
from classes.assassin import Assassin
from classes.player_enums import Races
from classes.elf import Elf
from classes.halfling import Halfling


if __name__ == "__main__":

 

    Blubb2 = PlayerClass(
        player_name="Anna",
        character_name="Luna the Wise",
        race=Halfling(),
        profession=Wizard() 
    )
    print(Blubb2)



    # Save the final character data to a JSON file
    save_character(Blubb2)

