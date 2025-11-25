"""Functions for character handling: save, load, and create new character."""
from src.sw_character_generator.classes.playerclass import PlayerClass
from src.sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model

def new_characterobj(app):
    """Create a new character object and update the view."""
    print("DEBUG new_characterobj: ----------------------------------------------------------------")
    print("Debug _new_characterobj: Creating new character object.")
    app.new_player = PlayerClass()
    app.rebuild_ui()

def apply_character(app, character: PlayerClass):
    """Apply changes to the character object."""
    print("DEBUG apply_character: ----------------------------------------------------------------")
    print("DEBUG apply_character: Applying changes to character object.")
    character.character_created = True
    app.cb_profession.config(state="disabled")
    app.cb_race.config(state="disabled")
    app.cb_alignment.config(state="disabled")
    app.btn_rollhp.config(state="disabled")
    app.btn_roll_stats.config(state="disabled")
    app.btn_switch_stats.config(state="disabled")
    update_view_from_model(app)