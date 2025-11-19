"""Update view from model function."""
import tkinter as tk
from dataclasses import asdict

def update_view_from_model(app):
    """Safely copy model fields into Tkinter variables, normalizing types."""
    model = app.new_player
    for field, value in asdict(model).items():
        var = getattr(app, f"{field}_var", None)
        if var is None:
            continue

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
