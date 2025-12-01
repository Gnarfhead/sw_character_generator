"""Update view from model function."""
import tkinter as tk
from dataclasses import fields

from sw_character_generator.gui.gui_functions.gui_immunities import on_immunities_changed
from sw_character_generator.gui.gui_functions.gui_save_bonuses import on_save_bonuses_changed
from sw_character_generator.gui.gui_functions.gui_special_abilities import on_special_abilities_changed
from sw_character_generator.gui.gui_functions.gui_magic import update_spell_table_widget



def _format_change_scrolledtext(value):
    """Format main_stats tuple into a readable string."""
    if isinstance(value, (tuple, list, set)): # Tuple, Liste or Set
        return "\n".join(str(v) for v in sorted(value)) # Join elements with newlines
    if isinstance(value, dict): # Dict
        return "\n".join(f"{k}={v}" for k, v in value.items()) # Key=Value pairs
    return str(value) # Fallback to string conversion

def _format_change_stringlabel(value):
    """Format main_stats tuple into a comma-separated string."""
    if isinstance(value, (tuple, list, set)): # Tuple, Liste or Set
        return ", ".join(str(v) for v in sorted(value)) # Join elements with commas
    if isinstance(value, dict): # Dict
        return ", ".join(f"{k}={v}" for k, v in value.items()) # Key=Value pairs
    return str(value) # Fallback to string conversion

def _format_items_dict(items: dict) -> str:
    """Format list of Item objects for display."""
    
    if not items:
        return ""
    
    lines = []
    for name, qty in sorted(items.items(), key=lambda kv: kv[0].lower()):
        try:
            q = int(qty)
        except Exception:
            q = 1
        if q > 1:
            lines.append(f"{name} x{q}")
        else:
            lines.append(name)
    return "\n".join(lines)

def update_view_from_model(app):
    """Safely copy model fields into Tkinter variables, normalizing types."""
    print("DEBUG update_view_from_model: ----------------------------------------------------------------")
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

        # Format special fields (main_stats, languages, special_abilities, immunities, save_bonuses)
        #if field in ("main_stats", "languages", "special_abilities", "immunities", "save_bonuses"):
        if field in ("special_abilities", "immunities", "save_bonuses"):
            value = _format_change_scrolledtext(value)

        # Format stringlabel fields
        if field in ("languages", "main_stats"):
            value = _format_change_stringlabel(value)

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
            # print(f"DEBUG update_view_from_model: Updating {field}_var from {current} to {value}")
            try:
                var.set(value)
            except tk.TclError:
                # Fallback for broken value (e.g. still "()")
                if isinstance(var, (tk.IntVar, tk.DoubleVar)):
                    var.set(0)
                else:
                    var.set(str(value))

    # refresh magic spell table if present
    try:
        print("DEBUG update_view_from_model: Updating spell table widget.")
        update_spell_table_widget(app)
    except Exception:
        print("DEBUG update_view_from_model: Failed to update spell table widget.")

    # Special handling for ScrolledText widgets (NACH der Schleife!)
    if hasattr(app, "special_abilities_txt"):
        # print("DEBUG update_view_from_model: Updating special_abilities_txt widget.")
        app.special_abilities_txt.unbind("<<Modified>>")  # Temporarily unbind to avoid triggering change event

        current_text = app.special_abilities_txt.get("1.0", "end-1c")
        # Generate new text from model
        new_text = _format_change_scrolledtext(model.special_abilities)

        if current_text != new_text:
            # print("DEBUG update_view_from_model: special_abilities_txt:", current_text, "->", new_text)
            app.special_abilities_txt.delete("1.0", "end")
            app.special_abilities_txt.insert("1.0", new_text)
        
        app.special_abilities_txt.edit_modified(False)
        # Rebind the event
        app.special_abilities_txt.bind("<<Modified>>", lambda event: on_special_abilities_changed(app))

    
    # Special handling for immunities_txt widget
    if hasattr(app, "immunities_txt"):
        # print("DEBUG update_view_from_model: Updating immunities_txt widget.")
        app.immunities_txt.unbind("<<Modified>>")  # Temporarily unbind to avoid triggering change event

        current_text = app.immunities_txt.get("1.0", "end-1c")
        # Generate new text from model
        new_text = _format_change_scrolledtext(model.immunities)

        if current_text != new_text:
            # print(f"DEBUG update_view_from_model: immunities_txt: '{current_text}' -> '{new_text}'")
            app.immunities_txt.delete("1.0", "end")
            app.immunities_txt.insert("1.0", new_text)

        app.immunities_txt.edit_modified(False)
        # Rebind the event
        app.immunities_txt.bind("<<Modified>>", lambda event: on_immunities_changed(app))
    
    # Special handling for save_bonuses_txt widget
    if hasattr(app, "save_bonuses_txt"):
        # print("DEBUG update_view_from_model: Updating save_bonuses_txt widget.")
        app.save_bonuses_txt.unbind("<<Modified>>")  # Temporarily unbind to avoid triggering change event

        current_text = app.save_bonuses_txt.get("1.0", "end-1c")
        # Generate new text from model
        new_text = _format_change_scrolledtext(model.save_bonuses)

        if current_text != new_text:
            # print(f"DEBUG update_view_from_model: save_bonuses_txt: '{current_text}' -> '{new_text}'")
            app.save_bonuses_txt.delete("1.0", "end")
            app.save_bonuses_txt.insert("1.0", new_text)
        
        app.save_bonuses_txt.edit_modified(False)
        # Rebind the event
        app.save_bonuses_txt.bind("<<Modified>>", lambda event: on_save_bonuses_changed(app))

    if hasattr(app, "inventory_txt"):
        # print("DEBUG update_view_from_model: Updating inventory_txt widget.")
        
        current_text = app.inventory_txt.get("1.0", "end-1c")
        new_text = _format_items_dict(model.inventory)
        
        if current_text != new_text:
            # print(f"DEBUG update_view_from_model: inventory_txt: '{current_text}' -> '{new_text}'")
            app.inventory_txt.config(state="normal")  # FIX: Temporarily enable
            app.inventory_txt.delete("1.0", "end")
            app.inventory_txt.insert("1.0", new_text)
            app.inventory_txt.config(state="disabled")  # FIX: Disable again
    
    if hasattr(app, "treasure_txt"):
        # print("DEBUG update_view_from_model: Updating treasure_txt widget.")
        
        current_text = app.treasure_txt.get("1.0", "end-1c")
        new_text = _format_items_dict(model.treasure)
        
        if current_text != new_text:
            # print(f"DEBUG update_view_from_model: treasure_txt: '{current_text}' -> '{new_text}'")
            app.treasure_txt.config(state="normal")  # FIX: Temporarily enable
            app.treasure_txt.delete("1.0", "end")
            app.treasure_txt.insert("1.0", new_text)
            app.treasure_txt.config(state="disabled")  # FIX: Disable again
