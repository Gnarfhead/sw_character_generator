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
    if "\n" in content or "," in content:  # multiple immunities
        lines = content.replace(",", "\n").split("\n")
        user_entries = {s.strip() for s in lines if s.strip()}
    else:
        user_entries = {content.strip()} if content.strip() else set()

    # Combine user entries with auto-generated entries
    auto_entries = app.new_player.immunities_race | app.new_player.immunities_profession

    # Update the character's immunities
    app.new_player.immunities_other = user_entries - auto_entries
    
    # Update the text widget to reflect combined entries
    app.immunities_txt.edit_modified(False)  # Reset the modified flag

    # print("DEBUG on_immunities_changed: Updated to", app.new_player.immunities)