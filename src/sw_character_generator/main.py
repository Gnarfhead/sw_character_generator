from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.functions.choosen_profession import choosen_profession_modifiers
from sw_character_generator.functions.choosen_race import choosen_race_modifiers
from sw_character_generator.functions.choosen_alignment import choosen_alignment_modifiers  
from sw_character_generator.functions.save_character import save_character


def main():

    # Roll Character

    Blubb = PlayerClass(
        player_name="Test Player",
        character_name="Aragorn",
        gender="Male",
        age=30,
    )
    
    # Choose profession
    choosen_profession_modifiers(Blubb, "Thief")

    # Choose race
    choosen_race_modifiers(Blubb, "Human")

    # Choose alignment
    choosen_alignment_modifiers(Blubb, "evil")

    print(Blubb.__repr__())
    save_character(Blubb)


if __name__ == "__main__":
    main()