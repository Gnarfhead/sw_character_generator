"""GUI application for the Swords & Wizardry character generator."""
import tkinter as tk
import tkinter.ttk as ttk

from sw_character_generator.classes.playerclass import PlayerClass

# Layout / sizing constants
ROOT_MIN_W = 900
ROOT_MIN_H = 600
LABEL_MIN_W = 120
VALUE_MIN_W = 160
ENTRY_WIDTH = 20
PADX = 8
PADY = 6

def _label_entry(parent, text, row, column, var=None, widget="entry", width=ENTRY_WIDTH, columnspan=1, **grid_opts):
    """Helper to create a label + entry/combobox and grid them neatly.
    - parent: parent widget
    - text: label text
    - row, column: position for label (value placed at column+1 by default)
    - widget: "entry" or "combobox"
    - width: widget width in characters
    - columnspan: how many columns the value widget should span (starting at column+1)
    """
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

def start_gui():
    """Start the GUI for the character generator."""
    root = tk.Tk()
    root.title("Swords & Wizardry Charaktergenerator")

    # sensible minimum size so the layout doesn't collapse
    root.minsize(ROOT_MIN_W, ROOT_MIN_H)

    # Make root use grid for all direct children and allow columns to expand
    # Set minsize for columns to give each column a useful minimum width and make value columns expand.
    for c in range(3):
        root.grid_columnconfigure(c, weight=1, minsize=VALUE_MIN_W)

    # Create top frame and place it with grid (do not mix pack/grid on root)
    top_frame = ttk.Frame(root, borderwidth=5, relief="ridge", padding=(6,6))
    top_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    # Configure top_frame columns for a responsive layout (6 logical columns: label/value pairs)
    # We'll set label (even) columns to small minsize and value (odd) columns to be expandable.
    for c in range(6):
        # label columns 0,2,4 -> small, value columns 1,3,5 -> expand
        if c % 2 == 0:
            top_frame.grid_columnconfigure(c, weight=0, minsize=LABEL_MIN_W)
        else:
            top_frame.grid_columnconfigure(c, weight=1, minsize=VALUE_MIN_W)

    # Use StringVars so values can be updated later
    player_var = tk.StringVar(value="Undefined Player")
    character_var = tk.StringVar(value="Undefined Character")
    level_var = tk.StringVar(value="1")
    profession_var = tk.StringVar(value="Unbekannt")
    race_var = tk.StringVar(value="Unbekannt")
    gender_var = tk.StringVar(value="Unbekannt")
    alignment_var = tk.StringVar(value="Unbekannt")
    god_var = tk.StringVar(value="Unbekannt")
    age_var = tk.StringVar(value="Unbekannt")
    xp_bonus_var = tk.StringVar(value="0")
    xp_var = tk.StringVar(value="0")
    main_stats_var = tk.StringVar(value="STR DEX CON INT WIS CHA")
    stat_str_var = tk.StringVar(value="0")
    stat_dex_var = tk.StringVar(value="0")
    stat_con_var = tk.StringVar(value="0")
    stat_int_var = tk.StringVar(value="0")
    stat_wis_var = tk.StringVar(value="0")
    stat_cha_var = tk.StringVar(value="0")

    # Row 0: use columnspan for entries where appropriate so they remain usable on narrow windows
    _label_entry(top_frame, "Spieler:in:", 0, 0, var=player_var, columnspan=1)
    _label_entry(top_frame, "SC Name:", 0, 2, var=character_var, columnspan=1)
    ttk.Label(top_frame, text="Level:").grid(row=0, column=4, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(top_frame, textvariable=level_var).grid(row=0, column=5, sticky="w", padx=PADX, pady=PADY)

    # Row 1
    _label_entry(top_frame, "Profession:", 1, 0, var=profession_var, widget="combobox")
    # configure values for last created child (combobox)
    # safer: keep a reference from the helper if needed; here we access the children directly
    profession_cb = top_frame.grid_slaves(row=1, column=1)[0]
    profession_cb.config(values=["Fighter", "Cleric", "Thief", "Wizard", "Ranger", "Paladin"])
    _label_entry(top_frame, "Rasse:", 1, 2, var=race_var, widget="combobox")
    race_cb = top_frame.grid_slaves(row=1, column=3)[0]
    race_cb.config(values=["Human", "Elf", "Dwarf", "Halfling", "Halfelf"])
    _label_entry(top_frame, "Geschlecht:", 1, 4, var=gender_var)

    # Row 2
    _label_entry(top_frame, "Gesinnung:", 2, 0, var=alignment_var, widget="combobox")
    align_cb = top_frame.grid_slaves(row=2, column=1)[0]
    align_cb.config(values=["Good", "Neutral", "Evil"])
    _label_entry(top_frame, "Gottheit:", 2, 2, var=god_var)
    _label_entry(top_frame, "Alter:", 2, 4, var=age_var)

    # Row 3 - main stats and XP; make main_stats span two columns so it doesn't wrap too early
    ttk.Label(top_frame, text="Main Stats:").grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(top_frame, textvariable=main_stats_var).grid(row=3, column=1, columnspan=1, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(top_frame, text="EP-Bonus (%):").grid(row=3, column=2, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(top_frame, textvariable=xp_bonus_var).grid(row=3, column=3, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(top_frame, text="EP:").grid(row=3, column=4, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(top_frame, textvariable=xp_var).grid(row=3, column=5, sticky="w", padx=PADX, pady=PADY)

    # Attribute frame (use LabelFrame for nicer title)
    attr_frame = ttk.LabelFrame(root, text="Attribute", borderwidth=5, padding=(6,6))
    attr_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    # label/value columns and their responsiveness
    attr_frame.grid_columnconfigure(0, weight=0, minsize=LABEL_MIN_W)
    attr_frame.grid_columnconfigure(1, weight=1, minsize=VALUE_MIN_W)

    # Create stat variables and place them with grid
    ttk.Label(attr_frame, text="Strength (STR):").grid(row=0, column=0, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(attr_frame, textvariable=stat_str_var).grid(row=0, column=1, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(attr_frame, text="Dexterity (DEX):").grid(row=1, column=0, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(attr_frame, textvariable=stat_dex_var).grid(row=1, column=1, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(attr_frame, text="Constitution (CON):").grid(row=2, column=0, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(attr_frame, textvariable=stat_con_var).grid(row=2, column=1, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(attr_frame, text="Intelligence (INT):").grid(row=3, column=0, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(attr_frame, textvariable=stat_int_var).grid(row=3, column=1, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(attr_frame, text="Wisdom (WIS):").grid(row=4, column=0, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(attr_frame, textvariable=stat_wis_var).grid(row=4, column=1, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(attr_frame, text="Charisma (CHA):").grid(row=5, column=0, sticky="w", padx=PADX, pady=PADY)
    ttk.Label(attr_frame, textvariable=stat_cha_var).grid(row=5, column=1, sticky="w", padx=PADX, pady=PADY)
    
    # Bonuses frame
    bonus_frame = ttk.LabelFrame(root, text="Attribute Bonuses", borderwidth=5, padding=(6,6))
    bonus_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
    bonus_frame.grid_columnconfigure(0, weight=0, minsize=LABEL_MIN_W)
    bonus_frame.grid_columnconfigure(1, weight=1, minsize=VALUE_MIN_W)

    bonus_labels = [
        "Melee Attack Bonus:", "Melee Damage Bonus:", "Carry Capacity Bonus:",
        "Door Crack Bonus:", "Ranged Attack Bonus:", "AC Bonus:", "TP Bonus:",
        "Raise Dead Modifier:", "Max Additional Languages:", "Special Hirelings Cap:"
    ]
    bonus_vars = [tk.StringVar(value="0") for _ in bonus_labels]
    for i, (lbl_text, var) in enumerate(zip(bonus_labels, bonus_vars), start=1):
        ttk.Label(bonus_frame, text=lbl_text).grid(row=i, column=0, sticky="w", padx=PADX, pady=PADY)
        ttk.Label(bonus_frame, textvariable=var).grid(row=i, column=1, sticky="w", padx=PADX, pady=PADY)

    # Stats / Other panels
    stats_frame = ttk.LabelFrame(root, text="Stats / Derived", borderwidth=5, padding=(6,6))
    stats_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
    stats_frame.grid_columnconfigure(0, weight=1)

    thief_frame = ttk.LabelFrame(root, text="Thief Skills", borderwidth=5, padding=(6,6))
    thief_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    weapons_frame = ttk.LabelFrame(root, text="Weapons", borderwidth=5, padding=(6,6))
    weapons_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    armor_frame = ttk.LabelFrame(root, text="Armor", borderwidth=5, padding=(6,6))
    armor_frame.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

    # Make lower rows/frames expand when window is resized
    root.grid_rowconfigure(1, weight=1, minsize=200)
    root.grid_rowconfigure(2, weight=1, minsize=200)

    # also make frames themselves expand internally where appropriate
    for f in (attr_frame, bonus_frame, stats_frame, thief_frame, weapons_frame, armor_frame):
        f.grid_rowconfigure(0, weight=0)
        f.grid_columnconfigure(0, weight=1)

    # Example: set a minimum width for some Entry widgets if you want explicit control
    # (already set via ENTRY_WIDTH, but you can set widget.configure(width=...) later)
    # e.g., player entry:
    # player_entry = top_frame.grid_slaves(row=0, column=1)[0]
    # player_entry.configure(width=28)

    root.mainloop()