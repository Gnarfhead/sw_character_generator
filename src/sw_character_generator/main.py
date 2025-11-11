from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.functions.choosen_profession import choosen_profession
from sw_character_generator.functions.choosen_race import choosen_race
from sw_character_generator.functions.choosen_alignment import choosen_alignment    
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
    choosen_profession(PlayerClass, "Paladin")

    # Choose race
    choosen_race(PlayerClass, "Human")

    # Choose alignment
    choosen_alignment(PlayerClass)

    save_character(Blubb)


if __name__ == "__main__":
    main()