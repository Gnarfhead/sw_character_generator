from typing import Optional
from typing import Tuple
from src.sw_character_generator.core.models import LocalPlayer, Character


def parse_age(age_str: str) -> Tuple[Optional[int], Optional[str]]:
    """Versuche, das Alter als int zu parsen. Liefere (age, error_message)."""
    if age_str is None:
        return None, None
    s = age_str.strip()
    if s == "":
        return None, None
    try:
        a = int(s)
        if a < 0:
            return None, "Alter darf nicht negativ sein."
        return a, None
    except ValueError:
        return None, "Ungültiges Alter: bitte Zahl eingeben."

def character_from_localplayer(lp: LocalPlayer, default_level: int = 1) -> Tuple[Character, list]:
    """Erzeuge ein Character-Objekt aus LocalPlayer. Gibt (Character, errors) zurück."""
    errors = []

    age, age_err = parse_age(lp.age)
    if age_err:
        errors.append(age_err)

    # Trimme Strings
    player_name = (lp.player_name or "").strip()
    character_name = (lp.character_name or "").strip()
    gender = (lp.gender or "").strip() or None
    deity = (lp.deity or "").strip() or None

    if not player_name:
        errors.append("Spieler:in darf nicht leer sein.")
    if not character_name:
        errors.append("SC Name darf nicht leer sein.")

    char = Character(
        player_name=player_name,
        character_name=character_name,
        age=age,
        gender=gender,
        deity=deity,
        level=default_level
    )
    return char, errors