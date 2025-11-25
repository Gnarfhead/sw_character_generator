"""Handle changes to the alignment selection."""
from sw_character_generator.functions.choosen_alignment import choosen_alignment_modifiers
from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model

def on_alignment_change(app, *args):
    """Handle alignment combobox changes."""
    print("DEBUG on_alignment_change: ------------------------------------------------")
    if getattr(app, "is_updating", False):
        print("DEBUG on_alignment_change: Alignment change ignored due to is_updating flag.")
        return
    name = app.alignment_var.get()
    if not name:
        print("DEBUG on_alignment_change: No alignment selected.")
        return
    try:
        # Update the model with the new alignment
        choosen_alignment_modifiers(app.new_player, name) # update alignment and related stats
        app.status_var.set(f"Alignment changed to {name}")
        app.lbl_alignment.config(style="Standard.TLabel")
        update_view_from_model(app) # refresh GUI to reflect model changes

        # Adjust top_frame style based on race and alignment selection
        print("DEBUG on_alignment_change: Checking race and alignment for top_frame style adjustment.")
        if app.race_var.get() != "Undefined" and app.alignment_var.get() != "Undefined":
            print("DEBUG on_alignment_change: app.race_var.get() =", app.race_var.get())
            print("DEBUG on_alignment_change: app.alignment_var.get() =", app.alignment_var.get())
            app.top_frame.config(style="Standard.TFrame")
            print("DEBUG on_alignment_change: Both race and alignment are defined; set top_frame to Standard.TFrame")
        else:
            print("DEBUG on_alignment_change: app.race_var.get() =", app.race_var.get())
            print("DEBUG on_alignment_change: app.alignment_var.get() =", app.alignment_var.get())
            app.top_frame.config(style="Attention.TFrame")
            print("DEBUG on_alignment_change: Either race or alignment is undefined; set top_frame to Attention.TFrame")

    except Exception as e:
        #app.status_var.set(f"DEBUG on_alignment_change: Error updating Alignment: {e}")
        print(f"DEBUG on_alignment_change: Alignment change error: {e}")