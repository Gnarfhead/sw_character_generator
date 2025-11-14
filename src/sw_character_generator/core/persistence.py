import json
from dataclasses import asdict
from typing import Optional
from src.sw_character_generator.core.models import LocalPlayer

DEFAULT_PATH = "last_player.json"

def save_local_player(lp: LocalPlayer, path: str = DEFAULT_PATH) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(asdict(lp), fh, ensure_ascii=False, indent=2)

def load_local_player(path: str = DEFAULT_PATH) -> Optional[LocalPlayer]:
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        return LocalPlayer(**{k: data.get(k, "") for k in ("player_name","character_name","age","gender","deity")})
    except Exception:
        return None