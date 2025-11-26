"""Handle changes to the treasure text widget."""

def on_treasure_changed(app):
    """Callback when user edits treasure_txt."""
    print("DEBUG on_treasure_changed: ------------------------------------------------")

    if getattr(app, "is_updating", False):
        print("DEBUG on_treasure_changed: Change ignored due to is_updating flag.")
        return

    # Read the content of the treasure_txt widget
    content = app.treasure_txt.get("1.0", "end-1c")

    # Parse back to SET (not tuple!)
    if "\n" in content or "," in content:  # multiple abilities
        lines = content.replace(",", "\n").split("\n")
        user_entries = {s.strip() for s in lines if s.strip()}
    else: # single entry
        user_entries = {content.strip()} if content.strip() else set()

    # Combine user entries with auto-generated entries
    auto_entries = app.new_player.treasure
    app.new_player.treasure = user_entries | auto_entries

    # Update the treasure_txt widget to reflect any changes
    app.is_updating = True
    try:
        app.treasure_txt.delete("1.0", "end")
        for item in sorted(app.new_player.treasure):
            app.treasure_txt.insert("end", item + "\n")
    finally:
        app.is_updating = False

    app.treasure_txt.edit_modified(False)  # Reset modified flag

    

    # print("DEBUG on_treasure_changed: Updated to", app.new_player.treasure)
