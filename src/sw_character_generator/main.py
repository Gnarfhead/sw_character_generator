from sw_character_generator.classes.playerclass import PlayerClass




def main():

    
    character = PlayerClass(
        player_name="Test Player",
        character_name="Aragorn",
        profession="ranger",
        race="human",
        alignment="good"
    )
    print(character)

if __name__ == "__main__":
    main()