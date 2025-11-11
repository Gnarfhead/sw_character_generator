from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.functions import choosen_alignment, choosen_profession
from sw_character_generator.functions import choosen_race
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