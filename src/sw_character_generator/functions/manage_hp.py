"""Functions to modify character HP and state based on changes."""
import random
from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model


def modify_hp(delta: int, app, character=None):
    """Adjust current HP by delta; clamp; set state."""
    print("DEBUG modify_hp: ----------------------------------------------------------------")
    # Determine the character to use
    if hasattr(app, "new_player"):
        player = app.new_player
    elif character is not None:
        player = character
    else:
        raise ValueError("ERROR modify_hp: No character provided for HP bonus calculation.")

    # Modify current HP
    current = player.hp_current # Current HP
    print(f"DEBUG modify_hp: Current HP before modification: {current}/{player.hp}")
    maximum = player.hp # Max HP
    print(f"DEBUG modify_hp: Max HP: {maximum}")
    print(f"DEBUG modify_hp: Modifying HP by {delta}.")

    # Adjust current HP based on delta
    if delta >= 0:
        print(f"DEBUG modify_hp: Increasing HP by {delta}.")
        player.hp_current = min(player.hp_current + delta, maximum) # Prevent exceeding max HP
    else:
        print(f"DEBUG modify_hp: Decreasing HP by {abs(delta)}.")
        player.hp_current = max(player.hp_current + delta, 0) # Prevent going below 0 HP

    # Reset the modify HP spinbox to 0
    app.spin_modify_hp.set(0)  # Reset the spinbox to 0 after modification

    # Set player player_state based on current HP percentage
    if player.hp_current <= 0:
        print("DEBUG modify_hp: Player HP is 0 or less; setting state to Dead.")
        player.player_state = "Dead"
        app.entry_player_state.config(style="Attention.TLabel")
    elif player.hp_current <= player.hp * 0.25:
        print("DEBUG modify_hp: Player HP is 25% or less; setting state to Critical.")
        player.player_state = "Critical"
        app.entry_player_state.config(style="Attention.TLabel")
    elif player.hp_current <= player.hp * 0.5:
        print("DEBUG modify_hp: Player HP is 50% or less; setting state to Injured.")
        player.player_state = "Injured"
        app.entry_player_state.config(style="Warning.TLabel")
    elif player.hp_current <= player.hp * 0.75:
        print("DEBUG modify_hp: Player HP is 75% or less; setting state to Wounded.")
        player.player_state = "Wounded"
        app.entry_player_state.config(style="Warning.TLabel")
    else:
        print("DEBUG modify_hp: Player HP is above 75%; setting state to Healthy.")
        player.player_state = "Healthy"
        app.entry_player_state.config(style="Standard.TLabel")


    # Update the UI to reflect the new HP values
    if hasattr(app, "new_player"): # If app has new_player attribute
        print(f"DEBUG modify_hp: HP modified by {delta}. Current HP: {player.hp_current}/{player.hp} ({player.player_state})")
        app.status_var.set(f"HP modified by {delta}. Current HP: {player.hp_current}/{player.hp} ({player.player_state})")
        update_view_from_model(app)
    else:
        print(f"DEBUG modify_hp: HP modified by {delta}. Current HP: {player.hp_current}/{player.hp} ({player.player_state})")
        app.status_var.set(f"HP modified by {delta}. Current HP: {player.hp_current}/{player.hp} ({player.player_state})")
        update_view_from_model(app)

def set_roll_hp_button(app):
    """Set the roll HP button text based on checkbox state."""
    print("DEBUG set_roll_hp_button: ----------------------------------------------------------------")
    #print("DEBUG set_roll_hp_button: Called with chk_starting_hp =", app.chk_opt_fullhplvl1_var.get())
    if app.chk_opt_fullhplvl1_var.get() is True:
        print("DEBUG set_roll_hp_button: Setting roll HP button to 'Set HP'")
        app.btn_rollhp.config(text="Set HP")
    else:
        print("DEBUG set_roll_hp_button: Setting roll HP button to 'Roll HP'")
        app.btn_rollhp.config(text="Roll HP")

def set_starting_hp(app, character:PlayerClass):
    """Roll/set starting HP for the character."""
    print("DEBUG set_starting_hp: ----------------------------------------------------------------")
    if app.chk_opt_fullhplvl1_var.get() is True:
        hit_die = character.hp_dice # Use max HP from hit die
        rolled_hp = hit_die # Max HP from hit die
        character.hp_last_roll = rolled_hp # Store the rolled HP before modifiers
        starting_hp = rolled_hp + character.hp_mod # Max HP at level 1
        character.hp_all_rolls[character.level] = starting_hp # Store all rolls
        starting_hp = max(1, starting_hp)  # Ensure at least 1 HP
        character.hp = starting_hp # Set max HP
        character.hp_current = starting_hp # Set current HP to max HP
        character.player_state = "Healthy"
        print(f"DEBUG set_starting_hp: Setting current HP to max HP: {character.hp}")
        starting_hp = character.hp
    else:
        print("DEBUG set_starting_hp: Rolling starting HP.")
        hit_die = character.hp_dice
        rolled_hp = random.randint(1, hit_die) # Roll the hit die
        character.hp_last_roll = rolled_hp # Store the rolled HP before modifiers
        starting_hp = rolled_hp + character.hp_mod # Add constitution modifier
        character.hp_all_rolls[character.level] = starting_hp # Store all rolls
        starting_hp = max(1, starting_hp)  # Ensure at least 1 HP
        character.hp = starting_hp # Set max HP
        character.hp_current = starting_hp # Set current HP to max HP
        character.player_state = "Healthy"
        print(f"DEBUG set_starting_hp: Rolled starting HP: {starting_hp} (Hit Die: d{hit_die}, Rolled: {rolled_hp}, CON Mod: {character.hp_mod})")

    # Update status and disable roll HP button
    app.status_var.set(f"Starting HP set to {starting_hp}")

    # Set roll options back to normal/disabled state
    app.btn_rollhp.config(state="disabled") # Disable the button
    app.chk_opt_fullhplvl1.config(state="disabled") # Disable the checkbox
    app.stats_frame.config(style="Standard.TFrame") # Reset stats frame style in case it was highlighted before

    # Manage Apply button state
    if app.race_var.get() != "Undefined" and app.profession_var.get() != "Undefined" and app.alignment_var.get() != "Undefined":
        app.btn_apply.config(style="Attention.TButton") # Highlight apply changes button
        app.footer_frame.config(style="Attention.TFrame") # Highlight footer frame
    
    # Update the UI to reflect the new HP values
    update_view_from_model(app)
    return starting_hp

def recalculate_hp(character: PlayerClass):
    """Recalculate max HP based on level and constitution modifier."""
    print("DEBUG recalculate_hp: ----------------------------------------------------------------")
    print("DEBUG recalculate_hp: Recalculating HP for character at level", character.level)
    character.hp = character.hp_last_roll + character.hp_mod # Recalculate max HP
    character.hp = max(1, character.hp)  # Ensure at least 1 HP
    character.hp_current = character.hp # Set current HP to max HP
  
def reenable_hp_roll_button(app):
    """Re-enable the HP roll button for level up."""
    print("DEBUG reenable_hp_roll_button: ----------------------------------------------------------------")
    print("DEBUG reenable_hp_roll_button: Re-enabling HP roll button for level up.")
    app.chk_opt_fullhplvl1.config(state="disabled")
    app.btn_rollhp.config(state="enabled")
    app.btn_rollhp.config(text="Roll HP")
    app.btn_rollhp.config(style="Attention.TButton")
    app.btn_rollhp.config(command=lambda: role_tp_for_level_up(app))

def role_tp_for_level_up(app, character=None):
    """Placeholder function for role TP allocation on level up."""
    print("DEBUG role_tp_for_level_up: ----------------------------------------------------------------")
    
    # Determine the character to use
    if hasattr(app, "new_player"):
        #print("DEBUG role_tp_for_level_up: Using app.new_player.")
        character = app.new_player
    elif character is not None:
        print("DEBUG role_tp_for_level_up: Using provided character.")
    else:
        raise ValueError("ERROR role_tp_for_level_up: No character provided for TP allocation.")

    # Roll HP for level up
    hit_die = character.hp_dice
    rolled_hp = random.randint(1, hit_die) # Roll the hit die
    character.hp_last_roll = rolled_hp # Store the rolled HP before modifiers
    starting_hp = rolled_hp + character.hp_mod # Add constitution modifier
    print(f"DEBUG role_tp_for_level_up: Total HP increase after CON mod: {starting_hp} (Rolled: {rolled_hp}, Hit die: d{hit_die}, CON Mod: {character.hp_mod})")
    character.hp_all_rolls[character.level] = starting_hp # Store all rolls
    starting_hp = max(1, starting_hp)  # Ensure at least 1 HP
    character.hp += starting_hp # Increase max HP
    print(f"DEBUG role_tp_for_level_up: New max HP after level up: {character.hp}")
    character.hp_current += starting_hp # Increase current HP
    print(f"DEBUG role_tp_for_level_up: New current HP after level up: {character.hp_current}")
    
    # Disable HP roll button after level up
    app.btn_rollhp.config(state="disabled")
    app.btn_rollhp.config(style="Standard.TButton")

    # Update the UI to reflect the new HP values
    update_view_from_model(app)


def remove_tp_on_level_down(app, character=None):
    """Placeholder function for removing role TP on level down."""
    print("DEBUG remove_tp_on_level_down: ----------------------------------------------------------------")

    # Determine the character to use
    if hasattr(app, "new_player"):
        #print("DEBUG role_tp_for_level_up: Using app.new_player.")
        character = app.new_player
    elif character is not None:
        print("DEBUG role_tp_for_level_up: Using provided character.")
    else:
        raise ValueError("ERROR role_tp_for_level_up: No character provided for TP allocation.")

    # Remove HP gained from last level
    last_level_tp = character.hp_all_rolls.get(character.level + 1, 0) # Get HP gained at last level
    print(f"DEBUG remove_tp_on_level_down: Removing TP from last level: {last_level_tp}")
    character.hp -= last_level_tp # Decrease max HP
    print(f"DEBUG remove_tp_on_level_down: New max HP after level down: {character.hp}") # Decrease current HP accordingly
    character.hp_current -= last_level_tp
    print(f"DEBUG remove_tp_on_level_down: New current HP after level down: {character.hp_current}")
    character.hp_all_rolls.pop(character.level + 1, None) # Remove last level's HP roll record
    print(f"DEBUG remove_tp_on_level_down: Removed HP roll record for level {character.level + 1}")

    update_view_from_model(app)
