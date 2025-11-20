"""GUI functions for the dice roller window."""
import tkinter as tk
from tkinter import ttk


def dice_roller(parent: tk.Tk):
    """Open the dice roller window."""

    win = tk.Toplevel()  # Create the modal window
    win.title("Dice Roller")  # Set the title of the window
    win.transient(parent)  # Set to be on top of the main window
    win.grab_set()  # Make modal

    # GUI Elements - row 0
    lbl_headline = ttk.Label(win, text="Dice Roller Functionality Here")
    lbl_headline.grid(row=0, column=0, padx=10, pady=10)

    # row 1
    lbl_dice_count = ttk.Label(win, text="Dice Count:")
    lbl_dice_count.grid(row=1, column=0, padx=10, pady=5)
    lbl_dice_side = ttk.Label(win, text="Dice Sides:")
    lbl_dice_side.grid(row=1, column=1, padx=10, pady=5)
    lbl_bonus = ttk.Label(win, text="Bonus:")
    lbl_bonus.grid(row=1, column=2, padx=10, pady=5)
    lbl_malus = ttk.Label(win, text="Malus:")
    lbl_malus.grid(row=1, column=3, padx=10, pady=5)

    # row 2
    entry_dice_count = ttk.Entry(win, width=5, textvariable=tk.IntVar())
    entry_dice_count.grid(row=2, column=0, padx=10, pady=5)
    entry_dice_side = ttk.Entry(win, width=5, textvariable=tk.IntVar())
    entry_dice_side.grid(row=2, column=1, padx=10, pady=5)
    sbx_bonus = ttk.Spinbox(win, from_=-100, to=100, width=5, variable=tk.IntVar())
    sbx_bonus.grid(row=2, column=2, padx=10, pady=5)
    sbx_malus = ttk.Spinbox(win, from_=-100, to=100, width=5, variable=tk.IntVar())
    sbx_malus.grid(row=2, column=3, padx=10, pady=5)
    chk_advantage = ttk.Checkbutton(win, text="Advantage", variable=tk.IntVar())
    chk_advantage.grid(row=2, column=4, padx=10, pady=5)
    chk_disadvantage = ttk.Checkbutton(win, text="Disadvantage", variable=tk.IntVar())
    chk_disadvantage.grid(row=2, column=5, padx=10, pady=5)