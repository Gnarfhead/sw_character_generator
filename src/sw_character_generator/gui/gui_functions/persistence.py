from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model


def on_var_change(self, field, var):
    """Callback when a GUI variable changes; update the model accordingly."""
    if self._updating:
        return
    try:
        raw = var.get()
    except tk.TclError:
        # Invalid/incompatible value in Tk variable (e.g. "Common" in IntVar)
        # Refresh from model and bail out
        with self.suppress_updates():
            update_view_from_model(self)
        return

    # Normalize by model field type
    current_val = getattr(self.new_player, field, None)

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

    setattr(self.new_player, field, raw)

    # Update view for any derived fields, but prevent recursion
    with self.suppress_updates():
        update_view_from_model(self)