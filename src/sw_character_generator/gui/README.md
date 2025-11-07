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

Save-Verhalten:
- Der "Save"-Button erstellt ein PlayerClass-Objekt und ruft `save_character` auf,
  sofern die entsprechenden Module im PYTHONPATH verfügbar sind. Es wird eine
  Messagebox mit Erfolg/Fehler angezeigt.

Testen:
- PYTHONPATH=src python -m sw_character_generator.main --gui
```