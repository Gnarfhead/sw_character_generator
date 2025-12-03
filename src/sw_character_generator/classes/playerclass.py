"""Module defining the PlayerClass dataclass for character representation."""
from dataclasses import dataclass, field
from typing import Any


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
    hp_all_rolls: dict[int, int] = field(default_factory=dict)
    save_throw: int = 0
    save_throw_progression: dict[int, int] = field(default_factory=dict)
    save_bonuses_race: set[str] = field(default_factory=set)
    save_bonuses_profession: set[str] = field(default_factory=set)
    save_bonuses_other: set[str] = field(default_factory=set)
    immunities_race: set[str] = field(default_factory=set)
    immunities_profession: set[str] = field(default_factory=set)
    immunities_other: set[str] = field(default_factory=set)
    special_abilities_race: set[str] = field(default_factory=set)
    special_abilities_profession: set[str] = field(default_factory=set)
    special_abilities_other: set[str] = field(default_factory=set)
    ac: int = 10 # base armor class
    ac_mod: int = 0 # calculated from dexterity
    ac_mod_temp: int = 0 # Set by spinbox
    ac_total: int = 10 # total AC after modifiers
    languages: set[str] = field(default_factory=set)
    additional_languages: list[str] = field(default_factory=list)
    stat_str: int = field(default=0)
    stat_str_temp: int = field(default=0)
    stat_dex: int = field(default=0)
    stat_dex_temp: int = field(default=0)
    stat_con: int = field(default=0)
    stat_con_temp: int = field(default=0)
    stat_wis: int = field(default=0)
    stat_wis_temp: int = field(default=0)
    stat_int: int = field(default=0)
    stat_int_temp: int = field(default=0)
    stat_char: int = field(default=0)
    stat_char_temp: int = field(default=0)
    inventory: dict[str, int] = field(default_factory=dict)
    strength_atck_mod: int = 0
    strength_atck_mod_temp: int = 0
    strength_damage_mod: int = 0
    strength_damage_mod_temp: int = 0
    carry_capacity_mod: int = 0
    door_crack_mod: float = 0
    ranged_atck_mod: int = 0
    ranged_atck_mod_race: int = 0 # Bonus from race (e.g., Halfling +1)
    ranged_atck_mod_temp: int = 0
    ranged_atck_mod_total: int = 0
    hp_mod: int = 0
    raise_dead_mod: int = 0
    max_add_langs: int = 0
    highest_spell_level: int = 0
    understand_spell: int = 0
    min_spells_per_level: int = 0
    max_spells_per_level: int = 0
    cap_spec_hirelings: int = 0
    treasure: dict[str, int] = field(default_factory=dict)
    coins_platinum: int = field(default=0)
    coins_gold: int = field(default=0)
    coins_electrum: int = field(default=0)
    coins_silver: int = field(default=0)
    coins_copper: int = field(default=0)
    allowed_alignment: str = "Undefined"
    allowed_races: tuple[str, ...] = field(default_factory=tuple)
    allowed_armor: str = "Undefined"
    allowed_weapon: str = "Undefined"
    delicate_tasks_profession: dict[int, int] = field(default_factory=dict)
    delicate_tasks_race: int = 0
    delicate_tasks: int = 0
    climb_walls_profession: dict[int, int] = field(default_factory=dict)
    # climb_walls_race: int = 0 # no race modifier in the rulebook
    climb_walls: int = 0
    hear_sounds_profession: dict[str, int] = field(default_factory=dict)
    # hear_sounds_race: str = "0:0" # no race modifier in the rulebook
    hear_sounds: str = "0:6"
    hide_in_shadows_profession: dict[int, int] = field(default_factory=dict)
    hide_in_shadows_race: int = 0
    hide_in_shadows: int = 0
    move_silently_profession: dict[int, int] = field(default_factory=dict)
    move_silently_race: int = 0
    move_silently: int = 0
    open_locks_profession: dict[int, int] = field(default_factory=dict)
    open_locks_race: int = 0
    open_locks: int = 0
    surprised: int = 2
    darkvision: bool = False
    parry: int = 0
    thief_user_class: bool = False
    magic_user_class: bool = False
    spell_table: dict[int, dict[int, int]] = field(default_factory=dict)
    spell_table_2: dict[int, dict[int, int]] = field(default_factory=dict)

    # Property for total coins
    @property
    def coins(self) -> int:  # Total coins in copper pieces
        """Calculate total coins in copper pieces."""
        return (self.coins_platinum * 1000) + (self.coins_gold * 100) + (self.coins_electrum * 50) + (self.coins_silver * 10) + self.coins_copper
    @coins.setter
    def coins(self, total_copper: int):  # Total coins in copper pieces
        """Set coin values based on total copper pieces."""
        self.coins_platinum = total_copper // 1000
        remainder = total_copper % 1000
        self.coins_gold = remainder // 100
        remainder = remainder % 100
        self.coins_electrum = remainder // 50
        remainder = remainder % 50
        self.coins_silver = remainder // 10
        remainder = remainder % 10
        self.coins_copper = remainder

    # Derived properties
    @property
    def save_bonuses(self) -> set[str]:  # Combine all save bonuses from race, class, and other sources.
        """Combine all save bonuses from race, class, and other sources."""
        return self.save_bonuses_race | self.save_bonuses_profession | self.save_bonuses_other
    
    @property
    def immunities(self) -> set[str]:  # Combine all immunities from race , class, and other sources.
        """Combine all immunities from race , class, and other sources."""
        return self.immunities_race | self.immunities_profession | self.immunities_other
    
    @property
    def special_abilities(self) -> set[str]: # Combine all special abilities from race, class, and other sources.
        """Combine all special abilities from race, class, and other sources."""
        return self.special_abilities_race | self.special_abilities_profession | self.special_abilities_other


    def __repr__(self):  # String representation of the PlayerClass instance.
        """Return a string representation of the PlayerClass instance."""
        return (
            f"Player Name={self.player_name}, Character Name={self.character_name}\n"
            f"Profession={self.profession}, Thief Class={self.thief_user_class}, Magic User Class={self.magic_user_class}\n"
            f"Level={self.level}, HP Dice=d{self.hp_dice}, Main Stats={self.main_stats}\n"
            f"XP={self.xp}, XP Bonus={self.xp_bonus}%, HP={self.hp}, HP current={self.hp_current}\n"
            f"Coins: Platinum={self.coins_platinum}, Gold={self.coins_gold}, Electrum={self.coins_electrum}, Silver={self.coins_silver}, Copper={self.coins_copper}\n"
            f"STR: {self.stat_str}, STR_temp: {self.stat_str_temp}, STR_mod: Attack={self.strength_atck_mod}, Attack_temp={self.strength_atck_mod_temp}, Damage={self.strength_damage_mod}, Damage_temp={self.strength_damage_mod_temp}, "
            f"Carry Capacity={self.carry_capacity_mod}, Door Crack={self.door_crack_mod}\n"
            f"DEX: {self.stat_dex}, DEX_temp: {self.stat_dex_temp}, DEX_mod: Ranged Attack={self.ranged_atck_mod}, Ranged Attack_temp={self.ranged_atck_mod_temp}, AC Bonus={self.ac_mod}, AC Bonus_temp={self.ac_mod_temp}\n"
            f"CON: {self.stat_con}, CON_temp: {self.stat_con_temp}, CON_mod: HP Bonus={self.hp_mod}, Raise Dead Chance={self.raise_dead_mod}%\n"
            f"INT: {self.stat_int}, INT_temp: {self.stat_int_temp}, INT_mod: max. additional languages={self.max_add_langs}, Spell Level={self.highest_spell_level}, "
            f"Understands Spell={self.understand_spell}%, "
            f"min/max Spells per Level={self.min_spells_per_level}/{self.max_spells_per_level}\n"
            f"WIS: {self.stat_wis}, WIS_temp: {self.stat_wis_temp}\n"
            f"CHA: {self.stat_char}, CHA_temp: {self.stat_char_temp}, CHA_mod: Max Hirelings={self.cap_spec_hirelings}\n"
            f"State: {self.player_state}, Alignment: {self.alignment}, Race: {self.race}, Gender: {self.gender}, God: {self.god}, Age: {self.age}\n"
            f"Save Throw: {self.save_throw}, Save Bonuses: {list(self.save_bonuses)}, Immunities: {list(self.immunities)}\n"
            f"Base AC: {self.ac}, AC Bonus: {self.ac_mod}, AC Bonus_temp: {self.ac_mod_temp}\n"
            f"Special Abilities: {list(self.special_abilities)}\n"
            f"Languages: {list(self.languages)}, Additional Languages: {list(self.additional_languages)}\n"
            f"Inventory: {self.inventory}\n"
            f"Treasure: {self.treasure}\n"
            f"Darkvision: {self.darkvision}, Parry: {self.parry}\n"
            f"Delicate Tasks: {self.delicate_tasks_profession}%, Delicate Tasks Race Bonus: {self.delicate_tasks_race}%, Climb Walls: {self.climb_walls_profession}%, Hear Sounds: {self.hear_sounds_profession}%\n"
            f"Hide in Shadows: {self.hide_in_shadows_profession}%, Hide in Shadows Race Bonus: {self.hide_in_shadows_race}%, Move Silently: {self.move_silently_profession}%\n" 
            f"Move Silently Race Bonus: {self.move_silently_race}%, Open Locks: {self.open_locks_profession}%, Open Locks Race Bonus: {self.open_locks_race}%, Surprised: {self.surprised}:6\n"
            f"Allowed Alignment: {self.allowed_alignment}, Allowed Races: {self.allowed_races}\n"
            f"Allowed Weapon: {self.allowed_weapon}, Allowed Armor: {self.allowed_armor}\n"
            f"Character Created: {self.character_created}, HP Last Roll: {self.hp_last_roll}, HP All Rolls: {self.hp_all_rolls}\n"
            f"Spells: {self.spell_table}\n"
            f"Spells 2: {self.spell_table_2}\n"
        )

    def to_dict(self):  # Convert the PlayerClass instance to a dictionary.
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
            "xp_progress": self.xp_progress,
            "xp": self.xp,
            "hp": self.hp,
            "hp_current": self.hp_current,
            "hp_last_roll": self.hp_last_roll,
            "hp_all_rolls": self.hp_all_rolls,
            "save_throw": self.save_throw,
            "save_throw_progression": self.save_throw_progression,
            "save_bonuses_race": list(self.save_bonuses_race),
            "save_bonuses_profession": list(self.save_bonuses_profession),
            "save_bonuses_other": list(self.save_bonuses_other),
            "immunities_race": list(self.immunities_race),
            "immunities_profession": list(self.immunities_profession),
            "immunities_other": list(self.immunities_other),
            "special_abilities_race": list(self.special_abilities_race),
            "special_abilities_profession": list(self.special_abilities_profession),
            "special_abilities_other": list(self.special_abilities_other),
            "ac": self.ac,
            "ac_mod": self.ac_mod,
            "ac_mod_temp": self.ac_mod_temp,
            "ac_total": self.ac_total,
            "languages": list(self.languages),
            "additional_languages": list(self.additional_languages),

            "stats": {
                "str": self.stat_str,
                "str_temp": self.stat_str_temp,
                "dex": self.stat_dex,
                "dex_temp": self.stat_dex_temp,
                "con": self.stat_con,
                "con_temp": self.stat_con_temp,
                "wis": self.stat_wis,
                "wis_temp": self.stat_wis_temp,
                "int": self.stat_int,
                "int_temp": self.stat_int_temp,
                "cha": self.stat_char,
                "cha_temp": self.stat_char_temp,
            },
            "inventory": self.inventory,
            "modifiers": {
                "strength": {
                    "attack": self.strength_atck_mod,
                    "attack_temp": self.strength_atck_mod_temp,
                    "damage": self.strength_damage_mod,
                    "damage_temp": self.strength_damage_mod_temp,
                    "carry_capacity": self.carry_capacity_mod,
                    "door_crack": self.door_crack_mod
                },
                "dexterity": {
                    "ranged_attack": self.ranged_atck_mod,
                    "ranged_attack_temp": self.ranged_atck_mod_temp,
                    "ac_mod": self.ac_mod,
                    "ac_mod_temp": self.ac_mod_temp
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
            "coins_platinum": self.coins_platinum,
            "coins_gold": self.coins_gold,
            "coins_electrum": self.coins_electrum,
            "coins_silver": self.coins_silver,
            "coins_copper": self.coins_copper,
            "allowed_alignment": self.allowed_alignment,
            "allowed_races": self.allowed_races,
            "allowed_armor": self.allowed_armor,
            "allowed_weapon": self.allowed_weapon,
            "delicate_tasks": self.delicate_tasks,
            "delicate_tasks_profession": self.delicate_tasks_profession,
            "delicate_tasks_race": self.delicate_tasks_race,
            "climb_walls": self.climb_walls,
            "climb_walls_profession": self.climb_walls_profession,
            "hear_sounds": self.hear_sounds,
            "hear_sounds_profession": self.hear_sounds_profession,
            "hide_in_shadows": self.hide_in_shadows,
            "hide_in_shadows_profession": self.hide_in_shadows_profession,
            "hide_in_shadows_race": self.hide_in_shadows_race,
            "move_silently": self.move_silently,
            "move_silently_profession": self.move_silently_profession,
            "move_silently_race": self.move_silently_race,
            "open_locks": self.open_locks,
            "open_locks_profession": self.open_locks_profession,
            "open_locks_race": self.open_locks_race,

            "surprised": self.surprised,
            "darkvision": self.darkvision,
            "parry": self.parry,
            "thief_user_class": self.thief_user_class,
            "magic_user_class": self.magic_user_class,
            "spell_table": self.spell_table,
            "spell_table_2": self.spell_table_2,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PlayerClass":  # Create a PlayerClass instance from a dictionary.
        """Create a PlayerClass instance from a dictionary."""
        print("DEBUG PlayerClass.from_dict: --------------------------------")
        stats = data.get("stats", {})
        modifiers = data.get("modifiers", {})
        strength_mods = modifiers.get("strength", {})
        dexterity_mods = modifiers.get("dexterity", {})
        constitution_mods = modifiers.get("constitution", {})
        intelligence_mods = modifiers.get("intelligence", {})
        charisma_mods = modifiers.get("charisma", {})
        
        return cls(
            player_name=data.get("player_name", "Unknown"),
            character_name=data.get("character_name", "Unnamed Hero"),
            character_created=data.get("character_created", False),
            profession=data.get("profession", "Undefined"),
            hp_dice=data.get("hp_dice", 0),
            main_stats=tuple(data.get("main_stats", [])),
            player_state=data.get("player_state", "Undefined"),
            alignment=data.get("alignment", "Undefined"),
            level=data.get("level", 1),
            race=data.get("race", "Undefined"),
            gender=data.get("gender", "Undefined"),
            god=data.get("god", "Undefined"),
            age=data.get("age", 0),
            xp_bonus=data.get("xp_bonus", 0),
            xp=data.get("xp", 0),
            xp_progress=data.get("xp_progress", {}),
            hp=data.get("hp", 0),
            hp_current=data.get("hp_current", 0),
            hp_last_roll=data.get("hp_last_roll", 0),
            hp_all_rolls=data.get("hp_all_rolls", {}),
            save_throw=data.get("save_throw", 0),
            save_throw_progression=data.get("save_throw_progression", {}),
            save_bonuses_race=set(data.get("save_bonuses_race", [])),
            save_bonuses_profession=set(data.get("save_bonuses_profession", [])),
            save_bonuses_other=set(data.get("save_bonuses_other", [])),
            immunities_race=set(data.get("immunities_race", [])),
            immunities_profession=set(data.get("immunities_profession", [])),
            immunities_other=set(data.get("immunities_other", [])),
            special_abilities_race=set(data.get("special_abilities_race", [])),
            special_abilities_profession=set(data.get("special_abilities_profession", [])),
            special_abilities_other=set(data.get("special_abilities_other", [])),
            ac=data.get("ac", 10),
            ac_mod_temp=data.get("ac_mod_temp", 0),
            ac_total=data.get("ac_total", 10),
            languages=set(data.get("languages", [])),
            additional_languages=data.get("additional_languages", []),
            stat_str=stats.get("str", 0),
            stat_str_temp=stats.get("str_temp", 0),
            stat_dex=stats.get("dex", 0),
            stat_dex_temp=stats.get("dex_temp", 0),
            stat_con=stats.get("con", 0),
            stat_con_temp=stats.get("con_temp", 0),
            stat_wis=stats.get("wis", 0),
            stat_wis_temp=stats.get("wis_temp", 0),
            stat_int=stats.get("int", 0),
            stat_int_temp=stats.get("int_temp", 0),
            stat_char=stats.get("cha", 0),
            stat_char_temp=stats.get("cha_temp", 0),
            inventory=data.get("inventory", {}),
            strength_atck_mod=strength_mods.get("attack", 0),
            strength_atck_mod_temp=strength_mods.get("attack_temp", 0),
            strength_damage_mod=strength_mods.get("damage", 0),
            strength_damage_mod_temp=strength_mods.get("damage_temp", 0),
            carry_capacity_mod=strength_mods.get("carry_capacity", 0),
            door_crack_mod=strength_mods.get("door_crack", 0.0),
            ranged_atck_mod=dexterity_mods.get("ranged_attack", 0),
            ranged_atck_mod_temp=dexterity_mods.get("ranged_attack_temp", 0),
            ac_mod=dexterity_mods.get("ac_mod", 0),
            hp_mod=constitution_mods.get("hp_mod", 0),
            raise_dead_mod=constitution_mods.get("raise_dead_chance", 0),
            max_add_langs=intelligence_mods.get("max_languages", 0),
            highest_spell_level=intelligence_mods.get("spell_level", 0),
            understand_spell=intelligence_mods.get("understand_spell", 0),
            min_spells_per_level=intelligence_mods.get("min_spells_per_level", 0),
            max_spells_per_level=intelligence_mods.get("max_spells_per_level", 0),
            cap_spec_hirelings=charisma_mods.get("max_hirelings", 0),
            treasure=data.get("treasure", {}),
            coins_platinum=data.get("coins_platinum", 0),
            coins_gold=data.get("coins_gold", 0),
            coins_electrum=data.get("coins_electrum", 0),
            coins_silver=data.get("coins_silver", 0),
            coins_copper=data.get("coins_copper", 0),
            allowed_alignment=data.get("allowed_alignment", "Undefined"),
            allowed_races=tuple(data.get("allowed_races", [])),
            allowed_armor=data.get("allowed_armor", "Undefined"),
            allowed_weapon=data.get("allowed_weapon", "Undefined"),
            delicate_tasks_profession=data.get("delicate_tasks_profession", {}),
            delicate_tasks_race=data.get("delicate_tasks_race", 0),
            delicate_tasks=data.get("delicate_tasks", 0),
            climb_walls_profession=data.get("climb_walls_profession", {}),
            climb_walls=data.get("climb_walls", 0),
            hear_sounds_profession=data.get("hear_sounds_profession", {}),
            hear_sounds=data.get("hear_sounds", "0:6"),
            hide_in_shadows_profession=data.get("hide_in_shadows_profession", {}),
            hide_in_shadows_race=data.get("hide_in_shadows_race", 0),
            hide_in_shadows=data.get("hide_in_shadows", 0),
            move_silently_profession=data.get("move_silently_profession", {}),
            move_silently_race=data.get("move_silently_race", 0),
            move_silently=data.get("move_silently", 0),
            open_locks_profession=data.get("open_locks_profession", {}),
            open_locks_race=data.get("open_locks_race", 0),
            open_locks=data.get("open_locks", 0),
            surprised=data.get("surprised", 2),
            darkvision=data.get("darkvision", False),
            parry=data.get("parry", 0),
            thief_user_class=data.get("thief_user_class", False),
            magic_user_class=data.get("magic_user_class", False),
            spell_table=data.get("spell_table", {}),
            spell_table_2=data.get("spell_table_2", {}),
        )
