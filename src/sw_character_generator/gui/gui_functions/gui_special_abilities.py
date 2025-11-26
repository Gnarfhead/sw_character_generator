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
        user_entries = {s.strip() for s in lines if s.strip()}
    else: # single entry
        user_entries = {content.strip()} if content.strip() else set()

    # Combine user entries with auto-generated entries
    auto_entries = app.new_player.special_abilities_race | app.new_player.special_abilities_profession    

    # Update the character's special abilities
    app.new_player.special_abilities_other = user_entries - auto_entries

    # Update the text widget to reflect any changes (if needed)
    app.special_abilities_txt.edit_modified(False)  # Reset the modified flag

    # print("DEBUG on_special_abilities_changed: Updated to", app.new_player.special_abilities)
