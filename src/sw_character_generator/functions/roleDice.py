import random

def wuerfle_3d6(dropLow=None):
    """Würfelt 4 sechsseitige Würfel und gibt die Summe und Einzelwürfe zurück."""
    
    if dropLow is None:
        print(f"Drop lowest ist inaktiv")
        wuerfe = [random.randint(1, 6) for _ in range(3)] 
        print(f"Würfe: {wuerfe}")       
    else:    
        print(f"Drop lowest ist aktiv")
        wuerfe = [random.randint(1, 6) for _ in range(4)] 
        print(f"Würfe: {wuerfe}") 
        wuerfe.remove(min(wuerfe))  
                  
    summe = sum(wuerfe)
    return summe, wuerfe

# Beispielaufruf
summe, gesamt = wuerfle_3d6(dropLow=None)
print(f"Würfe: {gesamt}")
print(f"Summe: {summe}")