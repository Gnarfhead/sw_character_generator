from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class LocalPlayer:
    """Minimaler DTO für Werte aus der GUI."""
    player_name: str = ""
    character_name: str = ""
    age: str = ""            # roher String aus dem GUI-Entry
    gender: str = ""
    deity: str = ""

@dataclass
class Character:
    """Einfaches Character-Objekt, das die GUI-Daten typisiert aufnimmt."""
    player_name: str
    character_name: str
    age: Optional[int] = None
    gender: Optional[str] = None
    deity: Optional[str] = None
    level: int = 1

    def to_dict(self):
        return asdict(self)