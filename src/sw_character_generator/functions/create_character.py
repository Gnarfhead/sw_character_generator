from dataclasses import dataclass
from classes.character import Character
from classes.fighter import Fighter
from functions.gen_char_stat_mods import analyze_mod_str, analyze_mod_dex, analyze_mod_con, analyze_mod_int, analyze_mod_char


@dataclass
class FullCharacter:
    """A dataclass that combines Character and Fighter data."""
    character: Character
    character_class: Fighter

    def __post_init__(self):
        #Calculate and set all STR derived modifiers after initialization."""
        (
            self.strength_atck_mod,
            self.strength_damage_mod,
            self.carry_capacity_mod,
            self.door_crack_mod
        ) = analyze_mod_str(
            self.character.stat_str,
            self.character_class.player_class
        )

        #Calculate and set all DEX derived modifiers after initialization."""
        (
            self.ranged_atck_mod,
            self.ac_bon
        ) = analyze_mod_dex(
            self.character.stat_dex,
            self.character_class.player_class
        )

        #Calculate and set all CON derived modifiers after initialization."""
        (
            self.tp_bon,
            self.raise_dead_mod
        ) = analyze_mod_con(
            self.character.stat_con,
            self.character_class.player_class
        )

        #Calculate and set all INT derived modifiers after initialization."""
        (
            self.max_add_langs,
            self.highest_spell_level,
            self.understand_spell,
            self.min_spells_per_level,
            self.max_spells_per_level
        ) = analyze_mod_int(
            self.character.stat_int,
            self.character_class.player_class
        )

        (
            self.cap_spec_hirelings
        ) = analyze_mod_char(
            self.character.stat_char,
            self.character_class.player_class
        )

    
    
    def __repr__(self):
        return (
            f"PlayerName={self.character.player_name}\n"
            f"CharacterName={self.character.character_name}\n"
            f"Class={self.character_class.player_class}\n"
            f"STR: {self.character.stat_str}    STR_mod: Attack={self.strength_atck_mod}, Damage={self.strength_damage_mod}, "
            f"Carry Capacity={self.carry_capacity_mod}, Door Crack={self.door_crack_mod}\n"
            f"DEX: {self.character.stat_dex}    DEX_mod: Ranged Attack={self.ranged_atck_mod}, AC Bonus={self.ac_bon}\n"
            f"CON: {self.character.stat_con}    CON_mod: HP Bonus={self.tp_bon}, Raise Dead Chance={self.raise_dead_mod}%\n"
            f"INT: {self.character.stat_int}    INT_mod: Languages={self.max_add_langs}, Spell Level={self.highest_spell_level}, "
            f"Understands Spell={self.understand_spell}, "
            f"min/max Spells per Level={self.min_spells_per_level}/{self.max_spells_per_level}\n"
            f"WIS: {self.character.stat_wis}\n"
            f"CHA: {self.character.stat_char}    CHA_mod: Max Hirelings={self.cap_spec_hirelings}"
        )



def create_character(character_data: Character, class_data: Fighter) -> FullCharacter:
    """Create a FullCharacter instance from Character and Fighter data."""
    #print(FullCharacter)
    return FullCharacter(character=character_data, character_class=class_data)
