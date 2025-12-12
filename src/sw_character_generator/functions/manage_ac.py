"""Module to manage Armor Class (AC) calculations for characters."""

def calculate_ac(character):
    """Calculate the Armor Class (AC) for the character."""
    print("DEBUG calculate_ac: ------------------------------------------------")
    base_ac = character.ac
    dex_mod = character.ac_mod
    temp_mod = character.ac_mod_temp
    armor_mod = character.ac_armor
    shield_mod = character.ac_shield
    
    # Berechne Total AC (Ascending AC: höher = besser)
    character.ac_total = base_ac + dex_mod + temp_mod + armor_mod + shield_mod
    
    print(f"DEBUG calculate_ac: Base AC={base_ac}, DEX Mod={dex_mod}, Temp Mod={temp_mod}, Armor Mod={armor_mod}, Shield Mod={shield_mod}, Total AC={character.ac_total}")
    return character.ac_total

def update_armor_ac(character):
    """Update character's AC based on ALL equipped items with AC bonus."""
    print("DEBUG update_armor_ac: ================================================")
    print(f"DEBUG: Checking equipment for AC bonuses...")
    
    # ← NEUE LISTE: Alle Equipment-Slots die AC-Bonus haben können
    equipment_slots = {
        'armor': character.armor,
        'off_hand': character.off_hand,      # Shield
        'helmet': character.helmet,
        'gloves': character.gloves,
        'boots': character.boots,
        'cloak': character.cloak,
        'ring_left': character.ring_left,
        'ring_right': character.ring_right,
        'amulet': character.amulet,
        'belt': character.belt
    }
    
    # Reset AC-Boni (wichtig für korrekte Neuberechnung!)
    total_armor_bonus = 0
    total_shield_bonus = 0
    
    # ← DURCHLAUFE ALLE EQUIPMENT-SLOTS
    for slot_name, item in equipment_slots.items():
        if not item:
            print(f"DEBUG: {slot_name} is empty")
            continue  # Slot ist leer
        
        # Prüfe ob Item ein AC-Bonus hat
        if not hasattr(item, 'acbonus') or item.acbonus is None:
            continue  # Kein AC-Bonus
        
        try:
            ac_bonus = int(item.acbonus)
        except (ValueError, TypeError):
            print(f"WARNING: Invalid acbonus for {slot_name}: {item.acbonus}")
            continue
        
        # ← SPEZIELLE BEHANDLUNG FÜR SHIELD
        if slot_name == 'off_hand' and hasattr(item, 'type') and item.type.lower() == 'shield':
            total_shield_bonus += ac_bonus
            print(f"DEBUG update_armor_ac: {slot_name} (Shield) '{item.name}' → AC +{ac_bonus}")
        else:
            # Alle anderen Items (Armor, Helmet, Gloves, etc.)
            total_armor_bonus += ac_bonus
            print(f"DEBUG update_armor_ac: {slot_name} '{item.name}' → AC +{ac_bonus}")
    
    # Setze berechnete Boni
    character.ac_armor = total_armor_bonus
    character.ac_shield = total_shield_bonus
    
    print(f"DEBUG update_armor_ac: Total Armor AC Bonus = {total_armor_bonus}")
    print(f"DEBUG update_armor_ac: Total Shield AC Bonus = {total_shield_bonus}")
    
    # Berechne AC neu
    calculate_ac(character)
    
    print(f"DEBUG update_armor_ac: Final AC Total = {character.ac_total}")
    print("DEBUG update_armor_ac: ================================================")