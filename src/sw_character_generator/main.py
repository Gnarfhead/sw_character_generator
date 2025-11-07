from sw_character_generator.classes.player_enums import Alignments, Professions, Races
from sw_character_generator.functions.save_character import save_character
from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.classes.profession.fighter import Fighter
from sw_character_generator.classes.profession.wizard import Wizard
from sw_character_generator.classes.profession.thief import Thief
from sw_character_generator.classes.profession.assassin import Assassin
from sw_character_generator.classes.race.elf import Elf
from sw_character_generator.classes.race.halfling import Halfling

import argparse
import enum as _enum
from typing import Any

# Die GUI-Funktion importieren (wird im feature-Branch hinzugefügt)
try:
    from sw_character_generator.gui import launch_gui
except Exception:
    launch_gui = None  # type: ignore


def _to_enum(target_enum: Any, value: Any):
    """
    Versucht, `value` in ein Mitglied von `target_enum` zu überführen.
    Akzeptiert:
    - bereits ein Mitglied von target_enum -> Rückgabe direkt
    - ein Enum anderer Klasse mit gleichem .name -> mappt auf target_enum[.name]
    - ein String -> versucht zuerst target_enum[name], ansonsten match über .value
    Gibt None zurück, wenn value None ist.
    Werft ValueError bei Mismatch.
    """
    if value is None:
        return None
    # bereits das richtige Enum-Mitglied
    if isinstance(value, target_enum):
        return value
    # andere Enum-Klasse mit passendem Namen
    if isinstance(value, _enum.Enum):
        name = value.name
        try:
            return target_enum[name]
        except Exception:
            pass
    # String: versuche Name dann Value
    if isinstance(value, str):
        try:
            return target_enum[value]
        except Exception:
            for member in target_enum:
                if getattr(member, "value", None) == value:
                    return member
    raise ValueError(f"Kann {value!r} nicht in {target_enum} umwandeln.")


def main():
    parser = argparse.ArgumentParser(description="sw_character_generator")
    parser.add_argument("--gui", action="store_true", help="Starte die Tkinter-GUI für die Charaktererstellung")
    args = parser.parse_args()

    if args.gui:
        if launch_gui is None:
            print("GUI ist nicht verfügbar (sw_character_generator.gui nicht gefunden).")
            return

        params = launch_gui()
        if params is None:
            print("GUI abgebrochen.")
            return

        # player_name / character_name sind Strings
        player_name = params.get("player_name", "").strip()
        character_name = params.get("character_name", "").strip()

        # race/profession/alignment in die Projekt-Enums konvertieren
        try:
            race_enum = _to_enum(Races, params.get("race"))
        except ValueError as e:
            print("Warnung: Race konnte nicht geparst werden:", e)
            race_enum = None

        try:
            prof_enum = _to_enum(Professions, params.get("profession"))
        except ValueError as e:
            print("Warnung: Profession konnte nicht geparst werden:", e)
            prof_enum = None

        try:
            align_enum = _to_enum(Alignments, params.get("alignment"))
        except ValueError as e:
            print("Warnung: Alignment konnte nicht geparst werden:", e)
            align_enum = None

        char = PlayerClass(
            player_name=player_name,
            character_name=character_name,
            race=race_enum,
            profession=prof_enum,
            alignment=align_enum,
        )
        print(char)
        save_character(char)
        return


if __name__ == "__main__":
    main()