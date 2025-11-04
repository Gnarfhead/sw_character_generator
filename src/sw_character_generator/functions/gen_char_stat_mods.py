def analyze_mod_str(strength: float):
    """Calculate attack modifier based on strength score."""
    if strength <= 4 and strength >= 3:
        strength_atck_mod = -2
        strength_damage_mod = -1
        carry_capacity_mod = -5
        door_crack_mod = 1
        return strength_atck_mod, strength_damage_mod, carry_capacity_mod, door_crack_mod
    elif strength <= 6 and strength >= 5:
        strength_atck_mod = -1
        strength_damage_mod = 0
        carry_capacity_mod = -2,5
        door_crack_mod = 1
        return strength_atck_mod, strength_damage_mod, carry_capacity_mod, door_crack_mod
    elif strength <= 8 and strength >= 7:
        strength_atck_mod = 0
        strength_damage_mod = 0
        carry_capacity_mod = 0
        door_crack_mod =2
        return strength_atck_mod, strength_damage_mod, carry_capacity_mod, door_crack_mod
    elif strength <= 12 and strength >= 9:
        strength_atck_mod = 0
        strength_damage_mod = 0 
        carry_capacity_mod = +2,5
        door_crack_mod = 2
        return strength_atck_mod, strength_damage_mod, carry_capacity_mod, door_crack_mod
    elif strength <= 15 and strength >= 13:
        strength_atck_mod = +1
        strength_damage_mod = 0
        carry_capacity_mod = +5
        door_crack_mod = 2
        return strength_atck_mod, strength_damage_mod, carry_capacity_mod, door_crack_mod
    elif strength == 16:
        strength_atck_mod = +1
        strength_damage_mod = +1
        carry_capacity_mod = +7,5
        door_crack_mod = 3
        return strength_atck_mod, strength_damage_mod, carry_capacity_mod, door_crack_mod
    elif strength == 17:
        strength_atck_mod = +2
        strength_damage_mod = +2
        carry_capacity_mod = +15
        door_crack_mod = 4
        return strength_atck_mod, strength_damage_mod, carry_capacity_mod, door_crack_mod
    elif strength == 18:
        strength_atck_mod = +2
        strength_damage_mod = +3
        carry_capacity_mod = +25
        door_crack_mod = 5
        return strength_atck_mod, strength_damage_mod, carry_capacity_mod, door_crack_mod
    
def analyze_mod_dex(dexterity: int):
    """Calculate attack modifier based on strength score."""
    if dexterity <= 8 and dexterity >= 3:
        ranged_atck_mod = -1
        ac_bon = -1
        return ranged_atck_mod, ac_bon
    elif dexterity <= 12 and dexterity >= 9:
        ranged_atck_mod = 0
        ac_bon = 0
        return ranged_atck_mod, ac_bon
    elif dexterity <= 18 and dexterity >= 13:
        ranged_atck_mod = +1
        ac_bon = +1
        return ranged_atck_mod, ac_bon

def analyze_mod_con(constitution: int):
    """Calculate constitution based modifiers."""
    if constitution <= 8 and constitution >= 3:
        tp_bon = -1
        raise_dead_mod = 50
        return tp_bon, raise_dead_mod
    elif constitution <= 12 and constitution >= 9:
        tp_bon = 0
        raise_dead_mod = 75
        return tp_bon, raise_dead_mod
    elif constitution <= 18 and constitution >= 13:
        tp_bon = +1
        raise_dead_mod = 100
        return tp_bon, raise_dead_mod
    

def analyze_mod_int(intelligence: int):
    """Calculate analyze modifier based on intelligence score."""
    if intelligence <= 7 and intelligence >= 3:
        max_add_langs = 0
        highest_spell_level = 4
        understand_spell = 30
        min_spells_per_level = 2
        max_spells_per_level = 4
        return max_add_langs, highest_spell_level, understand_spell, min_spells_per_level, max_spells_per_level
    elif intelligence == 8:
        max_add_langs = 1
        highest_spell_level = 5
        understand_spell = 40
        min_spells_per_level = 3
        max_spells_per_level = 5
        return max_add_langs, highest_spell_level, understand_spell, min_spells_per_level, max_spells_per_level
    elif intelligence == 9:
        max_add_langs = 1
        highest_spell_level = 45
        understand_spell = 45
        min_spells_per_level = 3
        max_spells_per_level = 5
        return max_add_langs, highest_spell_level, understand_spell, min_spells_per_level, max_spells_per_level
    elif intelligence == 10:
        max_add_langs = 2
        highest_spell_level = 5
        understand_spell = 50
        min_spells_per_level = 4
        max_spells_per_level = 6
        return max_add_langs, highest_spell_level, understand_spell, min_spells_per_level, max_spells_per_level
    elif intelligence == 11:
        max_add_langs = 2
        highest_spell_level = 6
        understand_spell = 50
        min_spells_per_level = 4
        max_spells_per_level = 6
        return max_add_langs, highest_spell_level, understand_spell, min_spells_per_level, max_spells_per_level
    elif intelligence == 12:
        max_add_langs = 3
        highest_spell_level = 5
        understand_spell = 55
        min_spells_per_level = 4
        max_spells_per_level = 6
        return max_add_langs, highest_spell_level, understand_spell, min_spells_per_level, max_spells_per_level
    elif intelligence == 13:
        max_add_langs = 3
        highest_spell_level = 7
        understand_spell = 65
        min_spells_per_level = 5
        max_spells_per_level = 8
        return max_add_langs, highest_spell_level, understand_spell, min_spells_per_level, max_spells_per_level
    elif intelligence == 14:
        max_add_langs = 4
        highest_spell_level = 7
        understand_spell = 65
        min_spells_per_level = 5
        max_spells_per_level = 8
        return max_add_langs, highest_spell_level, understand_spell, min_spells_per_level, max_spells_per_level
    elif intelligence == 15:
        max_add_langs = 4
        highest_spell_level = 8
        understand_spell = 75
        min_spells_per_level = 6
        max_spells_per_level = 10
        return max_add_langs, highest_spell_level, understand_spell, min_spells_per_level, max_spells_per_level
    elif intelligence == 16:
        max_add_langs = 5
        highest_spell_level = 8
        understand_spell = 75
        min_spells_per_level = 6
        max_spells_per_level = 10
        return max_add_langs, highest_spell_level, understand_spell, min_spells_per_level, max_spells_per_level
    elif intelligence == 17:
        max_add_langs = 5
        highest_spell_level = 9
        understand_spell = 85
        min_spells_per_level = 7
        max_spells_per_level = 100
        return max_add_langs, highest_spell_level, understand_spell, min_spells_per_level, max_spells_per_level
    elif intelligence == 18:
        max_add_langs = 6
        highest_spell_level = 9
        understand_spell = 95
        min_spells_per_level = 8
        max_spells_per_level = 100
        return max_add_langs, highest_spell_level, understand_spell, min_spells_per_level, max_spells_per_level
    
def analyze_mod_char(charisma: int):
    """Calculate constitution based modifiers."""
    if charisma <= 4 and charisma >= 3:
        cap_spec_hirelings = 1
        return cap_spec_hirelings
    elif charisma <= 6 and charisma >= 5:
        cap_spec_hirelings = 2
        return cap_spec_hirelings
    elif charisma <= 8 and charisma >= 7:
        cap_spec_hirelings = 3
        return cap_spec_hirelings
    elif charisma <= 12 and charisma >= 9:
        cap_spec_hirelings = 4
        return cap_spec_hirelings
    elif charisma <= 15 and charisma >= 13:
        cap_spec_hirelings = 5
        return cap_spec_hirelings
    elif charisma <= 17 and charisma >= 16:
        cap_spec_hirelings = 6
        return cap_spec_hirelings
    elif charisma == 18:
        cap_spec_hirelings = 7
        return cap_spec_hirelings
    


