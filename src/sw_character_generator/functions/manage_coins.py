"""Functions to manage player's coins."""

def modify_coins(app):
    """Modify the player's coins based on the GUI input."""
    print("DEBUG modify_coins: --------------------------------")

    if getattr(app, "is_updating", False):
        return

    # Get current coin values
    platinum = app.coins_platinum_var.get()
    gold = app.coins_gold_var.get()
    electrum = app.coins_electrum_var.get()
    silver = app.coins_silver_var.get()
    copper = app.coins_copper_var.get()

    # Get modification values
    platinum_mod = app.coins_platinum_mod_var.get()
    gold_mod = app.coins_gold_mod_var.get()
    electrum_mod = app.coins_electrum_mod_var.get()
    silver_mod = app.coins_silver_mod_var.get()
    copper_mod = app.coins_copper_mod_var.get()

    # Apply modifications
    platinum += platinum_mod
    gold += gold_mod
    electrum += electrum_mod
    silver += silver_mod
    copper += copper_mod

    # Ensure no negative coin values
    platinum = max(platinum, 0)
    gold = max(gold, 0)
    electrum = max(electrum, 0)
    silver = max(silver, 0)
    copper = max(copper, 0)

    # Update the player's coin values
    app.new_player.coins_platinum = platinum
    app.new_player.coins_gold = gold
    app.new_player.coins_electrum = electrum
    app.new_player.coins_silver = silver
    app.new_player.coins_copper = copper

    # Update the GUI variables to reflect changes
    app.coins_platinum_var.set(platinum)
    app.coins_gold_var.set(gold)
    app.coins_electrum_var.set(electrum)
    app.coins_silver_var.set(silver)
    app.coins_copper_var.set(copper)

    print(f"DEBUG modify_coins: Updated coins to: Platinum={platinum}, Gold={gold}, Electrum={electrum}, Silver={silver}, Copper={copper}")
    