"""Functions for character handling: save, load, and create new character."""
from src.sw_character_generator.classes.playerclass import PlayerClass

def new_characterobj(app):
    """Create a new character object and update the view."""
    print("Debug _new_characterobj: Creating new character object.")
    app.new_player = PlayerClass()
    app.rebuild_ui()

def apply_character(app, character: PlayerClass):
    """Apply changes to the character object."""
    print("Debug apply_character: Applying changes to character object.")
    # Implementation for applying changes can be added here