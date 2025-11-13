"""GUI application for the Swords & Wizardry character generator."""
import tkinter as tk
import tkinter.ttk as ttk

from sw_character_generator.classes.playerclass import PlayerClass

def start_gui():
    """Start the GUI for the character generator."""
    

    root = tk.Tk()
    root.title("Swords & Wizardry Charaktergenerator")
    
    # Create top frame
    top_frame = tk.Frame(root, bg="lightgrey")
    top_frame.grid(row=0, column=0, padx=10, pady=10)

    # Player Name
    lbl_player_name = tk.Label(
        top_frame, text="Spieler:in:", )
    lbl_player_name.grid(row=0, column=0, padx=20, pady=10)
    ent_player_name = tk.Entry(top_frame)
    ent_player_name.grid(row=0, column=1, padx=100, pady=10)

    # Character Name
    lbl_character_name = tk.Label(
        top_frame, text="SC Name:", )
    lbl_character_name.grid(row=0, column=2, padx=20, pady=10)
    ent_character_name = tk.Entry(top_frame)
    ent_character_name.grid(row=0, column=3, padx=100, pady=10)

    # player level
    lbl_level = tk.Label(
        top_frame, text="Level:", )
    lbl_level.grid(row=0, column=4, padx=5, pady=10)
    lbl_level2 = tk.Label(
        top_frame, text="1", )
    lbl_level2.grid(row=0, column=5, padx=5, pady=10)

    # Profession
    lbl_profession = tk.Label(
        top_frame, text="Profession:", )
    lbl_profession.grid(row=1, column=0, padx=5, pady=10)
    cb_profession = ttk.Combobox(top_frame, values=["Fighter", "Cleric", "Thief", "Wizard", "Ranger", "Paladin"])
    cb_profession.grid(row=1, column=1, padx=5, pady=10)

    # Race
    lbl_race = tk.Label(
        top_frame, text="Rasse:", )
    lbl_race.grid(row=1, column=2, padx=5, pady=10)
    cb_race = ttk.Combobox(top_frame, values=["Human", "Elf", "Dwarf", "Halfling", "halfelff"])
    cb_race.grid(row=1, column=3, padx=5, pady=10)

    # Gender
    lbl_gender = tk.Label(
        top_frame, text="Geschlecht:", )
    lbl_gender.grid(row=1, column=4, padx=5, pady=10)
    ent_gender = tk.Entry(top_frame)
    ent_gender.grid(row=1, column=5, padx=5, pady=10)

    # Alignment
    lbl_alignment = tk.Label(
        top_frame, text="Gesinnung:", )
    lbl_alignment.grid(row=2, column=0, padx=5, pady=10)
    cb_alignment = ttk.Combobox(top_frame, values=["Good", "Neutral", "Evil"])
    cb_alignment.grid(row=2, column=1, padx=5, pady=10)

    # God
    lbl_god = tk.Label(
        top_frame, text="Gottheit:", )
    lbl_god.grid(row=2, column=2, padx=5, pady=10)
    ent_god = tk.Entry(top_frame)
    ent_god.grid(row=2, column=3, padx=5, pady=10)

    # Age
    lbl_age = tk.Label(
        top_frame, text="Alter:", )
    lbl_age.grid(row=2, column=4, padx=5, pady=10)
    ent_age = tk.Entry(top_frame)
    ent_age.grid(row=2, column=5, padx=5, pady=10)

    # Main stats
    lbl_main_stats = tk.Label(
        top_frame, text="Main Stats:", )
    lbl_main_stats.grid(row=3, column=0, padx=20, pady=10)
    lbl_main_stats2 = tk.Label(
        top_frame, text="STR DEX CON INT WIS CHA", )
    lbl_main_stats2.grid(row=3, column=1, padx=20, pady=10)

    # EP-Bonus
    lbl_xp_bonus = tk.Label(
        top_frame, text="EP-Bonus (%):", )
    lbl_xp_bonus.grid(row=3, column=2, padx=20, pady=10)
    lbl_xp_bonus2 = tk.Label(
        top_frame, text="0", )
    lbl_xp_bonus2.grid(row=3, column=3, padx=20, pady=10)

    # EP
    lbl_xp = tk.Label(
        top_frame, text="EP:", )
    lbl_xp.grid(row=3, column=4, padx=20, pady=10)
    lbl_xp2 = tk.Label(
        top_frame, text="0", )
    lbl_xp2.grid(row=3, column=5, padx=20, pady=10)

    # Create attributes frame
    attr_frame = tk.Frame(root, bg="lightgrey")
    attr_frame.grid(row=1, column=0, padx=10, pady=10)

    lbl_attributes = tk.Label(
        attr_frame, text="Attribute", font=("Arial", 14))
    lbl_attributes.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    lbl_stat_str = tk.Label(
        attr_frame, text="Stärke (STR):", )
    lbl_stat_str.grid(row=1, column=0, padx=5, pady=5)
    lbl_stat_str2 = tk.Label(
        attr_frame, text="0", )
    lbl_stat_str2.grid(row=1, column=1, padx=5, pady=5)
    lbl_stat_dex = tk.Label(
        attr_frame, text="Geschicklichkeit (DEX):", )
    lbl_stat_dex.grid(row=2, column=0, padx=5, pady=5)
    lbl_stat_dex2 = tk.Label(
        attr_frame, text="0", )
    lbl_stat_dex2.grid(row=2, column=1, padx=5, pady=5)
    lbl_stat_con = tk.Label(
        attr_frame, text="Konstitution (CON):", )
    lbl_stat_con.grid(row=3, column=0, padx=5, pady=5)
    lbl_stat_con2 = tk.Label(
        attr_frame, text="0", )
    lbl_stat_con2.grid(row=3, column=1, padx=5, pady=5)
    lbl_stat_int = tk.Label(
        attr_frame, text="Intelligenz (INT):", )
    lbl_stat_int.grid(row=4, column=0, padx=5, pady=5)
    lbl_stat_int2 = tk.Label(
        attr_frame, text="0", )
    lbl_stat_int2.grid(row=4, column=1, padx=5, pady=5)
    lbl_stat_wis = tk.Label(
        attr_frame, text="Weisheit (WIS):", )
    lbl_stat_wis.grid(row=5, column=0, padx=5, pady=5)
    lbl_stat_wis2 = tk.Label(
        attr_frame, text="0", )
    lbl_stat_wis2.grid(row=5, column=1, padx=5, pady=5)
    lbl_stat_char = tk.Label(
        attr_frame, text="Charisma (CHA):", )
    lbl_stat_char.grid(row=6, column=0, padx=5, pady=5)
    lbl_stat_char2 = tk.Label(
        attr_frame, text="0", )
    lbl_stat_char2.grid(row=6, column=1, padx=5, pady=5)

    # Create bonus frame
    bonus_frame = tk.Frame(root, bg="lightgrey")
    bonus_frame.grid(row=1, column=1, padx=10, pady=10)

    lbl_bonuses = tk.Label(
        bonus_frame, text="Attribute Bonuses", font=("Arial", 14))
    lbl_bonuses.grid(row=0, column=0, padx=5, pady=5)

    lbl_strength_attack_mod = tk.Label(
        bonus_frame, text="Melee Attack Bonus:", )
    lbl_strength_attack_mod.grid(row=1, column=0, padx=5, pady=5)
    lbl_strength_attack_mod2 = tk.Label(
        bonus_frame, text="0", )
    lbl_strength_attack_mod2.grid(row=1, column=1, padx=5, pady=5)

    lbl_strength_damage_mod = tk.Label(
        bonus_frame, text="Melee Damage Bonus:", )
    lbl_strength_damage_mod.grid(row=2, column=0, padx=5, pady=5)
    lbl_strength_damage_mod2 = tk.Label(
        bonus_frame, text="0", )
    lbl_strength_damage_mod2.grid(row=2, column=1, padx=5, pady=5)
    lbl_carry_capacity_mod = tk.Label(
        bonus_frame, text="Carry Capacity Bonus:", )
    lbl_carry_capacity_mod.grid(row=3, column=0, padx=5, pady=5)
    lbl_carry_capacity_mod2 = tk.Label(
        bonus_frame, text="0", )
    lbl_carry_capacity_mod2.grid(row=3, column=1, padx=5, pady=5)
    lbl_door_crack_mod = tk.Label(
        bonus_frame, text="Door Crack Bonus:", )
    lbl_door_crack_mod.grid(row=4, column=0, padx=5, pady=5)
    lbl_door_crack_mod2 = tk.Label(
        bonus_frame, text="0", )
    lbl_door_crack_mod2.grid(row=4, column=1, padx=5, pady=5)
    lbl_ranged_attack_mod = tk.Label(
        bonus_frame, text="Ranged Attack Bonus:", )
    lbl_ranged_attack_mod.grid(row=5, column=0, padx=5, pady=5)
    lbl_ranged_attack_mod2 = tk.Label(
        bonus_frame, text="0", )
    lbl_ranged_attack_mod2.grid(row=5, column=1, padx=5, pady=5)
    lbl_ac_mod = tk.Label(
        bonus_frame, text="AC Bonus:", )
    lbl_ac_mod.grid(row=6, column=0, padx=5, pady=5)
    lbl_ac_mod2 = tk.Label(
        bonus_frame, text="0", )
    lbl_ac_mod2.grid(row=6, column=1, padx=5, pady=5)
    lbl_tp_mod = tk.Label(
        bonus_frame, text="TP Bonus:", )
    lbl_tp_mod.grid(row=7, column=0, padx=5, pady=5)
    lbl_tp_mod2 = tk.Label(
        bonus_frame, text="0", )
    lbl_tp_mod2.grid(row=7, column=1, padx=5, pady=5)
    lbl_raise_dead_mod = tk.Label(
        bonus_frame, text="Raise Dead Modifier:", )
    lbl_raise_dead_mod.grid(row=8, column=0, padx=5, pady=5)
    lbl_raise_dead_mod2 = tk.Label(
        bonus_frame, text="0", )
    lbl_raise_dead_mod2.grid(row=8, column=1, padx=5, pady=5)
    lbl_max_add_langs = tk.Label(
        bonus_frame, text="Max Additional Languages:", )
    lbl_max_add_langs.grid(row=9, column=0, padx=5, pady=5)
    lbl_max_add_langs2 = tk.Label(
        bonus_frame, text="0", )
    lbl_max_add_langs2.grid(row=9, column=1, padx=5, pady=5)
    lbl_cap_spec_hirelings = tk.Label(
        bonus_frame, text="Special Hirelings Cap:", )
    lbl_cap_spec_hirelings.grid(row=10, column=0, padx=5, pady=5)
    lbl_cap_spec_hirelings2 = tk.Label(
        bonus_frame, text="0", )
    lbl_cap_spec_hirelings2.grid(row=10, column=1, padx=5, pady=5) 
    
    # Create stats frame
    stats_frame = tk.Frame(root, bg="lightgrey")
    stats_frame.grid(row=1, column=2, padx=10, pady=10)

    # Create thief skills frame
    thief_frame = tk.Frame(root, bg="lightgrey")
    thief_frame.grid(row=2, column=0, padx=10, pady=10)

    # Create Weapons frame
    weapons_frame = tk.Frame(root, bg="lightgrey")
    weapons_frame.grid(row=2, column=1, padx=10, pady=10)

    # Create Armor frame
    armor_frame = tk.Frame(root, bg="lightgrey")
    armor_frame.grid(row=2, column=2, padx=10, pady=10)



    root.mainloop()
