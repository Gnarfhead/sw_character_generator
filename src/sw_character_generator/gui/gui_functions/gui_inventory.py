"""Handle changes to the inventory text widget."""

def on_inventory_changed(app):
    """Handle changes to the inventory text widget."""
    print("DEBUG on_inventory_changed: --------------------------------")

    if getattr(app, "is_updating", False):
        return
    content = app.inventory_txt.get("1.0", "end-1c").strip()
    new: dict[str,int] = {}
    if content:
        lines = content.replace(",", "\n").splitlines()
        for line in lines:
            s = line.strip()
            if not s:
                continue
            # parse "Name xN" or "Name XN" or "Name : N"
            qty = 1
            if " x" in s.lower():
                parts = s.rsplit("x", 1)
                name = parts[0].strip()
                try:
                    qty = int(parts[1].strip())
                except Exception:
                    qty = 1
            elif ":" in s:
                parts = s.rsplit(":", 1)
                name = parts[0].strip()
                try:
                    qty = int(parts[1].strip())
                except Exception:
                    qty = 1
            else:
                name = s
            new[name] = new.get(name, 0) + qty
    app.new_player.inventory = new
    app.inventory_txt.edit_modified(False)


    print(f"DEBUG on_inventory_changed: Updated inventory to: {app.new_player.inventory}")