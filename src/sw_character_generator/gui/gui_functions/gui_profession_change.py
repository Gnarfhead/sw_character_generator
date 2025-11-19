"""Callback when profession_var changes; update model profession accordingly."""
from sw_character_generator.functions.choosen_profession import choosen_profession_modifiers
from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model

def on_profession_change(app, *args):
    """Handle profession combobox changes."""
    if getattr(app, "is_updating", False):
        print("DEBUG on_profession_change: Profession change ignored due to is_updating flag.")
        return
    name = app.profession_var.get()
    if not name:
        print("DEBUG on_profession_change: No profession selected.")
        return
    try:
        # Update the model with the new profession
        choosen_profession_modifiers(app.new_player, name) # update profession and related stats
        app.status_var.set(f"Profession changed to {name}")
        app.race_cb.config(state="normal") # enable race selection
        app.alignment_cb.config(state="normal") # enable alignment selection
        app.race_var.set("Undefined") # reset if profession gets changed
        app.alignment_var.set("Undefined") # reset if profession gets changed
        app.lbl_profession.config(style="Standard.TLabel")
        app.lbl_race.config(style="Attention.TLabel")
        app.lbl_alignment.config(style="Attention.TLabel")
        refresh_race_values(app) # update race combobox values
        refresh_alignment_values(app) # update alignment combobox values
        update_view_from_model(app) # refresh GUI to reflect model changes
    except Exception as e:
        #app.status_var.set(f"DEBUG on_profession_change: Error updating profession: {e}")
        print(f"DEBUG on_profession_change: Profession change error: {e}")

def refresh_race_values(app):
    """Refresh the race combobox values based on the new player's allowed races."""
    app.race_cb.config(values=list(getattr(app.new_player, "allowed_races", ())))
    print(f"DEBUG refresh_race_values: Updated race combobox values to {app.race_cb['values']}")

def refresh_alignment_values(app):
    """Refresh the alignment combobox values based on the new player's allowed alignments."""
    app.alignment_cb.config(values=list(getattr(app.new_player, "allowed_alignment", ())))
    print(f"DEBUG refresh_alignment_values: Updated alignment combobox values to {app.alignment_cb['values']}")

