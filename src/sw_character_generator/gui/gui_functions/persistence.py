from dataclasses import asdict
import tkinter as tk
from .gui_update_view_from_model import update_view_from_model



def bind_model_vars(app):
    """Bind GUI variables/widgets back to the model."""
    for field in asdict(app.new_player).keys():
        var = getattr(app, f"{field}_var", None)
        if var is None:
            continue
        var.trace_add("write", lambda *a, f=field, v=var: on_var_change(app, f, v))