"""Handle changes to the inventory text widget."""

def update_equipment_comboboxes(app):
    """Update equipment comboboxes to show only items in inventory."""
    print("DEBUG update_equipment_comboboxes: ------------------------------------------------")
    
    # ← HELPER-FUNKTION: Hole Item-Name von Equipment-Slot
    def get_equipped_name(item):
        """Get name from equipped item (handles both Item objects and strings)."""
        if item is None:
            return ""
        if hasattr(item, 'name'):
            return item.name
        if isinstance(item, str):
            return item
        return ""
    
    # ← GEÄNDERT: Hole alle ausgerüsteten Items
    equipped_items = {
        "armor": get_equipped_name(app.new_player.armor),
        "main_hand": get_equipped_name(app.new_player.main_hand),
        "off_hand": get_equipped_name(app.new_player.off_hand),
        "helmet": get_equipped_name(app.new_player.helmet),
        "gloves": get_equipped_name(app.new_player.gloves),
        "boots": get_equipped_name(app.new_player.boots),
        "cloak": get_equipped_name(app.new_player.cloak),
        "ring_left": get_equipped_name(app.new_player.ring_left),
        "ring_right": get_equipped_name(app.new_player.ring_right),
        "amulet": get_equipped_name(app.new_player.amulet),
        "belt": get_equipped_name(app.new_player.belt)
    }
    
    print("DEBUG: Currently equipped items:")
    for slot, name in equipped_items.items():
        if name:
            print("DEBUG get_equipped_name", slot, name)
    
    # ← GEÄNDERT: Filter Items nach Typ (case-insensitive!)
    items_by_type = {
        "armor": [""],
        "weapon": [""],
        "shield": [""],
        "helmet": [""],
        "gloves": [""],
        "boots": [""],
        "cloak": [""],
        "ring": [""],
        "amulet": [""],
        "belt": [""]
    }
    
    for item in app.new_player.inventory_items:
        item_type = item.type.lower()  # ← WICHTIG: case-insensitive!
        if item_type in items_by_type:
            items_by_type[item_type].append(item.name)
    
    print("DEBUG get_equipped_name: Items by type:")
    for type_name, items in items_by_type.items():
        if len(items) > 1:  # Mehr als nur ""
            print("DEBUG items_by_type", type_name, items[1:])  # Zeige ohne ""
    
    # ← GEÄNDERT: Update Combobox-Werte für alle Slots
    # Armor
    app.cb_armor["values"] = items_by_type["armor"] if len(items_by_type["armor"]) > 1 else [""]
    app.armor_var.set(equipped_items["armor"])
    
    # Main Hand (nur Waffen)
    app.cb_main_hand["values"] = items_by_type["weapon"] if len(items_by_type["weapon"]) > 1 else [""]
    app.main_hand_var.set(equipped_items["main_hand"])
    
    # Off Hand (Waffen ODER Schilde)
    off_hand_items = [""] + items_by_type["weapon"][1:] + items_by_type["shield"][1:]
    app.cb_off_hand["values"] = off_hand_items if len(off_hand_items) > 1 else [""]
    app.off_hand_var.set(equipped_items["off_hand"])
    
    # Helmet
    app.cb_helmet["values"] = items_by_type["helmet"] if len(items_by_type["helmet"]) > 1 else [""]
    app.helmet_var.set(equipped_items["helmet"])
    
    # Gloves
    app.cb_gloves["values"] = items_by_type["gloves"] if len(items_by_type["gloves"]) > 1 else [""]
    app.gloves_var.set(equipped_items["gloves"])
    
    # Boots
    app.cb_boots["values"] = items_by_type["boots"] if len(items_by_type["boots"]) > 1 else [""]
    app.boots_var.set(equipped_items["boots"])
    
    # Cloak
    app.cb_cloak["values"] = items_by_type["cloak"] if len(items_by_type["cloak"]) > 1 else [""]
    app.cloak_var.set(equipped_items["cloak"])
    
    # Ring Left
    app.cb_ring_left["values"] = items_by_type["ring"] if len(items_by_type["ring"]) > 1 else [""]
    app.ring_left_var.set(equipped_items["ring_left"])
    
    # Ring Right
    app.cb_ring_right["values"] = items_by_type["ring"] if len(items_by_type["ring"]) > 1 else [""]
    app.ring_right_var.set(equipped_items["ring_right"])
    
    # Amulet
    app.cb_amulet["values"] = items_by_type["amulet"] if len(items_by_type["amulet"]) > 1 else [""]
    app.amulet_var.set(equipped_items["amulet"])
    
    # Belt
    app.cb_belt["values"] = items_by_type["belt"] if len(items_by_type["belt"]) > 1 else [""]
    app.belt_var.set(equipped_items["belt"])
    
    print(f"DEBUG: Final combobox values set")
    print("DEBUG update_equipment_comboboxes: DONE ==================================")