"""Main module for Swords & Wizardry RPG Character Generator."""

from src.sw_character_generator.classes.playerclass import PlayerClass
from src.sw_character_generator.functions.choosen_profession import choosen_profession_modifiers
from src.sw_character_generator.functions.choosen_race import choosen_race_modifiers
from src.sw_character_generator.functions.choosen_alignment import choosen_alignment_modifiers
from src.sw_character_generator.functions.save_character import save_character
import sys


def main():
    """Main function to run the character generator."""

    if len(sys.argv) == 1 or (len(sys.argv) > 1 and sys.argv[1] == '-gui'):
        from sw_character_generator.gui.app import start_gui
        start_gui()
    elif len(sys.argv) > 1 and sys.argv[1] == '-cli':
        from sw_character_generator.cli.commands import start_cli
        start_cli()
    else:
        print("Unbekannter Parameter! Benutze keine Parameter, '-gui', oder '-cli'.")


if __name__ == "__main__":
    main()
