import json
from pathlib import Path
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk, messagebox
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
    
def equip_item(self, slot: str, item_name: str):
    """Equip an item in the specified slot."""
    print("DEBUG equip_item called: --------------------------------")
    print("DEBUG equip_item slot:", slot, item_name)

    if "Select" in item_name:
        messagebox.showwarning("No item selected", f"Please select an item for {slot}.")
        return

    # Search for the Item object
    selected_item = next((item for item in self.item_database if item.name == item_name), None)
    print("DEBUG equip_item selected_item:", selected_item)
    if not selected_item:
        messagebox.showerror("Error", f"Item '{item_name}' not found.")
        return

    # Check if item is in inventory (optional requirement)
    if selected_item not in self.new_player.inventory_items:
        response = messagebox.askyesno(
            "Item not in inventory",
            f"'{item_name}' is not in your inventory. Equip anyway?"
        )
        if not response:
            return

    # Unequip previous item (return to inventory)
    current_item = getattr(self.new_player, slot, None)
    if current_item and isinstance(current_item, Item):
        self.new_player.inventory_items.append(current_item)

    # Equip new item (remove from inventory if present)
    setattr(self.new_player, slot, selected_item)
    if selected_item in self.new_player.inventory_items:
        self.new_player.inventory_items.remove(selected_item)

    messagebox.showinfo("Item equipped", f"'{selected_item.name}' equipped in {slot}.")
    
def unequip_item(self, slot: str):
    """Unequip an item and return it to inventory."""
    print("DEBUG unequip_item called: --------------------------------")
    current_item = getattr(self.new_player, slot, None)
    if not current_item or not isinstance(current_item, Item):
        messagebox.showwarning("No item equipped", f"No item is currently equipped in {slot}.")
        return
    
    # Return to inventory
    self.new_player.inventory_items.append(current_item)
    setattr(self.new_player, slot, None)
    
    messagebox.showinfo("Item unequipped", f"'{current_item.name}' returned to inventory.")



