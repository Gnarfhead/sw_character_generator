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
import traceback

from sw_character_generator.classes.playerclass import PlayerClass
from sw_character_generator.functions.manage_ac import calculate_ac, update_armor_ac
from sw_character_generator.functions.manage_coins import modify_coins
from sw_character_generator.functions.manage_hp import modify_hp, set_starting_hp, set_roll_hp_button
from sw_character_generator.functions.character_handling import save_character, load_character
from sw_character_generator.gui.gui_functions.gui_inventory import update_equipment_comboboxes
from sw_character_generator.gui.gui_functions.gui_new_character import apply_character, new_characterobj
from sw_character_generator.functions.manage_xp import add_xp
from sw_character_generator.gui.gui_functions.gui_inventory_dialog import on_edit_item_click, open_add_item_dialog
from sw_character_generator.gui.gui_functions.gui_magic import create_spell_table_widget
from sw_character_generator.gui.gui_functions.gui_dice_roller import dice_roller
from sw_character_generator.gui.gui_functions.gui_alignment_change import on_alignment_change
from sw_character_generator.gui.gui_functions.gui_race_change import on_race_change
from sw_character_generator.gui.gui_functions.gui_role_stats import role_stats, switch_stats
from sw_character_generator.gui.gui_functions.gui_profession_change import on_profession_change
from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model
from sw_character_generator.gui.gui_functions.gui_persistence import bind_model_vars
from sw_character_generator.gui.gui_functions.gui_widgets import widget_button, widget_entry_long, widget_extlabel_short, widget_label, widget_combobox, widget_label_var, widget_spinbox, widget_checkbutton, widget_spinbox_nolabel
from sw_character_generator.utility.linux_fullscreen import toggle_maximize
from sw_character_generator.functions.manage_items import equip_item, load_item_database

# Layout / sizing constants
ROOT_MIN_W = 900
ROOT_MIN_H = 600
LABEL_MIN_W = 120
VALUE_MIN_W = 160
ENTRY_WIDTH = 20
PADX = 15
PADY = 5


class App:
    """Class-based GUI for the character generator."""

    #----------------- initialization -----------------

    def __init__(self):
        # Create root first, then StringVars etc.
        self._updating = True  # flag to prevent recursive updates
        self.root = tk.Tk()
        self.root.title("Swords & Wizardry Charactergenerator")
        self.root.minsize(900, 600)
   
        # Maximiere Fenster (plattformunabhängig)
        try:
            # Windows/Mac
            self.root.state('zoomed')
        except tk.TclError:
            # Linux - maximiere manuell über Geometry
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        # Optional: F11 zum Togglen zwischen maximiert und normal
        self.root.bind("<F11>", lambda event: toggle_maximize(self, event))

        # Global player character instance (to be used by save/load functions)
        self.new_player = PlayerClass()

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
        self.stat_str_temp_var = tk.IntVar(master=self.root, value=0)
        self.stat_str_total_var = tk.IntVar(master=self.root, value=0)
        self.stat_dex_var = tk.IntVar(master=self.root, value=0)
        self.stat_dex_temp_var = tk.IntVar(master=self.root, value=0)
        self.stat_dex_total_var = tk.IntVar(master=self.root, value=0)
        self.stat_con_var = tk.IntVar(master=self.root, value=0)
        self.stat_con_temp_var = tk.IntVar(master=self.root, value=0)
        self.stat_con_total_var = tk.IntVar(master=self.root, value=0)
        self.stat_int_var = tk.IntVar(master=self.root, value=0)
        self.stat_int_temp_var = tk.IntVar(master=self.root, value=0)
        self.stat_int_total_var = tk.IntVar(master=self.root, value=0)
        self.stat_wis_var = tk.IntVar(master=self.root, value=0)
        self.stat_wis_temp_var = tk.IntVar(master=self.root, value=0)
        self.stat_wis_total_var = tk.IntVar(master=self.root, value=0)
        self.stat_char_var = tk.IntVar(master=self.root, value=0)
        self.stat_char_temp_var = tk.IntVar(master=self.root, value=0)
        self.stat_char_total_var = tk.IntVar(master=self.root, value=0)
        self.coins_platinum_var = tk.IntVar(master=self.root, value=0)
        self.coins_platinum_mod_var = tk.IntVar(master=self.root, value=0)
        self.coins_gold_var = tk.IntVar(master=self.root, value=0)
        self.coins_gold_mod_var = tk.IntVar(master=self.root, value=0)
        self.coins_electrum_var = tk.IntVar(master=self.root, value=0)
        self.coins_electrum_mod_var = tk.IntVar(master=self.root, value=0)
        self.coins_silver_var = tk.IntVar(master=self.root, value=0)
        self.coins_silver_mod_var = tk.IntVar(master=self.root, value=0)
        self.coins_copper_var = tk.IntVar(master=self.root, value=0)
        self.coins_copper_mod_var = tk.IntVar(master=self.root, value=0)
        self.delicate_tasks_var = tk.IntVar(master=self.root, value=0)
        self.climb_walls_var = tk.IntVar(master=self.root, value=0)
        self.hear_sounds_var = tk.StringVar(master=self.root, value="0:6")
        self.hide_in_shadows_var = tk.IntVar(master=self.root, value=0)
        self.move_silently_var = tk.IntVar(master=self.root, value=0)
        self.open_locks_var = tk.IntVar(master=self.root, value=0)
        self.player_state_var = tk.StringVar(master=self.root, value="Normal")
        self.hp_var = tk.IntVar(master=self.root, value=0)
        self.hp_current_var = tk.IntVar(master=self.root, value=0)
        self.hp_last_roll_var = tk.IntVar(master=self.root, value=0)
        self.hp_modify_var = tk.IntVar(master=self.root, value=0)
        self.save_throw_var = tk.IntVar(master=self.root, value=0)
        self.darkvision_var = tk.StringVar(master=self.root, value="No")
        self.parry_var = tk.IntVar(master=self.root, value=0)
        self.languages_var = tk.StringVar(master=self.root, value="")
        self.additional_languages_var = tk.StringVar(master=self.root, value="")
        self.special_abilities_var = tk.StringVar(master=self.root, value="")
        self.immunities_var = tk.StringVar(master=self.root, value="")
        self.strength_atck_mod_var = tk.IntVar(master=self.root, value=0)
        self.strength_atck_mod_temp_var = tk.IntVar(master=self.root, value=0)
        self.strength_atck_mod_total_var = tk.IntVar(master=self.root, value=0)
        self.strength_damage_mod_var = tk.IntVar(master=self.root, value=0)
        self.strength_damage_mod_temp_var = tk.IntVar(master=self.root, value=0)
        self.strength_damage_mod_total_var = tk.IntVar(master=self.root, value=0)
        self.carry_capacity_mod_var = tk.DoubleVar(master=self.root, value=0.0)
        self.door_crack_mod_var = tk.IntVar(master=self.root, value=0)
        self.ranged_atck_mod_var = tk.IntVar(master=self.root, value=0)
        self.ranged_atck_mod_temp_var = tk.IntVar(master=self.root, value=0)
        self.ranged_atck_mod_total_var = tk.IntVar(master=self.root, value=0)
        self.ac_var = tk.IntVar(master=self.root, value=0)
        self.ac_mod_var = tk.IntVar(master=self.root, value=0)
        self.ac_mod_temp_var = tk.IntVar(master=self.root, value=0)
        self.ac_total_var = tk.IntVar(master=self.root, value=0)
        self.hp_mod_var = tk.IntVar(master=self.root, value=0)
        self.raise_dead_mod_var = tk.IntVar(master=self.root, value=0)
        self.max_add_langs_var = tk.IntVar(master=self.root, value=0)
        self.cap_spec_hirelings_var = tk.IntVar(master=self.root, value=0)
        self.chk_opt_4d6dl_var = tk.BooleanVar(master=self.root, value=False)
        self.chk_opt_fullhplvl1_var = tk.BooleanVar(master=self.root, value=False)
        self.chk_opt_fullhplvl1_var.trace_add("write", lambda *args: set_roll_hp_button(self, self.chk_opt_fullhplvl1_var))
        self.add_xp_var = tk.IntVar(master=self.root, value=0)
        self.nextlevel_var = tk.IntVar(master=self.root, value=0)
        self.highest_spell_level_var = tk.IntVar(master=self.root, value=0)
        self.understand_spell_var = tk.IntVar(master=self.root, value=0)
        self.min_spells_per_level_var = tk.IntVar(master=self.root, value=0)
        self.max_spells_per_level_var = tk.IntVar(master=self.root, value=0)
        self.main_hand_var = tk.StringVar(master=self.root, value="")
        self.off_hand_var = tk.StringVar(master=self.root, value="")
        self.armor_var = tk.StringVar(master=self.root, value="")


    # ----------------- load data -----------------

        # Lade die Item-Datenbank
        try:
            self.item_database = load_item_database()
            if not self.item_database:
                messagebox.showwarning(
                    "Item Database Empty",
                    "No items loaded. Check itemdb.json for valid entries."
                )
        except Exception as e:
            self.item_database = []
            print("DEBUG - Fehler beim Laden der Item-Datenbank:", e)

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
                        foreground="#ff8e25")
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
        print("DEBUG: _build_ui() completed")

        # Bind GUI variables/widgets back to model
        bind_model_vars(self)
        print("DEBUG: bind_model_vars() completed")

        # Populate the view initially from the model
        update_view_from_model(self)
        print("DEBUG: update_view_from_model() completed") 

        
        # ← HINZUGEFÜGT: Setze Flag auf False
        self._updating = False
        print("DEBUG: Set _updating = False")
        
        # ← HINZUGEFÜGT: Update Equipment-Comboboxen NACH Initialisierung
        print("DEBUG: Scheduling equipment combobox update")
        self.root.after(200, lambda: self._safe_update_equipment())
        print("DEBUG: __init__ END")

    # ----------------- UI building -----------------

    def _build_ui(self):

        #################################
        # Create a main canvas with scrollbars
        self.main_canvas = tk.Canvas(self.root, highlightthickness=0)
        self.main_canvas.grid(row=0, column=0, sticky="nsew")
        
        # Vertical scrollbar
        self.v_scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.main_canvas.yview)
        self.v_scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Horizontal scrollbar
        self.h_scrollbar = ttk.Scrollbar(self.root, orient="horizontal", command=self.main_canvas.xview)
        self.h_scrollbar.grid(row=1, column=0, sticky="ew")
        
        self.main_canvas.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)
        
        # Create a frame inside the canvas
        self.scrollable_frame = ttk.Frame(self.main_canvas)
        self.canvas_window = self.main_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        # Configure scrolling region when frame size changes
        def configure_scroll_region(event=None):
            self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))
            # Wichtig: Canvas-Breite an Frame-Breite anpassen
            canvas_width = self.scrollable_frame.winfo_reqwidth()
            if canvas_width > 10:  # ← Prüfung hinzufügen
                self.main_canvas.itemconfig(self.canvas_window, width=canvas_width)

            # Auto-hide/show scrollbars based on content size
            self.root.update_idletasks()  # Ensure geometry is updated
            
            # Check if vertical scrollbar is needed
            canvas_height = self.main_canvas.winfo_height()
            content_height = self.scrollable_frame.winfo_reqheight()
            if content_height > canvas_height:
                self.v_scrollbar.grid()  # Show vertical scrollbar
            else:
                self.v_scrollbar.grid_remove()  # Hide vertical scrollbar
            
            # Check if horizontal scrollbar is needed
            canvas_width_actual = self.main_canvas.winfo_width()
            content_width = self.scrollable_frame.winfo_reqwidth()
            if content_width > canvas_width_actual:
                self.h_scrollbar.grid()  # Show horizontal scrollbar
            else:
                self.h_scrollbar.grid_remove()  # Hide horizontal scrollbar

        # Speichere als Instanz-Variable für späteren Zugriff
        self._configure_scroll_region = configure_scroll_region
        self.scrollable_frame.bind("<Configure>", self._configure_scroll_region)

        # Auch Canvas-Größe anpassen, wenn Fenster geändert wird
        def on_canvas_configure(event):
            # Setze Mindestbreite auf Canvas-Breite, damit horizontal gefüllt wird
            self.main_canvas.itemconfig(self.canvas_window, width=event.width)

        self.main_canvas.bind("<Configure>", on_canvas_configure)
        
        # Bind mousewheel scrolling (cross-platform)
        def on_mousewheel(event):
            if event.num == 4:  # Linux scroll up
                self.main_canvas.yview_scroll(-1, "units")
            elif event.num == 5:  # Linux scroll down
                self.main_canvas.yview_scroll(1, "units")
            else:  # Windows/Mac
                self.main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        # Recursive bind function
        def bind_mousewheel_recursive(widget):
            widget.bind("<MouseWheel>", on_mousewheel)
            widget.bind("<Button-4>", on_mousewheel)
            widget.bind("<Button-5>", on_mousewheel)
            for child in widget.winfo_children():
                bind_mousewheel_recursive(child)
        
        # Speichere als Instanz-Variable
        self._bind_mousewheel_recursive = bind_mousewheel_recursive
        
        # Make canvas expand with window
        self.root.grid_rowconfigure(0, weight=1)  # Canvas expandiert vertikal
        self.root.grid_rowconfigure(1, weight=0)  # H-Scrollbar bleibt fix
        self.root.grid_rowconfigure(2, weight=0)  # Status Bar bleibt fix
        self.root.grid_columnconfigure(0, weight=1)  # Canvas expandiert horizontal
        self.root.grid_columnconfigure(1, weight=0)  # V-Scrollbar bleibt fix
        
        # Configure columns for scrollable_frame (statt self.root)
        for c in range(3):
            self.scrollable_frame.grid_columnconfigure(c, weight=1, minsize=160)
        #################################

        ### Create top frame and place it with grid (do not mix pack/grid on root)
        self.top_frame = ttk.Frame(self.scrollable_frame, borderwidth=5, relief="ridge", padding=(6, 6), style="Standard.TFrame")
        self.top_frame.grid(row=0, column=0, columnspan=3, padx=PADX, pady=PADY, sticky="new")
    
        # Row 0: basic fields
        widget_entry_long(self.top_frame, "Player Name:", 0, 0, var=self.player_name_var, owner=self, name_label="lbl_player_name", name_entry="entry_player_name")
        widget_entry_long(self.top_frame, "Character Name:", 0, 2, var=self.character_name_var, owner=self, name_label="lbl_character_name", name_entry="entry_character_name")
        widget_combobox(self.top_frame, "Gender:", 0, 4, self.gender_var, ["Male", "Female", "Other"], state="active", owner=self, name_label="lbl_gender", name_combo="cb_gender")
        widget_extlabel_short(self.top_frame, "Level:", 0, 6, var=self.level_var, owner=self, name_label="lbl_level", name_value="entry_level")
        widget_extlabel_short(self.top_frame, "XP-Bonus (%):", 0, 8, var=self.xp_bonus_var, owner=self, name_label="lbl_xp_bonus", name_value="entry_xp_bonus")

        # Row 1
        widget_combobox(self.top_frame, "Profession:", 1, 0, self.profession_var, ["Assassin", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Thief", "Wizard"], state="disabled", owner=self, name_label="lbl_profession", name_combo="cb_profession")
        widget_combobox(self.top_frame, "Race:", 1, 2, self.race_var, list(getattr(self.new_player, "allowed_races", ())), state="disabled", owner=self, name_label="lbl_race", name_combo="cb_race")
        widget_combobox(self.top_frame, "Alignment:", 1, 4, self.alignment_var, ["Good", "Neutral", "Evil"], state="disabled", owner=self, name_label="lbl_alignment", name_combo="cb_alignment")
        widget_extlabel_short(self.top_frame, "XP:", 1, 6, var=self.xp_var, owner=self, name_label="lbl_xp", name_value="entry_xp")
        widget_extlabel_short(self.top_frame, "Next Level (XP):", 1, 8, var=self.nextlevel_var, owner=self, name_label="lbl_nextlevel", name_value="entry_nextlevel")

        # Row 2
        widget_extlabel_short(self.top_frame, "Main Stats:", 2, 0, var=self.main_stats_var, owner=self, name_label="lbl_main_stats", name_value="entry_main_stats")
        widget_entry_long(self.top_frame, "Gottheit:", 2, 2, var=self.god_var, owner=self, name_label="lbl_god", name_entry="entry_god")
        widget_entry_long(self.top_frame, "Alter:", 2, 4, var=self.age_var, owner=self, name_label="lbl_age", name_entry="entry_age")
        widget_spinbox(self.top_frame, "Add XP:", 2, 6, var=self.add_xp_var, owner=self, name_label="lbl_add_xp", name_spinbox="spin_add_xp")
        widget_button(self.top_frame, "Add XP", 2, 7, command=lambda: add_xp(self, self.add_xp_var.get()), owner=self, name_button="btn_add_xp", state="disabled")
 
        ### Attribute frame (use LabelFrame for nicer title)
        self.attr_frame = ttk.LabelFrame(self.scrollable_frame, text="Attribute", borderwidth=5, padding=(6, 6), style="Attention.TFrame")
        self.attr_frame.grid(row=1, column=0, padx=10, pady=10, sticky="new")
        widget_label(self.attr_frame, "Type", 0, 0, owner=self, name_label="lbl_attribute_header")
        widget_label(self.attr_frame, "Rolled", 0, 1, owner=self, name_label="lbl_rolled_stats_header")
        widget_label(self.attr_frame, "Temp", 0, 2, owner=self, name_label="lbl_temp_stats_header")
        widget_label(self.attr_frame, "Total", 0, 3, owner=self, name_label="lbl_total_stats_header")
        widget_extlabel_short(self.attr_frame, "Strength (STR):", 1, 0, var=self.stat_str_var, owner=self, name_label="lbl_str", name_value="entry_str")
        widget_spinbox_nolabel(self.attr_frame, 1, 2, var=self.stat_str_temp_var, owner=self, name_spinbox="spin_str_temp")
        widget_label_var(self.attr_frame, 1, 3, var=self.stat_str_total_var, owner=self, name_value="lbl_str_total")
        widget_extlabel_short(self.attr_frame, "Dexterity (DEX):", 2, 0, var=self.stat_dex_var, owner=self, name_label="lbl_dex", name_value="entry_dex")
        widget_spinbox_nolabel(self.attr_frame, 2, 2, var=self.stat_dex_temp_var, owner=self, name_spinbox="spin_dex_temp")
        widget_label_var(self.attr_frame, 2, 3, var=self.stat_dex_total_var, owner=self, name_value="lbl_dex_total")
        widget_extlabel_short(self.attr_frame, "Constitution (CON):", 3, 0, var=self.stat_con_var, owner=self, name_label="lbl_con", name_value="entry_con")
        widget_spinbox_nolabel(self.attr_frame, 3, 2, var=self.stat_con_temp_var, owner=self, name_spinbox="spin_con_temp")
        widget_label_var(self.attr_frame, 3, 3, var=self.stat_con_total_var, owner=self, name_value="lbl_con_total")
        widget_extlabel_short(self.attr_frame, "Intelligence (INT):", 4, 0, var=self.stat_int_var, owner=self, name_label="lbl_int", name_value="entry_int")
        widget_spinbox_nolabel(self.attr_frame, 4, 2, var=self.stat_int_temp_var, owner=self, name_spinbox="spin_int_temp")
        widget_label_var(self.attr_frame, 4, 3, var=self.stat_int_total_var, owner=self, name_value="lbl_int_total")
        widget_extlabel_short(self.attr_frame, "Wisdom (WIS):", 5, 0, var=self.stat_wis_var, owner=self, name_label="lbl_wis", name_value="entry_wis")
        widget_spinbox_nolabel(self.attr_frame, 5, 2, var=self.stat_wis_temp_var, owner=self, name_spinbox="spin_wis_temp")
        widget_label_var(self.attr_frame, 5, 3, var=self.stat_wis_total_var, owner=self, name_value="lbl_wis_total")
        widget_extlabel_short(self.attr_frame, "Charisma (CHA):", 6, 0, var=self.stat_char_var, owner=self, name_label="lbl_cha", name_value="entry_cha")
        widget_spinbox_nolabel(self.attr_frame, 6, 2, var=self.stat_char_temp_var, owner=self, name_spinbox="spin_cha_temp")
        widget_label_var(self.attr_frame, 6, 3, var=self.stat_char_total_var, owner=self, name_value="lbl_cha_total")

        # place Roll Stats button inside attr_frame
        self.btn_roll_stats = ttk.Button(self.attr_frame, text="Roll Stats", style="Attention.TButton", command=lambda: role_stats(self, self.new_player, self.chk_opt_4d6dl_var.get(), self.btn_roll_stats, self.btn_switch_stats))
        self.btn_roll_stats.grid(row=7, column=0, sticky="ew", padx=PADX, pady=PADY)

        ### Homebrew frame (use LabelFrame for nicer title)
        self.attr_homebrew_frame = ttk.LabelFrame(self.attr_frame, text="Homebrew", borderwidth=5, padding=(6, 6), style="Standard.TFrame")
        self.attr_homebrew_frame.grid(row=8, column=0, padx=PADX, pady=PADY, sticky="nsew")

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

        ### Bonuses frame
        self.bonus_frame = ttk.LabelFrame(self.scrollable_frame, text="Attribute Bonuses", borderwidth=5, padding=(6, 6), style="Standard.TFrame")
        self.bonus_frame.grid(row=1, column=1, padx=PADX, pady=PADY, sticky="new")

        # Create bonus labels and values
        widget_label(self.bonus_frame, "Type", 0, 0, owner=self, name_label="lbl_bonus_type_header")
        widget_label(self.bonus_frame, "Temp", 0, 1, owner=self, name_label="lbl_bonus_temp_bonus_header")
        widget_label(self.bonus_frame, "Total", 0, 2, owner=self, name_label="lbl_bonus_total_header")

        #widget_extlabel_short(self.bonus_frame, "Melee Attack Bonus:", 1, 0, var=self.strength_atck_mod_var, owner=self, name_label="lbl_strength_atck_bonus", name_value="entry_strength_atck_bonus")
        widget_label(self.bonus_frame, "Melee Attack:", 1, 0, owner=self, name_label="lbl_strength_atck_bonus")
        widget_spinbox_nolabel(self.bonus_frame, 1, 1, var=self.strength_atck_mod_temp_var, owner=self, name_spinbox="spin_strength_atck_temp_bonus")
        widget_label_var(self.bonus_frame, 1, 2, var=self.strength_atck_mod_total_var, owner=self, name_value="lbl_strength_atck_total_bonus")

        #widget_extlabel_short(self.bonus_frame, "Melee Damage Bonus:", 2, 0, var=self.strength_damage_mod_var, owner=self, name_label="lbl_strength_damage_bonus", name_value="entry_strength_damage_bonus")
        widget_label(self.bonus_frame, "Melee Damage:", 2, 0, owner=self, name_label="lbl_strength_damage_bonus")
        widget_spinbox_nolabel(self.bonus_frame, 2, 1, var=self.strength_damage_mod_temp_var, owner=self, name_spinbox="spin_strength_damage_temp_bonus")
        widget_label_var(self.bonus_frame, 2, 2, var=self.strength_damage_mod_total_var, owner=self, name_value="lbl_strength_damage_total_bonus")

        #widget_extlabel_short(self.bonus_frame, "Ranged Attack Bonus:", 3, 0, var=self.ranged_atck_mod_var, owner=self, name_label="lbl_ranged_atk_bonus", name_value="entry_ranged_atk_bonus")
        widget_label(self.bonus_frame, "Ranged Attack:", 3, 0, owner=self, name_label="lbl_ranged_atk_bonus")
        widget_spinbox_nolabel(self.bonus_frame, 3, 1, var=self.ranged_atck_mod_temp_var, owner=self, name_spinbox="spin_ranged_atk_temp_bonus")
        widget_label_var(self.bonus_frame, 3, 2, var=self.ranged_atck_mod_total_var, owner=self, name_value="lbl_ranged_atk_total_bonus")

        #widget_extlabel_short(self.bonus_frame, "Armor Class Bonus:", 4, 0, var=self.ac_mod_var, owner=self, name_label="lbl_ac_bonus", name_value="entry_ac_bonus")
        widget_label(self.bonus_frame, "Armor Class:", 4, 0, owner=self, name_label="lbl_ac_bonus")
        widget_spinbox_nolabel(self.bonus_frame, 4, 1, var=self.ac_mod_temp_var, owner=self, name_spinbox="spin_ac_temp_bonus")
        widget_label_var(self.bonus_frame, 4, 2, var=self.ac_total_var, owner=self, name_value="lbl_ac_total_bonus")

        #widget_extlabel_short(self.bonus_frame, "Carry Capacity Bonus:", 6, 0, var=self.carry_capacity_mod_var, owner=self, name_label="lbl_carry_capacity_bonus", name_value="entry_carry_capacity_bonus")
        widget_label(self.bonus_frame, "Carry Capacity (%):", 6, 0, owner=self, name_label="lbl_carry_capacity_bonus")
        widget_label_var(self.bonus_frame, 6, 2, var=self.carry_capacity_mod_var, owner=self, name_value="lbl_carry_capacity_total_bonus")
        
        #widget_extlabel_short(self.bonus_frame, "Crack Doors (x:6):", 7, 0, var=self.door_crack_mod_var, owner=self, name_label="lbl_door_crack_bonus", name_value="entry_door_crack_bonus")
        widget_label(self.bonus_frame, "Crack Doors (x:6):", 7, 0, owner=self, name_label="lbl_door_crack_bonus")
        widget_label_var(self.bonus_frame, 7, 2, var=self.door_crack_mod_var, owner=self, name_value="lbl_door_crack_total_bonus")

        #widget_extlabel_short(self.bonus_frame, "HP Bonus:", 8, 0, var=self.hp_mod_var, owner=self, name_label="lbl_hp_bonus", name_value="entry_hp_bonus")
        widget_label(self.bonus_frame, "HP Bonus:", 8, 0, owner=self, name_label="lbl_hp_bonus")
        widget_label_var(self.bonus_frame, 8, 2, var=self.hp_mod_var, owner=self, name_value="lbl_hp_total_bonus")

        #widget_extlabel_short(self.bonus_frame, "Raise Dead Modifier (%):", 9, 0, var=self.raise_dead_mod_var, owner=self, name_label="lbl_raise_dead_mod", name_value="entry_raise_dead_mod")
        widget_label(self.bonus_frame, "Raise Dead Mod (%):", 9, 0, owner=self, name_label="lbl_raise_dead_mod")
        widget_label_var(self.bonus_frame, 9, 2, var=self.raise_dead_mod_var, owner=self, name_value="lbl_raise_dead_total_mod")

        #widget_extlabel_short(self.bonus_frame, "Special Hirelings Cap:", 10, 0, var=self.cap_spec_hirelings_var, owner=self, name_label="lbl_cap_spec_hirelings", name_value="entry_cap_spec_hirelings")
        widget_label(self.bonus_frame, "Special Hirelings Cap:", 10, 0, owner=self, name_label="lbl_cap_spec_hirelings")
        widget_label_var(self.bonus_frame, 10, 2, var=self.cap_spec_hirelings_var, owner=self, name_value="lbl_cap_spec_hirelings_total")

        #widget_extlabel_short(self.bonus_frame, "Parry:", 11, 0, var=self.parry_var, owner=self, name_label="lbl_parry", name_value="entry_parry")
        widget_label(self.bonus_frame, "Parry:", 11, 0, owner=self, name_label="lbl_parry")
        widget_label_var(self.bonus_frame, 11, 2, var=self.parry_var, owner=self, name_value="lbl_parry_total") 

        ### Stats / Other panels
        self.stats_frame = ttk.LabelFrame(self.scrollable_frame, text="Stats / Derived", borderwidth=5, padding=(6, 6), style="Standard.TFrame")
        self.stats_frame.grid(row=1, column=2, padx=PADX, pady=PADY, sticky="new")

        # Create stat labels and values
        widget_extlabel_short(self.stats_frame, "Hit Points max.:", 0, 0, var=self.hp_var, owner=self, name_label="lbl_hp", name_value="entry_hp")
        widget_checkbutton(self.stats_frame, "Full TP on Level 1", 0, 2, self.chk_opt_fullhplvl1_var, owner=self, name_checkbutton="chk_opt_fullhplvl1")
        widget_button(self.stats_frame, "Roll HP", 0, 4, command=lambda: set_starting_hp(self, self.new_player), state="disabled", owner=self, name_button="btn_rollhp")
        widget_extlabel_short(self.stats_frame, "Hit Points current:", 1, 0, var=self.hp_current_var, owner=self, name_label="lbl_hp_current", name_value="entry_hp_current")
        widget_spinbox(self.stats_frame, "Modify HP by:", 1, 2, var=self.hp_modify_var, owner=self, name_label="lbl_modify_hp", name_spinbox="spin_modify_hp")
        widget_button(self.stats_frame, "Modify HP", 1, 4, command=lambda: modify_hp(self.hp_modify_var.get(), self, self.new_player), state="disabled", owner=self, name_button="btn_modify_hp")
        widget_extlabel_short(self.stats_frame, "State:", 2, 0, var=self.player_state_var, owner=self, name_label="lbl_player_state", name_value="entry_player_state")
        widget_extlabel_short(self.stats_frame, "Saving Throw:", 3, 0, var=self.save_throw_var, owner=self, name_label="lbl_save_throw", name_value="entry_save_throw")
        widget_extlabel_short(self.stats_frame, "Darkvision:", 5, 0, var=self.darkvision_var, owner=self, name_label="lbl_darkvision", name_value="entry_darkvision")
        widget_extlabel_short(self.stats_frame, "Languages:", 6, 0, var=self.languages_var, owner=self, name_label="lbl_languages", name_value="entry_languages")
        widget_extlabel_short(self.stats_frame, "Max. add. Languages:", 7, 0, var=self.max_add_langs_var, owner=self, name_label="lbl_max_additional_languages", name_value="entry_max_additional_languages")
        widget_entry_long(self.stats_frame, "", 7, 1, columnspan=4, var=self.additional_languages_var, owner=self, name_label="lbl_additional_languages", name_entry="entry_additional_languages")

        # Save Bonuses
        widget_label(self.stats_frame, "Save Bonuses:", 8, 0, owner=self, name_label="lbl_save_bonuses")
        # Use scrolledtext for save bonuses
        self.save_bonuses_txt = scrolledtext.ScrolledText(
        self.stats_frame,
        wrap="word",
        height=5,        # visible row height (can be adjusted)
        width=40,        # visible column width (char-based)
        font=("TkDefaultFont", 10),
        state="normal"
        )
        self.save_bonuses_txt.grid(row=8, column=1, columnspan=5, sticky="nsew", padx=PADX, pady=PADY)

        # Immunities
        widget_label(self.stats_frame, "Immunities:", 9, 0, owner=self, name_label="lbl_immunities")
        
        # Use scrolledtext for immunities
        self.immunities_txt = scrolledtext.ScrolledText(
        self.stats_frame,
        wrap="word",
        height=3,        # visible row height (can be adjusted)
        width=40,        # visible column width (char-based)
        font=("TkDefaultFont", 10),
        state="normal"
        )
        self.immunities_txt.grid(row=9, column=1, columnspan=5, sticky="nsew", padx=PADX, pady=PADY)

        ### Create a notebook for lower panels
        self.lower_notebook = ttk.Notebook(self.scrollable_frame)
        self.lower_notebook.grid(row=2, column=0, columnspan=3, padx=PADX, pady=PADY, sticky="new")
        # Create frames for each tab
        self.thief_frame = ttk.Frame(self.lower_notebook)
        self.weapons_frame = ttk.Frame(self.lower_notebook)
        self.inventory_frame = ttk.Frame(self.lower_notebook)
        self.magic_frame = ttk.Frame(self.lower_notebook)
        self.special_abilities_frame = ttk.Frame(self.lower_notebook)
        self.coins_frame = ttk.Frame(self.lower_notebook)
        # Add tabs to the notebook
        self.lower_notebook.add(self.thief_frame, text="Thief Skills", state="disabled")
        self.lower_notebook.add(self.weapons_frame, text="Weapons & Armor", state="normal")
        self.lower_notebook.add(self.inventory_frame, text="Inventory", state="normal")
        self.lower_notebook.add(self.coins_frame, text="Coins", state="normal")
        self.lower_notebook.add(self.magic_frame, text="Magic", state="disabled")
        self.lower_notebook.add(self.special_abilities_frame, text="Special Abilities", state="normal")

        ### Thief skills Tab/Frame
        self.thief_content_frame = ttk.LabelFrame(self.thief_frame, text="Thief Skills", borderwidth=5, padding=(6, 6), style="Standard.TFrame")
        self.thief_content_frame.grid(row=0, column=0, padx=PADX, pady=PADY, sticky="new")
  
        # Create thief skill labels and values
        widget_extlabel_short(self.thief_content_frame, "Delicate Tasks:", 0, 0, var=self.delicate_tasks_var, owner=self, name_label="lbl_delicate_tasks", name_value="entry_delicate_tasks")
        widget_extlabel_short(self.thief_content_frame, "Climb Walls:", 1, 0, var=self.climb_walls_var, owner=self, name_label="lbl_climb_walls", name_value="entry_climb_walls")
        widget_extlabel_short(self.thief_content_frame, "Hear Sounds:", 2, 0, var=self.hear_sounds_var, owner=self, name_label="lbl_hear_sounds", name_value="entry_hear_sounds")
        widget_extlabel_short(self.thief_content_frame, "Hide in Shadows:", 3, 0, var=self.hide_in_shadows_var, owner=self, name_label="lbl_hide_in_shadows", name_value="entry_hide_in_shadows")
        widget_extlabel_short(self.thief_content_frame, "Move Silently:", 4, 0, var=self.move_silently_var, owner=self, name_label="lbl_move_silently", name_value="entry_move_silently")
        widget_extlabel_short(self.thief_content_frame, "Open Locks:", 5, 0, var=self.open_locks_var, owner=self, name_label="lbl_open_locks", name_value="entry_open_locks")

        ### Weapons & Armor Tab/Frame
        self.weapons_content_frame = ttk.LabelFrame(self.weapons_frame, text="Weapons & Armor", borderwidth=5, padding=(6,6), style="Standard.TFrame")
        self.weapons_content_frame.grid(row=0, column=0, padx=PADX, pady=PADY, sticky="new")

        # Row 0: Combobox for Armor
        widget_combobox(self.weapons_content_frame, "Select Armor:", 0, 0, self.armor_var, [], state="readonly", owner=self, name_label="lbl_select_armor", name_combo="cb_armor", width=40)
        

        # Row 1: Combobox for Main Hand
        widget_combobox(self.weapons_content_frame, "Select Main Hand Weapon:", 1, 0, self.main_hand_var, [], state="readonly", owner=self, name_label="lbl_select_main_hand", name_combo="cb_main_hand", width=40)


        # Row 2: Combobox for Off Hand
        widget_combobox(self.weapons_content_frame, "Select Off Hand Item:", 2, 0, self.off_hand_var, [], state="readonly", owner=self, name_label="lbl_select_off_hand", name_combo="cb_off_hand", width=40)

        # ← HINZUGEFÜGT: Row 3: Equip Button
        widget_button(self.weapons_content_frame, "Equip Selected Items", 3, 0, command=lambda: self.on_equip_click(), owner=self, name_button="btn_equip")
    
        ### Inventory Tab/Frame
        self.inventory_content_frame = ttk.LabelFrame(self.inventory_frame, text="Inventory", borderwidth=5, padding=(6,6), style="Standard.TFrame")
        self.inventory_content_frame.grid(row=0, column=0, padx=PADX, pady=PADY, sticky="new")



       # Treeview für Item-Liste
        self.inventory_tree = ttk.Treeview(
            self.inventory_frame,
            columns=("Name", "Type", "Weight", "Value", "Quantity"),
            show="headings",
            height=15
        )
        self.inventory_tree.heading("Name", text="Item Name")
        self.inventory_tree.heading("Type", text="Type")
        self.inventory_tree.heading("Weight", text="Weight")
        self.inventory_tree.heading("Value", text="Value")
        self.inventory_tree.heading("Quantity", text="Qty")

        self.inventory_tree.column("Name", width=200)
        self.inventory_tree.column("Type", width=100)
        self.inventory_tree.column("Weight", width=80)
        self.inventory_tree.column("Value", width=80)
        self.inventory_tree.column("Quantity", width=60)

        self.inventory_tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Scrollbar
        inventory_scrollbar = ttk.Scrollbar(
            self.inventory_frame,
            orient="vertical",
            command=self.inventory_tree.yview
        )
        inventory_scrollbar.grid(row=0, column=1, sticky="ns")
        self.inventory_tree.configure(yscrollcommand=inventory_scrollbar.set)

        # Buttons
        btn_frame = ttk.Frame(self.inventory_frame)
        btn_frame.grid(row=1, column=0, columnspan=2, pady=10)

        ttk.Button(btn_frame, text="Add Item", command=lambda: open_add_item_dialog(self)).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Remove Item", command=self.remove_selected_item).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Edit Item", command=lambda: on_edit_item_click(self, self.inventory_tree)).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Refresh", command=self.refresh_inventory_display).pack(side="left", padx=5)

        # Weight/Value Summary
        self.inventory_summary_label = ttk.Label(
            self.inventory_frame,
            text="Total Weight: 0.0 | Total Value: 0 GM"
        )
        self.inventory_summary_label.grid(row=2, column=0, columnspan=2, pady=5)

        ### Coins Frame Tab/Frame
        self.coins_content_frame = ttk.LabelFrame(self.coins_frame, text="Coins", borderwidth=5, padding=(6,6), style="Standard.TFrame")
        self.coins_content_frame.grid(row=0, column=0, columnspan=6, padx=PADX, pady=PADY, sticky="new")

        widget_extlabel_short(self.coins_content_frame, "Platinum:", 0, 0, var=self.coins_platinum_var, owner=self, name_label="lbl_coins_platinum", name_value="entry_coins_platinum")
        widget_spinbox(self.coins_content_frame, "Modify Platinum:", 0, 2, var=self.coins_platinum_mod_var, owner=self, name_label="lbl_coins_platinum_mod", name_spinbox="spin_coins_platinum_mod")
        widget_extlabel_short(self.coins_content_frame, "Gold:", 1, 0, var=self.coins_gold_var, owner=self, name_label="lbl_coins_gold", name_value="entry_coins_gold")
        widget_spinbox(self.coins_content_frame, "Modify Gold:", 1, 2, var=self.coins_gold_mod_var, owner=self, name_label="lbl_coins_gold_mod", name_spinbox="spin_coins_gold_mod")
        widget_extlabel_short(self.coins_content_frame, "Electrum:", 2, 0, var=self.coins_electrum_var, owner=self, name_label="lbl_coins_electrum", name_value="entry_coins_electrum")
        widget_spinbox(self.coins_content_frame, "Modify Electrum:", 2, 2, var=self.coins_electrum_mod_var, owner=self, name_label="lbl_coins_electrum_mod", name_spinbox="spin_coins_electrum_mod")
        widget_extlabel_short(self.coins_content_frame, "Silver:", 3, 0, var=self.coins_silver_var, owner=self, name_label="lbl_coins_silver", name_value="entry_coins_silver")
        widget_spinbox(self.coins_content_frame, "Modify Silver:", 3, 2, var=self.coins_silver_mod_var, owner=self, name_label="lbl_coins_silver_mod", name_spinbox="spin_coins_silver_mod")
        widget_extlabel_short(self.coins_content_frame, "Copper:", 4, 0, var=self.coins_copper_var, owner=self, name_label="lbl_coins_copper", name_value="entry_coins_copper")
        widget_spinbox(self.coins_content_frame, "Modify Copper:", 4, 2, var=self.coins_copper_mod_var, owner=self, name_label="lbl_coins_copper_mod", name_spinbox="spin_coins_copper_mod")
        widget_button(self.coins_content_frame, "Modify Coins", 5, 2, command=lambda: modify_coins(self), owner=self, name_button="btn_modify_coins")

        ### Magic Tab/Frame
        self.magic_content_frame = ttk.LabelFrame(self.magic_frame, text="Spell Attributes", borderwidth=5, padding=(6,6), style="Standard.TFrame")
        self.magic_content_frame.grid(row=0, column=0, padx=PADX, pady=PADY, sticky="new")

        widget_extlabel_short(self.magic_content_frame, "Highest Spell Level:", 0, 0, var=self.highest_spell_level_var, owner=self, name_label="lbl_highest_spell_level", name_value="entry_highest_spell_level")
        widget_extlabel_short(self.magic_content_frame, "Understands Spells (%):", 1, 0, var=self.understand_spell_var, owner=self, name_label="lbl_understand_spell", name_value="entry_understand_spell")
        widget_extlabel_short(self.magic_content_frame, "Min. Spells to Memorize:", 2, 0, var=self.min_spells_per_level_var, owner=self, name_label="lbl_min_spell_level", name_value="entry_min_spell_level")
        widget_extlabel_short(self.magic_content_frame, "Max. Spells to Memorize:", 3, 0, var=self.max_spells_per_level_var, owner=self, name_label="lbl_max_spell_level", name_value="entry_max_spell_level")

        # Create spell table widget
        create_spell_table_widget(self)

        ### Special Abilities Tab/Frame
        self.special_abilities_content_frame = ttk.LabelFrame(self.special_abilities_frame, text="Special Abilities", borderwidth=5, padding=(6,6), style="Standard.TFrame")
        self.special_abilities_content_frame.grid(row=0, column=0, padx=PADX, pady=PADY, sticky="new")

        # Special Abilities
        widget_label(self.special_abilities_content_frame, "Special Abilities:", 0, 0, owner=self, name_label="lbl_special_abilities")

        # Use scrolledtext for special abilities
        self.special_abilities_txt = scrolledtext.ScrolledText(
        self.special_abilities_content_frame,
        wrap="word",
        height=10,        # visible row height (can be adjusted)
        width=150,        # visible column width (char-based)
        font=("TkDefaultFont", 10),
        state="normal"
        )
        self.special_abilities_txt.grid(row=0, column=1, sticky="new", padx=PADX, pady=PADY)

        ### Footerframe 
        self.footer_frame = ttk.Frame(self.scrollable_frame, borderwidth=5, padding=(6,6), style="Standard.TFrame")
        self.footer_frame.grid(row=3, column=0, columnspan=3, padx=PADX, pady=PADY, sticky="new")

        # place Save / Load buttons inside footer_frame on a new row so they're visually nearby
        self.btn_new = ttk.Button(self.footer_frame, text="New", command=lambda: new_characterobj(self))
        self.btn_new.grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
        self.btn_apply = ttk.Button(self.footer_frame, text="Apply", command=lambda: apply_character(self, self.new_player))
        self.btn_apply.grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)
        self.btn_save = ttk.Button(self.footer_frame, text="Save", command=self.on_save_click)
        self.btn_save.grid(row=0, column=2, sticky="w", padx=PADX, pady=PADY)
        self.btn_load = ttk.Button(self.footer_frame, text="Load", command=self.on_load_click)
        self.btn_load.grid(row=0, column=3, sticky="w", padx=PADX, pady=PADY)
        self.btn_dice_roller = ttk.Button(self.footer_frame, text="Dice Roller", command=lambda: dice_roller(self))
        self.btn_dice_roller.grid(row=0, column=4, sticky="w", padx=PADX, pady=PADY)
        self.btn_exit = ttk.Button(self.footer_frame, text="Exit", command=lambda: messagebox.askokcancel("Exit", "Do you really want to exit?", parent=self.root) and self.root.destroy())
        self.btn_exit.grid(row=0, column=6, sticky="e", padx=PADX, pady=PADY)

        # Configure column 5 to expand and push Exit button to the right
        self.footer_frame.grid_columnconfigure(5, weight=1) # spacer column

        ### Status bar at the very bottom (OUTSIDE scrollable_frame)
        # row=2: we want it below the canvas (row=0) and h-scrollbar (row=1)
        # columnspan=2: span both columns (canvas and v-scrollbar)
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief="sunken", anchor="w", padding=(4,4))
        self.status_bar.grid(row=2, column=0, columnspan=2, sticky="ew")  # ← self.root statt self.scrollable_frame
        # ----------------- configure resizing behavior -----------------

        # Make scrollable_frame rows expand
        self.scrollable_frame.grid_rowconfigure(0, weight=0)  # Top frame
        self.scrollable_frame.grid_rowconfigure(1, weight=0)  # Attribute/Bonus/Stats row
        self.scrollable_frame.grid_rowconfigure(2, weight=1)  # Notebook row
        self.scrollable_frame.grid_rowconfigure(3, weight=0)  # Footer row

        # Initial scroll region setup NACH UI-Aufbau
        self.root.after(100, lambda: (
            self._configure_scroll_region(),
            self._bind_mousewheel_recursive(self.scrollable_frame)
        ))

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

    def on_save_click(self):
        """Handle Save Character button click."""
        print("DEBUG on_save_click: --------------------------------")
        try:
            save_character(self.new_player, parent_window=self.root)
            self.status_var.set("Character saved successfully.")
        except Exception as e:
            self.status_var.set(f"Error saving character: {e}")
            print(f"ERROR on_save_click: {e}")

    def on_load_click(self):
        """Handle Load Character button click."""
        print("DEBUG on_load_click: --------------------------------")
        try:
            # Ask user for file
            loaded_character = load_character(parent_window=self.root)
            
            if loaded_character is None:
                self.status_var.set("Load cancelled.")
                return
            
            # Replace current character
            self.new_player = loaded_character
            
            # Update GUI
            with self.suppress_updates():
                update_view_from_model(self)
            
            self.status_var.set("Character loaded successfully.")
        except Exception as e:
            self.status_var.set(f"Error loading character: {e}")
            print(f"ERROR on_load_click: {e}")

    def rebuild_ui(self):
        """Zerstört alle Kinder der Root und baut UI neu auf."""
        for child in self.root.winfo_children():
            child.destroy()

        # Build UI again
        print("DEBUG rebuild_ui: Re-building UI")
        self._build_ui()


    def _safe_update_equipment(self):
        """Safely update equipment comboboxes."""
        print("DEBUG: _safe_update_equipment called")
        try:
            update_equipment_comboboxes(self)
            print("DEBUG: Equipment comboboxes updated")
        except Exception as e:
            print(f"ERROR: Failed to update equipment comboboxes: {e}")
            traceback.print_exc()

    # ← HINZUGEFÜGT: Neue Methode für Equip-Button
    def on_equip_click(self):
        """Handle Equip Button click."""
        print("DEBUG on_equip_click: ------------------------------------------------")
        # Hole ausgewählte Items
        armor_name = self.armor_var.get()
        main_hand_name = self.main_hand_var.get()
        off_hand_name = self.off_hand_var.get()
        
        print(f"DEBUG: Selected - Armor: '{armor_name}', Main: '{main_hand_name}', Off: '{off_hand_name}'")
        
        # Equip Armor
        if armor_name and armor_name != "":
            print(f"DEBUG: Equipping armor: {armor_name}")
            equip_item(self, "armor", armor_name)
        
        # Equip Main Hand
        if main_hand_name and main_hand_name != "":
            print(f"DEBUG: Equipping main hand: {main_hand_name}")
            equip_item(self, "main_hand", main_hand_name)
        
        # Equip Off Hand
        if off_hand_name and off_hand_name != "":
            print(f"DEBUG: Equipping off hand: {off_hand_name}")
            equip_item(self, "off_hand", off_hand_name)
        
        # Update AC
        print("DEBUG: Updating AC after equipping")
        update_armor_ac(self.new_player)
        calculate_ac(self.new_player)
        
        # Update GUI
        with self.suppress_updates():
            update_view_from_model(self)
        
        self.status_var.set("Equipment updated successfully")
        print("DEBUG on_equip_click: DONE ------------------------------------------------")

    
    def refresh_inventory_display(self):
        """Refresh the inventory treeview."""
        print("DEBUG refresh_inventory_display called: --------------------------------")
        # Clear current display
        for item in self.inventory_tree.get_children():
            self.inventory_tree.delete(item)
        
        # Count items
        item_counts = {}
        for item in self.new_player.inventory_items:
            if item.name in item_counts:
                item_counts[item.name]["count"] += 1
            else:
                item_counts[item.name] = {
                    "item": item,
                    "count": 1
                }
        
        # Display items
        total_weight = 0.0
        total_value = 0
        
        for item_name, data in item_counts.items():
            item = data["item"]
            count = data["count"]
            
            self.inventory_tree.insert("", "end", values=(
                item.name,
                item.type,
                f"{item.weight * count:.1f}",
                item.value,
                count
            ))
            
            total_weight += item.weight * count
            # Parse value (assuming format "X GM")
            try:
                value_num = int(item.value.split()[0])
                total_value += value_num * count
            except:
                pass
        
        # Update summary
        self.inventory_summary_label.config(
            text=f"Total Weight: {total_weight:.1f} | Total Value: {total_value} GM | Items: {len(self.new_player.inventory_items)}"
        )

        # Update Equipment Comboboxen
        update_equipment_comboboxes(self)

    def remove_selected_item(self):
        """Remove the selected item from inventory."""
        print("DEBUG remove_selected_item called: --------------------------------")
        selection = self.inventory_tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select an item to remove.")
            return
        
        item_data = self.inventory_tree.item(selection[0])
        item_name = item_data["values"][0]
        
        # Find and remove the first matching item
        for item in self.new_player.inventory_items:
            if item.name == item_name:
                self.new_player.inventory_items.remove(item)
                break
        
        self.refresh_inventory_display()
        messagebox.showinfo("Success", f"Removed {item_name}")

    # ----------------- run -----------------
    def run(self):
        """Run the main Tk event loop."""
        self.root.mainloop()


# Backwards-compatibility helper used by main.py
def start_gui():
    """Start the GUI application (for backwards compatibility)."""
    App().run()
