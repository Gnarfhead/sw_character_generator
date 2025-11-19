"""Module defining the PlayerClass dataclass for character representation."""
from dataclasses import dataclass, field

@dataclass
class PlayerClass:
    """Class representing a character in the game."""
    player_name: str = "Unknown"
    character_name: str = "Unnamed Hero"
    profession: str = "Undefined"
    hp_dice: int = 0
    main_stats: str = "Undefined"
    player_state: str = "alive"
    alignment: str = "Undefined"
    level: int = 1
    race: str = "Undefined"
    gender: str = "Undefined"
    god: str = "Undefined"
    age: int = 0
    xp_bonus = 0
    xp: int = 0
    hp: int = 0
    save_throw: int = 0
    save_bonuses: tuple[str, ...] = field(default_factory=tuple)
    immunity: tuple[str, ...] = field(default_factory=tuple)
    special_abilities: tuple[str, ...] = field(default_factory=tuple)
    ac: int = 10
    stat_str: int = field(default=0)
    stat_dex: int = field(default=0)
    stat_con: int = field(default=0)
    stat_wis: int = field(default=0)
    stat_int: int = field(default=0)
    stat_char: int = field(default=0)
    inventory: list[str] = field(default_factory=list)
    strength_atck_mod: float = 0.0
    strength_damage_mod: float = 0.0
    carry_capacity_mod: float = 0.0
    door_crack_mod: float = 0.0
    ranged_atck_mod: int = 0
    ac_mod: int = 0
    hp_mod: int = 0
    raise_dead_mod: int = 0
    max_add_langs: int = 0
    highest_spell_level: int = 0
    understand_spell: int = 0
    min_spells_per_level: int = 0
    max_spells_per_level: int = 0
    cap_spec_hirelings: int = 0
    add_langs: tuple[str, ...] = field(default_factory=tuple)
    treasure: list[str] = field(default_factory=list)
    coins: int = field(default=0)
    allowed_alignment: str = "Undefined"
    allowed_races: str = "Undefined"
    allowed_armor: str = "Undefined"
    allowed_weapon: str = "Undefined"
    delicate_tasks: int = 0
    climb_walls: int = 0
    hear_sounds: str = "0:6"
    hide_in_shadows: int = 0
    move_silently: int = 0
    open_locks: int = 0
    surprised: int = 2
    darkvision: bool = False
    parry: int = 0

    def post_init(self):
        """Initialize derived attributes after the main initialization."""
        self.inventory = ["Rope", "Torch", "Backpack", "Bedroll", "Waterskin", "Mess Kit"]
        self.treasure = ["Gold Coin", "Silver Ring"]


    def __repr__(self):
        """Return a string representation of the PlayerClass instance."""
        return (
            f"Player Name={self.player_name}, Character Name={self.character_name}\n"
            f"Profession={self.profession}, "
            f"Level={self.level}, HP Dice=d{self.hp_dice}, Main Stats={self.main_stats}\n"
            f"XP={self.xp}, XP Bonus={self.xp_bonus}%, HP={self.hp}, Coins={self.coins}\n"
            f"STR: {self.stat_str}    STR_mod: Attack={self.strength_atck_mod}, Damage={self.strength_damage_mod}, "
            f"Carry Capacity={self.carry_capacity_mod}, Door Crack={self.door_crack_mod}\n"
            f"DEX: {self.stat_dex}    DEX_mod: Ranged Attack={self.ranged_atck_mod}, AC Bonus={self.ac_mod}\n"
            f"CON: {self.stat_con}    CON_mod: HP Bonus={self.hp_mod}, Raise Dead Chance={self.raise_dead_mod}%\n"
            f"INT: {self.stat_int}    INT_mod: max. additional languages={self.max_add_langs}, Spell Level={self.highest_spell_level}, "
            f"Understands Spell={self.understand_spell}%, "
            f"min/max Spells per Level={self.min_spells_per_level}/{self.max_spells_per_level}\n"
            f"WIS: {self.stat_wis}\n"
            f"CHA: {self.stat_char}    CHA_mod: Max Hirelings={self.cap_spec_hirelings}\n"
            f"State: {self.player_state}, Alignment: {self.alignment}, Race: {self.race}, Gender: {self.gender}, God: {self.god}, Age: {self.age}\n"
            f"Save Throw: {self.save_throw}, Save Bonuses: {list(self.save_bonuses)}, Immunity: {list(self.immunity)}, AC: {self.ac}\n"
            f"Special Abilities: {list(self.special_abilities)}\n"
            f"Languages: {list(self.add_langs)}\n"
            f"Inventory: {self.inventory}\n"
            f"Treasure: {self.treasure}\n"
            f"Darkvision: {self.darkvision}, Parry: {self.parry}\n"
            f"Delicate Tasks: {self.delicate_tasks}%, Climb Walls: {self.climb_walls}%, Hear Sounds: {self.hear_sounds}%\n"
            f"Hide in Shadows: {self.hide_in_shadows}%, Move Silently: {self.move_silently}%, Open Locks: {self.open_locks}%, Surprised: {self.surprised}:6\n"
            f"Allowed Alignment: {self.allowed_alignment}, Allowed Races: {self.allowed_races}\n"
            f"Allowed Weapon: {self.allowed_weapon}, Allowed Armor: {self.allowed_armor}\n"
        )
    
    def to_dict(self):
        """Convert the PlayerClass instance to a dictionary."""
        return {
            "player_name": self.player_name,
            "character_name": self.character_name,
            "profession": self.profession,
            "main_stats": self.main_stats,
            "player_state": self.player_state,
            "hp_dice": self.hp_dice,
            "level": self.level,
            "alignment": self.alignment,
            "race": self.race,
            "gender": self.gender,
            "god": self.god,
            "age": self.age,
            "xp": self.xp,
            "xp_bonus": self.xp_bonus,
            "hp": self.hp,
            "save_throw": self.save_throw,
            "save_bonuses": list(self.save_bonuses),
            "immunity": list(self.immunity),
            "special_abilities": list(self.special_abilities),
            "languages": list(self.add_langs),
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
                    "ac_mod": self.ac_mod
                },
                "constitution": {
                    "hp_mod": self.hp_mod,
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
            "allowed_weapon": self.allowed_weapon,
            "delicate_tasks": self.delicate_tasks,
            "climb_walls": self.climb_walls,
            "hear_sounds": self.hear_sounds,
            "hide_in_shadows": self.hide_in_shadows,
            "move_silently": self.move_silently,
            "open_locks": self.open_locks,
            "surprised": self.surprised,
            "darkvision": self.darkvision,
            "parry": self.parry
        }