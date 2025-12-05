"""Functions to analyze character stats and return corresponding modifiers."""
from src.sw_character_generator.classes.playerclass import PlayerClass

def analyze_mod_str(player_character: PlayerClass):
    """Calculate strength-based modifiers. Positive bonuses only apply to fighters."""
    print("DEBUG analyze_mod_str: --------------------------------")

    # Use Total value if set, otherwise use base value
    effective_str = player_character.stat_str_total if player_character.stat_str_total > 0 else player_character.stat_str
    print("DEBUG analyze_mod_str: effective_str =", effective_str)
    
    try:
        if 3 <= effective_str <= 4:
            player_character.strength_atck_mod = -2
            player_character.strength_damage_mod = -1
            player_character.carry_capacity_mod = -5
            player_character.door_crack_mod = 1
        elif 5 <= effective_str <= 6:
            player_character.strength_atck_mod = -1
            player_character.strength_damage_mod = 0
            player_character.carry_capacity_mod = -2.5
            player_character.door_crack_mod = 1
        elif 7 <= effective_str <= 8:
            player_character.strength_atck_mod = 0
            player_character.strength_damage_mod = 0
            player_character.carry_capacity_mod = 0
            player_character.door_crack_mod = 2
        elif 9 <= effective_str <= 12:
            player_character.strength_atck_mod = 0
            player_character.strength_damage_mod = 0
            player_character.carry_capacity_mod = 2.5
            player_character.door_crack_mod = 2
        elif 13 <= effective_str <= 15:
            player_character.strength_atck_mod = 1 if player_character.profession.lower() == "fighter" else 0
            player_character.strength_damage_mod = 0
            player_character.carry_capacity_mod = 5
            player_character.door_crack_mod = 2
        elif effective_str == 16:
            player_character.strength_atck_mod = 1 if player_character.profession.lower() == "fighter" else 0
            player_character.strength_damage_mod = 1 if player_character.profession.lower() == "fighter" else 0
            player_character.carry_capacity_mod = 7.5
            player_character.door_crack_mod = 3
        elif effective_str == 17:
            player_character.strength_atck_mod = 2 if player_character.profession.lower() == "fighter" else 0
            player_character.strength_damage_mod = 2 if player_character.profession.lower() == "fighter" else 0
            player_character.carry_capacity_mod = 15
            player_character.door_crack_mod = 4
        elif effective_str == 18:
            player_character.strength_atck_mod = 2 if player_character.profession.lower() == "fighter" else 0
            player_character.strength_damage_mod = 3 if player_character.profession.lower() == "fighter" else 0
            player_character.carry_capacity_mod = 25
            player_character.door_crack_mod = 5
    except Exception as e:
        raise ValueError("DEBUG analyze_mod_str: Error calculating strength modifiers:", e)
    
    # Calculate total modifiers including temporary ones
    player_character.strength_atck_mod_total = player_character.strength_atck_mod + player_character.strength_atck_mod_temp
    player_character.strength_damage_mod_total = player_character.strength_damage_mod + player_character.strength_damage_mod_temp

def analyze_mod_dex(player_character: PlayerClass):
    """Calculate dexterity based modifiers."""
    print("DEBUG analyze_mod_dex: --------------------------------")

    # Use total value if set, otherwise use base value
    effective_dex = player_character.stat_dex_total if player_character.stat_dex_total > 0 else player_character.stat_dex
    print("DEBUG analyze_mod_dex: effective_dex =", effective_dex)

    try:
        if 3 <= effective_dex <= 8:
            player_character.ranged_atck_mod = -1
            player_character.ac_mod = -1
        elif 9 <= effective_dex <= 12:
            player_character.ranged_atck_mod = 0
            player_character.ac_mod = 0
        elif 13 <= effective_dex <= 18:
            player_character.ranged_atck_mod = 1
            player_character.ac_mod = 1
    except Exception as e:
        raise ValueError("DEBUG analyze_mod_dex: Error calculating dexterity modifiers:", e)
    
    player_character.ranged_atck_mod_total = (
        player_character.ranged_atck_mod + 
        player_character.ranged_atck_mod_race + 
        player_character.ranged_atck_mod_temp
    )
    
def analyze_mod_con(player_character: PlayerClass):
    """Calculate constitution based modifiers."""
    print("DEBUG analyze_mod_con: --------------------------------")

    # Use total value if set, otherwise use base value
    effective_con = player_character.stat_con_total if player_character.stat_con_total > 0 else player_character.stat_con
    print("DEBUG analyze_mod_con: effective_con =", effective_con)

    try:
        if 3 <= effective_con <= 8:
            player_character.hp_mod = -1
            player_character.raise_dead_mod = 50
        elif 9 <= effective_con <= 12:
            player_character.hp_mod = 0
            player_character.raise_dead_mod = 75
        elif 13 <= effective_con <= 18:
            player_character.hp_mod = 1
            player_character.raise_dead_mod = 100
    except Exception as e:
        raise ValueError("DEBUG analyze_mod_con: Error calculating constitution modifiers:", e)

def analyze_mod_int(player_character: PlayerClass):
    """Calculate intelligence based modifiers."""
    print("DEBUG analyze_mod_int: --------------------------------")

    # Use total value if set, otherwise use base value
    effective_int = player_character.stat_int_total if player_character.stat_int_total > 0 else player_character.stat_int
    print("DEBUG analyze_mod_int: effective_int =", effective_int)

    try:
        if 3 <= effective_int <= 7:
            player_character.max_add_langs = 0
            player_character.highest_spell_level = 4
            player_character.understand_spell = 30
            player_character.min_spells_per_level = 2
            player_character.max_spells_per_level = 4
        elif effective_int == 8:
            player_character.max_add_langs = 1
            player_character.highest_spell_level = 5
            player_character.understand_spell = 40
            player_character.min_spells_per_level = 3
            player_character.max_spells_per_level = 5
        elif effective_int == 9:
            player_character.max_add_langs = 1
            player_character.highest_spell_level = 5
            player_character.understand_spell = 45
            player_character.min_spells_per_level = 3
            player_character.max_spells_per_level = 5
        elif effective_int == 10:
            player_character.max_add_langs = 2
            player_character.highest_spell_level = 5
            player_character.understand_spell = 50
            player_character.min_spells_per_level = 4
            player_character.max_spells_per_level = 6
        elif effective_int == 11:
            player_character.max_add_langs = 2
            player_character.highest_spell_level = 6
            player_character.understand_spell = 50
            player_character.min_spells_per_level = 4
            player_character.max_spells_per_level = 6
        elif effective_int == 12:
            player_character.max_add_langs = 3
            player_character.highest_spell_level = 6
            player_character.understand_spell = 55
            player_character.min_spells_per_level = 4
            player_character.max_spells_per_level = 6
        elif effective_int == 13:
            player_character.max_add_langs = 3
            player_character.highest_spell_level = 7
            player_character.understand_spell = 65
            player_character.min_spells_per_level = 5
            player_character.max_spells_per_level = 8
        elif effective_int == 14:
            player_character.max_add_langs = 4
            player_character.highest_spell_level = 7
            player_character.understand_spell = 65
            player_character.min_spells_per_level = 5
            player_character.max_spells_per_level = 8
        elif effective_int == 15:
            player_character.max_add_langs = 4
            player_character.highest_spell_level = 8
            player_character.understand_spell = 75
            player_character.min_spells_per_level = 6
            player_character.max_spells_per_level = 10
        elif effective_int == 16:
            player_character.max_add_langs = 5
            player_character.highest_spell_level = 8
            player_character.understand_spell = 75
            player_character.min_spells_per_level = 6
            player_character.max_spells_per_level = 10
        elif effective_int == 17:
            player_character.max_add_langs = 5
            player_character.highest_spell_level = 9
            player_character.understand_spell = 85
            player_character.min_spells_per_level = 7
            player_character.max_spells_per_level = 100
        elif effective_int == 18:
            player_character.max_add_langs = 6
            player_character.highest_spell_level = 9
            player_character.understand_spell = 95
            player_character.min_spells_per_level = 8
            player_character.max_spells_per_level = 100
    except Exception as e:
        raise ValueError("DEBUG analyze_mod_int: Error calculating intelligence modifiers:", e)
    
def analyze_mod_wis(player_character: PlayerClass):
    """Calculate wisdom based modifiers."""
    print("DEBUG analyze_mod_wis: --------------------------------")

    effective_wis = player_character.stat_wis_total if player_character.stat_wis_total > 0 else player_character.stat_wis
    print("DEBUG analyze_mod_wis: effective_wis =", effective_wis)

def analyze_mod_char(player_character: PlayerClass):
    """Calculate charisma based modifiers."""
    print("DEBUG analyze_mod_char: --------------------------------")

    effective_char = player_character.stat_char_total if player_character.stat_char_total > 0 else player_character.stat_char
    print("DEBUG analyze_mod_char: effective_char =", effective_char)

    try:
        if 3 <= effective_char <= 4:
            player_character.cap_spec_hirelings = 1
        elif 5 <= effective_char <= 6:
            player_character.cap_spec_hirelings = 2
        elif 7 <= effective_char <= 8:
            player_character.cap_spec_hirelings = 3
        elif 9 <= effective_char <= 12:
            player_character.cap_spec_hirelings = 4
        elif 13 <= effective_char <= 15:
            player_character.cap_spec_hirelings = 5
        elif 16 <= effective_char <= 17:
            player_character.cap_spec_hirelings = 6
        elif effective_char == 18:
            player_character.cap_spec_hirelings = 7
    except Exception as e:
        raise ValueError("DEBUG analyze_mod_char: Error calculating charisma modifiers:", e)

def analyze_parry(player_character: PlayerClass):
    """Calculate parry based on DEX (Fighter only)."""
    print("DEBUG analyze_parry: --------------------------------")
    
    # Parry only applies to Fighters
    if player_character.profession.lower() != "fighter":
        player_character.parry = 0
        return
    
    # Use total value (base + temp) if set, otherwise use base value
    effective_dex = player_character.stat_dex_total if player_character.stat_dex_total > 0 else player_character.stat_dex
    
    try:
        if effective_dex >= 18:
            player_character.parry = -5
        elif effective_dex == 17:
            player_character.parry = -4
        elif effective_dex == 16:
            player_character.parry = -3
        elif effective_dex == 15:
            player_character.parry = -2
        elif effective_dex == 14:
            player_character.parry = -1
        else:
            player_character.parry = 0
    except Exception as e:
        raise ValueError("DEBUG analyze_parry: Error calculating parry modifier:", e)