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

    if armor and hasattr(armor, 'acbonus') and armor.acbonus is not None:
        character.ac_armor = armor.acbonus
        print("DEBUG update_armor_ac: Equipped armor", armor.name, "with AC bonus", armor.acbonus)
        print("DEBUG update_armor_ac: character.ac_armor set to", character.ac_armor)
    else:
        character.ac_armor = 0
        print("DEBUG update_armor_ac: No armor equipped or no AC bonus")
        print("DEBUG update_armor_ac: character.ac_armor set to", character.ac_armor)

    if shield and hasattr(shield, 'type') and shield.type.lower() == "shield" and hasattr(shield, 'acbonus') and shield.acbonus is not None:
        character.ac_shield = shield.acbonus
        print("DEBUG update_armor_ac: Equipped shield", shield.name, "with AC bonus", shield.acbonus)
        print("DEBUG update_armor_ac: character.ac_shield set to", character.ac_shield)
    else:
        character.ac_shield = 0
        print("DEBUG update_armor_ac: No shield equipped or no AC bonus")
        print("DEBUG update_armor_ac: character.ac_shield set to", character.ac_shield)

    calculate_ac(character)
    