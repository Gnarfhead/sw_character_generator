"""Handle changes to the special abilities text widget."""

def on_special_abilities_changed(app):
    """Callback when user edits special_abilities_txt."""
    print("DEBUG on_special_abilities_changed: ------------------------------------------------")

    if getattr(app, "is_updating", False):
        print("DEBUG on_special_abilities_changed: Change ignored due to is_updating flag.")
        return

    # Read the content of the special_abilities_txt widget
    content = app.special_abilities_txt.get("1.0", "end-1c")

    # Parse back to SET (not tuple!)
    if "\n" in content or "," in content:  # multiple abilities
        lines = content.replace(",", "\n").split("\n")
        app.new_player.special_abilities = {s.strip() for s in lines if s.strip()}  # ✓ set
    else:
        app.new_player.special_abilities = {content.strip()} if content.strip() else set()  # ✓ set

    app.special_abilities_txt.edit_modified(False)  # reset modified flag

    # print("DEBUG on_special_abilities_changed: Updated to", {app.new_player.special_abilities}, "type:", {type(app.new_player.special_abilities)},)
