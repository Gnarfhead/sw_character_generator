"""CLI commands for the Swords & Wizardry character generator."""
from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.functions.choosen_alignment import choosen_alignment_modifiers
from sw_character_generator.functions.choosen_profession import choosen_profession_modifiers
from sw_character_generator.functions.choosen_race import choosen_race_modifiers
from sw_character_generator.functions.gen_char_stat_mods import analyze_mod_char, analyze_mod_con, analyze_mod_dex, analyze_mod_int, analyze_mod_str
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

    # Roll stats
    print("About to roll character stats. Want to use the homebrew rule of rolling 4d6 and dropping the lowest? (y/n)")
    drop_low_input = input().lower()
    if drop_low_input == 'y':
        drop_low = True
        print("Using homebrew rule: rolling 4d6 and dropping the lowest.\n")
    elif drop_low_input == 'n':
        drop_low = None
        print("Not using homebrew rule: rolling standard 3d6.\n")
    else:
        drop_low = None
        print(f"Invalid input: {drop_low_input} - Not using homebrew rule: rolling standard 3d6.\n")
    

    print("Rolling character stats (3d6 each):\n")    
    player_character.stat_str = wuerfle_3d6(str_desc="Strength", drop_low=drop_low)
    player_character.stat_dex = wuerfle_3d6(str_desc="Dexterity", drop_low=drop_low)
    player_character.stat_con = wuerfle_3d6(str_desc="Constitution", drop_low=drop_low)
    player_character.stat_wis = wuerfle_3d6(str_desc="Wisdom", drop_low=drop_low)
    player_character.stat_int = wuerfle_3d6(str_desc="Intelligence", drop_low=drop_low)
    player_character.stat_char = wuerfle_3d6(str_desc="Charisma", drop_low=drop_low)
    print("\n")

    # Apply stat modifiers
    analyze_mod_str(player_character)
    analyze_mod_dex(player_character)
    analyze_mod_con(player_character)
    analyze_mod_int(player_character)
    analyze_mod_char(player_character)

    # Optional homebrew rule: Switch 2 stats
    print("Optional homebrew rule: Do you want to switch two stats? (y/n)")
    if input().lower() == 'y':
        stat1 = str(input("Enter the first stat to switch (str, dex, con, wis, int, char): "))
        stat2 = str(input("Enter the second stat to switch (str, dex, con, wis, int, char): "))
        temp = getattr(player_character, f'stat_{stat1}')
        setattr(player_character, f'stat_{stat1}', getattr(player_character, f'stat_{stat2}'))
        setattr(player_character, f'stat_{stat2}', temp)
        print(f"Switched {stat1} and {stat2}.\n")
    elif input().lower() == 'n':
        print("No stats switched.\n")
    else:
        print(f"Invalid input: {input()} - No stats switched.\n")
 
    # Roll starting coins
    print("Rolling starting coins (3d6 * 10):")
    player_character.coins = wuerfle_3d6(str_desc="Starting Coins") * 10
    print(f"Starting coins: {player_character.coins}\n")

    # Choose profession
    print("Choose your profession:")
    print(" Assassin\n Cleric\n Druid\n Fighter\n Monk\n Paladin\n Ranger\n Thief\n Wizard\n")
    profession_input = str(input("Please enter your profession: "))
    choosen_profession_modifiers(player_character, profession_input)
    print(f"Modifiers for profession {profession_input} applied.\n")

    # Optional homebrew rule: Get full TPs at level 1
    print("Optional homebrew rule: Do you want to start with max TP at level 1 or roll for it? (y/n)")
    if input().lower() == 'y':
        player_character.tp = player_character.tp_dice + player_character.tp_mod
        print(f"Set TP to full: {player_character.tp}\n")
    elif input().lower() == 'n':
        print(f"TP remains as rolled: {player_character.tp}\n")
    else:
        print(f"Invalid input: {input()} - TP remains as rolled: {player_character.tp}\n")

    # Choose race
    print("Choose your race:")
    print(f"{player_character.allowed_races}\n")
    race_input = str(input("Please enter your race: "))
    choosen_race_modifiers(player_character, race_input)
    print(f"Modifiers for race {race_input} applied.\n")

    # Choose alignment
    print("Choose your alignment:")
    print(f"{player_character.allowed_alignment}\n")
    alignment_input = str(input("Please enter your alignment: "))
    choosen_alignment_modifiers(player_character, alignment_input)
    print(f"Modifiers for alignment {alignment_input} applied.\n")

    # Final character output
    print(player_character)

    #save_character(player_character)
    print("Do you want to save your character? (y/n)")
    if input().lower() == 'y':
        save_character(player_character)
        print("Character saved.\n")
    elif input().lower() == 'n':
        print("Character not saved.\n")
    else:
        print(f"Invalid input: {input()} - Character not saved.\n")

    print("Thank you for using the Swords & Wizardry character generator CLI!\n")
