"""CLI commands for the Swords & Wizardry character generator."""
from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.functions.choosen_alignment import choosen_alignment_modifiers
from sw_character_generator.functions.choosen_profession import choosen_profession_modifiers
from sw_character_generator.functions.choosen_race import choosen_race_modifiers
from sw_character_generator.functions.role_dice import wuerfle_3d6
from sw_character_generator.functions.save_character import save_character


def start_cli():
    """Start the CLI for the character generator."""
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
    
    # Roll attributes
    print("Rolling attributes...")
    player_character.stat_str = wuerfle_3d6(str_desc="Strength")
    player_character.stat_dex = wuerfle_3d6(str_desc="Dexterity")
    player_character.stat_con = wuerfle_3d6(str_desc="Constitution")
    player_character.stat_int = wuerfle_3d6(str_desc="Intelligence")
    player_character.stat_wis = wuerfle_3d6(str_desc="Wisdom")
    player_character.stat_cha = wuerfle_3d6(str_desc="Charisma")
    print("\n")
    
    # Choose profession
    print("Choose your profession:")
    print(" Assassin\n Cleric\n Druid\n Fighter\n Monk\n Paladin\n Ranger\n Thief\n Wizard\n")
    profession_input = str(input("Please enter your profession: "))
    choosen_profession_modifiers(player_character, profession_input)
    print("\n")

    # Choose race
    print("Choose your race:")
    print(f"{player_character.allowed_races}\n")
    race_input = str(input("Please enter your race: "))
    choosen_race_modifiers(player_character, race_input)
    print("\n")

    # Choose alignment
    print("Choose your alignment:")
    print(f"{player_character.allowed_alignment}\n")
    alignment_input = str(input("Please enter your alignment: "))
    choosen_alignment_modifiers(player_character, alignment_input)
    print("\n")

    # Final character output
    print(player_character)

    #save_character(player_character)
    print("Do you want to save your character? (y/n)")
    if input().lower() == 'y':
        save_character(player_character)
        print("Character saved.")
    elif input().lower() == 'n':
        print("Character not saved.")
    else:
        print(f"Invalid input: {input()} - Character not saved.")

    print("Thank you for using the Swords & Wizardry character generator CLI!")
