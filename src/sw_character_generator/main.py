from functions.save_character import save_character
from classes.playerclass import PlayerClass
from classes.fighter import Fighter
from classes.wizard import Wizard
from classes.thief import Thief
from functions.role_dice import wuerfle_1d6, wuerfle_3d6, wuerfle_1d4, wuerfle_1d8, wuerfle_1d10, wuerfle_1d12, wuerfle_1d20, wuerfle_1d100

if __name__ == "__main__":

    Blubb = PlayerClass(
        player_name="Bert",
        character_name="Hiob the Bold",
        profession=Fighter(),
        coins=100
    )

    print("Wurf 1d6:", wuerfle_1d6(1))
    print("Wurf 3d6:", wuerfle_3d6(drop_low=1))
    print("Wurf 1d4:", wuerfle_1d4(1))
    print("Wurf 1d8:", wuerfle_1d8(1))
    print("Wurf 1d10:", wuerfle_1d10(1))
    print("Wurf 1d12:", wuerfle_1d12(1))
    print("Wurf 1d20:", wuerfle_1d20(1))
    print("Wurf 1d100:", wuerfle_1d100(1))

    print(Blubb)


    # Save the final character data to a JSON file
    save_character(Blubb)
