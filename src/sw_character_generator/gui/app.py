"""GUI application for the Swords & Wizardry character generator."""
import tkinter as tk
import tkinter.ttk as ttk

from sw_character_generator.classes.playerclass import PlayerClass

def start_gui():
    """Start the GUI for the character generator."""
    

    root = tk.Tk()
    root.title("Swords & Wizardry Charaktergenerator")
    
    # Player Name
    lbl_player_name = tk.Label(
        root, text="Spieler:in:", )
    lbl_player_name.grid(row=0, column=0, padx=20, pady=10)
    ent_player_name = tk.Entry(root)
    ent_player_name.grid(row=0, column=1, padx=100, pady=10)

    # Character Name
    lbl_character_name = tk.Label(
        root, text="SC Name:", )
    lbl_character_name.grid(row=0, column=2, padx=20, pady=10)
    ent_character_name = tk.Entry(root)
    ent_character_name.grid(row=0, column=3, padx=100, pady=10)

    # Profession
    lbl_profession = tk.Label(
        root, text="Profession:", )
    lbl_profession.grid(row=1, column=2, padx=5, pady=10)
    cb_profession = ttk.Combobox(root, values=["Fighter", "Cleric", "Thief", "Wizard", "Ranger", "Paladin"])
    cb_profession.grid(row=1, column=3, padx=5, pady=10)

    # Race
    lbl_race = tk.Label(
        root, text="Rasse:", )
    lbl_race.grid(row=1, column=4, padx=5, pady=10)
    cb_race = ttk.Combobox(root, values=["Human", "Elf", "Dwarf", "Halfling", "halfelff"])
    cb_race.grid(row=1, column=5, padx=5, pady=10)

    # Gender
    lbl_gender = tk.Label(
        root, text="Geschlecht:", )
    lbl_gender.grid(row=1, column=6, padx=5, pady=10)
    ent_gender = tk.Entry(root)
    ent_gender.grid(row=1, column=7, padx=5, pady=10)

    # Alignment
    lbl_alignment = tk.Label(
        root, text="Gesinnung:", )
    lbl_alignment.grid(row=2, column=2, padx=5, pady=10)
    cb_alignment = ttk.Combobox(root, values=["Good", "Neutral", "Evil"])
    cb_alignment.grid(row=2, column=3, padx=5, pady=10)

    # God
    lbl_god = tk.Label(
        root, text="Gottheit:", )
    lbl_god.grid(row=2, column=4, padx=5, pady=10)
    ent_god = tk.Entry(root)
    ent_god.grid(row=2, column=5, padx=5, pady=10)

    # Age
    lbl_age = tk.Label(
        root, text="Alter:", )
    lbl_age.grid(row=2, column=6, padx=5, pady=10)
    ent_age = tk.Entry(root)
    ent_age.grid(row=2, column=7, padx=5, pady=10)

    root.mainloop()
