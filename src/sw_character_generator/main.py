"""Main module for Swords & Wizardry RPG Character Generator."""

from src.sw_character_generator.classes.playerclass import PlayerClass
from src.sw_character_generator.functions.choosen_profession import choosen_profession_modifiers
from src.sw_character_generator.functions.choosen_race import choosen_race_modifiers
from src.sw_character_generator.functions.choosen_alignment import choosen_alignment_modifiers
from src.sw_character_generator.functions.save_character import save_character


def main():
    """Main function to run the character generator."""

    # Roll Character
    blubb = PlayerClass(
        player_name="Test Player",
        character_name="Aragorn",
        gender="Male",
        age=30,
    )
    # Choose profession
    choosen_profession_modifiers(blubb, "Thief")

    # Choose race
    choosen_race_modifiers(blubb, "Dwarf")

    # Choose alignment
    choosen_alignment_modifiers(blubb, "evil")

    print(blubb.__repr__())
    save_character(blubb)


if __name__ == "__main__":
    main()
