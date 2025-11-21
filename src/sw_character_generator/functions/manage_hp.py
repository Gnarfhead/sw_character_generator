"""Functions to modify character HP and state based on changes."""
from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.gui import app
from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model


def modify_hp(delta: int, character: PlayerClass):
    """Adjust current HP by delta; clamp; set state."""
    current = hp_current_var.get()
    maximum = hp_max_var.get()
    new_value = max(0, min(current + delta, maximum))
    hp_current_var.set(new_value)
    if new_value <= 0:
        state_var.set("Dead")
    elif new_value <= maximum * 0.25:
        state_var.set("Critical")
    elif new_value <= maximum * 0.5:
        state_var.set("Injured")
    elif new_value <= maximum * 0.75:
        state_var.set("Wounded")
    else:
        state_var.set("Healthy")

def set_roll_hp_button(app, chk_starting_hp, btn_rollhp=None):
    """Set the roll HP button text based on checkbox state."""
    print("DEBUG set_roll_hp_button: Called with chk_starting_hp =", chk_starting_hp.get())
    if app.chk_opt_fullhplvl1_var.get() is True:
        print("DEBUG set_roll_hp_button: Setting roll HP button to 'Set HP'")
        app.btn_rollhp.config(text="Set HP")
    else:
        print("DEBUG set_roll_hp_button: Setting roll HP button to 'Roll HP'")
        app.btn_rollhp.config(text="Roll HP")

def roll_starting_hp(app, character: PlayerClass, btn_rollhp):
    """Roll starting HP using provided dice roll function."""
    pass