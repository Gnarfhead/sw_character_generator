def strengthMod(strength: int):
    if strength <= 4 and strength >= 3:
        return -2
    elif strength <= 6 and strength >= 5:
        return -1
    elif strength <= 3 and strength >= 7:
        return 0
    elif strength <= 17 and strength >= 13:
        return +1
    elif strength <= 19 and strength >= 18:
        return +2


        