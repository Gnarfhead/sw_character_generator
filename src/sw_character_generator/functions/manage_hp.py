"""Functions to modify character HP and state based on changes."""
import random
from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.gui import app
from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model


def modify_hp(delta: int, app, character=None):
    """Adjust current HP by delta; clamp; set state."""

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

def set_roll_hp_button(app, chk_starting_hp):
    """Set the roll HP button text based on checkbox state."""
    print("DEBUG set_roll_hp_button: Called with chk_starting_hp =", chk_starting_hp.get())
    if app.chk_opt_fullhplvl1_var.get() is True:
        print("DEBUG set_roll_hp_button: Setting roll HP button to 'Set HP'")
        app.btn_rollhp.config(text="Set HP")
    else:
        print("DEBUG set_roll_hp_button: Setting roll HP button to 'Roll HP'")
        app.btn_rollhp.config(text="Roll HP")

def set_starting_hp(app, character:PlayerClass):
    """Roll/set starting HP for the character."""
    if app.chk_opt_fullhplvl1_var.get() is True:
        hit_die = character.hp_dice # Use max HP from hit die
        rolled_hp = hit_die # Max HP from hit die
        character.hp_last_roll = rolled_hp # Store the rolled HP before modifiers
        starting_hp = rolled_hp + character.hp_mod # Max HP at level 1
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
        starting_hp = max(1, starting_hp)  # Ensure at least 1 HP
        character.hp = starting_hp # Set max HP
        character.hp_current = starting_hp # Set current HP to max HP
        character.player_state = "Healthy"
        print(f"DEBUG set_starting_hp: Rolled starting HP: {starting_hp} (Hit Die: d{hit_die}, Rolled: {rolled_hp}, CON Mod: {character.hp_mod})")

    app.status_var.set(f"Starting HP set to {starting_hp}")
    app.btn_rollhp.config(state="disabled")
    app.chk_opt_fullhplvl1.config(state="disabled")
    app.stats_frame.config(style="Standard.TFrame") # Reset stats frame style in case it was highlighted before
    update_view_from_model(app)
    return starting_hp

def recalculate_hp(character: PlayerClass):
    """Recalculate max HP based on level and constitution modifier."""
    character.hp = character.hp_last_roll + character.hp_mod # Recalculate max HP
    character.hp = max(1, character.hp)  # Ensure at least 1 HP
    character.hp_current = character.hp # Set current HP to max HP
    #update_view_from_model(app)

    

