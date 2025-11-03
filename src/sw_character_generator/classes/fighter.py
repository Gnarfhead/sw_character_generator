from dataclasses import dataclass

@dataclass
class Fighter:
    playerClass: str = "Fighter",
    tpDice: int = 8,
    mainStat: str = "strength",
    allowedAlignment: str = "all",
    allowedRaces: str = "all",
    allowedArmor: str = "all",
    allowedWeapon: str = "all"
    