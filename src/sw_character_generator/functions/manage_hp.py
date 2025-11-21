"""Functions to modify character HP and state based on changes."""
import random
from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.gui import app
from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model


def modify_hp(delta: int, character: PlayerClass):
    """Adjust current HP by delta; clamp; set state."""
    current = character.hp_current
    maximum = character.hp_max
    new_value = max(0, min(current + delta, maximum))
    character.hp_current = new_value
    if new_value <= 0:
        character.state = "Dead"
    elif new_value <= maximum * 0.25:
        character.state = "Critical"
    elif new_value <= maximum * 0.5:
        character.state = "Injured"
    elif new_value <= maximum * 0.75:
        character.state = "Wounded"
    else:
        character.state = "Healthy"

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
        print(f"DEBUG set_starting_hp: Rolled starting HP: {starting_hp} (Hit Die: d{hit_die}, CON Mod: {character.hp_mod})")

    app.status_var.set(f"Starting HP set to {starting_hp}")
    update_view_from_model(app)
    app.btn_rollhp.config(state="disabled")
    #app.chk_opt_fullhplvl1_var.config(state="disabled")
    return starting_hp

def recalculate_hp(character: PlayerClass):
    """Recalculate max HP based on level and constitution modifier."""
    character.hp = character.hp_last_roll + character.hp_mod # Recalculate max HP
    character.hp = max(1, character.hp)  # Ensure at least 1 HP
    character.hp_current = character.hp # Set current HP to max HP
    #update_view_from_model(app)

    

