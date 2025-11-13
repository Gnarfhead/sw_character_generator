"""Functions to analyze character stats and return corresponding modifiers."""
from sw_character_generator.classes.playerclass import PlayerClass


def analyze_mod_str(player_character: PlayerClass):
    """Calculate strength-based modifiers. Positive bonuses only apply to fighters."""
    if 3 <= player_character.stat_str <= 4:
        player_character.strength_atck_mod = -2
        player_character.strength_damage_mod = -1
        player_character.carry_capacity_mod = -5
        player_character.door_crack_mod = 1
    elif 5 <= player_character.stat_str <= 6:
        player_character.strength_atck_mod = -1
        player_character.strength_damage_mod = 0
        player_character.carry_capacity_mod = -2.5
        player_character.door_crack_mod = 1
    elif 7 <= player_character.stat_str <= 8:
        player_character.strength_atck_mod = 0
        player_character.strength_damage_mod = 0
        player_character.carry_capacity_mod = 0
        player_character.door_crack_mod = 2
    elif 9 <= player_character.stat_str <= 12:
        player_character.strength_atck_mod = 0
        player_character.strength_damage_mod = 0
        player_character.carry_capacity_mod = 2.5
        player_character.door_crack_mod = 2
    elif 13 <= player_character.stat_str <= 15:
        player_character.strength_atck_mod = 1 if player_character.profession.lower() == "fighter" else 0
        player_character.strength_damage_mod = 0
        player_character.carry_capacity_mod = 5
        player_character.door_crack_mod = 2
    elif player_character.stat_str == 16:
        player_character.strength_atck_mod = 1 if player_character.profession.lower() == "fighter" else 0
        player_character.strength_damage_mod = 1 if player_character.profession.lower() == "fighter" else 0
        player_character.carry_capacity_mod = 7.5
        player_character.door_crack_mod = 3
    elif player_character.stat_str == 17:
        player_character.strength_atck_mod = 2 if player_character.profession.lower() == "fighter" else 0
        player_character.strength_damage_mod = 2 if player_character.profession.lower() == "fighter" else 0
        player_character.carry_capacity_mod = 15
        player_character.door_crack_mod = 4
    elif player_character.stat_str == 18:
        player_character.strength_atck_mod = 2 if player_character.profession.lower() == "fighter" else 0
        player_character.strength_damage_mod = 3 if player_character.profession.lower() == "fighter" else 0
        player_character.carry_capacity_mod = 25
        player_character.door_crack_mod = 5
    else:
        raise ValueError("Strength stat out of bounds:", player_character.stat_str)

def analyze_mod_dex(player_character: PlayerClass):
    """Calculate dexterity based modifiers."""
    if 3 <= player_character.stat_dex <= 8:
        player_character.ranged_atck_mod = -1
        player_character.ac_mod = -1
    elif 9 <= player_character.stat_dex <= 12:
        player_character.ranged_atck_mod = 0
        player_character.ac_mod = 0
    elif 13 <= player_character.stat_dex <= 18:
        player_character.ranged_atck_mod = 1
        player_character.ac_mod = 1
    else:
        raise ValueError("Dexterity stat out of bounds:", player_character.stat_dex)

    # Update AC with DEX modifier
    player_character.ac += player_character.ac_mod

def analyze_mod_con(player_character: PlayerClass):
    """Calculate constitution based modifiers."""
    if 3 <= player_character.stat_con <= 8:
        player_character.tp_mod = -1
        player_character.raise_dead_mod = 50
    elif 9 <= player_character.stat_con <= 12:
        player_character.tp_mod = 0
        player_character.raise_dead_mod = 75
    elif 13 <= player_character.stat_con <= 18:
        player_character.tp_mod = 1
        player_character.raise_dead_mod = 100
    else:
        raise ValueError("Constitution stat out of bounds:", player_character.stat_con)

def analyze_mod_int(player_character: PlayerClass):
    """Calculate intelligence based modifiers."""
    if 3 <= player_character.stat_int <= 7:
        player_character.max_add_langs = 0
        player_character.highest_spell_level = 4
        player_character.understand_spell = 30
        player_character.min_spells_per_level = 2
        player_character.max_spells_per_level = 4
    elif player_character.stat_int == 8:
        player_character.max_add_langs = 1
        player_character.highest_spell_level = 5
        player_character.understand_spell = 40
        player_character.min_spells_per_level = 3
        player_character.max_spells_per_level = 5
    elif player_character.stat_int == 9:
        player_character.max_add_langs = 1
        player_character.highest_spell_level = 5
        player_character.understand_spell = 45
        player_character.min_spells_per_level = 3
        player_character.max_spells_per_level = 5
    elif player_character.stat_int == 10:
        player_character.max_add_langs = 2
        player_character.highest_spell_level = 5
        player_character.understand_spell = 50
        player_character.min_spells_per_level = 4
        player_character.max_spells_per_level = 6
    elif player_character.stat_int == 11:
        player_character.max_add_langs = 2
        player_character.highest_spell_level = 6
        player_character.understand_spell = 50
        player_character.min_spells_per_level = 4
        player_character.max_spells_per_level = 6
    elif player_character.stat_int == 12:
        player_character.max_add_langs = 3
        player_character.highest_spell_level = 6
        player_character.understand_spell = 55
        player_character.min_spells_per_level = 4
        player_character.max_spells_per_level = 6
    elif player_character.stat_int == 13:
        player_character.max_add_langs = 3
        player_character.highest_spell_level = 7
        player_character.understand_spell = 65
        player_character.min_spells_per_level = 5
        player_character.max_spells_per_level = 8
    elif player_character.stat_int == 14:
        player_character.max_add_langs = 4
        player_character.highest_spell_level = 7
        player_character.understand_spell = 65
        player_character.min_spells_per_level = 5
        player_character.max_spells_per_level = 8
    elif player_character.stat_int == 15:
        player_character.max_add_langs = 4
        player_character.highest_spell_level = 8
        player_character.understand_spell = 75
        player_character.min_spells_per_level = 6
        player_character.max_spells_per_level = 10
    elif player_character.stat_int == 16:
        player_character.max_add_langs = 5
        player_character.highest_spell_level = 8
        player_character.understand_spell = 75
        player_character.min_spells_per_level = 6
        player_character.max_spells_per_level = 10
    elif player_character.stat_int == 17:
        player_character.max_add_langs = 5
        player_character.highest_spell_level = 9
        player_character.understand_spell = 85
        player_character.min_spells_per_level = 7
        player_character.max_spells_per_level = 100
    elif player_character.stat_int == 18:
        player_character.max_add_langs = 6
        player_character.highest_spell_level = 9
        player_character.understand_spell = 95
        player_character.min_spells_per_level = 8
        player_character.max_spells_per_level = 100
    else:
        raise ValueError("Intelligence stat out of bounds:", player_character.stat_int)

def analyze_mod_char(player_character: PlayerClass):
    """Calculate charisma based modifiers."""
    if 3 <= player_character.stat_char <= 4:
        player_character.cap_spec_hirelings = 1 
    elif 5 <= player_character.stat_char <= 6:
        player_character.cap_spec_hirelings = 2
    elif 7 <= player_character.stat_char <= 8:
        player_character.cap_spec_hirelings = 3
    elif 9 <= player_character.stat_char <= 12:
        player_character.cap_spec_hirelings = 4
    elif 13 <= player_character.stat_char <= 15:
        player_character.cap_spec_hirelings = 5
    elif 16 <= player_character.stat_char <= 17:
        player_character.cap_spec_hirelings = 6
    elif player_character.stat_char == 18:
        player_character.cap_spec_hirelings = 7
    else:
        raise ValueError("Charisma stat out of bounds:", player_character.stat_char)
