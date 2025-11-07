from sw_character_generator.classes.player_enums import Alignments, Professions, Races
from sw_character_generator.functions.save_character import save_character
from sw_character_generator.classes.playerclass import PlayerClass

import argparse
import enum as _enum
from typing import Any, Optional

# Die GUI-Funktion importieren (wird im feature-Branch hinzugefügt)
try:
    from sw_character_generator.gui import launch_gui
except Exception:
    launch_gui = None  # type: ignore


def _to_enum(target_enum: Any, value: Any) -> Optional[_enum.Enum]:
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


def _choose_from_enum(enum_cls: Any, prompt: str) -> Any:
    """
    Interaktives CLI-Auswahlmenü für Enum-Werte.
    Gibt das ausgewählte Enum-Mitglied zurück.
    """
    members = list(enum_cls)
    # Anzeige (nummeriert)
    print(f"\n{prompt}")
    for idx, m in enumerate(members, start=1):
        label = getattr(m, "value", None) or m.name
        print(f"  {idx}) {label}")
    while True:
        sel = input("Wähle eine Zahl oder gib den Namen ein: ").strip()
        if not sel:
            print("Bitte eine Auswahl treffen.")
            continue
        # Zahl?
        if sel.isdigit():
            i = int(sel)
            if 1 <= i <= len(members):
                return members[i - 1]
            print("Ungültige Zahl.")
            continue
        # Name oder value versuchen
        # Versuche Name
        try:
            return enum_cls[sel]
        except Exception:
            # Versuche Value match
            for m in members:
                if getattr(m, "value", None) == sel:
                    return m
            print("Ungültige Auswahl, versuche es erneut.")


def _interactive_cli() -> Optional[dict]:
    """
    Fragt per CLI die fünf Parameter ab und bietet an, zu speichern.
    Liefert dict wie launch_gui oder None bei Abbruch.
    """
    try:
        print("Interaktive Charaktererstellung (CLI). Leere Eingabe bricht ab.")
        player_name = input("Player name: ").strip()
        if player_name == "":
            print("Abbruch.")
            return None
        character_name = input("Character name: ").strip()
        if character_name == "":
            print("Abbruch.")
            return None

        race = _choose_from_enum(Races, "Rassen:")
        profession = _choose_from_enum(Professions, "Professionen:")
        alignment = _choose_from_enum(Alignments, "Alignment:")

        # Bestätigung und optionales Speichern
        while True:
            save = input("Charakter speichern? (y/N): ").strip().lower()
            if save in ("y", "yes"):
                try:
                    char = PlayerClass(
                        player_name=player_name,
                        character_name=character_name,
                        race=race,
                        profession=profession,
                        alignment=alignment,
                    )
                    save_character(char)
                    print("Charakter gespeichert.")
                except ValueError as e:
                    print("Fehler bei der Charaktererstellung:", e)
                    return                
                except Exception as e:
                    print("Fehler beim Speichern:", e)
                break
            if save in ("", "n", "no"):
                print("Nicht gespeichert.")
                break
            print("Bitte 'y' oder 'n' eingeben.")

        return {
            "player_name": player_name,
            "character_name": character_name,
            "race": race,
            "profession": profession,
            "alignment": alignment,
        }
    except (KeyboardInterrupt, EOFError):
        print("\nAbbruch.")
        return None


def main():
    parser = argparse.ArgumentParser(description="sw_character_generator")
    parser.add_argument("--gui", action="store_true", help="Starte die Tkinter-GUI für die Charaktererstellung")
    parser.add_argument("--cli", action="store_true", help="Starte die interaktive CLI für die Charaktererstellung")
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

        try:
            char = PlayerClass(
                player_name=player_name,
                character_name=character_name,
                race=race_enum,
                profession=prof_enum,
                alignment=align_enum,
            )
        except ValueError as e:
            print("Fehler bei der Charaktererstellung:", e)
            return    
        print(char)
        # In GUI-Version ruft die GUI bereits save_character beim Klick auf Save auf,
        # hier speichern wir zusätzlich, falls GUI nur Werte zurückliefert aber nicht gespeichert hat.
        try:
            save_character(char)
            print("Charakter gespeichert.")
        except Exception as e:
            print("Fehler beim Speichern:", e)
        return

    if args.cli:
        params = _interactive_cli()
        if params is None:
            return
        # Falls CLI schon gespeichert hat, ist das fine; wir geben die Werte aus.
        print("Eingaben:", params)
        return

print("Bitte --gui oder --cli angeben.")


if __name__ == "__main__":
    main()