import json
from dataclasses import asdict
from typing import Optional
from src.sw_character_generator.core.models import LocalPlayer

DEFAULT_PATH = "last_player.json"

def save_local_player(lp: LocalPlayer, path: str = DEFAULT_PATH) -> None:
    try:
        print(f"Saving LocalPlayer to {path}...")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(asdict(lp), fh, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving LocalPlayer: {e}")

def load_local_player(path: str = DEFAULT_PATH) -> Optional[LocalPlayer]:
    try:
        print(f"Loading LocalPlayer from {path}...")
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        return LocalPlayer(**{k: data.get(k, "") for k in ("player_name","character_name","age","gender","deity")})
    except Exception as e:
        print(f"Error loading LocalPlayer: {e}")
        return None