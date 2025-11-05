from dataclasses import dataclass, field
from functions.role_dice import wuerfle_3d6
from functions.gen_char_stat_mods import analyze_mod_str, analyze_mod_dex, analyze_mod_con, analyze_mod_int, analyze_mod_char


@dataclass
class Character:
    """Class representing a character in the game."""
    player_name: str = "Unknown"
    character_name: str = "Unnamed Hero"
    alignment: str = "Neutral"
    level: int = 1
    race: str = "Human"
    gender: str = "Undefined"
    god: str = "None"
    age: int = 18
    ep_bonus: int = 0
    xp: int =0
    tp: int = 0
    save_throw: int = 0
    ac: int = 10
    stat_str: int = wuerfle_3d6()
    stat_dex: int = wuerfle_3d6()
    stat_con: int = wuerfle_3d6()
    stat_wis: int = wuerfle_3d6()
    stat_int: int = wuerfle_3d6()
    stat_char: int = wuerfle_3d6()
    inventory: list[str] = field(default_factory=list)
    strength_atck_mod: float = field(init=False)
    strength_damage_mod: float = field(init=False)
    carry_capacity_mod: float = field(init=False)
    door_crack_mod: float = field(init=False)
    ranged_atck_mod: int = field(init=False)
    ac_bon: int = field(init=False)
    tp_bon: int = field(init=False)
    raise_dead_mod: int = field(init=False)
    max_add_langs: int = field(init=False)
    highest_spell_level: int = field(init=False)
    understand_spell: int = field(init=False)
    min_spells_per_level: int = field(init=False)
    max_spells_per_level: int = field(init=False)
    add_langs: list[str] = field(default_factory=list)
    cap_spec_hirelings: int = field(init=False)
    treasure: list[str] = field(default_factory=list)
    coins: int = 0

    def __post_init__(self):
        (
            self.strength_atck_mod,
            self.strength_damage_mod,
            self.carry_capacity_mod,
            self.door_crack_mod
        ) = analyze_mod_str(self.stat_str)
        (
            self.ranged_atck_mod,
            self.ac_bon
        ) = analyze_mod_dex(self.stat_dex)
        (
            self.tp_bon,
            self.raise_dead_mod
        ) = analyze_mod_con(self.stat_con)
        (
            self.max_add_langs,
            self.highest_spell_level,
            self.understand_spell,
            self.min_spells_per_level,
            self.max_spells_per_level
        ) = analyze_mod_int(self.stat_int)
        (
            self.cap_spec_hirelings
        ) = analyze_mod_char(self.stat_char)
