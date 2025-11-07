from sw_character_generator.functions.save_character import save_character
from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.classes.profession.fighter import Fighter
from sw_character_generator.classes.profession.wizard import Wizard
from sw_character_generator.classes.profession.thief import Thief
from sw_character_generator.classes.profession.assassin import Assassin
from sw_character_generator.classes.player_enums import Professions, Races
from sw_character_generator.classes.race.elf import Elf
from sw_character_generator.classes.race.halfling import Halfling
from sw_character_generator.classes.profession.profession import ProfessionBase



if __name__ == "__main__":
    
    # Example of creating a Fighter character
    Blubb2 = PlayerClass(
        player_name="Anna",
        character_name="Luna the Wise",
        race=Halfling(),
        profession=Wizard()
    )
    print(Blubb2)
    #Blubb2.profession.char_ability_wave_hand(Blubb2)

    # Save the final character data to a JSON file
    save_character(Blubb2)