import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass
from typing import Optional, Dict, Any, Type, List
import enum as _enum

# Importiere die Enums aus dem vorhandenen Modul.
# Erwartete Namen in repo: Races, Professions, Alignments.
try:
    from sw_character_generator.classes.player_enums import Races, Professions, Alignments
except Exception as exc:
    raise ImportError(
        "Konnte die Enums Races, Professions, Alignments aus "
        "sw_character_generator.classes.player_enums nicht importieren. "
        "Bitte prüfe die Modul- und Klassennamen."
    ) from exc

@dataclass
class CharacterParams:
    player_name: str = ""
    character_name: str = ""
    race: Optional[Races] = None
    profession: Optional[Professions] = None
    alignment: Optional[Alignments] = None


def enum_values(enum_cls: Type[_enum.Enum]) -> List[str]:
    """
    Liefert die darstellbaren Strings für Combobox:
    - bevorzugt .value wenn vorhanden (und string), sonst .name
    """
    values: List[str] = []
    for member in enum_cls:
        val = getattr(member, "value", None)
        if isinstance(val, str):
            values.append(val)
        else:
            values.append(member.name)
    return values


def parse_enum(enum_cls: Type[_enum.Enum], selected: str) -> _enum.Enum:
    """
    Konvertiert den ausgewählten String zurück in das Enum-Mitglied.
    Erwartet die gleiche Darstellung wie enum_values liefert.
    """
    for member in enum_cls:
        candidate = getattr(member, "value", None)
        if isinstance(candidate, str):
            if candidate == selected:
                return member
        else:
            if member.name == selected:
                return member
    raise ValueError(f"{selected!r} ist kein gültiges Mitglied von {enum_cls}")


class CharacterCreator(tk.Tk):
    """
    Ein einfacher, erweiterbarer Tkinter-Dialog zum Erfassen der Basis-Charakterdaten.
    Verwendung:
      app = CharacterCreator()
      result = app.run()  # result ist ein CharacterParams oder None, wenn abgebrochen
    """

    def __init__(self, initial: Optional[CharacterParams] = None):
        super().__init__()
        self.title("Character Creator")
        self.resizable(False, False)
        self.initial = initial or CharacterParams()
        self.result: Optional[CharacterParams] = None
        self._create_widgets()
        # zentrieren
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws // 2) - (w // 2)
        y = (hs // 3) - (h // 2)
        self.geometry(f"+{x}+{y}")

    def _create_widgets(self):
        pad = {"padx": 8, "pady": 6}

        frame = ttk.Frame(self, padding=10)
        frame.grid(row=0, column=0, sticky="nsew")

        # Player name
        ttk.Label(frame, text="Player name:").grid(row=0, column=0, sticky="w", **pad)
        self.player_var = tk.StringVar(value=self.initial.player_name)
        ttk.Entry(frame, textvariable=self.player_var, width=30).grid(row=0, column=1, **pad)

        # Character name
        ttk.Label(frame, text="Character name:").grid(row=1, column=0, sticky="w", **pad)
        self.char_var = tk.StringVar(value=self.initial.character_name)
        ttk.Entry(frame, textvariable=self.char_var, width=30).grid(row=1, column=1, **pad)

        # Race (aus Enum)
        ttk.Label(frame, text="Race:").grid(row=2, column=0, sticky="w", **pad)
        race_values = enum_values(Races)
        initial_race = ""
        if isinstance(self.initial.race, _enum.Enum):
            initial_race = getattr(self.initial.race, "value", None) or self.initial.race.name
        else:
            initial_race = race_values[0]
        self.race_var = tk.StringVar(value=initial_race)
        race_cb = ttk.Combobox(frame, textvariable=self.race_var, values=race_values, state="readonly", width=28)
        race_cb.grid(row=2, column=1, **pad)

        # Profession (aus Enum)
        ttk.Label(frame, text="Profession:").grid(row=3, column=0, sticky="w", **pad)
        prof_values = enum_values(Professions)
        initial_prof = ""
        if isinstance(self.initial.profession, _enum.Enum):
            initial_prof = getattr(self.initial.profession, "value", None) or self.initial.profession.name
        else:
            initial_prof = prof_values[0]
        self.prof_var = tk.StringVar(value=initial_prof)
        prof_cb = ttk.Combobox(frame, textvariable=self.prof_var, values=prof_values, state="readonly", width=28)
        prof_cb.grid(row=3, column=1, **pad)

        # Alignment (aus Enum)
        ttk.Label(frame, text="Alignment:").grid(row=4, column=0, sticky="w", **pad)
        align_values = enum_values(Alignments)
        initial_align = ""
        if isinstance(self.initial.alignment, _enum.Enum):
            initial_align = getattr(self.initial.alignment, "value", None) or self.initial.alignment.name
        else:
            initial_align = align_values[0]
        self.align_var = tk.StringVar(value=initial_align)
        align_cb = ttk.Combobox(frame, textvariable=self.align_var, values=align_values, state="readonly", width=28)
        align_cb.grid(row=4, column=1, **pad)

        # Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=(8, 0))

        save_btn = ttk.Button(btn_frame, text="Save", command=self._on_save)
        save_btn.grid(row=0, column=0, padx=6)
        cancel_btn = ttk.Button(btn_frame, text="Cancel", command=self._on_cancel)
        cancel_btn.grid(row=0, column=1, padx=6)

        # allow Enter to save, Escape to cancel
        self.bind("<Return>", lambda e: self._on_save())
        self.bind("<Escape>", lambda e: self._on_cancel())

    def _on_save(self):
        try:
            race_member = parse_enum(Races, self.race_var.get())
            prof_member = parse_enum(Professions, self.prof_var.get())
            align_member = parse_enum(Alignments, self.align_var.get())
        except ValueError:
            race_member = None
            prof_member = None
            align_member = None

        self.result = CharacterParams(
            player_name=self.player_var.get().strip(),
            character_name=self.char_var.get().strip(),
            race=race_member,
            profession=prof_member,
            alignment=align_member,
        )
        self.destroy()

    def _on_cancel(self):
        self.result = None
        self.destroy()

    def run(self) -> Optional[CharacterParams]:
        self.mainloop()
        return self.result


def launch_gui(initial: Optional[CharacterParams] = None) -> Optional[Dict[str, Any]]:
    app = CharacterCreator(initial=initial)
    result = app.run()
    if result is None:
        return None
    return {
        "player_name": result.player_name,
        "character_name": result.character_name,
        "race": result.race,
        "profession": result.profession,
        "alignment": result.alignment,
    }