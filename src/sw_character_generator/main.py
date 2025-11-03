"""
from gui.app import Application

if __name__ == "__main__":
    app = Application()
    app.run()
"""

from classes.character import PlayerCharacter

bob = PlayerCharacter("Bob")
print(bob.playerName)
print(bob.statStr)