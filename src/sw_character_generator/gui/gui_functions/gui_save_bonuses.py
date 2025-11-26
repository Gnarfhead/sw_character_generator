"""Handle changes to the save bonuses text widget."""

def on_save_bonuses_changed(app):
    """Callback when user edits save_bonuses_txt."""
    print("DEBUG on_save_bonuses_changed: ------------------------------------------------")

    if getattr(app, "is_updating", False):
        print("DEBUG on_save_bonuses_changed: Change ignored due to is_updating flag.")
        return

    # Read the content of the save_bonuses_txt widget
    content = app.save_bonuses_txt.get("1.0", "end-1c")

    # Parse back to SET (not tuple!)
    if "," in content:  # multiple save bonuses
        app.new_player.save_bonuses = {s.strip() for s in content.split(",") if s.strip()}  # ✓ set
    else:
        app.new_player.save_bonuses = {content} if content.strip() else set()  # ✓ set

    app.save_bonuses_txt.edit_modified(False)  # reset modified flag

    #print("DEBUG on_save_bonuses_changed: Updated to", {app.new_player.save_bonuses}, "type:", {type(app.new_player.save_bonuses)},)
