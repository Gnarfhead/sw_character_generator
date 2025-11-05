from functions.create_character import create_character
from functions.save_character import save_character
from classes.character import Character
from classes.fighter import Fighter

if __name__ == "__main__":

    testcharacter = Character(
        player_name="Bob",
        character_name="Frodo the Brave"
    )

    testcharacterclass = Fighter(
        player_class="Fighter"
    )

    Blubb = create_character(testcharacter, testcharacterclass)
    print(Blubb)

    # Save the final character data to a JSON file
    #save_character(Blubb)
