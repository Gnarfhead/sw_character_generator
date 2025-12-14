"""Functions to manage items in the character generator."""

import json
from pathlib import Path
from tkinter import messagebox
from sw_character_generator.classes.item import Item
from sw_character_generator.classes.playerclass import PlayerClass


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "itemdb.json"

def load_item_database() -> list[Item]:
    """Load the item database from the JSON file."""
    print("DEBUG load_item_database called: --------------------------------")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Filter and convert data to Item objects
    items = []
    for entry in data:
        try:
            # Checke, if required fields are present
            if "name" in entry and "type" in entry:
                items.append(Item(**entry))
            else:
                print("DEBUG: invalid entry:", {entry})
        except Exception as e:
            print("ERROR: Error loading item:", {entry}, "-", {e})
    
    return items

def manage_items(item_list: list[Item], action: str, item: Item | None = None) -> list[Item]:
    """
    Manage a list of items by adding or removing items.

    Parameters:
    item_list (list): The list of items to manage.
    action (str): The action to perform ('add' or 'remove').
    item: The item to add or remove from the list.

    Returns:
    list: The updated list of items.
    """
    print("DEBUG manage_items called: --------------------------------")
    if action == 'add':
        if item is not None:
            item_list.append(item)
        else:
            raise ValueError("Item must be provided to add.")
    elif action == 'remove':
        if item in item_list:
            item_list.remove(item)
        else:
            raise ValueError("Item not found in the list.")
    else:
        raise ValueError("Action must be 'add' or 'remove'.")

    return item_list

def add_item_to_inventory(player: PlayerClass, item: Item):
    """Add an item to a player's inventory."""
    print("DEBUG add_item_to_inventory called: --------------------------------")
    player.inventory_items = manage_items(player.inventory_items, action="add", item=item)

def remove_item_from_inventory(player: PlayerClass, item: Item):
    """Remove an item from a player's inventory."""
    print("DEBUG remove_item_from_inventory called: --------------------------------")
    player.inventory_items = manage_items(player.inventory_items, action="remove", item=item)
    
def equip_item(app, slot: str, item_name: str):
    """Equip an item to a specific slot."""
    print("DEBUG equip_item called: --------------------------------")
    print(f"DEBUG equip_item: slot={slot}, item_name='{item_name}', type={type(item_name)}")
        
    # KORRIGIERT: Behandle leere Auswahl 
    if not item_name or item_name == "":
        print(f"DEBUG: Empty selection for {slot}, unequipping")
        setattr(app.new_player, slot, None)
        # ← ENTFERNT: AC-Update und GUI-Update (wird in on_equip_click gemacht)
        return
    
    # Keine Platzhalter-Prüfung mehr nötig (verwenden nur noch leere Strings)
    
    # Finde Item in Inventar
    item_to_equip = None
    for item in app.new_player.inventory_items:
        if item.name == item_name:
            item_to_equip = item
            break
    
    if not item_to_equip:
        print(f"ERROR: Item '{item_name}' not found in inventory")
        print(f"DEBUG: Available items: {[item.name for item in app.new_player.inventory_items]}")
        messagebox.showerror("Error", f"Item '{item_name}' not found in inventory!")
        return
    
    print(f"DEBUG: Found item: {item_to_equip.name}, Type: {item_to_equip.type}")
    
    # Slot-spezifische Validierung
    valid_types = {
        "armor": ["armor"],
        "main_hand": ["weapon"],
        "off_hand": ["weapon", "shield"],
        "helmet": ["helmet"],
        "gloves": ["gloves"],
        "boots": ["boots"],
        "cloak": ["cloak"],
        "ring_left": ["ring"],
        "ring_right": ["ring"],
        "amulet": ["amulet"],
        "belt": ["belt"]
    }
    
    # Prüfe Item-Typ
    if slot in valid_types:
        if item_to_equip.type.lower() not in valid_types[slot]:
            messagebox.showerror("Error", f"'{item_name}' (type: {item_to_equip.type}) cannot be equipped in {slot}!")
            return
    
    # Spezielle Two-Handed Check
    if slot == "off_hand":
        main_hand = app.new_player.main_hand
        print(f"DEBUG: Checking two-handed restriction. Main hand: {main_hand}")
        
        if main_hand and isinstance(main_hand, Item) and hasattr(main_hand, 'twohanded') and main_hand.twohanded:
            print(f"DEBUG: Main hand weapon '{main_hand.name}' is two-handed, blocking off-hand")
            messagebox.showerror("Error", "Cannot equip off-hand with two-handed weapon!")
            return
    
    # Equip Item
    print(f"DEBUG: Successfully equipping {item_to_equip.name} to {slot}")
    setattr(app.new_player, slot, item_to_equip)
    
    
def unequip_item(app, slot: str):
    """Unequip an item and return it to inventory."""
    print("DEBUG unequip_item called: --------------------------------")
    current_item = getattr(app.new_player, slot, None)
    if not current_item or not isinstance(current_item, Item):
        messagebox.showwarning("No item equipped", f"No item is currently equipped in {slot}.")
        return
    
    # Return to inventory
    app.new_player.inventory_items.append(current_item)
    setattr(app.new_player, slot, None)

    messagebox.showinfo("Item unequipped", f"'{current_item.name}' returned to inventory.")

