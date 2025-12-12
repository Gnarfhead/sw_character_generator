"""Module to manage Armor Class (AC) calculations for characters."""

def calculate_ac(character):
    """Calculate the Armor Class (AC) for the character."""
    print("DEBUG calculate_ac: ------------------------------------------------")
    base_ac = character.ac
    dex_mod = character.ac_mod
    temp_mod = character.ac_mod_temp
    armor_mod = character.ac_armor
    shield_mod = character.ac_shield
    character.ac_total = base_ac + dex_mod + temp_mod + armor_mod + shield_mod
    print("DEBUG calculate_ac: Base AC=", {base_ac}, "DEX Mod=", {dex_mod}, "Temp Mod=", {temp_mod}, "Armor Mod=", {armor_mod}, "Shield Mod=", {shield_mod}, "Total AC=", {character.ac_total})
    return character.ac_total

def update_armor_ac(character):
    """Update character's AC based on equipped armor."""
    print("DEBUG update_armor_ac: ------------------------------------------------")
    armor = character.armor
    shield = character.off_hand

    # ← KORRIGIERT: Prüfe auf Item-Objekt
    if armor:
        if hasattr(armor, 'acbonus') and armor.acbonus is not None:
            character.ac_armor = armor.acbonus
            print(f"DEBUG update_armor_ac: Equipped armor '{armor.name if hasattr(armor, 'name') else armor}' with AC bonus {armor.acbonus}")
        elif isinstance(armor, str):
            print(f"WARNING: armor is string '{armor}', cannot get AC bonus")
            character.ac_armor = 0
        else:
            character.ac_armor = 0
            print("DEBUG update_armor_ac: No armor equipped or no AC bonus")
    else:
        character.ac_armor = 0
        print("DEBUG update_armor_ac: No armor equipped")

    # ← KORRIGIERT: Prüfe Shield
    if shield:
        if hasattr(shield, 'type') and shield.type.lower() == "shield":
            if hasattr(shield, 'acbonus') and shield.acbonus is not None:
                character.ac_shield = shield.acbonus
                print(f"DEBUG update_armor_ac: Equipped shield '{shield.name if hasattr(shield, 'name') else shield}' with AC bonus {shield.acbonus}")
            else:
                character.ac_shield = 0
                print("DEBUG update_armor_ac: Shield has no AC bonus")
        elif isinstance(shield, str):
            print(f"WARNING: off_hand is string '{shield}', cannot get AC bonus")
            character.ac_shield = 0
        else:
            character.ac_shield = 0
            print("DEBUG update_armor_ac: Off-hand is not a shield")
    else:
        character.ac_shield = 0
        print("DEBUG update_armor_ac: No shield equipped")

    # Berechne AC
    calculate_ac(character)
    print(f"DEBUG update_armor_ac: Final AC Total = {character.ac_total}")

    