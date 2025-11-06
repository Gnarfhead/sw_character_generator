import random

def wuerfle_3d6(str_desc: str, drop_low = None):
    """Würfelt 4 sechsseitige Würfel und gibt die Summe der höchsten 3 zurück, wenn drop_low gesetzt ist."""
    if drop_low is None:
        wuerfe = [random.randint(1, 6) for _ in range(3)]
        print("Würfe:", wuerfe, str_desc)
    else:
        wuerfe = [random.randint(1, 6) for _ in range(4)]
        print("Würfe:", wuerfe, "-> niedrigster Wurf wird entfernt.", str_desc)
        wuerfe.remove(min(wuerfe))
    summe = sum(wuerfe)
    return summe

def wuerfle_1d6(str_desc: str, count: int):
    """Würfelt sechsseitige Würfel und gibt die Summe zurück."""
    wuerfe = [random.randint(1, 6) for _ in range(count)]
    print("Würfe:", wuerfe, str_desc)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d4(str_desc: str, count: int):
    """Würfelt vierseitige Würfel und gibt die Summe zurück."""
    wuerfe = [random.randint(1, 4) for _ in range(count)]
    print("Würfe:", wuerfe, str_desc)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d8(str_desc: str, count: int):
    """Würfelt achtseitige Würfel und gibt die Summe zurück."""
    wuerfe = [random.randint(1, 8) for _ in range(count)]
    print("Würfe:", wuerfe, str_desc)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d10(str_desc: str, count: int):
    """Würfelt zehnseitige Würfel und gibt die Summe zurück."""
    wuerfe = [random.randint(1, 10) for _ in range(count)]
    print("Würfe:", wuerfe, str_desc)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d12(str_desc: str, count: int):
    """Würfelt zwölfseitige Würfel und gibt die Summe zurück."""
    wuerfe = [random.randint(1, 12) for _ in range(count)]
    print("Würfe:", wuerfe, str_desc)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d20(str_desc: str, count: int):
    """Würfelt zwanzigseitige Würfel und gibt die Summe zurück."""
    wuerfe = [random.randint(1, 20) for _ in range(count)]
    print("Würfe:", wuerfe, str_desc)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d100(str_desc: str, count: int):
    """Würfelt hundertseitige Würfel und gibt die Summe zurück."""
    wuerfe = [random.randint(1, 100) for _ in range(count)]
    print("Würfe:", wuerfe, str_desc)
    summe = sum(wuerfe)
    return summe

