"""Handle changes to the inventory text widget."""

# Bind to track changes and sync back to model
def on_inventory_text_changed(app, event):
    """Callback for inventory text widget changes."""
    print("DEBUG on_inventory_text_changed: --------------------------------")
    if getattr(app, "is_updating", False):
        return
    # Parse text back to inventory dict
    text = app.inventory_txt.get("1.0", "end-1c").strip()
    if not text:
        app.new_player.inventory = {}
        return

    new_inventory = {}
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        # Parse "Item x5" or "Item"
        if " x" in line:
            parts = line.rsplit(" x", 1)
            item_name = parts[0].strip()
            try:
                quantity = int(parts[1].strip())
            except (ValueError, IndexError):
                quantity = 1
        else:
            item_name = line
            quantity = 1
        new_inventory[item_name] = quantity
            
    app.new_player.inventory = new_inventory 