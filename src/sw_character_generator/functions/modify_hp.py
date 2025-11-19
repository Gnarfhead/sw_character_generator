def modify_hp(delta: int, hp_current_var, hp_max_var, state_var):
    """Adjust current HP by delta; clamp; set state."""
    current = hp_current_var.get()
    maximum = hp_max_var.get()
    new_value = max(0, min(current + delta, maximum))
    hp_current_var.set(new_value)
    if new_value <= 0:
        state_var.set("Dead")
    elif new_value <= maximum * 0.25:
        state_var.set("Critical")
    else:
        state_var.set("Healthy")