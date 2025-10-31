import random

def wuerfle_3d6():
    """Würfelt 3 sechsseitige Würfel und gibt die Summe und Einzelwürfe zurück."""
    wuerfe = [random.randint(1, 6) for _ in range(3)]
    summe = sum(wuerfe)
    return summe

# Beispielaufruf
gesamt = wuerfle_3d6()
print(f"Summe: {gesamt}")