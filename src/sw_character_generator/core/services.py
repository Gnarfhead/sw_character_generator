from .models import LocalPlayer
from src.sw_character_generator.core.persistence import save_local_player, load_local_player
from sw_character_generator.classes.playerclass import PlayerClass
import sys

def bind_to_playerclass(lp: LocalPlayer) -> bool:
    """Best-effort: versuche PlayerClass zu instanziieren und Felder zu setzen."""
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
    any_set = False
    for local_field, candidates in mappings.items():
        val = getattr(lp, local_field)
        for cand in candidates:
            try:
                if hasattr(p, cand):
                    setattr(p, cand, val)
                    any_set = True
                    break
                setter = f"set_{cand}"
                if hasattr(p, setter):
                    getattr(p, setter)(val)
                    any_set = True
                    break
            except Exception:
                continue
    if any_set:
        save_local_player(lp)
    return any_set

def save_player_local(lp: LocalPlayer, path: str = None):
    save_local_player(lp, path) if path else save_local_player(lp)