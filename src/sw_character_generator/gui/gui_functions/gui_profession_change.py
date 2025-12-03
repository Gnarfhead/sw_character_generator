"""Callback when profession_var changes; update model profession accordingly."""

from sw_character_generator.functions.choosen_profession import choosen_profession_modifiers
from sw_character_generator.functions.manage_magic import manage_magic_tab
from sw_character_generator.functions.manage_saving_throw import calculate_saving_throw
from sw_character_generator.functions.manage_thief_skills import calculate_thief_skills, manage_thief_tab
from sw_character_generator.functions.manage_xp import calculate_next_level_xp, calculate_xp_bonus
from sw_character_generator.functions.update_derived_stats import update_derived_stats
from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model

def on_profession_change(app, *args):
    """Handle profession combobox changes."""
    print("DEBUG on_profession_change: ------------------------------------------------")
    if getattr(app, "is_updating", False):
        print("DEBUG on_profession_change: Profession change ignored due to is_updating flag.")
        return
    name = app.profession_var.get() # get selected profession name
    if not name: # no profession selected
        print("DEBUG on_profession_change: No profession selected.")
        return
    try:
        # Clear profession-related attributes before applying new profession
        for attr in ("immunities_profession", "special_abilities_profession", "save_bonuses_profession",
                     "immunities_other", "special_abilities_other", "save_bonuses_other"):
            existing = getattr(app.new_player, attr, None) # get existing attribute
            # print(f"DEBUG on_profession_change: Clearing attribute {attr}, existing value: {existing}")
            if isinstance(existing, set): # clear set attributes
                existing.clear() # clear existing set
            else:
                setattr(app.new_player, attr, set()) # reset to empty set

        # Update the model with the new profession
        print("DEBUG on_profession_change: Changing profession to", name)
        choosen_profession_modifiers(app.new_player, name) # update profession and related stats
        app.status_var.set(f"Profession changed to {name}")
        app.cb_race.config(state="normal") # enable race selection
        app.cb_alignment.config(state="normal") # enable alignment selection

        # Reset dependent selections and stats
        app.race_var.set("Undefined") # reset if profession gets changed
        app.alignment_var.set("Undefined") # reset if profession gets changed

        # Highlight profession label and reset others
        app.lbl_profession.config(style="Standard.TLabel")
        app.lbl_race.config(style="Attention.TLabel")
        app.lbl_alignment.config(style="Attention.TLabel")
        app.stats_frame.config(style="Attention.TFrame")

        # Enable add XP button and highlight stats frame
        app.btn_add_xp.config(state="normal")
        calculate_xp_bonus(app.new_player) # recalculate XP bonus
        calculate_next_level_xp(app, app.new_player) # recalculate next level XP
        calculate_saving_throw(app.new_player) # recalculate saving throws

        # Recalculate ability score bonuses
        update_derived_stats(app.new_player, app)  # recalculate derived stats

        # Reset thief and magic tab values
        manage_thief_tab(app.new_player, app)  # recalculate thief class status
        calculate_thief_skills(app.new_player) # recalculate thief skills
        manage_magic_tab(app.new_player, app)  # recalculate magic class status

        # Refresh race and alignment values
        refresh_race_values(app) # update race combobox values
        refresh_alignment_values(app) # update alignment combobox values

        # Enable roll HP button if all selections are valid
        app.new_player.hp = 0 # reset HP values
        app.new_player.hp_current = 0 # reset current HP
        app.new_player.hp_last_roll = 0 # reset last rolled HP
        app.btn_modify_hp.config(state="normal")
        if app.race_var.get() != "Undefined" and app.profession_var.get() != "Undefined" and app.alignment_var.get() != "Undefined":
            app.btn_rollhp.config(state="normal")
            app.btn_rollhp.config(style="Attention.TButton")
            app.stats_frame.config(style="Attention.TFrame")

        # Refresh the GUI to reflect model changes
        with app.suppress_updates(): # prevent recursive updates
            update_view_from_model(app) # refresh GUI to reflect model changes
    except Exception as e:
        print(f"DEBUG on_profession_change: Profession change error: {e}")

def refresh_race_values(app):
    """Refresh the race combobox values based on the new player's allowed races."""
    print("DEBUG refresh_race_values: ------------------------------------------------")
    app.cb_race.config(values=list(getattr(app.new_player, "allowed_races", ())))
    # print("DEBUG refresh_race_values: Updated race combobox values to", {app.cb_race['values']})

def refresh_alignment_values(app):
    """Refresh the alignment combobox values based on the new player's allowed alignments."""
    print("DEBUG refresh_alignment_values: ------------------------------------------------")
    app.cb_alignment.config(values=list(getattr(app.new_player, "allowed_alignment", ())))
    # print("DEBUG refresh_alignment_values: Updated alignment combobox values to", {app.cb_alignment['values']})

