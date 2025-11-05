from dataclasses import dataclass, field
from functions.role_dice import wuerfle_3d6
from functions.gen_char_stat_mods import analyze_mod_str, analyze_mod_dex, analyze_mod_con, analyze_mod_int, analyze_mod_char
from classes.fighter import Fighter
from classes.professions import Profession

@dataclass
class Character:
    """Class representing a character in the game."""
    player_name: str = "Unknown"
    character_name: str = "Unnamed Hero"
    #player_class: str = "Fighter"
    profession: Profession = field(default_factory=Fighter)
    tp_dice: int = 8
    main_stat: str = "strength"
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
    allowed_alignment: str = "all"
    allowed_races: str = "all"
    allowed_armor: str = "all"
    allowed_weapon: str = "all"
    
    
    def __post_init__(self):

        self.profession.apply_class_modifiers(self)
        #Calculate and set all STR derived modifiers after initialization."""
        (
            self.strength_atck_mod,
            self.strength_damage_mod,
            self.carry_capacity_mod,
            self.door_crack_mod
        ) = analyze_mod_str(
            self.stat_str,
            self.profession
        )

        #Calculate and set all DEX derived modifiers after initialization."""
        (
            self.ranged_atck_mod,
            self.ac_bon
        ) = analyze_mod_dex(
            self.stat_dex,
            self.profession
        )

        #Calculate and set all CON derived modifiers after initialization."""
        (
            self.tp_bon,
            self.raise_dead_mod
        ) = analyze_mod_con(
            self.stat_con,
            self.profession
        )

        #Calculate and set all INT derived modifiers after initialization."""
        (
            self.max_add_langs,
            self.highest_spell_level,
            self.understand_spell,
            self.min_spells_per_level,
            self.max_spells_per_level
        ) = analyze_mod_int(
            self.stat_int,
            self.profession
        )

        (
            self.cap_spec_hirelings
        ) = analyze_mod_char(
            self.stat_char,
            self.profession
        )
    
    def __repr__(self):
            return (
                f"PlayerName={self.player_name}\n"
                f"CharacterName={self.character_name}\n"
                f"Class={self.profession}\n"
                f"STR: {self.stat_str}    STR_mod: Attack={self.strength_atck_mod}, Damage={self.strength_damage_mod}, "
                f"Carry Capacity={self.carry_capacity_mod}, Door Crack={self.door_crack_mod}\n"
                f"DEX: {self.stat_dex}    DEX_mod: Ranged Attack={self.ranged_atck_mod}, AC Bonus={self.ac_bon}\n"
                f"CON: {self.stat_con}    CON_mod: HP Bonus={self.tp_bon}, Raise Dead Chance={self.raise_dead_mod}%\n"
                f"INT: {self.stat_int}    INT_mod: Languages={self.max_add_langs}, Spell Level={self.highest_spell_level}, "
                f"Understands Spell={self.understand_spell}, "
                f"min/max Spells per Level={self.min_spells_per_level}/{self.max_spells_per_level}\n"
                f"WIS: {self.stat_wis}\n"
                f"CHA: {self.stat_char}    CHA_mod: Max Hirelings={self.cap_spec_hirelings}"
            )
    
    def to_dict(self):
        return {
            "player_name": self.player_name,
            "character_name": self.character_name,
            "profession": self.profession.name,
            "main_stat": self.main_stat,
            "tp_dice": self.tp_dice,
            "level": self.level,
            "alignment": self.alignment,
            "race": self.race,
            "gender": self.gender,
            "god": self.god,
            "age": self.age,
            "xp": self.xp,
            "tp": self.tp,
            "save_throw": self.save_throw,
            "ac": self.ac,
            "stats": {
                "str": self.stat_str,
                "dex": self.stat_dex,
                "con": self.stat_con,
                "wis": self.stat_wis,
                "int": self.stat_int,
                "cha": self.stat_char
            },
            "modifiers": {
                "strength": {
                    "attack": self.strength_atck_mod,
                    "damage": self.strength_damage_mod,
                    "carry_capacity": self.carry_capacity_mod,
                    "door_crack": self.door_crack_mod
                },
                "dexterity": {
                    "ranged_attack": self.ranged_atck_mod,
                    "ac_bonus": self.ac_bon
                },
                "constitution": {
                    "hp_bonus": self.tp_bon,
                    "raise_dead_chance": self.raise_dead_mod
                },
                "intelligence": {
                    "languages": self.max_add_langs,
                    "spell_level": self.highest_spell_level,
                    "understand_spell": self.understand_spell,
                    "min_spells_per_level": self.min_spells_per_level,
                    "max_spells_per_level": self.max_spells_per_level
                },
                "charisma": {
                    "max_hirelings": self.cap_spec_hirelings
                }
            },
            "inventory": self.inventory,
            "treasure": self.treasure,
            "coins": self.coins,
            "allowed_alignment": self.allowed_alignment,
            "allowed_races": self.allowed_races,
            "allowed_armor": self.allowed_armor,
            "allowed_weapon": self.allowed_weapon
        }