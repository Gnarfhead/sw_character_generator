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
    if "\n" in content or "," in content:  # multiple save bonuses
        lines = content.replace(",", "\n").split("\n")
        user_entries = {s.strip() for s in lines if s.strip()}
    else:
        user_entries = {content.strip()} if content.strip() else set()

    # Combine user entries with auto-generated entries
    auto_entries = app.new_player.save_bonuses_race | app.new_player.save_bonuses_profession

    # Update the character's save bonuses
    app.new_player.save_bonuses_other = user_entries - auto_entries

    # Update the text widget to reflect combined entries
    app.save_bonuses_txt.edit_modified(False)  # Reset the modified flag

    # print("DEBUG on_save_bonuses_changed: Updated to", app.new_player.save_bonuses)
