"""Docstring for sw_character_generator.classes.item module."""

from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Item:
    name: str
    damage: Optional[int] = None        # Schadenswert, falls Waffe
    ac_bonus: Optional[int] = None      # Rüstungsbonus, falls Rüstung
    spell_slots: Optional[int] = None   # Zauberplätze, falls Zauberbuch
    two_handed: bool = False
    weight: float = 0.0              # Pfund o.ä.
    value: int = 0                   # in Münzen
    description: str = ""
    tags: List[str] = field(default_factory=list) # z.B. "melee", "ranged", "light armor", etc.