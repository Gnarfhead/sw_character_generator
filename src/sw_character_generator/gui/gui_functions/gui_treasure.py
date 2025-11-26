"""Handle changes to the treasure text widget."""
from sw_character_generator.classes.item import Item


def on_treasure_changed(app):
    """Callback when user edits treasure_txt."""
    print("DEBUG on_treasure_changed: ------------------------------------------------")

    if getattr(app, "is_updating", False):
        print("DEBUG on_treasure_changed: Change ignored due to is_updating flag.")
        return

    content = app.treasure_txt.get("1.0", "end-1c")

    # Parse treasure entries (same format as inventory)
    treasure = []
    if "\n" in content or "," in content:
        lines = content.replace(",", "\n").split("\n")
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            if " x" in line or " X" in line:
                parts = line.replace(" X", " x").split(" x")
                name = parts[0].strip()
                try:
                    quantity = int(parts[1].strip())
                except (ValueError, IndexError):
                    quantity = 1
                treasure.append(Item(name=name, quantity=quantity, category="Treasure"))
            else:
                treasure.append(Item(name=line, category="Treasure"))
    elif content.strip():
        treasure.append(Item(name=content.strip(), category="Treasure"))

    app.new_player.treasure = treasure

    app.treasure_txt.edit_modified(False)
    print(f"DEBUG on_treasure_changed: Updated treasure to: {app.new_player.treasure}")