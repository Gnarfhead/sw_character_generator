from functions.create_character import create_character
from functions.save_character import save_character

if __name__ == "__main__":

    testcharacter = {
        "player_name": "Alice",
        "character_name": "Thorin"
        }
    
    testcharacterclass = {
        "player_class": "Fighter"
    }

    Bob = create_character(testcharacter, testcharacterclass)
    #print("Bob: ", Bob)

    # Save the final character data to a JSON file
    save_character(Bob)



