"""Handle changes to the inventory text widget."""

# Bind to track changes and sync back to model

def update_equipment_comboboxes(app):
    """Update equipment comboboxes to show only items in inventory."""
    print("DEBUG update_equipment_comboboxes called: --------------------------------")
    
    # ← KORRIGIERT: Prüfe auf Item-Objekt mit hasattr
    equipped_armor = ""
    if app.new_player.armor:
        if hasattr(app.new_player.armor, 'name'):
            equipped_armor = app.new_player.armor.name
        elif isinstance(app.new_player.armor, str):
            equipped_armor = app.new_player.armor
            print(f"WARNING: armor is string '{equipped_armor}', converting to Item")
            # Optional: Finde Item-Objekt
            for item in app.new_player.inventory_items:
                if item.name == equipped_armor:
                    app.new_player.armor = item
                    break
    
    equipped_main = ""
    if app.new_player.main_hand:
        if hasattr(app.new_player.main_hand, 'name'):
            equipped_main = app.new_player.main_hand.name
        elif isinstance(app.new_player.main_hand, str):
            equipped_main = app.new_player.main_hand
            print(f"WARNING: main_hand is string '{equipped_main}', converting to Item")
            for item in app.new_player.inventory_items:
                if item.name == equipped_main:
                    app.new_player.main_hand = item
                    break
    
    equipped_off = ""
    if app.new_player.off_hand:
        if hasattr(app.new_player.off_hand, 'name'):
            equipped_off = app.new_player.off_hand.name
        elif isinstance(app.new_player.off_hand, str):
            equipped_off = app.new_player.off_hand
            print(f"WARNING: off_hand is string '{equipped_off}', converting to Item")
            for item in app.new_player.inventory_items:
                if item.name == equipped_off:
                    app.new_player.off_hand = item
                    break
    
    print(f"DEBUG: Currently equipped - Armor: '{equipped_armor}', Main: '{equipped_main}', Off: '{equipped_off}'")
    
    # Filter items by type
    armor_items = [""] + [item.name for item in app.new_player.inventory_items if item.type.lower() == "armor"]
    weapon_items = [""] + [item.name for item in app.new_player.inventory_items if item.type.lower() == "weapon"]
    shield_items = [""] + [item.name for item in app.new_player.inventory_items if item.type.lower() == "shield"]
    off_hand_items = [""] + weapon_items[1:] + shield_items[1:]  # Combine weapons and shields
    
    print(f"DEBUG: Armor items: {armor_items}")
    print(f"DEBUG: Weapon items: {weapon_items}")
    print(f"DEBUG: Shield items: {shield_items}")
    
    # Update combobox values
    app.cb_armor["values"] = armor_items if armor_items != [""] else ["No armor in inventory"]
    app.cb_main_hand["values"] = weapon_items if weapon_items != [""] else ["No weapons in inventory"]
    app.cb_off_hand["values"] = off_hand_items if off_hand_items != [""] else ["No items in inventory"]
    
    # Set current selection
    app.armor_var.set(equipped_armor)
    app.main_hand_var.set(equipped_main)
    app.off_hand_var.set(equipped_off)
    
    print(f"DEBUG: Final selections - Armor: '{app.armor_var.get()}', Main: '{app.main_hand_var.get()}', Off: '{app.off_hand_var.get()}'")