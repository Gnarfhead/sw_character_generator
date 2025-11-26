"""Module defining the Item class for inventory management."""
from dataclasses import dataclass

@dataclass
class Item:
    """Class representing an item in the inventory."""
    name: str
    description: str = ""
    value_copper: int = 0
    weight: float = 0.0
    quantity: int = 1
    category: str = "Miscellaneous"
    equipped: bool = False

    def __hash__(self):
        """Hash based on name to allow usage in sets if needed."""
        return hash(self.name)
    
    def __eq__(self, other):
        """Two items are equal if they have the same name."""
        if not isinstance(other, Item):
            return False
        return self.name == other.name
    
    def __repr__(self):
        """String representation of the item."""
        equipped_str = " [EQUIPPED]" if self.equipped else ""
        if self.quantity > 1:
            return f"{self.name} x{self.quantity}{equipped_str} ({self.weight * self.quantity} lbs, {self.value_copper * self.quantity} cp)"
        return f"{self.name}{equipped_str} ({self.weight} lbs, {self.value_copper} cp)"
    
    def to_dict(self):
        """Convert Item to dictionary for JSON serialization."""
        return {
            "name": self.name,
            "quantity": self.quantity,
            "weight": self.weight,
            "value_copper": self.value_copper,
            "description": self.description,
            "category": self.category,
            "equipped": self.equipped
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Item":
        """Create Item from dictionary."""
        return cls(
            name=data.get("name", "Unknown Item"),
            quantity=data.get("quantity", 1),
            weight=data.get("weight", 0.0),
            value_copper=data.get("value_copper", 0),
            description=data.get("description", ""),
            category=data.get("category", "Misc"),
            equipped=data.get("equipped", False)
        )