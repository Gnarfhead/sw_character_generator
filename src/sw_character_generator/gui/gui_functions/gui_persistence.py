"""GUI persistence functions: binding GUI variables/widgets to the model."""
from dataclasses import asdict
import tkinter as tk

from sw_character_generator.functions.update_derived_stats import update_derived_stats
from .gui_update_view_from_model import update_view_from_model


def on_var_change(app, field, var):
    """Callback when a GUI variable changes; update the model accordingly."""
    if getattr(app, "is_updating", False): # Prevent recursion
        return
    
    # Ignore changes to derived/calculated fields
    if field in ("ac_total", "nextlevel", "hp", "hp_current", "save_throw", 
                 "delicate_tasks", "climb_walls", "hear_sounds", "hide_in_shadows",
                 "move_silently", "open_locks", "strength_atck_mod", "strength_damage_mod",
                 "ranged_atck_mod", "ac_mod", "hp_mod", "raise_dead_mod",
                 "max_add_langs", "cap_spec_hirelings", "carry_capacity_mod", "door_crack_mod",
                 "highest_spell_level", "understand_spell", "min_spells_per_level", "max_spells_per_level",
                 "parry", "xp_bonus", "main_stats", "languages", "darkvision"):
        print("DEBUG on_var_change: Ignoring change to derived field", {field})
        return
    
    
    try:
        raw = var.get() # Get raw value from Tk variable
    except tk.TclError:
        # Invalid/incompatible value in Tk variable (e.g. "Common" in IntVar)
        # Refresh from model and bail out
        with app.suppress_updates(): # Prevent recursion
            update_view_from_model(app)
        return

    # Normalize by model field type
    current_val = getattr(app.new_player, field, None) # Current model value

    # If model has numeric, coerce; if coercion fails, ignore change
    if isinstance(current_val, int): # Coerce to int
        try:
            if isinstance(raw, (tuple, list)): # Handle case where raw is a list/tuple
                raw = raw[0] if raw else 0 # Default to 0 if empty
            raw = int(raw) # Coerce to int
        except (ValueError, TypeError): # Coercion failed
            return
    elif isinstance(current_val, float): # Coerce to float
        try:
            if isinstance(raw, (tuple, list)): # Handle case where raw is a list/tuple
                raw = raw[0] if raw else 0.0 # Default to 0.0 if empty
            raw = float(raw) # Coerce to float
        except (ValueError, TypeError): # Coercion failed
            return

    # Only update if value actually changed
    if current_val == raw:
        print(f"DEBUG on_var_change: No change for {field}, skipping update")
        return

    setattr(app.new_player, field, raw) # Update model field

    # Recalculate derived stats if stat fields changed
    if field.startswith("stat_") or field in ("ac_mod_temp",):
        print("DEBUG on_var_change: updating derived stats due to change in", field)
        update_derived_stats(app.new_player, app)
    else:
        print("DEBUG on_var_change: no derived stats update needed for change in", field)
        with app.suppress_updates(): # Prevent recursion
            update_view_from_model(app)



def bind_model_vars(app):
    """Bind GUI variables/widgets back to the model."""
    for field in asdict(app.new_player).keys(): # Iterate over model fields
        var = getattr(app, f"{field}_var", None) # Get corresponding Tk variable
        if var is None: # No corresponding Tk variable; skip
            continue # Skip if no corresponding Tk variable
        var.trace_add("write", lambda *a, f=field, v=var: on_var_change(app, f, v)) # Bind variable change to callback
