"""Centralized function to update all derived character statistics."""
from sw_character_generator.functions.manage_ac import calculate_ac
from sw_character_generator.functions.gen_char_stat_mods import analyze_mod_char, analyze_mod_con, analyze_mod_dex, analyze_mod_int, analyze_mod_str, analyze_mod_wis, analyze_parry
from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model

def update_derived_stats(character, app=None):
    """
    Recalculate all derived stats for the character.
    
    Args:
        character: PlayerClass instance
        app: Optional App instance for GUI updates
    """
    print("DEBUG update_derived_stats: --------------------------------")
    
    # Recalculate attribute bonuses
    analyze_mod_str(character)
    analyze_mod_char(character)
    analyze_mod_con(character)
    analyze_mod_dex(character)
    analyze_mod_int(character)
    analyze_mod_wis(character)

    # Recalculate parry (depends on strength and dexterity)
    analyze_parry(character)

    # Recalculate AC (depends on dexterity)
    calculate_ac(character)
    
    # Update GUI if app is provided
    if app:
        
        with app.suppress_updates():
            update_view_from_model(app)
    
    print("DEBUG update_derived_stats: AC Total =", {character.ac_total})