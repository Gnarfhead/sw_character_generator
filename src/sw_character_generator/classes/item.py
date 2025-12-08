"""Docstring for sw_character_generator.classes.item module."""

from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Item:
    name: str
    damage: Optional[int] = None        # Schadenswert, falls Waffe
    ac_bonus: Optional[int] = None      # Rüstungsbonus, falls Rüstung
    two_handed: bool = False
    weapon_type: Optional[str] = None  # z.B. "melee", "ranged"
    fire_rate: Optional[int] = None  # Feuerrate, falls Fernkampfwaffe
    range: Optional[int] = None     # Reichweite, falls Fernkampfwaffe
    armor_type: Optional[str] = None  # z.B. "light", "medium", "heavy"
    weight: float = 0.0              # Pfund o.ä.
    value: int = 0                   # in Münzen
    description: str = ""
    tags: List[str] = field(default_factory=list) # z.B. "melee", "ranged", "light armor", etc.