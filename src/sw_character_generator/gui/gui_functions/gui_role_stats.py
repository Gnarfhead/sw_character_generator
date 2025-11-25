""""Module for rolling and assigning role stats to a character."""
import tkinter as tk
from tkinter import ttk
from src.sw_character_generator.functions.gen_char_stat_mods import analyze_mod_char, analyze_mod_con, analyze_mod_dex, analyze_mod_int, analyze_mod_str, analyze_mod_wis
from src.sw_character_generator.functions.role_dice import wuerfle_3d6
#from src.sw_character_generator.gui import app
from src.sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model
from sw_character_generator.functions.manage_xp import calculate_xp_bonus
from sw_character_generator.functions.manage_hp import recalculate_hp
#from sw_character_generator.gui import app


def switch_stats(parent: tk.Tk, character, btn_switch_stats=None) -> str | None:
    """
    Open a modal Toplevel that returns a value to the caller.
    We set an attribute on the child window and read it after wait_window.
    """
    print("DEBUG switch_stats: type(parent) =", {type(parent)})

    win = tk.Toplevel(parent)  # Use parent as the modal window
    win.title("Return value") # Set the title of the window
    win.transient(parent) # Set to be on top of the main window
    win.grab_set() # Make modal

    # Variables for checkbuttons
    str_var = tk.BooleanVar()
    dex_var = tk.BooleanVar()
    con_var = tk.BooleanVar()
    int_var = tk.BooleanVar()
    wis_var = tk.BooleanVar()
    char_var = tk.BooleanVar()

    # Checkbuttons for stat selection
    tk.Label(win, text="Choose 2 stats:").grid(row=0, column=0, columnspan=2, pady=(10, 5))
    chkbox_stat_str = ttk.Checkbutton(win, text="Strength", variable=str_var)
    chkbox_stat_str.grid(row=1, column=0, sticky="w", padx=20, pady=5)
    chkbox_stat_dex = ttk.Checkbutton(win, text="Dexterity", variable=dex_var)
    chkbox_stat_dex.grid(row=1, column=1, sticky="w", padx=20, pady=5)
    chkbox_stat_con = ttk.Checkbutton(win, text="Constitution", variable=con_var)
    chkbox_stat_con.grid(row=2, column=0, sticky="w", padx=20, pady=5)
    chkbox_stat_int = ttk.Checkbutton(win, text="Intelligence", variable=int_var)
    chkbox_stat_int.grid(row=2, column=1, sticky="w", padx=20, pady=5)
    chkbox_stat_wis = ttk.Checkbutton(win, text="Wisdom", variable=wis_var)
    chkbox_stat_wis.grid(row=3, column=0, sticky="w", padx=20, pady=5)
    chkbox_stat_char = ttk.Checkbutton(win, text="Charisma", variable=char_var)
    chkbox_stat_char.grid(row=3, column=1, sticky="w", padx=20, pady=5)
    
 

    # Internal function to switch stats
    def internal_switch_stats():
        """Switch the two selected stats in the character object."""
        #print("DEBUG internal_switch_stats: type(app_instance)", {type(app_instance)})
        #print("DEBUG internal_switch_stats: hasattr new_player =", {hasattr(app_instance, 'new_player')})

        selected_stats = []
        if str_var.get():
            selected_stats.append("Strength")
        if dex_var.get():
            selected_stats.append("Dexterity")
        if con_var.get():
            selected_stats.append("Constitution")
        if int_var.get():
            selected_stats.append("Intelligence")
        if wis_var.get():
            selected_stats.append("Wisdom")
        if char_var.get():
            selected_stats.append("Charisma")

        # Ensure exactly two stats are selected
        if len(selected_stats) != 2:
            tk.messagebox.showerror("Error", "Please select exactly 2 stats.")
            return
                    
        # Mapping von stat Namen zu character Attributen
        stat_mapping = {
            "Strength": "stat_str",
            "Dexterity": "stat_dex", 
            "Constitution": "stat_con",
            "Intelligence": "stat_int",
            "Wisdom": "stat_wis",
            "Charisma": "stat_char"
        }
            
        # Die beiden ausgewählten Stats tauschen
        stat1_attr = stat_mapping[selected_stats[0]]
        print("DEBUG gui_role_stats: stat1_attr =", stat1_attr)
        stat2_attr = stat_mapping[selected_stats[1]]
        print("DEBUG gui_role_stats: stat2_attr =", stat2_attr)
            
        # Werte zwischenspeichern und tauschen
        temp_value = getattr(character, stat1_attr)
        setattr(character, stat1_attr, getattr(character, stat2_attr))
        setattr(character, stat2_attr, temp_value)

        # Analyze stat modifiers and apply to character
        analyze_mod_str(character)
        analyze_mod_dex(character)
        analyze_mod_con(character)
        recalculate_hp(character)
        analyze_mod_wis(character)
        analyze_mod_int(character)
        analyze_mod_char(character)
        #calculate_xp_bonus(app=app, character=character)
        calculate_xp_bonus(character)

        # Update buttons if provided
        if btn_switch_stats is not None:
            print("DEBUG gui_role_stats: Button found, updating...")
            btn_switch_stats.config(text="Stats switched", state="disabled")

        # Set result and close window
        win.result = f"Switched stats: {selected_stats[0]} and {selected_stats[1]}"
        win.destroy()    


    # Switch button
    btn_switch = ttk.Button(win, text="Switch Stats", command=internal_switch_stats)
    btn_switch.grid(row=4, column=0, columnspan=1, pady=(10, 10))
    btn_exit = ttk.Button(win, text="Cancel", command=win.destroy)
    btn_exit.grid(row=4, column=1, columnspan=1, pady=(10, 10))

    # Wait for window to close
    win.focus_set()
    parent.wait_window(win)

    # Set result and close window
    #win.result = f"Switched stats: {selected_stats[0]} and {selected_stats[1]}"
    #swin.destroy()    

def role_stats(app, character, chk_opt_4d6dl_var, btn_roll_stats=None, btn_switch_stats=None):
    """Rolls and assigns role stats to the character based on the 4d6 drop lowest option."""
    print("DEBUG gui_role_stats: Rolling role stats...")
    print("DEBUG gui_role_stats: 4d6 drop lowest option is set to:", chk_opt_4d6dl_var)

    # Roll stats
    if chk_opt_4d6dl_var is True: # 4d6 drop lowest
        print("DEBUG gui_role_stats: Rolling stats using 4d6 drop lowest method.")
        character.stat_str = wuerfle_3d6("strength", drop_low=True)
        character.stat_dex = wuerfle_3d6("dexterity", drop_low=True)
        character.stat_con = wuerfle_3d6("constitution", drop_low=True)
        character.stat_int = wuerfle_3d6("intelligence", drop_low=True)
        character.stat_wis = wuerfle_3d6("wisdom", drop_low=True)
        character.stat_char = wuerfle_3d6("charisma", drop_low=True)
    else: # Standard 3d6
        print("DEBUG gui_role_stats: Rolling stats using standard 3d6 method.")
        character.stat_str = wuerfle_3d6("strength", drop_low=False)
        character.stat_dex = wuerfle_3d6("dexterity", drop_low=False)
        character.stat_con = wuerfle_3d6("constitution", drop_low=False)
        character.stat_int = wuerfle_3d6("intelligence", drop_low=False)
        character.stat_wis = wuerfle_3d6("wisdom", drop_low=False)
        character.stat_char = wuerfle_3d6("charisma", drop_low=False)

    # Update buttons if provided
    if btn_roll_stats is not None: # Update roll stats button
        print("DEBUG gui_role_stats: Button found, updating...")
        btn_roll_stats.config(text="Stats Rolled", state="disabled") # Disable roll button after rolling
        app.chk_opt_4d6dl.config(state="disabled") # Disable 4d6 drop lowest option
        btn_switch_stats.config(state="normal") # Enable switch stats button
        app.cb_profession.config(state="normal") # Enable profession combobox
        app.top_frame.config(style="Attention.TFrame") # Highlight top frame to indicate next step
        app.lbl_profession.config(style="Attention.TLabel") # Highlight profession label
        app.attr_frame.config(style="Standard.TFrame") # Reset attribute frame style in case it was highlighted before
        

    # Starting coins: roll 3d6 and multiply by 10
    print("DEBUG gui_role_stats: Rolling starting coins (3d6 * 10):")
    character.coins = wuerfle_3d6(str_desc="Starting Coins") * 10
    print("DEBUG gui_role_stats: Starting coins rolled:", character.coins)

    # Analyze stat modifiers and apply to character
    print("DEBUG gui_role_stats: Analyzing stat modifiers and applying to character...")
    analyze_mod_str(character) # Apply strength modifier
    analyze_mod_dex(character) # Apply dexterity modifier
    analyze_mod_con(character) # Apply constitution modifier
    analyze_mod_int(character) # Apply intelligence modifier
    analyze_mod_wis(character) # Apply wisdom modifier
    analyze_mod_char(character) # Apply charisma modifier
    calculate_xp_bonus(character)

    # Update status and GUI
    print("DEBUG gui_role_Stats: Set Frame styles and status message...")
    app.status_var.set("Stats and start coins rolled.")

    # Update the GUI from the model
    update_view_from_model(app)

  

