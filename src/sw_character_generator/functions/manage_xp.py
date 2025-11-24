"""Manage Experience Point (XP) calculations for characters."""


from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model


def calculate_xp_bonus(app, character=None):
    """Berechnet XP-Bonus; akzeptiert entweder App oder (fallback) Character direkt."""
    # Determine the character to use
    if hasattr(app, "new_player"):
        player = app.new_player
    elif character is not None:
        player = character
    else:
        raise ValueError("ERROR calculate_xp_bonus: No character provided for XP bonus calculation.")
    
    # General bonus calculation
    print("DEBUG calculate_xp_bonus: Calculating XP bonus for character...")    # General attribute bonuses
    player.xp_bonus = 0  # Reset XP bonus
    if player.stat_wis >= 13:
        player.xp_bonus += 5
    if player.stat_char >= 13:
        player.xp_bonus += 5

    # Profession-specific bonuses
    if player.profession.lower() == "assassin":
        print("DEBUG calculate_xp_bonus: Profession is assassin.")
        if player.stat_str >= 13:
            player.xp_bonus += 5
        if player.stat_dex >= 13:
            player.xp_bonus += 5
        if player.stat_int >= 13:
            player.xp_bonus += 5
    elif player.profession.lower() == "cleric":
        print("DEBUG calculate_xp_bonus: Profession is cleric.")
        if player.stat_wis >= 13:
            player.xp_bonus += 5
    elif player.profession.lower() == "druid":
        print("DEBUG calculate_xp_bonus: Profession is druid.")
        if player.stat_wis >= 13:
            player.xp_bonus += 5
        if player.stat_char >= 13:
            player.xp_bonus += 5
    elif player.profession.lower() == "fighter":
        print("DEBUG calculate_xp_bonus: Profession is Fighter.")
        if player.stat_str >= 13:
            player.xp_bonus += 5
    elif player.profession.lower() == "monk":
        print("DEBUG calculate_xp_bonus: Profession is monk.")
        if player.stat_wis >= 13:
            player.xp_bonus += 5
    elif player.profession.lower() == "paladin":
        print("DEBUG calculate_xp_bonus: Profession is paladin.")
        if player.stat_str >= 13:
            player.xp_bonus += 5
    elif player.profession.lower() == "ranger":
        print("DEBUG calculate_xp_bonus: Profession is ranger.")
        if player.stat_str >= 13:
            player.xp_bonus += 5
    elif player.profession.lower() == "thief":
        print("DEBUG calculate_xp_bonus: Profession is thief.")
        if player.stat_dex >= 13:
            player.xp_bonus += 5
    elif player.profession.lower() == "wizard":
        print("DEBUG calculate_xp_bonus: Profession is wizard.")
        if player.stat_int >= 13:
            player.xp_bonus += 5
    else:
        print(f"ERROR calculate_xp_bonus: Unknown profession '{player.profession}'")

    # Final debug output
    print(f"DEBUG calculate_xp_bonus: Total XP bonus calculated: {player.xp_bonus}")

    # Update the GUI to reflect the new XP bonus
    if hasattr(app, "new_player"):
        update_view_from_model(app)
    

def add_xp(app, amount):
    """Fügt dem Charakter XP hinzu und aktualisiert die Ansicht."""
    if hasattr(app, "new_player"):
        player = app.new_player
        current_level = player.level
        next_level = player.xp_progression.get(current_level + 1)
        #next_level_xp = 
        print(f"DEBUG add_xp: Current level: {current_level}")
        
        
        player.xp = max(0, player.xp + amount) # Ensure XP does not go below 0
        
        
        print(f"DEBUG add_xp: Added {amount} XP. New total: {player.xp}")
        update_view_from_model(app)
    else:
        raise ValueError("ERROR add_xp: No character available to add XP to.")
