from character import PlayerCharacter

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
        allowedWeapon = "all"
    ):
        super().__init__(
            characterName=characterName,
            #playerClass=playerClass,
            mainStat=mainStat
        )
        self.playerClass = playerClass
        self.tpDice = tpDice
        self.allowedAlignment = allowedAlignment
        self.allowedRaces = allowedRaces
        self.allowedArmor = allowedArmor
        self.allowedWeapon = allowedWeapon



bob = Fighter("Bob")
print(bob.characterName)
print(bob.playerClass)