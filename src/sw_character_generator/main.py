"""
from gui.app import Application

if __name__ == "__main__":
    app = Application()
    app.run()
"""

from classes.character import Character

bob = Character(characterName="Bob")
#print(f"{bob.characterName} created with the following stats:")
#print(f"{bob.statStr} STR   {bob.statDex} DEX   {bob.statCon} CON  {bob.statWis} WIS   {bob.statInt} INT   {bob.statChar} CHAR")
#print(f"{bob.statStr} - {bob.atckBon}")
print(bob)