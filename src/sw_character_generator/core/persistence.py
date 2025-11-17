"""Persistence module for saving and loading character data."""
from sw_character_generator.functions.save_character import save_character

def save_characterobj(character):
   """Saves the character to a file."""
   try:
       save_character(character)
   except Exception as e:
       print(f"Error saving character: {e}\n")
   else:
       print("Character saved.\n")
