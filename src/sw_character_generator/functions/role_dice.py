import random

def wuerfle_3d6(str_desc: str, drop_low = None):
    """Rolls three six-sided dice and returns the sum. If drop_low is provided, rolls four dice and drops the lowest."""
    if drop_low is None:
        wuerfe = [random.randint(1, 6) for _ in range(3)]
        #print("Rolls:", wuerfe, str_desc)
    else:
        wuerfe = [random.randint(1, 6) for _ in range(4)]
        #print("Rolls:", wuerfe, "-> lowest roll is dropped.", str_desc)
        wuerfe.remove(min(wuerfe))
    summe = sum(wuerfe)
    return summe

def wuerfle_1d6(str_desc: str, count: int):
    """Rolls six-sided dice and returns the sum."""
    wuerfe = [random.randint(1, 6) for _ in range(count)]
    #print("Rolls:", wuerfe, str_desc)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d4(str_desc: str, count: int):
    """Rolls four-sided dice and returns the sum."""
    wuerfe = [random.randint(1, 4) for _ in range(count)]
    #print("Rolls:", wuerfe, str_desc)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d8(str_desc: str, count: int):
    """Rolls eight-sided dice and returns the sum."""
    wuerfe = [random.randint(1, 8) for _ in range(count)]
    #print("Rolls:", wuerfe, str_desc)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d10(str_desc: str, count: int):
    """Rolls ten-sided dice and returns the sum."""
    wuerfe = [random.randint(1, 10) for _ in range(count)]
    #print("Rolls:", wuerfe, str_desc)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d12(str_desc: str, count: int):
    """Rolls twelve-sided dice and returns the sum."""
    wuerfe = [random.randint(1, 12) for _ in range(count)]
    #print("Rolls:", wuerfe, str_desc)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d20(str_desc: str, count: int):
    """Rolls twenty-sided dice and returns the sum."""
    wuerfe = [random.randint(1, 20) for _ in range(count)]
    #print("Rolls:", wuerfe, str_desc)
    summe = sum(wuerfe)
    return summe

def wuerfle_1d100(str_desc: str, count: int):
    """Rolls one hundred-sided dice and returns the sum."""
    wuerfe = [random.randint(1, 100) for _ in range(count)]
    #print("Rolls:", wuerfe, str_desc)
    summe = sum(wuerfe)
    return summe

