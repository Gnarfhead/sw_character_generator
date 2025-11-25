"""Handle changes to the special abilities text widget."""

def on_special_abilities_changed(app):
    """Callback when user edits special_abilities_txt."""
    print("DEBUG on_special_abilities_changed: ------------------------------------------------")

    if getattr(app, "is_updating", False):
        print("DEBUG on_special_abilities_changed: Change ignored due to is_updating flag.")
        return

    # Read the content of the special_abilities_txt widget
    content = app.special_abilities_txt.get("1.0", "end-1c")

    # Parse back to tuple if comma-separated, or keep as string
    if "," in content:  # multiple abilities
        app.new_player.special_abilities = tuple(s.strip() for s in content.split(",")) # convert to tuple
    else:
        app.new_player.special_abilities = (content,) if content else () # single ability or empty

    app.special_abilities_txt.edit_modified(False) # reset modified flag