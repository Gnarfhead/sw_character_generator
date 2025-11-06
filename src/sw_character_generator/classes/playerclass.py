from dataclasses import dataclass, field
from typing import Set
from sw_character_generator.functions.role_dice import wuerfle_3d6
from sw_character_generator.functions.gen_char_stat_mods import analyze_mod_str, analyze_mod_dex, analyze_mod_con, analyze_mod_int, analyze_mod_char
from sw_character_generator.classes.fighter import Fighter
from sw_character_generator.classes.professions import Profession
from sw_character_generator.classes.player_enums import MainStat, Alignments, Races, PlayerStates, Profession
from sw_character_generator.classes.races import Race
from sw_character_generator.classes.elf import Elf
from sw_character_generator.classes.halfling import Halfling
from sw_character_generator.classes.assassin import Assassin
from sw_character_generator.classes.thief import Thief
from sw_character_generator.classes.wizard import Wizard

# Mapping Enum → Klassen
PROFESSION_CLASS_MAP = {
    Profession.FIGHTER: Fighter,
    Profession.WIZARD: Wizard,
    Profession.THIEF: Thief,
    Profession.ASSASSIN: Assassin,
    #Profession.CLERIC: Cleric,
    #Profession.DRUID: Druid,
    #Profession.PALADIN: Paladin,
}

# Mapping Enum → Klassen
RACE_CLASS_MAP = {
    Races.ELF: Elf,
    Races.HALFLING: Halfling,
    #Races.DWARF: Dwarf,
    #Races.HUMAN: Human,
    #Races.HALFELF: HalfElf,
}

@dataclass
class PlayerClass:
    """Class representing a character in the game."""
    player_name: str = "Unknown"
    character_name: str = "Unnamed Hero"
    profession: object = field(default_factory=Fighter)
    tp_dice: int = 8
    main_stats: Set[MainStat] = field(default_factory=lambda: {MainStat.STRENGTH})
    player_state: Set[PlayerStates] = field(default_factory=lambda: {PlayerStates.ALIVE})
    alignment: Alignments = Alignments.GOOD
    level: int = 1
    race: object = field(default_factory=Elf)
    gender: str = "Undefined"
    god: str = "None"
    age: int = 18
    xp_bonus: int = 0
    xp: int = 0
    tp: int = 0
    save_throw: int = 0
    save_bonuses: tuple[str, ...] = field(default_factory=tuple)
    immunity: tuple[str, ...] = field(default_factory=tuple)
    special_abilities: tuple[str, ...] = field(default_factory=tuple)
    ac: int = 10
    stat_str: int = field(default_factory=lambda: wuerfle_3d6(str_desc="Strength"))
    stat_dex: int = field(default_factory=lambda: wuerfle_3d6(str_desc="Dexterity"))
    stat_con: int = field(default_factory=lambda: wuerfle_3d6(str_desc="Constitution"))
    stat_wis: int = field(default_factory=lambda: wuerfle_3d6(str_desc="Wisdom"))
    stat_int: int = field(default_factory=lambda: wuerfle_3d6(str_desc="Intelligence"))
    stat_char: int = field(default_factory=lambda: wuerfle_3d6(str_desc="Charisma"))
    inventory: list[str] = field(default_factory=list)
    strength_atck_mod: float = field(init=False)
    strength_damage_mod: float = field(init=False)
    carry_capacity_mod: float = field(init=False)
    door_crack_mod: float = field(init=False)
    ranged_atck_mod: int = field(init=False)
    ac_mod: int = field(init=False)
    tp_mod: int = field(init=False)
    raise_dead_mod: int = field(init=False)
    max_add_langs: int = field(init=False)
    highest_spell_level: int = field(init=False)
    understand_spell: int = field(init=False)
    min_spells_per_level: int = field(init=False)
    max_spells_per_level: int = field(init=False)
    add_langs: tuple[str, ...] = field(default_factory=tuple)
    cap_spec_hirelings: int = field(init=False)
    treasure: list[str] = field(default_factory=list)
    coins: int = field(default_factory=lambda: wuerfle_3d6(str_desc="Starting Coins") * 10)
    allowed_alignment: Set[Alignments] = field(default_factory=lambda: {Alignments.GOOD})
    allowed_races: Set[Races] = field(default_factory=lambda: {Races.HUMAN})
    allowed_armor: str = "all"
    allowed_weapon: str = "all"
    delicate_tasks: int = 0
    climb_walls: int = 0
    hear_sounds: int = 0
    hide_in_shadows: int = 0
    move_silently: int = 0 
    open_locks: int = 0
    surprised: int = 2
    darkvision: bool = False
    parry: int = 0
    
    
    def __post_init__(self):

        # Wenn profession noch ein Enum ist, wandel um
        if isinstance(self.profession, Profession):
            klass = PROFESSION_CLASS_MAP[self.profession]
            self.profession = klass()

        # Calculate and set all STR derived modifiers after initialization."""
        (
            self.strength_atck_mod,
            self.strength_damage_mod,
            self.carry_capacity_mod,
            self.door_crack_mod
        ) = analyze_mod_str(
            self.stat_str,
            self.profession
        )
        print("DEBUG analyze_mod_str: ", self.stat_str, self.profession)

        #Calculate and set all DEX derived modifiers after initialization."""
        (
            self.ranged_atck_mod,
            self.ac_mod
        ) = analyze_mod_dex(
            self.stat_dex,
            self.profession
        )
        print("DEBUG analyze_mod_dex: ", self.stat_dex, self.profession)

        #Calculate and set all CON derived modifiers after initialization."""
        (
            self.tp_mod,
            self.raise_dead_mod
        ) = analyze_mod_con(
            self.stat_con,
            self.profession
        )
        print("DEBUG analyze_mod_con: ", self.stat_con, self.profession)

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
        print("DEBUG analyze_mod_int: ", self.stat_int, self.profession)
        
        #Calculate and set all CHAR derived modifiers after initialization."""
        (
            self.cap_spec_hirelings
        ) = analyze_mod_char(
            self.stat_char,
            self.profession
        )
        print("DEBUG analyze_mod_char: ", self.stat_char, self.profession)

        # Re-apply class modifiers that depend on stats
        self.profession.apply_profession_dependent_modifiers(self)

        # calculate profession stat modifiers...
        self.profession.apply_stat_dependent_modifiers(self)

        # calculate race stat modifiers...
        self.race.apply_race_dependent_modifiers(self)

    
    def __repr__(self):
        """Return a string representation of the PlayerClass instance."""
        return (
            f"{self.__class__.__name__}("
            f"PlayerName={self.player_name}, CharacterName={self.character_name}\n"
            f"Class={self.profession.name}, "
            f"Level={self.level}, TP_Dice=d{self.tp_dice}, MainStats={[stat.value for stat in self.main_stats]}\n"
            f"xp={self.xp}, xp_bonus={self.xp_bonus}%, TP={self.tp}, Coins={self.coins}\n"
            f"STR: {self.stat_str}    STR_mod: Attack={self.strength_atck_mod}, Damage={self.strength_damage_mod}, "
            f"Carry Capacity={self.carry_capacity_mod}, Door Crack={self.door_crack_mod}\n"
            f"DEX: {self.stat_dex}    DEX_mod: Ranged Attack={self.ranged_atck_mod}, AC Bonus={self.ac_mod}\n"
            f"CON: {self.stat_con}    CON_mod: HP Bonus={self.tp_mod}, Raise Dead Chance={self.raise_dead_mod}%\n"
            f"INT: {self.stat_int}    INT_mod: max. Languages={self.max_add_langs}, Spell Level={self.highest_spell_level}, "
            f"Understands Spell={self.understand_spell}%, "
            f"min/max Spells per Level={self.min_spells_per_level}/{self.max_spells_per_level}\n"
            f"WIS: {self.stat_wis}\n"
            f"CHA: {self.stat_char}    CHA_mod: Max Hirelings={self.cap_spec_hirelings}\n"
            f"State: {[stat.value for stat in self.player_state]}, Alignment: {self.alignment.value}, Race: {self.race.name}, Gender: {self.gender}, God: {self.god}, Age: {self.age}\n"
            f"Save Throw: {self.save_throw}, Save Bonuses: {list(self.save_bonuses)}, Immunity: {list(self.immunity)}, AC: {self.ac}\n"
            f"Special Abilities: {list(self.special_abilities)}\n"
            f"Languages: {list(self.add_langs)}\n"
            f"Inventory: {self.inventory}\n"
            f"Treasure: {self.treasure}\n"
            f"darkvision: {self.darkvision}, parry: {self.parry}\n"
            f"delicate_tasks: {self.delicate_tasks}%, climb_walls: {self.climb_walls}%, hear_sounds: {self.hear_sounds}%\n"
            f"hide_in_shadows: {self.hide_in_shadows}%, move_silently: {self.move_silently}%, open_locks: {self.open_locks}%, surprised: {self.surprised}:6\n"
            f"allowed_alignment: {[stat.value for stat in self.allowed_alignment]}, allowed_races: {[stat.value for stat in self.allowed_races]}"
            f")"
        )
    
    def to_dict(self):
        """Convert the PlayerClass instance to a dictionary."""
        return {
            "player_name": self.player_name,
            "character_name": self.character_name,
            "profession": self.profession.name,
            "main_stats": [stat.value for stat in self.main_stats],
            "tp_dice": self.tp_dice,
            "level": self.level,
            "alignment": self.alignment.value,
            "race": self.race.name,
            "gender": self.gender,
            "god": self.god,
            "age": self.age,
            "xp": self.xp,
            "xp_bonus": self.xp_bonus,
            "tp": self.tp,
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
                    "hp_mod": self.tp_mod,
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
            "allowed_alignment": [stat.value for stat in self.allowed_alignment],
            "allowed_races": [stat.value for stat in self.allowed_races],
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