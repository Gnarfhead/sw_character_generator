"""Definition of the Item class for the Swords & Wizardry character generator."""

from dataclasses import dataclass, field
from typing import Any, Optional, List

@dataclass
class Item:
    name: str
    type: str                     # z.B. "weapon", "armor", "consumable", etc.
    value: str                   # z.B. "10 GM"
    weight: float                # Gewicht des Items
    damage: Optional[str] = None  # z.B. "1d6", nur für Waffen
    acbonus: Optional[int] = None # Rüstungsbonus, nur für Rüstungen
    atckbonus: Optional[int] = None # Angriffsbonus, nur für Waffen
    dmgbonus: Optional[int] = None  # Schadensbonus, nur für Waffen
    twohanded: bool = False        # Nur für Waffen
    versatile: bool = False       # Nur für Waffen
    weapontype: Optional[str] = None # z.B. "melee", "ranged", nur für Waffen
    firerate: Optional[int] = None   # 
    count: Optional[int] = None      # Nur für Verbrauchsgegenstände
    range: Optional[int] = None     # Nur für Fernkampfwaffen
    armortype: Optional[str] = None  # z.B. "light", "medium", "heavy", nur für Rüstungen
    description: str = ""
    tags: List[str] = field(default_factory=list) 

    def to_dict(self) -> dict[str, Any]:
        """Convert the item to a dictionary."""
        return {
            "name": self.name,
            "type": self.type,
            "value": self.value,
            "weight": self.weight,
            "damage": self.damage,
            "acbonus": self.acbonus,
            "atckbonus": self.atckbonus,
            "dmgbonus": self.dmgbonus,
            "twohanded": self.twohanded,
            "versatile": self.versatile,
            "weapontype": self.weapontype,
            "firerate": self.firerate,
            "count": self.count,
            "range": self.range,
            "armortype": self.armortype,
            "description": self.description,
            "tags": self.tags
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Item":
        """Create an item from a dictionary."""
        return cls(
            name=data.get("name", ""),
            type=data.get("type", ""),
            value=data.get("value", "0 GM"),
            weight=float(data.get("weight", 0)),
            damage=data.get("damage"),
            acbonus=data.get("acbonus"),
            atckbonus=data.get("atckbonus"),
            dmgbonus=data.get("dmgbonus"),
            twohanded=data.get("twohanded", False),
            versatile=data.get("versatile", False),
            weapontype=data.get("weapontype"),
            firerate=data.get("firerate"),
            count=data.get("count"),
            range=data.get("range"),
            armortype=data.get("armortype"),
            description=data.get("description", ""),
            tags=data.get("tags", [])
        )