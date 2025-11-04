"""
from gui.app import Application

if __name__ == "__main__":
    app = Application()
    app.run()
"""

from dataclasses import make_dataclass, asdict
from classes.character import Character
from classes.fighter import Fighter

#def main():
player_character = Character(playerName="Alice", characterName="Thorin")
#player_class = Fighter(playerClass="Fighter")
player_class = Fighter(playerClass="Fighter")

merged_character = asdict(player_class) | asdict(player_character)
FinalPlayerCharacter = make_dataclass("FinalPlayerCharacter", merged_character.keys())
final_character_instance = FinalPlayerCharacter(**merged_character)

print(final_character_instance)
print(f"Character Details: {final_character_instance.characterName}, Class: {final_character_instance.playerClass}")
print(final_character_instance.characterName, final_character_instance.playerClass)


    

