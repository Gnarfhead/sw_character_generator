"""Module defining the PlayerClass dataclass for character representation."""
from dataclasses import dataclass, field

@dataclass
class PlayerClass:
    """Class representing a character in the game."""
    player_name: str = "Unknown"
    character_name: str = "Unnamed Hero"
    character_created: bool = False
    profession: str = "Undefined"
    hp_dice: int = 0
    main_stats: tuple[str, ...] = field(default_factory=tuple)
    player_state: str = "Undefined"
    alignment: str = "Undefined"
    level: int = 1
    race: str = "Undefined"
    gender: str = "Undefined"
    god: str = "Undefined"
    age: int = 0
    xp_bonus: int = 0
    xp: int = 0
    xp_progress: dict[str, int] = field(default_factory=dict)
    hp: int = 0
    hp_current: int = 0
    hp_last_roll: int = 0
    save_throw: int = 0
    save_bonuses: set[str] = field(default_factory=set)
    immunities: set[str] = field(default_factory=set)
    special_abilities: set[str] = field(default_factory=set)
    ac: int = 10
    languages: set[str] = field(default_factory=set)
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
    treasure: list[str] = field(default_factory=list)
    coins: int = field(default=0)
    allowed_alignment: str = "Undefined"
    #allowed_races: str = "Undefined"
    allowed_races: tuple[str, ...] = field(default_factory=tuple)
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
    spells_lvl1: int = 0
    spells_lvl2: int = 0
    spells_lvl3: int = 0
    spells_lvl4: int = 0
    spells_lvl5: int = 0
    spells_lvl6: int = 0
    spells_lvl7: int = 0
    spells_lvl8: int = 0
    spells_lvl9: int = 0

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
            f"Spells Lvl1-9: {self.spells_lvl1}, {self.spells_lvl2}, {self.spells_lvl3}, {self.spells_lvl4}, {self.spells_lvl5}, {self.spells_lvl6}, {self.spells_lvl7}, {self.spells_lvl8}, {self.spells_lvl9}\n"
            f"WIS: {self.stat_wis}\n"
            f"CHA: {self.stat_char}    CHA_mod: Max Hirelings={self.cap_spec_hirelings}\n"
            f"State: {self.player_state}, Alignment: {self.alignment}, Race: {self.race}, Gender: {self.gender}, God: {self.god}, Age: {self.age}\n"
            f"Save Throw: {self.save_throw}, Save Bonuses: {list(self.save_bonuses)}, Immunities: {list(self.immunities)}, AC: {self.ac}\n"
            f"Special Abilities: {list(self.special_abilities)}\n"
            f"Languages: {list(self.languages)}\n"
            f"Inventory: {self.inventory}\n"
            f"Treasure: {self.treasure}\n"
            f"Darkvision: {self.darkvision}, Parry: {self.parry}\n"
            f"Delicate Tasks: {self.delicate_tasks}%, Climb Walls: {self.climb_walls}%, Hear Sounds: {self.hear_sounds}%\n"
            f"Hide in Shadows: {self.hide_in_shadows}%, Move Silently: {self.move_silently}%, Open Locks: {self.open_locks}%, Surprised: {self.surprised}:6\n"
            f"Allowed Alignment: {self.allowed_alignment}, Allowed Races: {self.allowed_races}\n"
            f"Allowed Weapon: {self.allowed_weapon}, Allowed Armor: {self.allowed_armor}\n"
            f"Character Created: {self.character_created}, HP Last Roll: {self.hp_last_roll}\n"
        )
    
    def to_dict(self):
        """Convert the PlayerClass instance to a dictionary."""
        return {
            "player_name": self.player_name,
            "character_name": self.character_name,
            "character_created": self.character_created,
            "profession": self.profession,
            "hp_dice": self.hp_dice,
            "main_stats": self.main_stats,
            "player_state": self.player_state,
            "alignment": self.alignment,
            "level": self.level,
            "race": self.race,
            "gender": self.gender,
            "god": self.god,
            "age": self.age,
            "xp_bonus": self.xp_bonus,
            "xp": self.xp,
            "hp": self.hp,
            "hp_current": self.hp_current,
            "hp_last_roll": self.hp_last_roll,
            "save_throw": self.save_throw,
            "save_bonuses": list(self.save_bonuses),
            "immunities": list(self.immunities),
            "special_abilities": list(self.special_abilities),
            "ac": self.ac,
            "languages": list(self.languages),
            
            "stats": {
                "str": self.stat_str,
                "dex": self.stat_dex,
                "con": self.stat_con,
                "wis": self.stat_wis,
                "int": self.stat_int,
                "cha": self.stat_char
            },
            "inventory": self.inventory,
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
                    "max_languages": self.max_add_langs,
                    "spell_level": self.highest_spell_level,
                    "understand_spell": self.understand_spell,
                    "min_spells_per_level": self.min_spells_per_level,
                    "max_spells_per_level": self.max_spells_per_level
                },
                "charisma": {
                    "max_hirelings": self.cap_spec_hirelings
                }
            },
            
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
            "parry": self.parry,
            "spells": {
                "spells_lvl1": self.spells_lvl1,
                "spells_lvl2": self.spells_lvl2,
                "spells_lvl3": self.spells_lvl3,
                "spells_lvl4": self.spells_lvl4,
                "spells_lvl5": self.spells_lvl5,
                "spells_lvl6": self.spells_lvl6,
                "spells_lvl7": self.spells_lvl7,
                "spells_lvl8": self.spells_lvl8,
                "spells_lvl9": self.spells_lvl9
            }
        }

    def from_dict(self, data: dict) -> "PlayerClass":
        """Create a PlayerClass instance from a dictionary."""
        stats = data.get("stats", {})
        modifiers = data.get("modifiers", {})
        strength_mods = modifiers.get("strength", {})
        dexterity_mods = modifiers.get("dexterity", {})
        constitution_mods = modifiers.get("constitution", {})
        intelligence_mods = modifiers.get("intelligence", {})
        charisma_mods = modifiers.get("charisma", {})
        spells = data.get("spells", {})

        self.player_name = stats.get("player_name", self.player_name)
        self.character_name = data.get("character_name", self.character_name)
        self.character_created = data.get("character_created", self.character_created)
        self.profession = data.get("profession", self.profession)
        self.hp_dice = data.get("hp_dice", self.hp_dice)
        self.main_stats = data.get("main_stats", self.main_stats)
        self.player_state = data.get("player_state", self.player_state)
        self.alignment = data.get("alignment", self.alignment)
        self.level = data.get("level", self.level)
        self.race = data.get("race", self.race)
        self.gender = data.get("gender", self.gender)
        self.god = data.get("god", self.god)
        self.age = data.get("age", self.age)
        self.xp_bonus = data.get("xp_bonus", self.xp_bonus)
        self.xp = data.get("xp", self.xp)
        self.hp = data.get("hp", self.hp)
        self.hp_current = data.get("hp_current", self.hp_current)
        self.hp_last_roll = data.get("hp_last_roll", self.hp_last_roll)
        self.save_throw = data.get("save_throw", self.save_throw)
        self.save_bonuses = set(data.get("save_bonuses", []))
        self.immunities = set(data.get("immunities", []))
        self.special_abilities = set(data.get("special_abilities", []))
        self.ac = data.get("ac", self.ac)
        self.languages = set(data.get("languages", []))
        self.stat_str = stats.get("str", self.stat_str)
        self.stat_dex = stats.get("dex", self.stat_dex)
        self.stat_con = stats.get("con", self.stat_con)
        self.stat_wis = stats.get("wis", self.stat_wis)
        self.stat_int = stats.get("int", self.stat_int)
        self.stat_char = stats.get("cha", self.stat_char)
        self.inventory = data.get("inventory", self.inventory)
        self.strength_atck_mod = strength_mods.get("attack", self.strength_atck_mod)
        self.strength_damage_mod = strength_mods.get("damage", self.strength_damage_mod)
        self.carry_capacity_mod = strength_mods.get("carry_capacity", self.carry_capacity_mod)
        self.door_crack_mod = strength_mods.get("door_crack", self.door_crack_mod)
        self.ranged_atck_mod = dexterity_mods.get("ranged_attack", self.ranged_atck_mod)
        self.ac_mod = dexterity_mods.get("ac_mod", self.ac_mod)
        self.hp_mod = constitution_mods.get("hp_mod", self.hp_mod)
        self.raise_dead_mod = constitution_mods.get("raise_dead_chance", self.raise_dead_mod)
        self.max_add_langs = intelligence_mods.get("max_languages", self.max_add_langs)
        self.highest_spell_level = intelligence_mods.get("spell_level", self.highest_spell_level)
        self.understand_spell = intelligence_mods.get("understand_spell", self.understand_spell)
        self.min_spells_per_level = intelligence_mods.get("min_spells_per_level", self.min_spells_per_level)
        self.max_spells_per_level = intelligence_mods.get("max_spells_per_level", self.max_spells_per_level)
        self.cap_spec_hirelings = charisma_mods.get("max_hirelings", self.cap_spec_hirelings)
        self.treasure = data.get("treasure", self.treasure)
        self.coins = data.get("coins", self.coins)
        self.allowed_alignment = data.get("allowed_alignment", self.allowed_alignment)
        self.allowed_races = tuple(data.get("allowed_races", []))
        self.allowed_armor = data.get("allowed_armor", self.allowed_armor)
        self.allowed_weapon = data.get("allowed_weapon", self.allowed_weapon)
        self.delicate_tasks = data.get("delicate_tasks", self.delicate_tasks)
        self.climb_walls = data.get("climb_walls", self.climb_walls)
        self.hear_sounds = data.get("hear_sounds", self.hear_sounds)
        self.hide_in_shadows = data.get("hide_in_shadows", self.hide_in_shadows)
        self.move_silently = data.get("move_silently", self.move_silently)
        self.open_locks = data.get("open_locks", self.open_locks)
        self.surprised = data.get("surprised", self.surprised)
        self.darkvision = data.get("darkvision", self.darkvision)
        self.parry = data.get("parry", self.parry)
        self.spells_lvl1 = spells.get("spells_lvl1", self.spells_lvl1)
        self.spells_lvl2 = spells.get("spells_lvl2", self.spells_lvl2)
        self.spells_lvl3 = spells.get("spells_lvl3", self.spells_lvl3)
        self.spells_lvl4 = spells.get("spells_lvl4", self.spells_lvl4)
        self.spells_lvl5 = spells.get("spells_lvl5", self.spells_lvl5)
        self.spells_lvl6 = spells.get("spells_lvl6", self.spells_lvl6)
        self.spells_lvl7 = spells.get("spells_lvl7", self.spells_lvl7)
        self.spells_lvl8 = spells.get("spells_lvl8", self.spells_lvl8)
        self.spells_lvl9 = spells.get("spells_lvl9", self.spells_lvl9)