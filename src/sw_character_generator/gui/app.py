"""GUI application for the Swords & Wizardry character generator.

This file provides an App class that encapsulates the Tk GUI, previously implemented
as a collection of functions. The module still exposes start_gui() for backwards
compatibility (main.py imports start_gui).
"""
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as scrolledtext
import sys
from dataclasses import asdict
from src.sw_character_generator.core.persistence import save_local_player, load_local_player
from src.sw_character_generator.gui.widgets import label_entry
from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.core.models import LocalPlayer


# Layout / sizing constants
ROOT_MIN_W = 900
ROOT_MIN_H = 600
LABEL_MIN_W = 120
VALUE_MIN_W = 160
ENTRY_WIDTH = 20
PADX = 8
PADY = 6

def label_entry(parent, text, row, column, var=None, widget="entry", width=ENTRY_WIDTH, columnspan=1, **grid_opts):
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY)
    if widget == "entry":
        ent = ttk.Entry(parent, textvariable=var, width=width)
        ent.grid(row=row, column=column + 1, columnspan=columnspan, sticky="ew", padx=PADX, pady=PADY, **grid_opts)
        return lbl, ent
    elif widget == "combobox":
        cb = ttk.Combobox(parent, textvariable=var, state="readonly", width=width)
        cb.grid(row=row, column=column + 1, columnspan=columnspan, sticky="ew", padx=PADX, pady=PADY, **grid_opts)
        return lbl, cb
    else:
        raise ValueError("Unsupported widget type")

class App:
    """Class-based GUI for the character generator."""

    def __init__(self):
        # Create root first, then StringVars etc.
        self.root = tk.Tk()
        self.root.title("Swords & Wizardry Charaktergenerator")
        self.root.minsize(ROOT_MIN_W, ROOT_MIN_H)

        # Make root use grid for all direct children and allow columns to expand
        for c in range(3):
            self.root.grid_columnconfigure(c, weight=1, minsize=VALUE_MIN_W)

        # Application state
        self.current_local_player: LocalPlayer = LocalPlayer()

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

        # Try to pre-load last saved values if present
        last = load_local_player()
        if last:
            try:
                print("Found saved LocalPlayer, loading into fields...")
                self.player_var.set(last.get("player_name", ""))
                self.character_var.set(last.get("character_name", ""))
                self.age_var.set(last.get("age", ""))
                self.gender_var.set(last.get("gender", ""))
                self.god_var.set(last.get("deity", ""))
                self.god_var.set(last.get("deity", ""))
                self.update_status("Automatisch geladene gespeicherte Werte.")
            except Exception:
                pass

    # ----------------- UI building -----------------


    def _build_ui(self):
        # Create top frame and place it with grid (do not mix pack/grid on root)
        self.top_frame = ttk.Frame(self.root, borderwidth=5, relief="ridge", padding=(6, 6))
        self.top_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
       
        # Row 0: basic fields
        label_entry(self.top_frame, "Spieler:in:", 0, 0, var=self.player_var, columnspan=1)
        label_entry(self.top_frame, "SC Name:", 0, 2, var=self.character_var, columnspan=1)
        ttk.Label(self.top_frame, text="Level:").grid(row=0, column=4, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, textvariable=self.level_var).grid(row=0, column=5, sticky="w", padx=PADX, pady=PADY)

        # Row 1
        label_entry(self.top_frame, "Profession:", 1, 0, var=self.profession_var, widget="combobox")
        profession_cb = self.top_frame.grid_slaves(row=1, column=1)[0]
        profession_cb.config(values=["Fighter", "Cleric", "Thief", "Wizard", "Ranger", "Paladin"])
        label_entry(self.top_frame, "Rasse:", 1, 2, var=self.race_var, widget="combobox")
        race_cb = self.top_frame.grid_slaves(row=1, column=3)[0]
        race_cb.config(values=["Human", "Elf", "Dwarf", "Halfling", "Halfelf"])
        label_entry(self.top_frame, "Geschlecht:", 1, 4, var=self.gender_var)

        # Row 2
        label_entry(self.top_frame, "Gesinnung:", 2, 0, var=self.alignment_var, widget="combobox")
        align_cb = self.top_frame.grid_slaves(row=2, column=1)[0]
        align_cb.config(values=["Good", "Neutral", "Evil"])
        label_entry(self.top_frame, "Gottheit:", 2, 2, var=self.god_var)
        label_entry(self.top_frame, "Alter:", 2, 4, var=self.age_var)

        # Row 3 - main stats and XP
        ttk.Label(self.top_frame, text="Main Stats:").grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, textvariable=self.main_stats_var).grid(row=3, column=1, columnspan=1, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, text="EP-Bonus (%):").grid(row=3, column=2, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, textvariable=self.xp_bonus_var).grid(row=3, column=3, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, text="EP:").grid(row=3, column=4, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(self.top_frame, textvariable=self.xp_var).grid(row=3, column=5, sticky="w", padx=PADX, pady=PADY)

        # --- Save / Load controls for the rudimentary binding ---
        status_label = ttk.Label(self.root, textvariable=self.status_var, anchor="w")
        status_label.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=(0, 8))

        # place Save / Load buttons inside top_frame on a new row so they're visually nearby
        btn_save = ttk.Button(self.top_frame, text="Save", command=self.on_save_player)
        btn_save.grid(row=4, column=4, columnspan=1, sticky="e", padx=PADX, pady=PADY)
        btn_load = ttk.Button(self.top_frame, text="Load", command=self.on_load_player)
        btn_load.grid(row=4, column=5, columnspan=1, sticky="w", padx=PADX, pady=PADY)

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

        # Make lower rows/frames expand when window is resized
        self.root.grid_rowconfigure(1, weight=1, minsize=200)
        self.root.grid_rowconfigure(2, weight=1, minsize=200)
        self.root.grid_rowconfigure(3, weight=1, minsize=150)

        # also make frames themselves expand internally where appropriate
        for f in (self.attr_frame, self.bonus_frame, self.stats_frame, self.thief_frame, self.weapons_frame, self.inventory_frame):
            f.grid_rowconfigure(0, weight=1)
            f.grid_columnconfigure(0, weight=1)

    # ----------------- utilities / actions -----------------
    def update_status(self, msg: str):
        """Update the status bar message."""
        self.status_var.set(msg)
        print(msg)

    def build_local_player_from_vars(self) -> LocalPlayer:
        """Build a LocalPlayer instance from the current GUI variable values."""
        print("Building LocalPlayer from GUI fields...")
        return LocalPlayer(
            player_name=self.player_var.get().strip(),
            character_name=self.character_var.get().strip(),
            age=self.age_var.get().strip(),
            gender=self.gender_var.get().strip(),
            deity=self.god_var.get().strip(),
        )

    def try_bind_to_playerclass(self, lp: LocalPlayer) -> bool:
        """Attempt to create/update a PlayerClass instance with the given fields.

        Returns True on success, False on any failure. This is intentionally tolerant:
        it will try to setattr common attribute names and ignore failures.
        """
        try:
            # try no-arg constructor first
            p = PlayerClass()
        except Exception:
            try:
                # try a two-arg constructor common in some models (player, character)
                p = PlayerClass(lp.player_name, lp.character_name)
            except Exception as e:
                # can't instantiate PlayerClass -> bail out
                print("Could not instantiate PlayerClass:", e, file=sys.stderr)
                return False

        # map of local fields -> candidate attribute names on PlayerClass
        mappings = {
            "player_name": ["player_name", "player", "playername", "owner"],
            "character_name": ["character_name", "character", "name", "char_name"],
            "age": ["age", "alter"],
            "gender": ["gender", "sex"],
            "deity": ["deity", "god", "gottheit"],
        }

        success_any = False
        for local_field, candidates in mappings.items():
            val = getattr(lp, local_field)
            for cand in candidates:
                try:
                    if hasattr(p, cand):
                        setattr(p, cand, val)
                        success_any = True
                        break
                    else:
                        # try setter method pattern set_<field>
                        setter = f"set_{cand}"
                        if hasattr(p, setter):
                            getattr(p, setter)(val)
                            success_any = True
                            break
                except Exception as e:
                    # ignore individual failures but log
                    print(f"Failed setting {cand} on PlayerClass: {e}", file=sys.stderr)
                    continue

        # If at least one attribute was set, we consider it useful and print the object
        print("Attempting to update PlayerClass instance:", p)
        if success_any:
            try:
                print("Updated PlayerClass instance:", p)
            except Exception:
                pass
            # optionally persist a small JSON with values
            save_local_player(lp)
            #_safe_json_dump(asdict(lp), _PLAYER_PERSIST_FILE)
            self.update_status("PlayerClass instanziert/aktualisiert und lokal gespeichert.")
            return True

        return False

    def on_save_player(self):
        """Handle Save button click: save current fields to LocalPlayer and try to bind to PlayerClass."""
        print("Saving LocalPlayer from GUI fields...")
        lp = self.build_local_player_from_vars()
        # Save to local model first
        self.current_local_player = lp
        # Try to bind to PlayerClass (best-effort)
        bound = self.try_bind_to_playerclass(lp)
        if bound:
            print("PlayerClass erfolgreich aktualisiert.")
            self.update_status("Daten erfolgreich in PlayerClass geschrieben.")
        else:
            print("Konnte PlayerClass nicht aktualisieren.")
            # fallback: save JSON locally so it isn't lost
            save_local_player(lp)
            self.update_status("Lokale Felder gespeichert (PlayerClass nicht aktualisiert).")

    def on_load_player(self):
        """Handle Load button click: load fields from persisted LocalPlayer JSON."""
        print("Loading LocalPlayer from persisted JSON...")
        data = load_local_player()
        if data:
            print("Loaded LocalPlayer data:", data)
            self.current_local_player = LocalPlayer(**{k: str(v) for k, v in data.items()})
            # update GUI fields
            self.player_var.set(self.current_local_player.player_name)
            self.character_var.set(self.current_local_player.character_name)
            self.age_var.set(self.current_local_player.age)
            self.gender_var.set(self.current_local_player.gender)
            self.god_var.set(self.current_local_player.deity)
            self.update_status("Gespeicherte Werte geladen.")
        else:
            print("No persisted LocalPlayer data found.")
            self.update_status("Keine gespeicherten Werte gefunden.")

    # ----------------- run -----------------
    def run(self):
        """Run the main Tk event loop."""
        self.root.mainloop()


# Backwards-compatibility helper used by main.py
def start_gui():
    App().run()