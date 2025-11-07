```markdown
# GUI (Tkinter) — sw_character_generator

Diese GUI ist ein erster, einfacher Dialog zum Erfassen von:
- player_name
- character_name
- race (Enum)
- profession (Enum)
- alignment (Enum)

Wichtig:
- Die Dropdowns nutzen die Enums aus `sw_character_generator.classes.player_enums`.
  Erwartete Klassennamen: `Races`, `Professions`, `Alignments`.
  Falls eure Enums andere Namen haben, passe `app.py` entsprechend an.

Dateien:
- src/sw_character_generator/gui/app.py: Haupt-UI + `launch_gui()` Funktion
- src/sw_character_generator/gui/__init__.py: Package-Export

Integration:
- Importiere `launch_gui` und nutze das zurückgelieferte dict, z.B.:

```python
from sw_character_generator.gui import launch_gui

params = launch_gui()
if params is None:
    print("GUI abgebrochen.")
else:
    # player_name, character_name sind strings
    # race, profession, alignment sind Enum-Mitglieder aus player_enums
    print(params["player_name"], params["race"])
```

Testen:
- PYTHONPATH=src python -m sw_character_generator.main --gui
```