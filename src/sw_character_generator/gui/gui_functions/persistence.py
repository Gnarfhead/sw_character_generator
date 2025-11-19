from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model


def on_var_change(app, field, var):
    """Callback when a GUI variable changes; update the model accordingly."""
    if suppress_updates := getattr(app, "_suppress_updates", False):
        return
    try:
        raw = var.get()
    except tk.TclError:
        # Invalid/incompatible value in Tk variable (e.g. "Common" in IntVar)
        # Refresh from model and bail out
        with app.suppress_updates():
            update_view_from_model(app)
        return

    # Normalize by model field type
    current_val = getattr(app.new_player, field, None)

    # If model has numeric, coerce; if coercion fails, ignore change
    if isinstance(current_val, int):
        try:
            if isinstance(raw, (tuple, list)):
                raw = raw[0] if raw else 0
            raw = int(raw)
        except (ValueError, TypeError):
            return
    elif isinstance(current_val, float):
        try:
            if isinstance(raw, (tuple, list)):
                raw = raw[0] if raw else 0.0
            raw = float(raw)
        except (ValueError, TypeError):
            return

    setattr(app.new_player, field, raw)

    # Update view for any derived fields, but prevent recursion
    with app.suppress_updates():
        update_view_from_model(app)