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

from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.core.persistence import save_characterobj


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

    # Global player character instance (to be used by save/load functions)
    new_player = PlayerClass(
        player_name="New Player"
    )

    def __init__(self):
        # Create root first, then StringVars etc.
        self._updating = False  # flag to prevent recursive updates
        self.root = tk.Tk()
        self.root.title("Swords & Wizardry Charaktergenerator")
        self.root.minsize(ROOT_MIN_W, ROOT_MIN_H)

        # Global player character instance (to be used by save/load functions)
        self.new_player = PlayerClass(
            player_name="New Player"
        )

        # Make root use grid for all direct children and allow columns to expand
        for c in range(3):
            self.root.grid_columnconfigure(c, weight=1, minsize=VALUE_MIN_W)

        # GUI-bound variables (created after root exists)
        self.player_var = tk.StringVar(master=self.root)
        self.character_var = tk.StringVar(master=self.root)
        self.level_var = tk.StringVar(master=self.root, value="1")
        self.profession_var = tk.StringVar(master=self.root)
        self.race_var = tk.StringVar(master=self.root)
        self.gender_var = tk.StringVar(master=self.root)
        self.alignment_var = tk.StringVar(master=self.root)
        self.god_var = tk.StringVar(master=self.root)
        self.age_var = tk.StringVar(master=self.root)
        self.xp_bonus_var = tk.StringVar(master=self.root, value="0")
        self.xp_var = tk.StringVar(master=self.root, value="0")
        self.main_stats_var = tk.StringVar(master=self.root, value="STR DEX CON INT WIS CHA")
        self.status_var = tk.StringVar(master=self.root, value="Ready")
        self.stat_str_var = tk.StringVar(master=self.root, value="0")
        self.stat_dex_var = tk.StringVar(master=self.root, value="0")
        self.stat_con_var = tk.StringVar(master=self.root, value="0")
        self.stat_int_var = tk.StringVar(master=self.root, value="0")
        self.stat_wis_var = tk.StringVar(master=self.root, value="0")
        self.stat_cha_var = tk.StringVar(master=self.root, value="0")
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
        
    # ----------------- build UI -----------------
       
        # Build UI
        self._build_ui()
  
    # ----------------- UI building -----------------


    def _build_ui(self):
        # Create top frame and place it with grid (do not mix pack/grid on root)
        self.top_frame = ttk.Frame(self.root, borderwidth=5, relief="ridge", padding=(6, 6))
        self.top_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
       
        # Row 0: basic fields
        ttk.Label(self.top_frame, text="Spieler:in:").grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Entry(self.top_frame, textvariable=self.player_var).grid(row=0, column=1, sticky="ew", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, text="SC Name:").grid(row=0, column=2, sticky="w", padx=PADX, pady=PADY)
        ttk.Entry(self.top_frame, textvariable=self.character_var).grid(row=0, column=3, sticky="ew", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, text="Level:").grid(row=0, column=4, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, textvariable=self.level_var).grid(row=0, column=5, sticky="w", padx=PADX, pady=PADY)

        # Row 1
        ttk.Label(self.top_frame, text="Profession:").grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)
        profession_cb = ttk.Combobox(self.top_frame, textvariable=self.profession_var)
        profession_cb.grid(row=1, column=1, sticky="ew", padx=PADX, pady=PADY)
        profession_cb.config(values=["Fighter", "Cleric", "Thief", "Wizard", "Ranger", "Paladin"])
        ttk.Label(self.top_frame, text="Rasse:").grid(row=1, column=2, sticky="w", padx=PADX, pady=PADY)
        race_cb = ttk.Combobox(self.top_frame, textvariable=self.race_var)
        race_cb.grid(row=1, column=3, sticky="ew", padx=PADX, pady=PADY)
        race_cb.config(values=["Human", "Elf", "Dwarf", "Halfling", "Halfelf"])
        ttk.Label(self.top_frame, text="Geschlecht:").grid(row=1, column=4, sticky="w", padx=PADX, pady=PADY)
        gender_cb = ttk.Combobox(self.top_frame, textvariable=self.gender_var)
        gender_cb.grid(row=1, column=5, sticky="ew", padx=PADX, pady=PADY)
        gender_cb.config(values=["Male", "Female", "Other"])

        # Row 2
        ttk.Label(self.top_frame, text="Gesinnung:").grid(row=2, column=0, sticky="w", padx=PADX, pady=PADY)
        align_cb = ttk.Combobox(self.top_frame, textvariable=self.alignment_var)
        align_cb.grid(row=2, column=1, sticky="ew", padx=PADX, pady=PADY)
        align_cb.config(values=["Good", "Neutral", "Evil"])
        ttk.Label(self.top_frame, text="Gottheit:").grid(row=2, column=2, sticky="w", padx=PADX, pady=PADY)
        ttk.Entry(self.top_frame, textvariable=self.god_var).grid(row=2, column=3, sticky="ew", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, text="Alter:").grid(row=2, column=4, sticky="w", padx=PADX, pady=PADY)
        ttk.Entry(self.top_frame, textvariable=self.age_var).grid(row=2, column=5, sticky="ew", padx=PADX, pady=PADY)

        # Row 3 - main stats and XP
        ttk.Label(self.top_frame, text="Main Stats:").grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, textvariable=self.main_stats_var).grid(row=3, column=1, columnspan=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, text="EP-Bonus (%):").grid(row=3, column=2, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, textvariable=self.xp_bonus_var).grid(row=3, column=3, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, text="EP:").grid(row=3, column=4, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, textvariable=self.xp_var).grid(row=3, column=5, sticky="w", padx=PADX, pady=PADY)

        # ----------------- rest of the UI (attributes / bonuses / panels) -----------------
        # Attribute frame (use LabelFrame for nicer title)
        self.attr_frame = ttk.LabelFrame(self.root, text="Attribute", borderwidth=5, padding=(6, 6))
        self.attr_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Create stat variables and place them with grid
        ttk.Label(self.attr_frame, text="Strength (STR):").grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.attr_frame, textvariable=self.stat_str_var).grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.attr_frame, text="Dexterity (DEX):").grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.attr_frame, textvariable=self.stat_dex_var).grid(row=1, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.attr_frame, text="Constitution (CON):").grid(row=2, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.attr_frame, textvariable=self.stat_con_var).grid(row=2, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.attr_frame, text="Intelligence (INT):").grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.attr_frame, textvariable=self.stat_int_var).grid(row=3, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.attr_frame, text="Wisdom (WIS):").grid(row=4, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.attr_frame, textvariable=self.stat_wis_var).grid(row=4, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.attr_frame, text="Charisma (CHA):").grid(row=5, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.attr_frame, textvariable=self.stat_cha_var).grid(row=5, column=1, sticky="w", padx=PADX, pady=PADY)

        # Bonuses frame
        self.bonus_frame = ttk.LabelFrame(self.root, text="Attribute Bonuses", borderwidth=5, padding=(6, 6))
        self.bonus_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Create bonus labels and values
        ttk.Label(self.bonus_frame, text="Melee Attack Bonus:").grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, textvariable=self.strength_atck_mod_var).grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, text="Melee Damage Bonus:").grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, textvariable=self.strength_damage_mod_var).grid(row=1, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, text="Carry Capacity Bonus:").grid(row=2, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, textvariable=self.carry_capacity_mod_var).grid(row=2, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, text="Door Crack Bonus:").grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, textvariable=self.door_crack_mod_var).grid(row=3, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, text="Ranged Attack Bonus:").grid(row=4, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, textvariable=self.ranged_atck_mod_var).grid(row=4, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, text="AC Bonus:").grid(row=5, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, textvariable=self.ac_mod_var).grid(row=5, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, text="HP Bonus:").grid(row=6, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, textvariable=self.hp_mod_var).grid(row=6, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, text="Raise Dead Modifier:").grid(row=7, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, textvariable=self.raise_dead_mod_var).grid(row=7, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, text="Max Additional Languages:").grid(row=8, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, textvariable=self.max_add_langs_var).grid(row=8, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, text="Special Hirelings Cap:").grid(row=9, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.bonus_frame, textvariable=self.cap_spec_hirelings_var).grid(row=9, column=1, sticky="w", padx=PADX, pady=PADY)

        # Stats / Other panels
        self.stats_frame = ttk.LabelFrame(self.root, text="Stats / Derived", borderwidth=5, padding=(6, 6))
        self.stats_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

        # Create stat labels and values
        ttk.Label(self.stats_frame, text="State").grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, textvariable=self.player_state_var).grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, text="Hit Points (HP):").grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, textvariable=self.hp_var).grid(row=1, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, text="Saving Throw:").grid(row=2, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, textvariable=self.save_throw_var).grid(row=2, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, text="Armor Class (AC):").grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, textvariable=self.ac_var).grid(row=3, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, text="Darkvision:").grid(row=4, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, textvariable=self.darkvision_var).grid(row=4, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, text="Parry:").grid(row=5, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, textvariable=self.parry_var).grid(row=5, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, text="Languages:").grid(row=6, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, textvariable=self.add_langs_var).grid(row=6, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, text="Special Abilities:").grid(row=7, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, textvariable=self.special_abilities_var).grid(row=7, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, text="Immunities:").grid(row=8, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.stats_frame, textvariable=self.immunities_var).grid(row=8, column=1, sticky="w", padx=PADX, pady=PADY)

        # Thief skills panel
        self.thief_frame = ttk.LabelFrame(self.root, text="Thief Skills", borderwidth=5, padding=(6, 6))
        self.thief_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
  
        # Create thief skill labels and values
        ttk.Label(self.thief_frame, text="Delicate Tasks:").grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.thief_frame, textvariable=self.delicate_tasks_var).grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.thief_frame, text="Climb Walls:").grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.thief_frame, textvariable=self.climb_walls_var).grid(row=1, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.thief_frame, text="Hear Sounds:").grid(row=2, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.thief_frame, textvariable=self.hear_sounds_var).grid(row=2, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.thief_frame, text="Hide in Shadows:").grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.thief_frame, textvariable=self.hide_in_shadows_var).grid(row=3, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.thief_frame, text="Move Silently:").grid(row=4, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.thief_frame, textvariable=self.move_silently_var).grid(row=4, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.thief_frame, text="Open Locks:").grid(row=5, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.thief_frame, textvariable=self.open_locks_var).grid(row=5, column=1, sticky="w", padx=PADX, pady=PADY)

        # Weapons & Armor frame
        self.weapons_frame = ttk.LabelFrame(self.root, text="Weapons & Armor", borderwidth=5, padding=(6,6))
        self.weapons_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Inventory frame
        self.inventory_frame = ttk.LabelFrame(self.root, text="Inventory", borderwidth=5, padding=(6,6))
        self.inventory_frame.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.inventory_frame, text="Coins:").grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.inventory_frame, textvariable=self.coins_var).grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.inventory_frame, text="Treasure:").grid(row=1, column=0, sticky="nw", padx=PADX, pady=PADY)
        treasure_txt = scrolledtext.ScrolledText(
        self.inventory_frame,
        wrap="word",
        height=5,        # sichtbare Zeilenhöhe (kann angepasst werden)
        width=50,        # sichtbare Spaltenbreite (char-basiert)
        font=("TkDefaultFont", 10)
        )
        treasure_txt.grid(row=1, column=1, sticky="nsew", padx=PADX, pady=PADY)
        ttk.Label(self.inventory_frame, text="Inventory:").grid(row=2, column=0, sticky="nw", padx=PADX, pady=PADY)
        inventory_txt = scrolledtext.ScrolledText(
        self.inventory_frame,
        wrap="word",
        height=5,        # sichtbare Zeilenhöhe (kann angepasst werden)
        width=50,        # sichtbare Spaltenbreite (char-basiert)
        font=("TkDefaultFont", 10)
        )
        inventory_txt.grid(row=2, column=1, sticky="nsew", padx=PADX, pady=PADY)

        # Footerframe (if needed in future)
        self.footer_frame = ttk.Frame(self.root, borderwidth=5, padding=(6,6))
        self.footer_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        # place Save / Load buttons inside footer_frame on a new row so they're visually nearby
        btn_save = ttk.Button(self.footer_frame, text="Save", command=lambda: save_characterobj(self.new_player))
        btn_save.grid(row=0, column=0, sticky="e", padx=PADX, pady=PADY)
        btn_load = ttk.Button(self.footer_frame, text="Load", command="")
        btn_load.grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)

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


    @contextmanager
    def _suspend_updates(self):
        """Context manager to suspend update callbacks temporarily."""
        self._updating = True
        try:
            yield
        finally:
            self._updating = False

    def update_view_from_model(self):
        """Update all GUI-bound variables from the new_player model."""
        with self._suspend_updates():
            for field, val in asdict(self.new_player).items():
                var = getattr(self, f"{field}_var", None)
                if var is None:
                    continue
                s = str(val) if val is not None else ""
                if var.get() != s:
                    var.set(s)

    # ----------------- run -----------------
    def run(self):
        """Run the main Tk event loop."""
        self.root.mainloop()


# Backwards-compatibility helper used by main.py
def start_gui():
    """Start the GUI application (for backwards compatibility)."""
    App().run()