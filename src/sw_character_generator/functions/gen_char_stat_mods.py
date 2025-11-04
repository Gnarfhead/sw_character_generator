def strength_atck_mod(strength: int):
    """Calculate attack modifier based on strength score."""
    if strength <= 4 and strength >= 3:
        return -2
    elif strength <= 6 and strength >= 5:
        return -1
    elif strength <= 8 and strength >= 7:
        return 0
    elif strength <= 12 and strength >= 9:
        return 0
    elif strength <= 15 and strength >= 13:
        return +1
    elif strength == 16:
        return +1
    elif strength == 17:
        return +2
    elif strength == 18:
        return +2
    
def strength_damage_mod(strength: int):
    """Calculate damage modifier based on strength score."""
    if strength <= 4 and strength >= 3:
        return -1
    elif strength <= 6 and strength >= 5:
        return -0
    elif strength <= 8 and strength >= 7:
        return 0
    elif strength <= 12 and strength >= 9:
        return 0
    elif strength <= 15 and strength >= 13:
        return +0
    elif strength == 16:
        return +1
    elif strength == 17:
        return +2
    elif strength == 18:
        return +3
    
def carry_capacity_mod(strength: int):
    """Calculate carrying capacity modifier based on strength score."""
    if strength <= 4 and strength >= 3:
        return -5
    elif strength <= 6 and strength >= 5:
        return -2.5
    elif strength <= 8 and strength >= 7:
        return 0
    elif strength <= 12 and strength >= 9:
        return +2.5
    elif strength <= 15 and strength >= 13:
        return +5
    elif strength == 16:
        return +7.5
    elif strength == 17:
        return +15
    elif strength == 18:
        return +25

def door_crack_mod(strength: int):
    """Calculate door cracking modifier based on strength score."""
    if strength <= 4 and strength >= 3:
        return 1
    elif strength <= 6 and strength >= 5:
        return 1
    elif strength <= 8 and strength >= 7:
        return 2
    elif strength <= 12 and strength >= 9:
        return 2
    elif strength <= 15 and strength >= 13:
        return 2
    elif strength == 16:
        return 3
    elif strength == 17:
        return 4
    elif strength == 18:
        return 5
    

def ranged_atck_mod(dexterity: int):
    """Calculate ranged attack modifier based on dexterity score."""
    if dexterity <= 8 and dexterity >= 3:
        return -1
    elif dexterity <= 12 and dexterity >= 9:
        return 0
    elif dexterity <= 18 and dexterity >= 13:
        return +1
        
def armor_class_mod(dexterity: int):
    """Calculate armor class modifier based on dexterity score."""
    if dexterity <= 8 and dexterity >= 3:
        return -1
    elif dexterity <= 12 and dexterity >= 9:
        return 0
    elif dexterity <= 18 and dexterity >= 13:
        return +1
    
def tp_mod(constitution: int):
    """Calculate TP modifier based on constitution score."""
    if constitution <= 8 and constitution >= 3:
        return -1
    elif constitution <= 12 and constitution >= 9:
        return 0
    elif constitution <= 18 and constitution >= 13:
        return +1
    
def raise_dead_mod(constitution: int):
    """Calculate raise dead modifier based on constitution score."""
    if constitution <= 8 and constitution >= 3:
        return 50
    elif constitution <= 12 and constitution >= 9:
        return 75
    elif constitution <= 18 and constitution >= 13:
        return 100