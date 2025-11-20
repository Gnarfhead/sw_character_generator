"""Functions to modify character HP and state based on changes."""
from sw_character_generator.classes.playerclass import PlayerClass


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

def roll_starting_hp(app, character: PlayerClass):
    """Roll starting HP using provided dice roll function."""
   