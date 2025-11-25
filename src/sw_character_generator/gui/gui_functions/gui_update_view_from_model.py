"""Update view from model function."""
import tkinter as tk
from dataclasses import asdict, fields



def _format_change_mainstats(value):
    """Format main_stats tuple into a readable string."""
    if isinstance(value, (tuple, list, set)): # Tuple, Liste or Set
        return ", ".join(str(v) for v in value) # Join elements with commas
    if isinstance(value, dict): # Dict
        return ", ".join(f"{k}={v}" for k, v in value.items()) # Key=Value pairs
    return str(value) # Fallback to string conversion



def update_view_from_model(app):
    """Safely copy model fields into Tkinter variables, normalizing types."""
    print("DEBUG update_view_from_model: ----------------------------------------------------------------")
    print("DEBUG update_view_from_model: app parameter:", app)
    if app is None:
        print("DEBUG update_view_from_model: No app provided, skipping update.")
        return
    model = app.new_player # Assuming new_player is the model instance

    for field_obj in fields(model):
        field = field_obj.name
        value = getattr(model, field)
        var = getattr(app, f"{field}_var", None)
        if var is None:
            continue

        # Format special fields (main_stats, languages, special_abilities, immunity, etc.)
        if field in ("main_stats", "languages", "special_abilities", "immunity", "save_bonuses"):
            value = _format_change_mainstats(value)

        # Normalize numeric targets
        if isinstance(var, (tk.IntVar, tk.DoubleVar)): # Only for IntVar and DoubleVar
            if isinstance(value, (tuple, list)):
                value = value[0] if value else 0
            elif not isinstance(value, (int, float)):
                try:
                    value = int(value)
                except (TypeError, ValueError):
                    value = 0

        # Normalize string targets
        elif isinstance(var, tk.StringVar): # Only for StringVar
            if not isinstance(value, str):
                value = str(value)

        try:
            current = var.get()
        except tk.TclError:
            # Variable type mismatch; force reset
            current = None

        if current != value: # Only update if value has changed
            print(f"DEBUG update_view_from_model: Updating {field}_var from {current} to {value}")
            try:
                var.set(value)
            except tk.TclError:
                # Fallback for broken value (e.g. still "()")
                if isinstance(var, (tk.IntVar, tk.DoubleVar)):
                    var.set(0)
                else:
                    var.set(str(value))

    # Special handling for ScrolledText widgets (NACH der Schleife!)
    if hasattr(app, "special_abilities_txt"):
        print("DEBUG update_view_from_model: Updating special_abilities_txt widget.")
        current_text = app.special_abilities_txt.get("1.0", "end-1c")
        new_text = _format_change_mainstats(model.special_abilities)
        if current_text != new_text:
            print("DEBUG update_view_from_model: special_abilities_txt:", current_text, "->", new_text)
            app.special_abilities_txt.delete("1.0", "end")
            app.special_abilities_txt.insert("1.0", new_text)
            app.special_abilities_txt.edit_modified(False)
    
    if hasattr(app, "treasure_txt"):
        print("DEBUG update_view_from_model: Updating treasure_txt widget.")
        current_text = app.treasure_txt.get("1.0", "end-1c")
        new_text = str(getattr(model, "treasure", ""))
        if current_text != new_text:
            print("DEBUG update_view_from_model: treasure_txt:", current_text, "->", new_text)
            app.treasure_txt.delete("1.0", "end")
            app.treasure_txt.insert("1.0", new_text)
            app.treasure_txt.edit_modified(False)
    
    if hasattr(app, "inventory_txt"):
        print("DEBUG update_view_from_model: Updating inventory_txt widget.")
        current_text = app.inventory_txt.get("1.0", "end-1c")
        new_text = _format_change_mainstats(getattr(model, "inventory", []))
        if current_text != new_text:
            print("DEBUG update_view_from_model: inventory_txt:", current_text, "->", new_text)
            app.inventory_txt.delete("1.0", "end")
            app.inventory_txt.insert("1.0", new_text)
            app.inventory_txt.edit_modified(False)
