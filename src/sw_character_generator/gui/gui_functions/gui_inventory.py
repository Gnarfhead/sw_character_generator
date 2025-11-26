"""Handle changes to the inventory text widget."""
from src.sw_character_generator.classes.item import Item


def on_inventory_changed(app):
    """Callback when user edits inventory_txt."""
    print("DEBUG on_inventory_changed: ------------------------------------------------")

    if getattr(app, "is_updating", False):
        print("DEBUG on_inventory_changed: Change ignored due to is_updating flag.")
        return

    content = app.inventory_txt.get("1.0", "end-1c")

    # Parse inventory entries (format: "Item Name x Quantity")
    inventory = []
    if "\n" in content or "," in content:
        lines = content.replace(",", "\n").split("\n")
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Try to parse "Name x Quantity" format
            if " x" in line or " X" in line:
                parts = line.replace(" X", " x").split(" x")
                name = parts[0].strip()
                try:
                    quantity = int(parts[1].strip())
                except (ValueError, IndexError):
                    quantity = 1
                inventory.append(Item(name=name, quantity=quantity))
            else:
                # Single item without quantity
                inventory.append(Item(name=line))
    elif content.strip():
        inventory.append(Item(name=content.strip()))

    app.new_player.inventory = inventory

    app.inventory_txt.edit_modified(False)
    print(f"DEBUG on_inventory_changed: Updated inventory to: {app.new_player.inventory}")