import random

def wuerfle_3d6(drop_low = None):
    """Würfelt 4 sechsseitige Würfel und gibt die Summe und Einzelwürfe zurück."""
    if drop_low is None:
        wuerfe = [random.randint(1, 6) for _ in range(3)]
    else:
        wuerfe = [random.randint(1, 6) for _ in range(4)]
        wuerfe.remove(min(wuerfe))
    summe = sum(wuerfe)
    return summe
