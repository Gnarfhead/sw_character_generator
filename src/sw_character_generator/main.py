from sw_character_generator.functions.save_character import save_character
from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.classes.fighter import Fighter
from sw_character_generator.classes.wizard import Wizard
from sw_character_generator.classes.thief import Thief
from sw_character_generator.classes.assassin import Assassin
from sw_character_generator.classes.player_enums import Profession, Races
from sw_character_generator.classes.elf import Elf
from sw_character_generator.classes.halfling import Halfling



if __name__ == "__main__":
    
    # Example of creating a Fighter character
    Blubb2 = PlayerClass(
        player_name="Anna",
        character_name="Luna the Wise",
        race=Halfling(),
        profession=Profession.WIZARD
    )
    print(Blubb2)

    # Save the final character data to a JSON file
    save_character(Blubb2)