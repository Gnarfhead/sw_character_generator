#from sw_character_generator.functions import roleDice

class PlayerCharacter:
    def __init__(
        self,
        playerName: str = "",
        characterName: str = "",
        #playerClass: str = "",
        alignment: str = "",
        mainStat: str = "",
        level: int = 1,
        race: str = "",
        gender: str = "",
        god: str = "",
        age: int = 18,
        epBonus: int = 1,
        xp: int = 0,
        tp: int = 0, 
        savThrow: int = 0,
        ac: int = 10,
        inventory: list = None
    ):
        self.playerName = playerName
        self.characterName = characterName
        #self.playerClass = playerClass
        self.alignment = alignment
        self.mainStat = mainStat
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
