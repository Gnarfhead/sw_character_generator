"""
from gui.app import Application

if __name__ == "__main__":
    app = Application()
    app.run()
"""

from classes.character import Character

bob = Character(characterName="Bob")
print(bob)