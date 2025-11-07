# (Ausschnitt: CharacterCreator._on_save geändert, komplette Datei zur Klarheit)
import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass
from typing import Optional, Dict, Any, Type, List
import enum as _enum

try:
    from sw_character_generator.classes.player_enums import Races, Professions, Alignments
except Exception as exc:
    raise ImportError(
        "Konnte die Enums Races, Professions, Alignments aus "
        "sw_character_generator.classes.player_enums nicht importieren. "
        "Bitte prüfe die Modul- und Klassennamen."
    ) from exc

try:
    from sw_character_generator.functions.save_character import save_character
    from sw_character_generator.classes.playerclass import PlayerClass
except Exception:
    save_character = None  # type: ignore
    PlayerClass = None  # type: ignore

@dataclass
class CharacterParams:
    player_name: str = ""
    character_name: str = ""
    race: Optional[Races] = None
    profession: Optional[Professions] = None
    alignment: Optional[Alignments] = None

# ... rest of file omitted for brevity; only _on_save shown/changed here:

    def _on_save(self):
        try:
            race_member = parse_enum(Races, self.race_var.get())
            prof_member = parse_enum(Professions, self.prof_var.get())
            align_member = parse_enum(Alignments, self.align_var.get())
        except ValueError as e:
            messagebox.showerror("Invalid selection", f"Ungültige Auswahl: {e}")
            return

        self.result = CharacterParams(
            player_name=self.player_var.get().strip(),
            character_name=self.char_var.get().strip(),
            race=race_member,
            profession=prof_member,
            alignment=align_member,
        )

        # Versuche zuerst, ein PlayerClass-Objekt zu erzeugen, um Validierungen (z.B. allowed combos) zu triggern.
        if PlayerClass is not None:
            try:
                char = PlayerClass(
                    player_name=self.result.player_name,
                    character_name=self.result.character_name,
                    race=self.result.race,
                    profession=self.result.profession,
                    alignment=self.result.alignment,
                )
            except ValueError as e:
                # Zeige dem Nutzer die Fehlermeldung und lass das Fenster offen, damit er korrigieren kann
                messagebox.showerror("Ungültige Kombination", str(e))
                return

            # Wenn save_character verfügbar ist, speichere direkt und bestätige dem Nutzer
            if save_character is not None:
                try:
                    save_character(char)
                    messagebox.showinfo("Saved", "Charakter erfolgreich gespeichert.")
                except Exception as e:
                    messagebox.showerror("Save error", f"Fehler beim Speichern: {e}")
        else:
            # Falls PlayerClass nicht importierbar, nur schließen und liefern
            if save_character is not None:
                try:
                    # Build a minimal representative object or skip saving
                    messagebox.showwarning("Info", "PlayerClass nicht importierbar; Speicherfunktion übersprungen.")
                except Exception:
                    pass

        # Fenster schließen (unabhängig vom Save)
        self.destroy()