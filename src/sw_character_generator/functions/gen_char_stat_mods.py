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
    


        