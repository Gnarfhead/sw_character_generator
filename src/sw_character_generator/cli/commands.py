from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.functions.choosen_alignment import choosen_alignment_modifiers
from sw_character_generator.functions.choosen_profession import choosen_profession_modifiers
from sw_character_generator.functions.choosen_race import choosen_race_modifiers
from sw_character_generator.functions.save_character import save_character


def start_cli():
    print("Willkommen zur CLI des Charaktergenerators!")
    # Hier weitere Interaktion oder Argument-Parsing ergänzen


    # Roll Character
    player_character = PlayerClass(
        player_name = str(input("Please enter your player name: ")),
        character_name = str(input("Please enter your character name: ")),
        gender = str(input("Please enter your gender: ")),
        age = int(input("Please enter your age: ")),
        god = str(input("Please enter your god: "))
    )
    print(f"Character {player_character.character_name} created for player {player_character.player_name}.")
    
    
    # Choose profession
    print("Choose your profession:")
    print(" Assassin\n Cleric\n Druid\n Fighter\n Monk\n Paladin\n Ranger\n Thierf\n Wizard\n")
    choosen_profession_modifiers(player_character, input("Please enter your profession: "))
    print("\n")

    # Choose race
    print(f"Choose your race:")
    print(f"{player_character.allowed_races}\n")
    choosen_race_modifiers(player_character, input("Please enter your race: "))
    print("\n")

    # Choose alignment
    print(f"Choose your alignment:")
    print(f"{player_character.allowed_alignment}\n")
    choosen_alignment_modifiers(player_character, input("Please enter your alignment: "))
    print("\n")

    print(player_character)
    #save_character(player_character)
