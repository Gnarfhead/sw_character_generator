"""Functions for character handling: save, load, and create new character."""

from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model
from sw_character_generator.functions.update_base_stats import update_base_stats
from sw_character_generator.functions.update_derived_stats import update_derived_stats

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
    
    # Mark character as created and disable further modifications
    character.character_created = True # Mark character as created
    app.cb_profession.config(state="disabled") # Disable profession selection
    app.cb_race.config(state="disabled") # Disable race selection
    app.cb_alignment.config(state="disabled") # Disable alignment selection
    app.btn_rollhp.config(state="disabled") # Disable HP rolling
    app.btn_roll_stats.config(state="disabled") # Disable stat rolling
    app.btn_switch_stats.config(state="disabled") # Disable stat switching
    app.btn_apply.config(state="disabled") # Disable apply button after applying
    app.footer_frame.config(style="Standard.TFrame") # Reset footer frame style
    
    # Update derived and base stats
    update_derived_stats(character, app)  # Ensure derived stats are up to date
    update_base_stats(character)  # Update total base stats
    
    # Update the GUI to reflect the applied character
    app.status_var.set("Character applied and locked.") # Update status
    update_view_from_model(app)
