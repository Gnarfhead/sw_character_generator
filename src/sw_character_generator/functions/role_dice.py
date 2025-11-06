import random

def wuerfle_3d6(drop_low = None):
    """Würfelt 4 sechsseitige Würfel und gibt die Summe der höchsten 3 zurück, wenn drop_low gesetzt ist."""
    if drop_low is None:
        wuerfe = [random.randint(1, 6) for _ in range(3)]
        print("Würfe:", wuerfe)
    else:
        wuerfe = [random.randint(1, 6) for _ in range(4)]
        print("Würfe:", wuerfe, "-> niedrigster Wurf wird entfernt.")
        wuerfe.remove(min(wuerfe))
    summe = sum(wuerfe)
    return summe

def wuerfle_1d6(count: int):
    """Würfelt sechsseitige Würfel und gibt die Summe zurück."""
    wuerfe = [random.randint(1, 6) for _ in range(count)]
    print("Würfe:", wuerfe)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d4(count: int):
    """Würfelt vierseitige Würfel und gibt die Summe zurück."""
    wuerfe = [random.randint(1, 4) for _ in range(count)]
    print("Würfe:", wuerfe)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d8(count: int):
    """Würfelt achtseitige Würfel und gibt die Summe zurück."""
    wuerfe = [random.randint(1, 8) for _ in range(count)]
    print("Würfe:", wuerfe)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d10(count: int):
    """Würfelt zehnseitige Würfel und gibt die Summe zurück."""
    wuerfe = [random.randint(1, 10) for _ in range(count)]
    print("Würfe:", wuerfe)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d12(count: int):
    """Würfelt zwölfseitige Würfel und gibt die Summe zurück."""
    wuerfe = [random.randint(1, 12) for _ in range(count)]
    print("Würfe:", wuerfe)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d20(count: int):
    """Würfelt zwanzigseitige Würfel und gibt die Summe zurück."""
    wuerfe = [random.randint(1, 20) for _ in range(count)]
    print("Würfe:", wuerfe)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d100(count: int):
    """Würfelt hundertseitige Würfel und gibt die Summe zurück."""
    wuerfe = [random.randint(1, 100) for _ in range(count)]
    print("Würfe:", wuerfe)
    summe = sum(wuerfe)
    return summe

