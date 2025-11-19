"""GUI application for the Swords & Wizardry character generator.

This file provides an App class that encapsulates the Tk GUI, previously implemented
as a collection of functions. The module still exposes start_gui() for backwards
compatibility (main.py imports start_gui).
"""
from contextlib import contextmanager
from dataclasses import asdict
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext
import tkinter.messagebox

from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.core.persistence import save_characterobj
from sw_character_generator.gui.gui_functions.gui_race_change import on_race_change
from sw_character_generator.gui.gui_functions.gui_role_stats import role_stats, switch_stats
from sw_character_generator.gui.gui_functions.gui_profession_change import on_profession_change
from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model


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
        self.root.minsize(ROOT_MIN_W, ROOT_MIN_H)

        # Global player character instance (to be used by save/load functions)
        self.new_player = PlayerClass()

        # Make root use grid for all direct children and allow columns to expand
        for c in range(3):
            self.root.grid_columnconfigure(c, weight=1, minsize=VALUE_MIN_W)

        # GUI-bound variables (created after root exists)
        self.player_name_var = tk.StringVar(master=self.root)
        self.character_name_var = tk.StringVar(master=self.root)
        self.level_var = tk.StringVar(master=self.root, value="1")
        self.profession_var = tk.StringVar(master=self.root)
        self.profession_var.trace_add("write", lambda *args: on_profession_change(self, *args))
        self.race_var = tk.StringVar(master=self.root)
        self.race_var.trace_add("write", lambda *args: on_race_change(self, *args))
        self.gender_var = tk.StringVar(master=self.root)
        self.alignment_var = tk.StringVar(master=self.root)
        self.god_var = tk.StringVar(master=self.root)
        self.age_var = tk.StringVar(master=self.root)
        self.xp_bonus_var = tk.StringVar(master=self.root, value="0")
        self.xp_var = tk.StringVar(master=self.root, value="0")
        self.main_stats_var = tk.StringVar(master=self.root)
        self.status_var = tk.StringVar(master=self.root, value="Ready")
        self.stat_str_var = tk.StringVar(master=self.root, value="0")
        self.stat_dex_var = tk.StringVar(master=self.root, value="0")
        self.stat_con_var = tk.StringVar(master=self.root, value="0")
        self.stat_int_var = tk.StringVar(master=self.root, value="0")
        self.stat_wis_var = tk.StringVar(master=self.root, value="0")
        self.stat_char_var = tk.StringVar(master=self.root, value="0")
        self.coins_var = tk.StringVar(master=self.root, value="0")
        self.delicate_tasks_var = tk.StringVar(master=self.root, value="0")
        self.climb_walls_var = tk.StringVar(master=self.root, value="0")
        self.hear_sounds_var = tk.StringVar(master=self.root, value="0")
        self.hide_in_shadows_var = tk.StringVar(master=self.root, value="0")
        self.move_silently_var = tk.StringVar(master=self.root, value="0")
        self.open_locks_var = tk.StringVar(master=self.root, value="0")
        self.player_state_var = tk.StringVar(master=self.root, value="Normal")
        self.hp_var = tk.StringVar(master=self.root, value="0")
        self.save_throw_var = tk.StringVar(master=self.root, value="0")
        self.ac_var = tk.StringVar(master=self.root, value="0")
        self.darkvision_var = tk.StringVar(master=self.root, value="No")
        self.parry_var = tk.StringVar(master=self.root, value="0")
        self.add_langs_var = tk.StringVar(master=self.root, value="0")
        self.special_abilities_var = tk.StringVar(master=self.root, value="")
        self.immunities_var = tk.StringVar(master=self.root, value="")
        self.strength_atck_mod_var = tk.StringVar(master=self.root, value="0")
        self.strength_damage_mod_var = tk.StringVar(master=self.root, value="0")
        self.carry_capacity_mod_var = tk.StringVar(master=self.root, value="0")
        self.door_crack_mod_var = tk.StringVar(master=self.root, value="0")
        self.ranged_atck_mod_var = tk.StringVar(master=self.root, value="0")
        self.ac_mod_var = tk.StringVar(master=self.root, value="0")
        self.hp_mod_var = tk.StringVar(master=self.root, value="0")
        self.raise_dead_mod_var = tk.StringVar(master=self.root, value="0")
        self.max_add_langs_var = tk.StringVar(master=self.root, value="0")
        self.cap_spec_hirelings_var = tk.StringVar(master=self.root, value="0")
        self.chk_opt_4d6dl_var = tk.BooleanVar(master=self.root, value=False)   
        
    # ----------------- setup UI -----------------

        style = ttk.Style()
        # Optional: anderes Theme wählen (manche Themes erlauben bessere Farbkontrolle)
        # verfügbare Themes: style.theme_names()
        style.theme_use("clam")

        # Buttons mit verschiedenen Styles
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

        # Labels mit verschiedenen Styles
        style.configure("Standard.TLabel",
                        foreground="#000000")
        
        style.configure("Attention.TLabel",
                        foreground="#c82333")
        
        # Frames mit verschiedenen Styles
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
        self._bind_model_vars()

        # Populate the view initially from the model
        update_view_from_model(self)
  
    # ----------------- UI building -----------------

    def _build_ui(self):

        # Create top frame and place it with grid (do not mix pack/grid on root)
        self.top_frame = ttk.Frame(self.root, borderwidth=5, relief="ridge", padding=(6, 6), style="Standard.TFrame")
        self.top_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
       
        # Row 0: basic fields
        self.lbl_player_name = ttk.Label(self.top_frame, text="Spieler:in:", style="Standard.TLabel")
        self.lbl_player_name.grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_player_name = ttk.Entry(self.top_frame, textvariable=self.player_name_var)
        self.entry_player_name.grid(row=0, column=1, sticky="ew", padx=PADX, pady=PADY)

        self.lbl_character_name = ttk.Label(self.top_frame, text="SC Name:", style="Standard.TLabel")
        self.lbl_character_name.grid(row=0, column=2, sticky="w", padx=PADX, pady=PADY)
        self.entry_character_name = ttk.Entry(self.top_frame, textvariable=self.character_name_var)
        self.entry_character_name.grid(row=0, column=3, sticky="ew", padx=PADX, pady=PADY)

        self.lbl_level = ttk.Label(self.top_frame, text="Level:", style="Standard.TLabel")
        self.lbl_level.grid(row=0, column=4, sticky="w", padx=PADX, pady=PADY)
        self.entry_level = ttk.Label(self.top_frame, textvariable=self.level_var)
        self.entry_level.grid(row=0, column=5, sticky="w", padx=PADX, pady=PADY)

        # Row 1
        self.lbl_profession = ttk.Label(self.top_frame, text="Profession:", style="Standard.TLabel")
        self.lbl_profession.grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)
        self.profession_cb = ttk.Combobox(self.top_frame, textvariable=self.profession_var, state="disabled")
        self.profession_cb.grid(row=1, column=1, sticky="ew", padx=PADX, pady=PADY)
        self.profession_cb.config(values=["Fighter", "Cleric", "Thief", "Wizard", "Ranger", "Paladin", "Druid"])

        self.lbl_race = ttk.Label(self.top_frame, text="Rasse:", style="Standard.TLabel")
        self.lbl_race.grid(row=1, column=2, sticky="w", padx=PADX, pady=PADY)
        self.race_cb = ttk.Combobox(self.top_frame, textvariable=self.race_var, state="disabled")
        self.race_cb.grid(row=1, column=3, sticky="ew", padx=PADX, pady=PADY)
        self.race_cb.config(values=list(getattr(self.new_player, "allowed_races", ())))

        self.lbl_gender = ttk.Label(self.top_frame, text="Geschlecht:", style="Standard.TLabel")
        self.lbl_gender.grid(row=1, column=4, sticky="w", padx=PADX, pady=PADY)
        self.gender_cb = ttk.Combobox(self.top_frame, textvariable=self.gender_var)
        self.gender_cb.grid(row=1, column=5, sticky="ew", padx=PADX, pady=PADY)
        self.gender_cb.config(values=["Male", "Female", "Other"])

        # Row 2
        self.lbl_alignment = ttk.Label(self.top_frame, text="Gesinnung:", style="Standard.TLabel")
        self.lbl_alignment.grid(row=2, column=0, sticky="w", padx=PADX, pady=PADY)
        self.align_cb = ttk.Combobox(self.top_frame, textvariable=self.alignment_var)
        self.align_cb.grid(row=2, column=1, sticky="ew", padx=PADX, pady=PADY)
        self.align_cb.config(values=["Good", "Neutral", "Evil"])

        self.lbl_god = ttk.Label(self.top_frame, text="Gottheit:", style="Standard.TLabel")
        self.lbl_god.grid(row=2, column=2, sticky="w", padx=PADX, pady=PADY)
        self.entry_god = ttk.Entry(self.top_frame, textvariable=self.god_var)
        self.entry_god.grid(row=2, column=3, sticky="ew", padx=PADX, pady=PADY)

        self.lbl_age = ttk.Label(self.top_frame, text="Alter:", style="Standard.TLabel")
        self.lbl_age.grid(row=2, column=4, sticky="w", padx=PADX, pady=PADY)
        self.entry_age = ttk.Entry(self.top_frame, textvariable=self.age_var)
        self.entry_age.grid(row=2, column=5, sticky="ew", padx=PADX, pady=PADY)

        # Row 3 - main stats and XP
        self.lbl_main_stats = ttk.Label(self.top_frame, text="Main Stats:", style="Standard.TLabel")
        self.lbl_main_stats.grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_main_stats = ttk.Label(self.top_frame, textvariable=self.main_stats_var)
        self.entry_main_stats.grid(row=3, column=1, columnspan=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_xp_bonus = ttk.Label(self.top_frame, text="EP-Bonus (%):", style="Standard.TLabel")
        self.lbl_xp_bonus.grid(row=3, column=2, sticky="w", padx=PADX, pady=PADY)
        self.entry_xp_bonus = ttk.Label(self.top_frame, textvariable=self.xp_bonus_var)
        self.entry_xp_bonus.grid(row=3, column=3, sticky="w", padx=PADX, pady=PADY)

        self.lbl_xp = ttk.Label(self.top_frame, text="EP:", style="Standard.TLabel")
        self.lbl_xp.grid(row=3, column=4, sticky="w", padx=PADX, pady=PADY)
        self.entry_xp = ttk.Label(self.top_frame, textvariable=self.xp_var)
        self.entry_xp.grid(row=3, column=5, sticky="w", padx=PADX, pady=PADY)

        # Attribute frame (use LabelFrame for nicer title)
        self.attr_frame = ttk.LabelFrame(self.root, text="Attribute", borderwidth=5, padding=(6, 6), style="Attention.TFrame")
        self.attr_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Row 0
        self.lbl_str = ttk.Label(self.attr_frame, text="Strength (STR):", style="Standard.TLabel")
        self.lbl_str.grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_str = ttk.Label(self.attr_frame, textvariable=self.stat_str_var)
        self.entry_str.grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)

        # Row 1
        self.lbl_dex = ttk.Label(self.attr_frame, text="Dexterity (DEX):", style="Standard.TLabel")
        self.lbl_dex.grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_dex = ttk.Label(self.attr_frame, textvariable=self.stat_dex_var)
        self.entry_dex.grid(row=1, column=1, sticky="w", padx=PADX, pady=PADY)

        # Row 2
        self.lbl_con = ttk.Label(self.attr_frame, text="Constitution (CON):", style="Standard.TLabel")
        self.lbl_con.grid(row=2, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_con = ttk.Label(self.attr_frame, textvariable=self.stat_con_var)
        self.entry_con.grid(row=2, column=1, sticky="w", padx=PADX, pady=PADY)

        # Row 3
        self.lbl_int = ttk.Label(self.attr_frame, text="Intelligence (INT):", style="Standard.TLabel")
        self.lbl_int.grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_int = ttk.Label(self.attr_frame, textvariable=self.stat_int_var)
        self.entry_int.grid(row=3, column=1, sticky="w", padx=PADX, pady=PADY)

        # Row 4
        self.lbl_wis = ttk.Label(self.attr_frame, text="Wisdom (WIS):", style="Standard.TLabel")
        self.lbl_wis.grid(row=4, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_wis = ttk.Label(self.attr_frame, textvariable=self.stat_wis_var)
        self.entry_wis.grid(row=4, column=1, sticky="w", padx=PADX, pady=PADY)

        # Row 5
        self.lbl_cha = ttk.Label(self.attr_frame, text="Charisma (CHA):", style="Standard.TLabel")
        self.lbl_cha.grid(row=5, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_cha = ttk.Label(self.attr_frame, textvariable=self.stat_char_var)
        self.entry_cha.grid(row=5, column=1, sticky="w", padx=PADX, pady=PADY)

        # place Roll Stats button inside attr_frame
        self.btn_roll_stats = ttk.Button(self.attr_frame, text="Roll Stats", style="Attention.TButton", command=lambda: role_stats(self, self.new_player, self.chk_opt_4d6dl_var.get(), self.btn_roll_stats, self.btn_switch_stats))
        self.btn_roll_stats.grid(row=6, column=0, sticky="ew", padx=PADX, pady=PADY)

        # Homebrew frame (use LabelFrame for nicer title)
        self.attr_homebrew_frame = ttk.LabelFrame(self.attr_frame, text="Homebrew", borderwidth=5, padding=(6, 6), style="Standard.TFrame")
        self.attr_homebrew_frame.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")

        # Switch Stats button inside homebrew frame
        def homebrew_switch_stats(self, character, btn_switch_stats):
            switch_stats(self.root, character, btn_switch_stats)
            self.status_var.set("Stats switched.")
            update_view_from_model(self)

        # Switch Stats button
        self.btn_switch_stats = ttk.Button(self.attr_homebrew_frame, text="Switch Stats", style="Standard.TButton", command=lambda: homebrew_switch_stats(self, self.new_player, self.btn_switch_stats))
        self.btn_switch_stats.config(state="disabled")  # Disabled for now
        self.btn_switch_stats.grid(row=0, column=1, sticky="ew", padx=PADX, pady=PADY)
        self.chk_opt_4d6dl = ttk.Checkbutton(self.attr_homebrew_frame, text="4d6 drop lowest", variable=self.chk_opt_4d6dl_var)
        self.chk_opt_4d6dl.grid(row=0, column=0, sticky="ew", padx=PADX, pady=PADY)

        # Bonuses frame
        self.bonus_frame = ttk.LabelFrame(self.root, text="Attribute Bonuses", borderwidth=5, padding=(6, 6), style="Standard.TFrame")
        self.bonus_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Create bonus labels and values
        self.lbl_strength_atck_bonus = ttk.Label(self.bonus_frame, text="Melee Attack Bonus:", style="Standard.TLabel")
        self.lbl_strength_atck_bonus.grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_strength_atck_bonus = ttk.Label(self.bonus_frame, textvariable=self.strength_atck_mod_var)
        self.entry_strength_atck_bonus.grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_strength_damage_bonus = ttk.Label(self.bonus_frame, text="Melee Damage Bonus:", style="Standard.TLabel")
        self.lbl_strength_damage_bonus.grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_strength_damage_bonus = ttk.Label(self.bonus_frame, textvariable=self.strength_damage_mod_var)
        self.entry_strength_damage_bonus.grid(row=1, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_carry_capacity_bonus = ttk.Label(self.bonus_frame, text="Carry Capacity Bonus:", style="Standard.TLabel")
        self.lbl_carry_capacity_bonus.grid(row=2, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_carry_capacity_bonus = ttk.Label(self.bonus_frame, textvariable=self.carry_capacity_mod_var)
        self.entry_carry_capacity_bonus.grid(row=2, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_door_crack_bonus = ttk.Label(self.bonus_frame, text="Door Crack Bonus:", style="Standard.TLabel")
        self.lbl_door_crack_bonus.grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_door_crack_bonus = ttk.Label(self.bonus_frame, textvariable=self.door_crack_mod_var)
        self.entry_door_crack_bonus.grid(row=3, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_ranged_atk_bonus = ttk.Label(self.bonus_frame, text="Ranged Attack Bonus:", style="Standard.TLabel")
        self.lbl_ranged_atk_bonus.grid(row=4, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_ranged_atk_bonus = ttk.Label(self.bonus_frame, textvariable=self.ranged_atck_mod_var)
        self.entry_ranged_atk_bonus.grid(row=4, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_ac_bonus = ttk.Label(self.bonus_frame, text="AC Bonus:", style="Standard.TLabel")
        self.lbl_ac_bonus.grid(row=5, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_ac_bonus = ttk.Label(self.bonus_frame, textvariable=self.ac_mod_var)
        self.entry_ac_bonus.grid(row=5, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_hp_bonus = ttk.Label(self.bonus_frame, text="HP Bonus:", style="Standard.TLabel")
        self.lbl_hp_bonus.grid(row=6, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_hp_bonus = ttk.Label(self.bonus_frame, textvariable=self.hp_mod_var)
        self.entry_hp_bonus.grid(row=6, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_raise_dead_mod = ttk.Label(self.bonus_frame, text="Raise Dead Modifier:", style="Standard.TLabel")
        self.lbl_raise_dead_mod.grid(row=7, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_raise_dead_mod = ttk.Label(self.bonus_frame, textvariable=self.raise_dead_mod_var)
        self.entry_raise_dead_mod.grid(row=7, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_max_add_langs = ttk.Label(self.bonus_frame, text="Max Additional Languages:", style="Standard.TLabel")
        self.lbl_max_add_langs.grid(row=8, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_max_add_langs = ttk.Label(self.bonus_frame, textvariable=self.max_add_langs_var)
        self.entry_max_add_langs.grid(row=8, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_cap_spec_hirelings = ttk.Label(self.bonus_frame, text="Special Hirelings Cap:", style="Standard.TLabel")
        self.lbl_cap_spec_hirelings.grid(row=9, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_cap_spec_hirelings = ttk.Label(self.bonus_frame, textvariable=self.cap_spec_hirelings_var)
        self.entry_cap_spec_hirelings.grid(row=9, column=1, sticky="w", padx=PADX, pady=PADY)

        # Stats / Other panels
        self.stats_frame = ttk.LabelFrame(self.root, text="Stats / Derived", borderwidth=5, padding=(6, 6), style="Standard.TFrame")
        self.stats_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

        # Create stat labels and values
        self.lbl_player_state = ttk.Label(self.stats_frame, text="State:", style="Standard.TLabel")
        self.lbl_player_state.grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_player_state = ttk.Label(self.stats_frame, textvariable=self.player_state_var)
        self.entry_player_state.grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY) 

        self.lbl_hp = ttk.Label(self.stats_frame, text="Hit Points (HP):", style="Standard.TLabel")
        self.lbl_hp.grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_hp = ttk.Label(self.stats_frame, textvariable=self.hp_var)
        self.entry_hp.grid(row=1, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_save_throw = ttk.Label(self.stats_frame, text="Saving Throw:", style="Standard.TLabel")
        self.lbl_save_throw.grid(row=2, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_save_throw = ttk.Label(self.stats_frame, textvariable=self.save_throw_var)
        self.entry_save_throw.grid(row=2, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_ac = ttk.Label(self.stats_frame, text="Armor Class (AC):", style="Standard.TLabel")
        self.lbl_ac.grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_ac = ttk.Label(self.stats_frame, textvariable=self.ac_var)
        self.entry_ac.grid(row=3, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_darkvision = ttk.Label(self.stats_frame, text="Darkvision:", style="Standard.TLabel")
        self.lbl_darkvision.grid(row=4, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_darkvision = ttk.Label(self.stats_frame, textvariable=self.darkvision_var)
        self.entry_darkvision.grid(row=4, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_parry = ttk.Label(self.stats_frame, text="Parry:", style="Standard.TLabel")
        self.lbl_parry.grid(row=5, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_parry = ttk.Label(self.stats_frame, textvariable=self.parry_var)
        self.entry_parry.grid(row=5, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_add_langs = ttk.Label(self.stats_frame, text="Languages:", style="Standard.TLabel")
        self.lbl_add_langs.grid(row=6, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_add_langs = ttk.Label(self.stats_frame, textvariable=self.add_langs_var)
        self.entry_add_langs.grid(row=6, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_immunities = ttk.Label(self.stats_frame, text="Immunities:", style="Standard.TLabel")
        self.lbl_immunities.grid(row=7, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_immunities = ttk.Label(self.stats_frame, textvariable=self.immunities_var)
        self.entry_immunities.grid(row=7, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_special_abilities = ttk.Label(self.stats_frame, text="Special Abilities:", style="Standard.TLabel")
        self.lbl_special_abilities.grid(row=8, column=0, sticky="w", padx=PADX, pady=PADY)

        # Use scrolledtext for special abilities
        special_abilities_txt = scrolledtext.ScrolledText(
        self.stats_frame,
        wrap="word",
        height=5,        # sichtbare Zeilenhöhe (kann angepasst werden)
        width=40,        # sichtbare Spaltenbreite (char-basiert)
        font=("TkDefaultFont", 10)
        )
        special_abilities_txt.grid(row=8, column=1, sticky="nsew", padx=PADX, pady=PADY)   


        # Thief skills panel
        self.thief_frame = ttk.LabelFrame(self.root, text="Thief Skills", borderwidth=5, padding=(6, 6), style="Standard.TFrame")
        self.thief_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
  
        # Create thief skill labels and values
        self.lbl_delicate_tasks = ttk.Label(self.thief_frame, text="Delicate Tasks:", style="Standard.TLabel")
        self.lbl_delicate_tasks.grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_delicate_tasks = ttk.Label(self.thief_frame, textvariable=self.delicate_tasks_var)
        self.entry_delicate_tasks.grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_climb_walls = ttk.Label(self.thief_frame, text="Climb Walls:", style="Standard.TLabel")
        self.lbl_climb_walls.grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_climb_walls = ttk.Label(self.thief_frame, textvariable=self.climb_walls_var)
        self.entry_climb_walls.grid(row=1, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_hear_sounds = ttk.Label(self.thief_frame, text="Hear Sounds:", style="Standard.TLabel")
        self.lbl_hear_sounds.grid(row=2, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_hear_sounds = ttk.Label(self.thief_frame, textvariable=self.hear_sounds_var)
        self.entry_hear_sounds.grid(row=2, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_hide_in_shadows = ttk.Label(self.thief_frame, text="Hide in Shadows:", style="Standard.TLabel")
        self.lbl_hide_in_shadows.grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_hide_in_shadows = ttk.Label(self.thief_frame, textvariable=self.hide_in_shadows_var)
        self.entry_hide_in_shadows.grid(row=3, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_move_silently = ttk.Label(self.thief_frame, text="Move Silently:", style="Standard.TLabel")
        self.lbl_move_silently.grid(row=4, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_move_silently = ttk.Label(self.thief_frame, textvariable=self.move_silently_var)
        self.entry_move_silently.grid(row=4, column=1, sticky="w", padx=PADX, pady=PADY)

        self.lbl_open_locks = ttk.Label(self.thief_frame, text="Open Locks:", style="Standard.TLabel")
        self.lbl_open_locks.grid(row=5, column=0, sticky="w", padx=PADX, pady=PADY)
        self.entry_open_locks = ttk.Label(self.thief_frame, textvariable=self.open_locks_var)
        self.entry_open_locks.grid(row=5, column=1, sticky="w", padx=PADX, pady=PADY)

        # Weapons & Armor frame
        self.weapons_frame = ttk.LabelFrame(self.root, text="Weapons & Armor", borderwidth=5, padding=(6,6), style="Standard.TFrame")
        self.weapons_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Inventory frame
        self.inventory_frame = ttk.LabelFrame(self.root, text="Inventory", borderwidth=5, padding=(6,6), style="Standard.TFrame")
        self.inventory_frame.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.inventory_frame, text="Coins:").grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.inventory_frame, textvariable=self.coins_var).grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.inventory_frame, text="Treasure:").grid(row=1, column=0, sticky="nw", padx=PADX, pady=PADY)
        
        # Use scrolledtext for treasure
        treasure_txt = scrolledtext.ScrolledText(
        self.inventory_frame,
        wrap="word",
        height=5,        # sichtbare Zeilenhöhe (kann angepasst werden)
        width=50,        # sichtbare Spaltenbreite (char-basiert)
        font=("TkDefaultFont", 10)
        )
        treasure_txt.grid(row=1, column=1, sticky="nsew", padx=PADX, pady=PADY)
        ttk.Label(self.inventory_frame, text="Inventory:").grid(row=2, column=0, sticky="nw", padx=PADX, pady=PADY)
        
        # Use scrolledtext for inventory
        inventory_txt = scrolledtext.ScrolledText(
        self.inventory_frame,
        wrap="word",
        height=5,        # sichtbare Zeilenhöhe (kann angepasst werden)
        width=50,        # sichtbare Spaltenbreite (char-basiert)
        font=("TkDefaultFont", 10)
        )
        inventory_txt.grid(row=2, column=1, sticky="nsew", padx=PADX, pady=PADY)

        # Footerframe (if needed in future)
        self.footer_frame = ttk.Frame(self.root, borderwidth=5, padding=(6,6), style="Standard.TFrame")
        self.footer_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        # place Save / Load buttons inside footer_frame on a new row so they're visually nearby
        self.btn_save = ttk.Button(self.footer_frame, text="Save", command=lambda: save_characterobj(self.new_player))
        self.btn_save.grid(row=0, column=0, sticky="e", padx=PADX, pady=PADY)
        self.btn_load = ttk.Button(self.footer_frame, text="Load", command="")
        self.btn_load.grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)
        self.btn_exit = ttk.Button(self.footer_frame, text="Exit", command=lambda: tkinter.messagebox.askokcancel("Exit", "Do you really want to exit?", parent=self.root) and self.root.destroy())
        self.btn_exit.grid(row=0, column=2, sticky="e", padx=PADX, pady=PADY)


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
    
    def _bind_model_vars(self):
        """Bind GUI variables/widgets back to the model."""
        for field in asdict(self.new_player).keys():
            var = getattr(self, f"{field}_var", None)
            if var is None:
                continue
            var.trace_add("write", lambda *a, f=field, v=var: self._on_var_change(f, v))

    def _on_var_change(self, field, var):
        """Callback when a GUI variable changes; update the model accordingly."""
        if self._updating:
            return
        val = var.get()
        # Convert to appropriate type if necessary (e.g., int)
        current_val = getattr(self.new_player, field)
        if isinstance(current_val, int):
            try:
                val = int(val)
            except ValueError:
                val = 0  # or some default/fallback
        setattr(self.new_player, field, val)
        # Optionally, update the view again to reflect any derived changes
        update_view_from_model(self)

    # ----------------- run -----------------
    def run(self):
        """Run the main Tk event loop."""
        self.root.mainloop()


# Backwards-compatibility helper used by main.py
def start_gui():
    """Start the GUI application (for backwards compatibility)."""
    App().run()