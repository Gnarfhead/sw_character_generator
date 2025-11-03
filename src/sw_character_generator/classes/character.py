from src.sw_character_generator.functions.roleDice import wuerfle_3d6


#/workspaces/sw_character_generator/src/sw_character_generator/functions/roleDice.py

class PlayerCharacter:
    def __init__(
        self,
        playerName: str = "",
        characterName: str = "",
        alignment: str = "",
        level: int = 1,
        race: str = "",
        gender: str = "",
        god: str = "",
        age: int = 18,
        epBonus: int = 0,
        xp: int = 0,
        tp: int = 0, 
        savThrow: int = 0,
        ac: int = 10,
        inventory: list = None,
        statStr: int = 0,
        statDex: int = 0,
        statCon: int = 0,
        statWis: int = 0,
        statInt: int = 0,
        statChar: int = 0
    ):
        self.playerName = playerName
        self.characterName = characterName
        self.alignment = alignment
        self.level = level
        self.race = race
        self.gender = gender
        self.god = god
        self.age = age
        self.epBonus = epBonus
        self.xp = xp
        self.tp = tp
        self.savThrow = savThrow
        self.ac = ac
        self.inventory = inventory if inventory is not None else []
        self.statStr = wuerfle_3d6()



class Fighter(PlayerCharacter):
    def __init__(
        self,
        characterName: str = "",
        playerClass: str = "Fighter",
        tpDice: int = 8,
        mainStat: str = "strength",
        allowedAlignment: str = "all",
        allowedRaces: str = "all",
        allowedArmor: str = "all",
        allowedWeapon: str = "all",
        statStr: int = 0
    ):
        super().__init__(
            statStr=statStr
            )
        self.characterName = characterName
        self.playerClass = playerClass
        self.tpDice = tpDice
        self.mainStat = mainStat
        self.allowedAlignment = allowedAlignment
        self.allowedRaces = allowedRaces
        self.allowedArmor = allowedArmor
        self.allowedWeapon = allowedWeapon


