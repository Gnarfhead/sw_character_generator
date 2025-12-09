import json
from pathlib import Path
from tkinter import messagebox
from sw_character_generator.classes.item import Item
from sw_character_generator.classes.playerclass import PlayerClass

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "itemdb.json"

def load_item_database() -> list[Item]:
    """Lade die Item-Datenbank aus der JSON-Datei."""
    print("DEBUG load_item_database aufgerufen: --------------------------------")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Filtere ungültige Einträge heraus
    items = []
    for entry in data:
        try:
            # Prüfe, ob Mindestfelder vorhanden sind
            if "name" in entry and "type" in entry:
                items.append(Item(**entry))
            else:
                print("DEBUG: Überspringe ungültigen Eintrag:", {entry})
        except Exception as e:
            print("ERROR: Fehler beim Laden von Item:", {entry}, "-", {e})
    
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
    """Füge ein Item zum Inventar eines Spielers hinzu."""
    player.inventory_items = manage_items(player.inventory_items, action="add", item=item)

def remove_item_from_inventory(player: PlayerClass, item: Item):
    """Entferne ein Item aus dem Inventar eines Spielers."""
    player.inventory_items = manage_items(player.inventory_items, action="remove", item=item)
    
def equip_item(self, slot: str, item_name: str):
    """Rüste ein Item in den angegebenen Slot aus."""
    if item_name in ["Select Armor", "Select Main Hand", "Select Off Hand"]:
        messagebox.showwarning("Kein Item ausgewählt", f"Bitte wähle ein Item für {slot}.")
        return

    # KORREKTUR: Suche das Item-Objekt in der Datenbank
    selected_item = next((item for item in self.item_database if item.name == item_name), None)
    if not selected_item:
        messagebox.showerror("Fehler", f"Item '{item_name}' nicht in der Datenbank gefunden.")
        return

    # Speichere das Item-Objekt, nicht den String!
    if slot == "armor":
        self.new_player.armor = selected_item  # ← RICHTIG!
    elif slot == "main_hand":
        self.new_player.main_hand = selected_item  # ← RICHTIG!
    elif slot == "off_hand":
        self.new_player.off_hand = selected_item  # ← RICHTIG!

    messagebox.showinfo("Item ausgerüstet", f"'{selected_item.name}' wurde in {slot} ausgerüstet.")