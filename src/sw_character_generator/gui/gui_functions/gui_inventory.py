"""Handle changes to the inventory text widget."""

from tkinter import messagebox
import traceback
from sw_character_generator.functions.manage_ac import calculate_ac, update_armor_ac
from sw_character_generator.functions.manage_items import equip_item
from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model


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





def safe_update_equipment(app):
    """Safely update equipment comboboxes."""
    print("DEBUG: safe_update_equipment called")
    try:
        update_equipment_comboboxes(app)
        print("DEBUG: Equipment comboboxes updated")
    except Exception as e:
        print(f"ERROR: Failed to update equipment comboboxes: {e}")
        traceback.print_exc()

def on_equip_click(app):
    """Handle Equip Button click."""
    print("DEBUG on_equip_click: ------------------------------------------------")
    # Hole ausgewählte Items
    equipment_selections = {
        "armor": app.armor_var.get(),
        "main_hand": app.main_hand_var.get(),
        "off_hand": app.off_hand_var.get(),
        "helmet": app.helmet_var.get(),
        "gloves": app.gloves_var.get(),
        "boots": app.boots_var.get(),
        "cloak": app.cloak_var.get(),
        "ring_left": app.ring_left_var.get(),
        "ring_right": app.ring_right_var.get(),
        "amulet": app.amulet_var.get(),
        "belt": app.belt_var.get()
    }
        
    print("DEBUG on_equip_click: Equipment selections:")
    for slot, item_name in equipment_selections.items():
        print(f"  {slot}: '{item_name}'")
        
    # Equip alle ausgewählten Items
    equipped_count = 0
    for slot, item_name in equipment_selections.items():
        if item_name and item_name != "":
            print(f"DEBUG on_equip_click: Equipping {slot}: {item_name}")
            equip_item(app, slot, item_name)
            equipped_count += 1
        
    # Update AC IMMER (da alle Items AC beeinflussen können)
    print("DEBUG on_equip_click: Updating AC after equipping")
    update_armor_ac(app.new_player)
    calculate_ac(app.new_player)
      
    # Update GUI
    with app.suppress_updates():
        update_view_from_model(app)
        
    # Status-Nachricht
    if equipped_count > 0:
        app.status_var.set(f"{equipped_count} item(s) equipped successfully")
    else:
        app.status_var.set("No items selected to equip")
        
    print(f"DEBUG on_equip_click: Equipped {equipped_count} items.")

    
def refresh_inventory_display(app):
    """Refresh the inventory treeview."""
    print("DEBUG refresh_inventory_display called: --------------------------------")
    # Clear current display
    for item in app.inventory_tree.get_children():
        app.inventory_tree.delete(item)
        
    # Count items
    item_counts = {}
    for item in app.new_player.inventory_items:
        if item.name in item_counts:
            item_counts[item.name]["count"] += 1
        else:
            item_counts[item.name] = {
                "item": item,
                "count": 1
            }
        
    # Display items
    total_weight = 0.0
    total_value = 0
        
    for item_name, data in item_counts.items():
        item = data["item"]
        count = data["count"]
            
        app.inventory_tree.insert("", "end", values=(
            item.name,
            item.type,
            f"{item.weight * count:.1f}",
            item.value,
            count
        ))
            
        total_weight += item.weight * count
        # Parse value (assuming format "X GM")
        try:
            value_num = int(item.value.split()[0])
            total_value += value_num * count
        except Exception as e:
            print(f"DEBUG refresh_inventory_display: Error parsing item value '{item.value}': {e}")
        
    # Update summary
    app.inventory_summary_label.config(
        text=f"Total Weight: {total_weight:.1f} | Total Value: {total_value} GM | Items: {len(app.new_player.inventory_items)}"
    )

    # Update Equipment Comboboxen
    update_equipment_comboboxes(app)
def remove_selected_item(app):
    """Remove the selected item from inventory."""
    print("DEBUG remove_selected_item called: --------------------------------")
    selection = app.inventory_tree.selection()
    if not selection:
        messagebox.showwarning("No Selection", "Please select an item to remove.")
        return
        
    item_data = app.inventory_tree.item(selection[0])
    item_name = item_data["values"][0]
       
    # Find and remove the first matching item
    for item in app.new_player.inventory_items:
        if item.name == item_name:
            app.new_player.inventory_items.remove(item)
            break
        
    refresh_inventory_display(app)
    messagebox.showinfo("Success", f"Removed {item_name}")