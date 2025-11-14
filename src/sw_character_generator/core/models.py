from dataclasses import dataclass

@dataclass
class LocalPlayer:
    player_name: str = ""
    character_name: str = ""
    age: str = ""
    gender: str = ""
    deity: str = ""