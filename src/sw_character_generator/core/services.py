from typing import Tuple, Optional
from .models import LocalPlayer, Character
from .persistence import save_local_player
import sys

def parse_age(age_str: str) -> Tuple[Optional[int], Optional[str]]:
    """Parst age_str in ein Optional[int].
    Gibt (age, None) zurück bei Erfolg, sonst (None, error_message).
    """
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
    """Erstellt Character aus LocalPlayer."""
    errors = []
    age, age_err = parse_age(lp.age)
    if age_err:
        errors.append(age_err)
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

def bind_to_playerclass(lp: LocalPlayer, PlayerClass) -> bool:
    """Best-effort: versucht PlayerClass zu instanziieren und Felder zu setzen.
    PlayerClass wird als Abhängigkeit injiziert, damit Tests leichter sind."""
    try:
        p = PlayerClass()
    except Exception:
        try:
            p = PlayerClass(lp.player_name, lp.character_name)
        except Exception as e:
            print("Could not instantiate PlayerClass:", e, file=sys.stderr)
            return False

    mappings = {
        "player_name": ["player_name", "player", "playername", "owner"],
        "character_name": ["character_name", "character", "name", "char_name"],
        "age": ["age", "alter"],
        "gender": ["gender", "sex"],
        "deity": ["deity", "god", "gottheit"],
    }

    success_any = False
    for local_field, candidates in mappings.items():
        val = getattr(lp, local_field)
        for cand in candidates:
            try:
                if hasattr(p, cand):
                    setattr(p, cand, val)
                    success_any = True
                    break
                setter = f"set_{cand}"
                if hasattr(p, setter):
                    getattr(p, setter)(val)
                    success_any = True
                    break
            except Exception:
                continue

    if success_any:
        save_local_player(lp)  # persist local copy as well
    return success_any