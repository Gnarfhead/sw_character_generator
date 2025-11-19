"""Handle changes to the race selection."""
from sw_character_generator.functions.choosen_race import choosen_race_modifiers
from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model

def on_race_change(app, *args):
    """Handle race combobox changes."""
    if getattr(app, "is_updating", False):
        print("DEBUG on_race_change: Race change ignored due to is_updating flag.")
        return
    name = app.race_var.get()
    if not name:
        print("DEBUG on_race_change: No race selected.")
        return
    try:
        # Update the model with the new race
        choosen_race_modifiers(app.new_player, name) # update race and related stats 
        app.status_var.set(f"Race changed to {name}")
        app.lbl_race.config(style="Standard.TLabel")
        update_view_from_model(app) # refresh GUI to reflect model changes

        # Adjust top_frame style based on race and alignment selection
        print("DEBUG on_race_change: Checking race and alignment for top_frame style adjustment.")
        if app.race_var.get() != "Undefined" and app.alignment_var.get() != "Undefined":
            print("DEBUG on_race_change: app.race_var.get() =", app.race_var.get())
            print("DEBUG on_race_change: app.alignment_var.get() =", app.alignment_var.get())
            app.top_frame.config(style="Standard.TFrame")
            print("DEBUG on_race_change: Both race and alignment are defined; set top_frame to Standard.TFrame")
        else:
            print("DEBUG on_race_change: app.race_var.get() =", app.race_var.get())
            print("DEBUG on_race_change: app.alignment_var.get() =", app.alignment_var.get())
            app.top_frame.config(style="Attention.TFrame")
            print("DEBUG on_race_change: Either race or alignment is undefined; set top_frame to Attention.TFrame")

    except Exception as e:
        #app.status_var.set(f"DEBUG on_race_change: Error updating race: {e}")
        print(f"DEBUG on_race_change: Race change error: {e}")
