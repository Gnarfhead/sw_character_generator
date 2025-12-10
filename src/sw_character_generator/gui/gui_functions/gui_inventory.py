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
    
    # Verhindere Update während bereits am Updaten
    if app.is_updating:
        print("DEBUG: Skipping update_equipment_comboboxes (is_updating=True)")
        return

    # HINZUGEFÜGT: Merke aktuelle Auswahl VOR dem Update
    current_armor_selection = app.armor_var.get()
    current_main_hand_selection = app.main_hand_var.get()
    current_off_hand_selection = app.off_hand_var.get()
    
    print(f"DEBUG: Current selections - Armor: '{current_armor_selection}', Main: '{current_main_hand_selection}', Off: '{current_off_hand_selection}'")

    # Sammle alle Items aus dem Inventar
    inventory_items = app.new_player.inventory_items
    
    # Filtere nach Typ
    armor_items = [""] + [item.name for item in inventory_items if item.type.lower() == "armor"]
    weapon_items = [""] + [item.name for item in inventory_items if item.type.lower() == "weapon"]
    shield_items = [item.name for item in inventory_items if item.type.lower() == "shield"]
    off_hand_items = [""] + weapon_items[1:] + shield_items

    # Helper-Funktion: Hole Item-Namen sicher
    def get_item_name(item):
        """Get name from item (handles both Item objects and strings)."""
        if not item:
            return ""
        if isinstance(item, Item):
            return item.name
        if isinstance(item, str):
            return item
        return ""

    # SETZE FLAG WÄHREND UPDATE
    app._updating = True
    
    try:
        # ========== ARMOR COMBOBOX ==========
        app.cb_armor["values"] = armor_items if len(armor_items) > 1 else ["No armor in inventory"]
        
        # PRIORITÄT 1: Behalte User-Auswahl, wenn noch gültig
        if current_armor_selection and current_armor_selection in armor_items:
            app.armor_var.set(current_armor_selection)
            print(f"DEBUG: Kept user armor selection: {current_armor_selection}")
        # PRIORITÄT 2: Zeige ausgerüstetes Item
        elif app.new_player.armor:
            armor_name = get_item_name(app.new_player.armor)
            if armor_name in armor_items:
                app.armor_var.set(armor_name)
                print(f"DEBUG: Set equipped armor: {armor_name}")
            else:
                app.armor_var.set("")
        # PRIORITÄT 3: Platzhalter oder leer
        elif len(armor_items) <= 1:
            app.armor_var.set("No armor in inventory")
        else:
            app.armor_var.set("")
        
        # ========== MAIN HAND COMBOBOX ==========
        app.cb_main_hand["values"] = weapon_items if len(weapon_items) > 1 else ["No weapons in inventory"]
        
        # PRIORITÄT 1: Behalte User-Auswahl, wenn noch gültig
        if current_main_hand_selection and current_main_hand_selection in weapon_items:
            app.main_hand_var.set(current_main_hand_selection)
            print(f"DEBUG: Kept user main hand selection: {current_main_hand_selection}")
        # PRIORITÄT 2: Zeige ausgerüstetes Item
        elif app.new_player.main_hand:
            main_hand_name = get_item_name(app.new_player.main_hand)
            if main_hand_name in weapon_items:
                app.main_hand_var.set(main_hand_name)
                print(f"DEBUG: Set equipped main hand: {main_hand_name}")
            else:
                app.main_hand_var.set("")
        # PRIORITÄT 3: Platzhalter oder leer
        elif len(weapon_items) <= 1:
            app.main_hand_var.set("No weapons in inventory")
        else:
            app.main_hand_var.set("")
        
        # ========== OFF HAND COMBOBOX ==========
        app.cb_off_hand["values"] = off_hand_items if len(off_hand_items) > 1 else ["No items in inventory"]
        
        # PRIORITÄT 1: Behalte User-Auswahl, wenn noch gültig
        if current_off_hand_selection and current_off_hand_selection in off_hand_items:
            app.off_hand_var.set(current_off_hand_selection)
            print(f"DEBUG: Kept user off hand selection: {current_off_hand_selection}")
        # PRIORITÄT 2: Zeige ausgerüstetes Item
        elif app.new_player.off_hand:
            off_hand_name = get_item_name(app.new_player.off_hand)
            if off_hand_name in off_hand_items:
                app.off_hand_var.set(off_hand_name)
                print(f"DEBUG: Set equipped off hand: {off_hand_name}")
            else:
                app.off_hand_var.set("")
        # PRIORITÄT 3: Platzhalter oder leer
        elif len(off_hand_items) <= 1:
            app.off_hand_var.set("No items in inventory")
        else:
            app.off_hand_var.set("")
    
    finally:
        # RESET FLAG
        app._updating = False
    
    print(f"DEBUG: Final selections - Armor: '{app.armor_var.get()}', Main: '{app.main_hand_var.get()}', Off: '{app.off_hand_var.get()}'")