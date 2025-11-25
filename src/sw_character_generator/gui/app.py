"""GUI application for the Swords & Wizardry character generator.

This file provides an App class that encapsulates the Tk GUI, previously implemented
as a collection of functions. The module still exposes start_gui() for backwards
compatibility (main.py imports start_gui).
"""
from contextlib import contextmanager
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox

from src.sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.functions.manage_hp import modify_hp, set_starting_hp, set_roll_hp_button
from src.sw_character_generator.functions.character_handling import save_character, load_character
from src.sw_character_generator.gui.gui_functions.gui_new_character import apply_character, new_characterobj
from sw_character_generator.functions.manage_xp import add_xp
from .gui_functions.gui_dice_roller import dice_roller
from .gui_functions.gui_alignment_change import on_alignment_change
from .gui_functions.gui_race_change import on_race_change
from .gui_functions.gui_role_stats import role_stats, switch_stats
from .gui_functions.gui_profession_change import on_profession_change
from .gui_functions.gui_update_view_from_model import update_view_from_model
from .gui_functions.gui_persistence import bind_model_vars
from .gui_functions.gui_widgets import widget_button, widget_extlabel, widget_label, widget_entry, widget_combobox, widget_spinbox, widget_checkbutton

# Layout / sizing constants
ROOT_MIN_W = 900
ROOT_MIN_H = 600
LABEL_MIN_W = 120
VALUE_MIN_W = 160
ENTRY_WIDTH = 20
PADX = 8
PADY = 6


class App:
    """Class-based GUI for the character generator."""

    #----------------- initialization -----------------

    def __init__(self):
        # Create root first, then StringVars etc.
        self._updating = False  # flag to prevent recursive updates
        self.root = tk.Tk()
        self.root.title("Swords & Wizardry Charaktergenerator")
        self.root.minsize(900, 600)

        # Global player character instance (to be used by save/load functions)
        self.new_player = PlayerClass()

        # Make root use grid for all direct children and allow columns to expand
        for c in range(3):
            self.root.grid_columnconfigure(c, weight=1, minsize=160)

        # GUI-bound variables (created after root exists)
        self.player_name_var = tk.StringVar(master=self.root)
        self.character_name_var = tk.StringVar(master=self.root)
        self.level_var = tk.IntVar(master=self.root, value=1)
        self.profession_var = tk.StringVar(master=self.root)
        self.profession_var.trace_add("write", lambda *args: on_profession_change(self))
        self.race_var = tk.StringVar(master=self.root)
        self.race_var.trace_add("write", lambda *args: on_race_change(self, *args))
        self.gender_var = tk.StringVar(master=self.root)
        self.alignment_var = tk.StringVar(master=self.root)
        self.alignment_var.trace_add("write", lambda *args: on_alignment_change(self, *args))
        self.god_var = tk.StringVar(master=self.root)
        self.age_var = tk.IntVar(master=self.root, value=0)
        self.xp_bonus_var = tk.IntVar(master=self.root, value=0)
        self.xp_var = tk.IntVar(master=self.root, value=0)
        self.main_stats_var = tk.StringVar(master=self.root)
        self.status_var = tk.StringVar(master=self.root, value="Ready")
        self.stat_str_var = tk.IntVar(master=self.root, value=0)
        self.stat_dex_var = tk.IntVar(master=self.root, value=0)
        self.stat_con_var = tk.IntVar(master=self.root, value=0)
        self.stat_int_var = tk.IntVar(master=self.root, value=0)
        self.stat_wis_var = tk.IntVar(master=self.root, value=0)
        self.stat_char_var = tk.IntVar(master=self.root, value=0)
        self.coins_var = tk.IntVar(master=self.root, value=0)
        self.delicate_tasks_var = tk.IntVar(master=self.root, value=0)
        self.climb_walls_var = tk.IntVar(master=self.root, value=0)
        self.hear_sounds_var = tk.IntVar(master=self.root, value=0)
        self.hide_in_shadows_var = tk.IntVar(master=self.root, value=0)
        self.move_silently_var = tk.IntVar(master=self.root, value=0)
        self.open_locks_var = tk.IntVar(master=self.root, value=0)
        self.player_state_var = tk.StringVar(master=self.root, value="Normal")
        self.hp_var = tk.IntVar(master=self.root, value=0)
        self.hp_current_var = tk.IntVar(master=self.root, value=0)
        self.hp_last_roll_var = tk.IntVar(master=self.root, value=0)
        self.hp_modify_var = tk.IntVar(master=self.root, value=0)
        self.save_throw_var = tk.IntVar(master=self.root, value=0)
        self.ac_var = tk.IntVar(master=self.root, value=0)
        self.darkvision_var = tk.StringVar(master=self.root, value="No")
        self.parry_var = tk.IntVar(master=self.root, value=0)
        self.languages_var = tk.StringVar(master=self.root, value="")
        self.special_abilities_var = tk.StringVar(master=self.root, value="")
        self.immunities_var = tk.StringVar(master=self.root, value="")
        self.strength_atck_mod_var = tk.DoubleVar(master=self.root, value=0.0)
        self.strength_damage_mod_var = tk.DoubleVar(master=self.root, value=0.0)
        self.carry_capacity_mod_var = tk.DoubleVar(master=self.root, value=0.0)
        self.door_crack_mod_var = tk.DoubleVar(master=self.root, value=0.0)
        self.ranged_atck_mod_var = tk.IntVar(master=self.root, value=0)
        self.ac_mod_var = tk.IntVar(master=self.root, value=0)
        self.hp_mod_var = tk.IntVar(master=self.root, value=0)
        self.raise_dead_mod_var = tk.IntVar(master=self.root, value=0)
        self.max_add_langs_var = tk.IntVar(master=self.root, value=0)
        self.cap_spec_hirelings_var = tk.IntVar(master=self.root, value=0)
        self.chk_opt_4d6dl_var = tk.BooleanVar(master=self.root, value=False)
        self.chk_opt_fullhplvl1_var = tk.BooleanVar(master=self.root, value=False)
        self.chk_opt_fullhplvl1_var.trace_add("write", lambda *args: set_roll_hp_button(self, self.chk_opt_fullhplvl1_var))
        self.add_xp_var = tk.IntVar(master=self.root, value=0)
        self.nextlevel_var = tk.IntVar(master=self.root, value=0)

    # ----------------- setup UI -----------------

        style = ttk.Style()
        # Optional: choose a different theme (some themes allow better color control)
        # available themes: style.theme_names()
        style.theme_use("clam")

        # Buttons with different styles
        style.configure("Standard.TButton",
                background="#e2e3e5",
                foreground="black",
                font=("Helvetica", 10, "bold"),
                padding=8)
        style.map("Standard.TButton",
                background=[("active", "#bebfc2"), ("pressed", "#e2e3e5"), ("disabled", "#e2e3e5")],)
                #foreground=[("disabled", "#d9d9d9")])

        style.configure("Attention.TButton",
                        background="#dc3545",
                        foreground="white",
                        font=("Helvetica", 10, "bold"),
                        padding=8)
        style.map("Attention.TButton",
                background=[("active", "#c82333"), ("pressed", "#e2e3e5"), ("disabled", "#e2e3e5")],)
        
        # Labels with different styles
        style.configure("Standard.TLabel",
                        foreground="#000000")
        style.configure("Warning.TLabel",
                        foreground="#FA9702E4")
        style.configure("Attention.TLabel",
                        foreground="#c82333")
        
        # Frames with different styles
        style.configure("Standard.TFrame",
                        borderwidth=2,
                        relief="ridge",
                        padding=(6, 6),
                        bordercolor="#000000")

        style.configure("Attention.TFrame",
                        borderwidth=25,
                        relief="ridge",
                        padding=(6, 6),
                        bordercolor="#c82333")

    # ----------------- build UI -----------------
        # Build UI
        self._build_ui()

        # Bind GUI variables/widgets back to model
        bind_model_vars(self)

        # Populate the view initially from the model
        update_view_from_model(self)
    # ----------------- UI building -----------------

    def _build_ui(self):

        # Create top frame and place it with grid (do not mix pack/grid on root)
        self.top_frame = ttk.Frame(self.root, borderwidth=5, relief="ridge", padding=(6, 6), style="Standard.TFrame")
        self.top_frame.grid(row=0, column=0, columnspan=3, padx=PADX, pady=PADY, sticky="ew")
    
        # Row 0: basic fields
        widget_entry(self.top_frame, "Player Name:", 0, 0, var=self.player_name_var, owner=self, name_label="lbl_player_name", name_entry="entry_player_name")
        widget_entry(self.top_frame, "Character Name:", 0, 2, var=self.character_name_var, owner=self, name_label="lbl_character_name", name_entry="entry_character_name")
        widget_combobox(self.top_frame, "Gender:", 0, 4, self.gender_var, ["Male", "Female", "Other"], state="active", owner=self, name_label="lbl_gender", name_combo="cb_gender")
        widget_extlabel(self.top_frame, "Level:", 0, 6, var=self.level_var, owner=self, name_label="lbl_level", name_value="entry_level")
        widget_extlabel(self.top_frame, "XP-Bonus (%):", 0, 8, var=self.xp_bonus_var, owner=self, name_label="lbl_xp_bonus", name_value="entry_xp_bonus")

        # Row 1
        widget_combobox(self.top_frame, "Profession:", 1, 0, self.profession_var, ["Fighter", "Cleric", "Thief", "Wizard", "Ranger", "Paladin", "Druid", "Assassin", "Monk"], state="disabled", owner=self, name_label="lbl_profession", name_combo="cb_profession")
        widget_combobox(self.top_frame, "Race:", 1, 2, self.race_var, list(getattr(self.new_player, "allowed_races", ())), state="disabled", owner=self, name_label="lbl_race", name_combo="cb_race")
        widget_combobox(self.top_frame, "Alignment:", 1, 4, self.alignment_var, ["Good", "Neutral", "Evil"], state="disabled", owner=self, name_label="lbl_alignment", name_combo="cb_alignment")
        widget_extlabel(self.top_frame, "XP:", 1, 6, var=self.xp_var, owner=self, name_label="lbl_xp", name_value="entry_xp")
        widget_extlabel(self.top_frame, "Next Level (XP):", 1, 8, var=self.nextlevel_var, owner=self, name_label="lbl_nextlevel", name_value="entry_nextlevel")
        
   
        # Row 2
        widget_extlabel(self.top_frame, "Main Stats:", 2, 0, var=self.main_stats_var, owner=self, name_label="lbl_main_stats", name_value="entry_main_stats")
        widget_entry(self.top_frame, "Gottheit:", 2, 2, var=self.god_var, owner=self, name_label="lbl_god", name_entry="entry_god")
        widget_entry(self.top_frame, "Alter:", 2, 4, var=self.age_var, owner=self, name_label="lbl_age", name_entry="entry_age")
        widget_spinbox(self.top_frame, "Add XP:", 2, 6, var=self.add_xp_var, owner=self, name_label="lbl_add_xp", name_spinbox="spin_add_xp")
        widget_button(self.top_frame, "Add XP", 2, 7, command=lambda: add_xp(self, self.add_xp_var.get()), owner=self, name_button="btn_add_xp", state="disabled")
 
        # Attribute frame (use LabelFrame for nicer title)
        self.attr_frame = ttk.LabelFrame(self.root, text="Attribute", borderwidth=5, padding=(6, 6), style="Attention.TFrame")
        self.attr_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        widget_extlabel(self.attr_frame, "Strength (STR):", 0, 0, var=self.stat_str_var, owner=self, name_label="lbl_str", name_value="entry_str")
        widget_extlabel(self.attr_frame, "Dexterity (DEX):", 1, 0, var=self.stat_dex_var, owner=self, name_label="lbl_dex", name_value="entry_dex")
        widget_extlabel(self.attr_frame, "Constitution (CON):", 2, 0, var=self.stat_con_var, owner=self, name_label="lbl_con", name_value="entry_con")
        widget_extlabel(self.attr_frame, "Intelligence (INT):", 3, 0, var=self.stat_int_var, owner=self, name_label="lbl_int", name_value="entry_int")
        widget_extlabel(self.attr_frame, "Wisdom (WIS):", 4, 0, var=self.stat_wis_var, owner=self, name_label="lbl_wis", name_value="entry_wis")
        widget_extlabel(self.attr_frame, "Charisma (CHA):", 5, 0, var=self.stat_char_var, owner=self, name_label="lbl_cha", name_value="entry_cha")

        # place Roll Stats button inside attr_frame
        self.btn_roll_stats = ttk.Button(self.attr_frame, text="Roll Stats", style="Attention.TButton", command=lambda: role_stats(self, self.new_player, self.chk_opt_4d6dl_var.get(), self.btn_roll_stats, self.btn_switch_stats))
        self.btn_roll_stats.grid(row=6, column=0, sticky="ew", padx=PADX, pady=PADY)

        # Homebrew frame (use LabelFrame for nicer title)
        self.attr_homebrew_frame = ttk.LabelFrame(self.attr_frame, text="Homebrew", borderwidth=5, padding=(6, 6), style="Standard.TFrame")
        self.attr_homebrew_frame.grid(row=7, column=0, padx=PADX, pady=PADY, sticky="nsew")

        # Switch Stats button inside homebrew frame
        def homebrew_switch_stats(self, character, btn_switch_stats):
            switch_stats(self.root, character, btn_switch_stats) #
            self.status_var.set("Stats switched.")
            update_view_from_model(self)

        # Switch Stats button
        self.btn_switch_stats = ttk.Button(self.attr_homebrew_frame, text="Switch Stats", style="Standard.TButton", command=lambda: homebrew_switch_stats(self, self.new_player, self.btn_switch_stats))
        self.btn_switch_stats.config(state="disabled")  # Disabled for now
        self.btn_switch_stats.grid(row=0, column=1, sticky="ew", padx=PADX, pady=PADY)
        self.chk_opt_4d6dl = ttk.Checkbutton(self.attr_homebrew_frame, text="4d6 dl", variable=self.chk_opt_4d6dl_var)
        self.chk_opt_4d6dl.grid(row=0, column=0, sticky="ew", padx=PADX, pady=PADY)

        # Bonuses frame
        self.bonus_frame = ttk.LabelFrame(self.root, text="Attribute Bonuses", borderwidth=5, padding=(6, 6), style="Standard.TFrame")
        self.bonus_frame.grid(row=1, column=1, padx=PADX, pady=PADY, sticky="nsew")

        # Create bonus labels and values
        widget_extlabel(self.bonus_frame, "Melee Attack Bonus:", 0, 0, var=self.strength_atck_mod_var, owner=self, name_label="lbl_strength_atck_bonus", name_value="entry_strength_atck_bonus")
        widget_extlabel(self.bonus_frame, "Melee Damage Bonus:", 1, 0, var=self.strength_damage_mod_var, owner=self, name_label="lbl_strength_damage_bonus", name_value="entry_strength_damage_bonus")
        widget_extlabel(self.bonus_frame, "Carry Capacity Bonus:", 2, 0, var=self.carry_capacity_mod_var, owner=self, name_label="lbl_carry_capacity_bonus", name_value="entry_carry_capacity_bonus")
        widget_extlabel(self.bonus_frame, "Door Crack Bonus:", 3, 0, var=self.door_crack_mod_var, owner=self, name_label="lbl_door_crack_bonus", name_value="entry_door_crack_bonus")
        widget_extlabel(self.bonus_frame, "Ranged Attack Bonus:", 4, 0, var=self.ranged_atck_mod_var, owner=self, name_label="lbl_ranged_atk_bonus", name_value="entry_ranged_atk_bonus")
        widget_extlabel(self.bonus_frame, "AC Bonus:", 5, 0, var=self.ac_mod_var, owner=self, name_label="lbl_ac_bonus", name_value="entry_ac_bonus")
        widget_extlabel(self.bonus_frame, "HP Bonus:", 6, 0, var=self.hp_mod_var, owner=self, name_label="lbl_hp_bonus", name_value="entry_hp_bonus")
        widget_extlabel(self.bonus_frame, "Raise Dead Modifier:", 7, 0, var=self.raise_dead_mod_var, owner=self, name_label="lbl_raise_dead_mod", name_value="entry_raise_dead_mod")
        widget_extlabel(self.bonus_frame, "Max Additional Languages:", 8, 0, var=self.max_add_langs_var, owner=self, name_label="lbl_max_add_langs", name_value="entry_max_add_langs")
        widget_extlabel(self.bonus_frame, "Special Hirelings Cap:", 9, 0, var=self.cap_spec_hirelings_var, owner=self, name_label="lbl_cap_spec_hirelings", name_value="entry_cap_spec_hirelings")
        
        # Stats / Other panels
        self.stats_frame = ttk.LabelFrame(self.root, text="Stats / Derived", borderwidth=5, padding=(6, 6), style="Standard.TFrame")
        self.stats_frame.grid(row=1, column=2, padx=PADX, pady=PADY, sticky="nsew")

        # Create stat labels and values
        widget_extlabel(self.stats_frame, "Hit Points max.:", 0, 0, var=self.hp_var, owner=self, name_label="lbl_hp", name_value="entry_hp")
        widget_checkbutton(self.stats_frame, "Full TP on Level 1", 0, 2, self.chk_opt_fullhplvl1_var, owner=self, name_checkbutton="chk_opt_fullhplvl1")
        widget_button(self.stats_frame, "Roll HP", 0, 4, command=lambda: set_starting_hp(self, self.new_player), state="disabled", owner=self, name_button="btn_rollhp")
        widget_extlabel(self.stats_frame, "Hit Points current:", 1, 0, var=self.hp_current_var, owner=self, name_label="lbl_hp_current", name_value="entry_hp_current")
        widget_spinbox(self.stats_frame, "Modify HP by:", 1, 2, var=self.hp_modify_var, owner=self, name_label="lbl_modify_hp", name_spinbox="spin_modify_hp")
        widget_button(self.stats_frame, "Modify HP", 1, 4, command=lambda: modify_hp(self.hp_modify_var.get(), self, self.new_player), state="disabled", owner=self, name_button="btn_modify_hp")
        widget_extlabel(self.stats_frame, "State:", 2, 0, var=self.player_state_var, owner=self, name_label="lbl_player_state", name_value="entry_player_state")
        widget_extlabel(self.stats_frame, "Saving Throw:", 3, 0, var=self.save_throw_var, owner=self, name_label="lbl_save_throw", name_value="entry_save_throw")
        widget_extlabel(self.stats_frame, "Armor Class (AC):", 4, 0, var=self.ac_var, owner=self, name_label="lbl_ac", name_value="entry_ac")
        widget_extlabel(self.stats_frame, "Darkvision:", 5, 0, var=self.darkvision_var, owner=self, name_label="lbl_darkvision", name_value="entry_darkvision")
        widget_extlabel(self.stats_frame, "Parry:", 6, 0, var=self.parry_var, owner=self, name_label="lbl_parry", name_value="entry_parry")
        widget_extlabel(self.stats_frame, "Languages:", 7, 0, var=self.languages_var, owner=self, name_label="lbl_add_langs", name_value="entry_add_langs")
        widget_extlabel(self.stats_frame, "Immunities:", 8, 0, var=self.immunities_var, owner=self, name_label="lbl_immunities", name_value="entry_immunities")
        widget_label(self.stats_frame, "Special Abilities:", 9, 0, owner=self, name_label="lbl_special_abilities")
        
        # Use scrolledtext for special abilities
        special_abilities_txt = scrolledtext.ScrolledText(
        self.stats_frame,
        wrap="word",
        height=5,        # visible row height (can be adjusted)
        width=40,        # visible column width (char-based)
        font=("TkDefaultFont", 10)
        )
        special_abilities_txt.grid(row=9, column=1, columnspan=4, sticky="nsew", padx=PADX, pady=PADY)


        # Thief skills panel
        self.thief_frame = ttk.LabelFrame(self.root, text="Thief Skills", borderwidth=5, padding=(6, 6), style="Standard.TFrame")
        self.thief_frame.grid(row=2, column=0, padx=PADX, pady=PADY, sticky="nsew")
  
        # Create thief skill labels and values
        widget_extlabel(self.thief_frame, "Delicate Tasks:", 0, 0, var=self.delicate_tasks_var, owner=self, name_label="lbl_delicate_tasks", name_value="entry_delicate_tasks")
        widget_extlabel(self.thief_frame, "Climb Walls:", 1, 0, var=self.climb_walls_var, owner=self, name_label="lbl_climb_walls", name_value="entry_climb_walls")
        widget_extlabel(self.thief_frame, "Hear Sounds:", 2, 0, var=self.hear_sounds_var, owner=self, name_label="lbl_hear_sounds", name_value="entry_hear_sounds")
        widget_extlabel(self.thief_frame, "Hide in Shadows:", 3, 0, var=self.hide_in_shadows_var, owner=self, name_label="lbl_hide_in_shadows", name_value="entry_hide_in_shadows")
        widget_extlabel(self.thief_frame, "Move Silently:", 4, 0, var=self.move_silently_var, owner=self, name_label="lbl_move_silently", name_value="entry_move_silently")
        widget_extlabel(self.thief_frame, "Open Locks:", 5, 0, var=self.open_locks_var, owner=self, name_label="lbl_open_locks", name_value="entry_open_locks") 

        # Weapons & Armor frame
        self.weapons_frame = ttk.LabelFrame(self.root, text="Weapons & Armor", borderwidth=5, padding=(6,6), style="Standard.TFrame")
        self.weapons_frame.grid(row=2, column=1, padx=PADX, pady=PADY, sticky="nsew")

        # Inventory frame
        self.inventory_frame = ttk.LabelFrame(self.root, text="Inventory", borderwidth=5, padding=(6,6), style="Standard.TFrame")
        self.inventory_frame.grid(row=2, column=2, padx=PADX, pady=PADY, sticky="nsew")

        ttk.Label(self.inventory_frame, text="Coins:").grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.inventory_frame, textvariable=self.coins_var).grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)


        ttk.Label(self.inventory_frame, text="Treasure:").grid(row=1, column=0, sticky="nw", padx=PADX, pady=PADY)
        # Use scrolledtext for treasure
        treasure_txt = scrolledtext.ScrolledText(
        self.inventory_frame,
        wrap="word",
        height=5,        # visible row height (can be adjusted)
        width=50,        # visible column width (char-based)
        font=("TkDefaultFont", 10)
        )
        treasure_txt.grid(row=1, column=1, sticky="nsew", padx=PADX, pady=PADY)


        ttk.Label(self.inventory_frame, text="Inventory:").grid(row=2, column=0, sticky="nw", padx=PADX, pady=PADY)
        # Use scrolledtext for inventory
        inventory_txt = scrolledtext.ScrolledText(
        self.inventory_frame,
        wrap="word",
        height=5,        # visible row height (can be adjusted)
        width=50,        # visible column width (char-based)
        font=("TkDefaultFont", 10)
        )
        inventory_txt.grid(row=2, column=1, sticky="nsew", padx=PADX, pady=PADY)

        # Footerframe (if needed in future)
        self.footer_frame = ttk.Frame(self.root, borderwidth=5, padding=(6,6), style="Standard.TFrame")
        self.footer_frame.grid(row=3, column=0, columnspan=3, padx=PADX, pady=PADY, sticky="ew")

        # place Save / Load buttons inside footer_frame on a new row so they're visually nearby
        self.btn_new = ttk.Button(self.footer_frame, text="New", command=lambda: new_characterobj(self))
        self.btn_new.grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        self.btn_apply = ttk.Button(self.footer_frame, text="Apply", command=lambda: apply_character(self, self.new_player))
        self.btn_apply.grid(row=0, column=1, sticky="e", padx=PADX, pady=PADY)
        self.btn_save = ttk.Button(self.footer_frame, text="Save", command=lambda: save_character(self.new_player))
        self.btn_save.grid(row=0, column=2, sticky="e", padx=PADX, pady=PADY)
        self.btn_load = ttk.Button(self.footer_frame, text="Load", command=lambda: load_character(self))
        self.btn_load.grid(row=0, column=3, sticky="w", padx=PADX, pady=PADY)
        self.btn_dice_roller = ttk.Button(self.footer_frame, text="Dice Roller", command=lambda: dice_roller(self))
        self.btn_dice_roller.grid(row=0, column=4, sticky="e", padx=PADX, pady=PADY)
        self.btn_exit = ttk.Button(self.footer_frame, text="Exit", command=lambda: messagebox.askokcancel("Exit", "Do you really want to exit?", parent=self.root) and self.root.destroy())
        self.btn_exit.grid(row=0, column=5, sticky="e", padx=PADX, pady=PADY)


        # Status bar at the very bottom
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief="sunken", anchor="w", padding=(4,4))
        self.status_bar.grid(row=4, column=0, columnspan=3, sticky="ew")

        # ----------------- configure resizing behavior -----------------

        # Make lower rows/frames expand when window is resized
        self.root.grid_rowconfigure(1, weight=1, minsize=200)
        self.root.grid_rowconfigure(2, weight=1, minsize=200)
        self.root.grid_rowconfigure(3, weight=1, minsize=150)

        # also make frames themselves expand internally where appropriate
        for f in (self.attr_frame, self.bonus_frame, self.stats_frame, self.thief_frame, self.weapons_frame, self.inventory_frame):
            f.grid_rowconfigure(0, weight=1)
            f.grid_columnconfigure(0, weight=1)

    # ----------------- model-view synchronization -----------------

    @property
    def is_updating(self) -> bool:
        """Public, read-only view of the updating flag."""
        return self._updating
    
    @contextmanager
    def suppress_updates(self):
        """Temporarily set updating to True to prevent recursive callbacks."""
        prev = self._updating
        self._updating = True
        try:
            yield
        finally:
            self._updating = prev

    def rebuild_ui(self):
        """Zerstört alle Kinder der Root und baut UI neu auf."""
        for child in self.root.winfo_children():
            child.destroy()

        # Build UI again
        self._build_ui()
        with self.suppress_updates():
            update_view_from_model(self)
    # ----------------- run -----------------
    def run(self):
        """Run the main Tk event loop."""
        self.root.mainloop()


# Backwards-compatibility helper used by main.py
def start_gui():
    """Start the GUI application (for backwards compatibility)."""
    App().run()
