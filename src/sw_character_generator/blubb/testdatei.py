from dataclasses import dataclass

@dataclass
class Adresse:
    strasse: str
    stadt: str
    plz: str

@dataclass
class Kontakt:
    email: str
    telefon: str

@dataclass
class Person:
    name: str
    adresse: Adresse
    kontakt: Kontakt

# Objekt zusammensetzen
adresse = Adresse(strasse="Musterstraße 1", stadt="Karlsruhe", plz="76133")
kontakt = Kontakt(email="daniel@example.com", telefon="0721-123456")
person = Person(name="Daniel", adresse=adresse, kontakt=kontakt)

print(person.adresse.strasse)


