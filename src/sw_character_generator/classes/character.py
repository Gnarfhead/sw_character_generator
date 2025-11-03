from functions.roleDice import wuerfle_3d6
from functions.genCharStatMods import strengthMod
from dataclasses import dataclass, field

@dataclass
class Character:
    playerName: str = "Unknown"
    characterName: str = "Unnamed Hero"
    alignment: str = "Neutral"
    level: int = 1
    race: str = "Human"
    gender: str = "Undefined"
    god: str = "None"
    age: int = 18
    epBonus: int = 0
    xp: int = 0
    tp: int = 0,
    saveThrow: int = 0
    ac: int = 10
    inventory: list = None
    statStr: int = wuerfle_3d6()
    statDex: int = wuerfle_3d6()
    statCon: int = wuerfle_3d6()
    statWis: int = wuerfle_3d6()
    statInt: int = wuerfle_3d6()
    statChar: int = wuerfle_3d6()
    inventory: list[str] = field(default_factory=list)
    atckBon: int = strengthMod(statStr)
    dmgBon: int = 0
    carryBon: int = 0
    crackDoorBon: int = 0
    rangeBon: int = 0
    acBon: int = 0
    tpBon: int = 0
    raiseDeadBon: int = 0
    addLangs: list[str] = field(default_factory=list)
    capSpecHirelings: int = 0
    treasure: list[str] = field(default_factory=list)
    coins: int = 0

    
    




