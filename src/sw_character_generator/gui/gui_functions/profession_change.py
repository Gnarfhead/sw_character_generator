"""Callback when profession_var changes; update model profession accordingly."""
from sw_character_generator.functions.choosen_profession import choosen_profession_modifiers

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
        choosen_profession_modifiers(app.new_player, name)        
        app.status_var.set(f"Profession changed to {name}")
        app.race_cb.config(state="normal")
        app.lbl_race.config(style="Attention.TLabel")
        app.lbl_profession.config(style="Standard.TLabel")
        refresh_race_values(app)
        app.update_view_from_model()
    except Exception as e:
        app.status_var.set(f"DEBUG on_profession_change: Error updating profession: {e}")
        print(f"DEBUG on_profession_change: Profession change error: {e}")

def refresh_race_values(app):
    """Refresh the race combobox values based on the new player's allowed races."""
    app.race_cb.config(values=list(getattr(app.new_player, "allowed_races", ())))
    print(f"DEBUG refresh_race_values: Updated race combobox values to {app.race_cb['values']}")

# call this from your profession-change handler after updating self.new_player
    #self.refresh_race_values()