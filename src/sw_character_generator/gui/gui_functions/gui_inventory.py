"""Handle changes to the inventory text widget."""

# Bind to track changes and sync back to model
from sw_character_generator.classes.item import Item


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

def update_equipment_comboboxes(app):
    """Update equipment comboboxes to show only items in inventory."""
    print("DEBUG update_equipment_comboboxes called: --------------------------------")
    
    # Sammle alle Items aus dem Inventar
    inventory_items = app.new_player.inventory_items
    
    # Filtere nach Typ
    armor_items = [""] + [item.name for item in inventory_items if item.type.lower() == "armor"]
    weapon_items = [""] + [item.name for item in inventory_items if item.type.lower() == "weapon"]
    shield_items = [item.name for item in inventory_items if item.type.lower() == "shield"]
    off_hand_items = [""] + weapon_items + shield_items  # Off-Hand kann Waffe oder Schild sein

    # Aktualisiere Armor Combobox
    app.cb_armor["values"] = armor_items if len(armor_items) > 1 else ["No armor in inventory"]
    
    # Setze auf aktuell ausgerüstetes Item oder leer
    current_armor = app.new_player.armor
    
    # KORRIGIERT: Prüfe ob current_armor ein Item oder String ist
    if current_armor:
        if isinstance(current_armor, Item):
            armor_name = current_armor.name
        else:
            armor_name = str(current_armor)  # Falls es ein String ist
        
        app.armor_var.set(armor_name if armor_name in armor_items else "")
    elif len(armor_items) <= 1:
        app.armor_var.set("No armor in inventory")
    else:
        app.armor_var.set("")  # Leer = nichts ausgerüstet
    
    # Aktualisiere Main Hand Combobox
    app.cb_main_hand["values"] = weapon_items if len(weapon_items) > 1 else ["No weapons in inventory"]
    
    current_main_hand = app.new_player.main_hand
    
    # KORRIGIERT: Prüfe ob current_main_hand ein Item oder String ist
    if current_main_hand:
        if isinstance(current_main_hand, Item):
            main_hand_name = current_main_hand.name
        else:
            main_hand_name = str(current_main_hand)
        
        app.main_hand_var.set(main_hand_name if main_hand_name in weapon_items else "")
    elif len(weapon_items) <= 1:
        app.main_hand_var.set("No weapons in inventory")
    else:
        app.main_hand_var.set("")
    
    # Aktualisiere Off Hand Combobox
    app.cb_off_hand["values"] = off_hand_items if len(off_hand_items) > 1 else ["No items in inventory"]
    
    current_off_hand = app.new_player.off_hand
    
    # KORRIGIERT: Prüfe ob current_off_hand ein Item oder String ist
    if current_off_hand:
        if isinstance(current_off_hand, Item):
            off_hand_name = current_off_hand.name
        else:
            off_hand_name = str(current_off_hand)
        
        app.off_hand_var.set(off_hand_name if off_hand_name in off_hand_items else "")
    elif len(off_hand_items) <= 1:
        app.off_hand_var.set("No items in inventory")
    else:
        app.off_hand_var.set("")