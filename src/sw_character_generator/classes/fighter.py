from dataclasses import dataclass

@dataclass
class Fighter:
    """Class representing a Fighter character class."""
    player_class: str = "Fighter"
    tp_dice: int = 8
    main_stat: str = "strength"
    allowed_alignment: str = "all"
    allowed_races: str = "all"
    allowed_armor: str = "all"
    allowed_weapon: str = "all"
