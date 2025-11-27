"""Manage Experience Point (XP) calculations for characters."""

from sw_character_generator.functions.manage_hp import reenable_hp_roll_button, remove_tp_on_level_down
from sw_character_generator.functions.manage_saving_throw import calculate_saving_throw
from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model


def calculate_xp_bonus(character=None):
    """Berechnet XP-Bonus; akzeptiert entweder App oder (fallback) Character direkt."""
    print("DEBUG calculate_xp_bonus: ----------------------------------------------------------------")

    # Determine the character to use
    if character is None:
        raise ValueError("ERROR calculate_xp_bonus: No character provided for XP bonus calculation.")
    
    # General bonus calculation
    print("DEBUG calculate_xp_bonus: Calculating XP bonus for character...")    # General attribute bonuses
    character.xp_bonus = 0  # Reset XP bonus
    if character.stat_wis >= 13:
        character.xp_bonus += 5
    if character.stat_char >= 13:
        character.xp_bonus += 5

    # Profession-specific bonuses
    if character.profession.lower() == "assassin":
        print("DEBUG calculate_xp_bonus: Profession is assassin.")
        if character.stat_str >= 13:
            character.xp_bonus += 5
        if character.stat_dex >= 13:
            character.xp_bonus += 5
        if character.stat_int >= 13:
            character.xp_bonus += 5
    elif character.profession.lower() == "cleric":
        print("DEBUG calculate_xp_bonus: Profession is cleric.")
        if character.stat_wis >= 13:
            character.xp_bonus += 5
    elif character.profession.lower() == "druid":
        print("DEBUG calculate_xp_bonus: Profession is druid.")
        if character.stat_wis >= 13:
            character.xp_bonus += 5
        if character.stat_char >= 13:
            character.xp_bonus += 5
    elif character.profession.lower() == "fighter":
        print("DEBUG calculate_xp_bonus: Profession is Fighter.")
        if character.stat_str >= 13:
            character.xp_bonus += 5
    elif character.profession.lower() == "monk":
        print("DEBUG calculate_xp_bonus: Profession is monk.")
        if character.stat_wis >= 13:
            character.xp_bonus += 5
    elif character.profession.lower() == "paladin":
        print("DEBUG calculate_xp_bonus: Profession is paladin.")
        if character.stat_str >= 13:
            character.xp_bonus += 5
    elif character.profession.lower() == "ranger":
        print("DEBUG calculate_xp_bonus: Profession is ranger.")
        if character.stat_str >= 13:
            character.xp_bonus += 5
    elif character.profession.lower() == "thief":
        print("DEBUG calculate_xp_bonus: Profession is thief.")
        if character.stat_dex >= 13:
            character.xp_bonus += 5
    elif character.profession.lower() == "wizard":
        print("DEBUG calculate_xp_bonus: Profession is wizard.")
        if character.stat_int >= 13:
            character.xp_bonus += 5
    else:
        print(f"ERROR calculate_xp_bonus: Unknown profession '{character.profession}'")

    # Final debug output
    print(f"DEBUG calculate_xp_bonus: Total XP bonus calculated: {character.xp_bonus}")


def calculate_next_level_xp(app, character=None):
    """Berechnet die XP-Anforderungen für die nächste Stufe und aktualisiert die Ansicht."""
    print("DEBUG calculate_next_level_xp: ----------------------------------------------------------------")

    # Determine the character to use
    if character is None:
        raise ValueError("ERROR calculate_next_level_xp: No character provided for XP calculation.")

    # Determine current and next level XP requirements
    current_level = character.level # Current level of the character
    print("DEBUG calculate_next_level_xp: Current level is:", current_level)
    next_level = character.level + 1 # Next level to reach
    print("DEBUG calculate_next_level_xp: Next level is:", next_level)
    next_level_xp = character.xp_progression.get(next_level, None)  # XP required for the level after next
    print("DEBUG calculate_next_level_xp: Next level XP requirement is:", next_level_xp)
    app.nextlevel_var.set(next_level_xp) # Update the GUI variable
    print("DEBUG calculate_next_level_xp: Current XP:", character.xp)

    # Calculate the XP needed for the next level
    update_view_from_model(app)


def add_xp(app, amount = 0, character=None):
    """Fügt dem Charakter XP hinzu und aktualisiert die Ansicht."""
    print("DEBUG add_xp: ----------------------------------------------------------------")

    # Determine the character to use
    if hasattr(app, "new_player"):
        print("DEBUG add_xp: Using app.new_player.")
        player = app.new_player
    elif character is not None:
        print("DEBUG add_xp: Using provided character.")
        player = character
    else:
        raise ValueError("ERROR add_xp: No character provided for XP calculation.")

    # Apply XP bonus
    print("DEBUG add_xp: Base amount to add:", amount)
    modified_amount = round(amount * (1 + player.xp_bonus / 100), 0) # Apply XP bonus
    print("DEBUG add_xp: Modified amount and type after applying bonus and rounding:", modified_amount, type(modified_amount))
    modified_amount = int(modified_amount)
    print("DEBUG add_xp: Modified amount and type after conversion to integer:", modified_amount, type(modified_amount))

    # Update player's XP
    print("DEBUG add_xp: Adding amount:", amount)
    player.xp = max(0, player.xp + modified_amount) # Ensure XP does not go below 0
    print("DEBUG add_xp: New XP:", player.xp)
    app.status_var.set(f"Added {modified_amount} XP (base: {amount}, bonus: {player.xp_bonus}%). New XP: {player.xp}.")
    app.spin_add_xp.set(0)  # Reset the add XP spinbox

    # Level up calculation
    next_level_xp = player.xp_progression.get(player.level + 1, None)
    print("DEBUG add_xp: Next level xp requirement:", next_level_xp)
    if next_level_xp is not None and player.xp >= next_level_xp: # Level up check
        player.level += 1 # Increase level
        print("DEBUG add_xp: Level up! New level:", player.level)
        app.status_var.set(f"Congratulations! You've reached level {player.level}!")
        # Enable HP roll button
        reenable_hp_roll_button(app) # re-enable HP roll button
        # calculate XP for next level
        calculate_next_level_xp(app, player) # calculate XP for next level
        calculate_saving_throw(player) # recalculate saving throws
    elif next_level_xp is not None and player.xp < player.xp_progression.get(player.level, 0): # Level down check
        player.level -= 1 if player.level > 1 else 1 # Prevent level going below 1
        print("DEBUG add_xp: Level down! New level:", player.level)
        app.status_var.set(f"You have dropped to level {player.level}.")
        remove_tp_on_level_down(app, player) # remove TP on level down
        calculate_next_level_xp(app, player) # calculate XP for next level
        calculate_saving_throw(player) # recalculate saving throws
    else:   
        print("DEBUG add_xp: No level change.")
        
    # Update the GUI to reflect the new XP values
    update_view_from_model(app)
