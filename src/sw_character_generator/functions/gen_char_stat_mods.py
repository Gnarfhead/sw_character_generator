
"""Functions to analyze character stats and return corresponding modifiers."""
from sw_character_generator.classes.player_enums import Professions


def analyze_mod_str(strength: float, character_class: str):
    """Calculate strength-based modifiers. Positive bonuses only apply to fighters."""
    if 3 <= strength <= 4:
        return -2, -1, -5, 1
    elif 5 <= strength <= 6:
        return -1, 0, -2.5, 1
    elif 7 <= strength <= 8:
        return 0, 0, 0, 2
    elif 9 <= strength <= 12:
        return 0, 0, 2.5, 2
    elif 13 <= strength <= 15:
        strength_atck_mod = 1 if character_class == Professions.FIGHTER else 0
        #strength_atck_mod = 1 if character_class.name.lower() == "fighter" else 0
        return strength_atck_mod, 0, 5, 2
    elif strength == 16:
        #strength_atck_mod = 1 if character_class.name.lower() == "fighter" else 0
        #strength_damage_mod = 1 if character_class.name.lower() == "fighter" else 0
        strength_atck_mod = 1 if character_class == Professions.FIGHTER else 0
        strength_damage_mod = 1 if character_class == Professions.FIGHTER else 0
        return strength_atck_mod, strength_damage_mod, 7.5, 3
    elif strength == 17:
        #strength_atck_mod = 2 if character_class.name.lower() == "fighter" else 0
        #strength_damage_mod = 2 if character_class.name.lower() == "fighter" else 0
        strength_atck_mod = 2 if character_class == Professions.FIGHTER else 0
        strength_damage_mod = 2 if character_class == Professions.FIGHTER else 0
        return strength_atck_mod, strength_damage_mod, 15, 4
    elif strength == 18:
        #strength_atck_mod = 2 if character_class.name.lower() == "fighter" else 0
        #strength_damage_mod = 3 if character_class.name.lower() == "fighter" else 0
        strength_atck_mod = 2 if character_class == Professions.FIGHTER else 0
        strength_damage_mod = 3 if character_class == Professions.FIGHTER else 0
        return strength_atck_mod, strength_damage_mod, 25, 5
    else:
        return None

def analyze_mod_dex(dexterity: int, character_class: str):
    """Calculate dexterity based modifiers."""
    if 3 <= dexterity <= 8:
        return -1, -1
    elif 9 <= dexterity <= 12:
        return 0, 0
    elif 13 <= dexterity <= 18:
        return 1, 1
    else:
        return None

def analyze_mod_con(constitution: int, character_class: str):
    """Calculate constitution based modifiers."""
    if 3 <= constitution <= 8:
        return -1, 50
    elif 9 <= constitution <= 12:
        return 0, 75
    elif 13 <= constitution <= 18:
        return 1, 100
    else:
        return None

def analyze_mod_int(intelligence: int, character_class: str):
    """Calculate intelligence based modifiers."""
    if 3 <= intelligence <= 7:
        return 0, 4, 30, 2, 4
    elif intelligence == 8:
        return 1, 5, 40, 3, 5
    elif intelligence == 9:
        return 1, 6, 45, 4, 6
    elif intelligence == 10:
        return 2, 5, 50, 4, 6
    elif intelligence == 11:
        return 2, 6, 50, 4, 6
    elif intelligence == 12:
        return 3, 5, 55, 4, 6
    elif intelligence == 13:
        return 3, 6, 65, 5, 7
    elif intelligence == 14:
        return 4, 7, 65, 5, 8
    elif intelligence == 15:
        return 4, 8, 75, 6, 10
    elif intelligence == 16:
        return 5, 8, 75, 6, 10
    elif intelligence == 17:
        return 5, 9, 85, 7, 100
    elif intelligence == 18:
        return 6, 9, 95, 8, 100
    else:
        return None
    
def analyze_mod_char(charisma: int, character_class: str):
    """Calculate charisma based modifiers."""
    if 3 <= charisma <= 4:
        return 1
    elif 5 <= charisma <= 6:
        return 2
    elif 7 <= charisma <= 8:
        return 3
    elif 9 <= charisma <= 12:
        return 4
    elif 13 <= charisma <= 15:
        return 5
    elif 16 <= charisma <= 17:
        return 6
    elif charisma == 18:
        return 7
    else:
        return None
