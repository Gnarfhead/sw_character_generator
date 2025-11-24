"""Update view from model function."""
import tkinter as tk
from dataclasses import asdict



def _format_change_mainstats(value):
    """Format main_stats tuple into a readable string."""
    if isinstance(value, (tuple, list, set)): # Tuple, Liste or Set
        return ", ".join(str(v) for v in value) # Join elements with commas
    if isinstance(value, dict): # Dict
        return ", ".join(f"{k}={v}" for k, v in value.items()) # Key=Value pairs
    return str(value) # Fallback to string conversion



def update_view_from_model(app):
    """Safely copy model fields into Tkinter variables, normalizing types."""
    model = app.new_player
    for field, value in asdict(model).items():
        var = getattr(app, f"{field}_var", None)
        if var is None:
            continue

        if field == "main_stats":
            print(f"DEBUG update_view_from_model: Formatting main_stats value: {value}")
            value = _format_change_mainstats(value)
            print(f"DEBUG update_view_from_model: Formatted main_stats value: {value}")

        # Normalize numeric targets
        if isinstance(var, (tk.IntVar, tk.DoubleVar)):
            if isinstance(value, (tuple, list)):
                value = value[0] if value else 0
            elif not isinstance(value, (int, float)):
                try:
                    value = int(value)
                except (TypeError, ValueError):
                    value = 0

        # Normalize string targets
        elif isinstance(var, tk.StringVar):
            if not isinstance(value, str):
                value = str(value)

        try:
            current = var.get()
        except tk.TclError:
            # Variable type mismatch; force reset
            current = None

        if current != value:
            try:
                var.set(value)
            except tk.TclError:
                # Fallback for broken value (e.g. still "()")
                if isinstance(var, (tk.IntVar, tk.DoubleVar)):
                    var.set(0)
                else:
                    var.set(str(value))
