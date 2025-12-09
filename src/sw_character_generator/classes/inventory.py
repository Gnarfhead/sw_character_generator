"""Module defining the Inventory class for managing character items."""

from dataclasses import dataclass, field
from typing import List
from sw_character_generator.classes.item import Item

@dataclass
class Inventory:
    """Class representing a character's inventory."""
    main_hand: List[Item] = field(default_factory=list)
    off_hand: List[Item] = field(default_factory=list)
    armor: List[Item] = field(default_factory=list)
    items: List[Item] = field(default_factory=list)

    def add_item(self, item: Item, location: str = "items"):
        """Add an item to the specified location in the inventory."""
        print("DEBUG add_item called: --------------------------------")
        if location == "main_hand":
            self.main_hand.append(item)
        elif location == "off_hand":
            self.off_hand.append(item)
        elif location == "armor":
            self.armor.append(item)
        else:
            self.items.append(item)

    def remove_item(self, item: Item, location: str = "items"):
        """Remove an item from the specified location in the inventory."""
        print("DEBUG remove_item called: --------------------------------")
        if location == "main_hand":
            self.main_hand.remove(item)
        elif location == "off_hand":
            self.off_hand.remove(item)
        elif location == "armor":
            self.armor.remove(item)
        else:
            self.items.remove(item)

    def list_items(self, location: str = "items") -> List[Item]:
        """Return a list of all items in the specified location."""
        print("DEBUG list_items called: --------------------------------")
        if location == "main_hand":
            return self.main_hand
        elif location == "off_hand":
            return self.off_hand
        elif location == "armor":
            return self.armor
        else:
            return self.items
        
    def total_weight(self) -> float:
        """Calculate the total weight of all items in the inventory."""
        print("DEBUG total_weight called: --------------------------------")
        total = 0.0
        for item in self.main_hand + self.off_hand + self.armor + self.items:
            total += item.weight
        return total