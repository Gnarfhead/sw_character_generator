"""Handle changes to the immunities text widget."""

def on_immunities_changed(app):
    """Callback when user edits immunities_txt."""
    print("DEBUG on_immunities_changed: ------------------------------------------------")

    if getattr(app, "is_updating", False):
        print("DEBUG on_immunities_changed: Change ignored due to is_updating flag.")
        return

    # Read the content of the immunities_txt widget
    content = app.immunities_txt.get("1.0", "end-1c")

    # Parse back to SET (not tuple!)
    if "," in content:  # multiple immunities
        app.new_player.immunities = {s.strip() for s in content.split(",") if s.strip()}  # ✓ set
    else:
        app.new_player.immunities = {content} if content.strip() else set()  # ✓ set

    app.immunities_txt.edit_modified(False)  # reset modified flag

    #print("DEBUG on_immunities_changed: Updated to", {app.new_player.immunities}, "type:", {type(app.new_player.immunities)},)
