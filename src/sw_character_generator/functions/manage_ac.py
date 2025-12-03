"""Module to manage Armor Class (AC) calculations for characters."""

def calculate_ac(character):
    """Calculate the Armor Class (AC) for the character."""
    print("DEBUG calculate_ac: ------------------------------------------------")
    base_ac = character.ac
    dex_mod = character.ac_mod
    temp_mod = character.ac_mod_temp
    character.ac_total = base_ac + dex_mod + temp_mod
    print("DEBUG calculate_ac: Base AC=", {base_ac}, "DEX Mod=", {dex_mod}, "Temp Mod=", {temp_mod}, "Total AC=", {character.ac_total})
    return character.ac_total