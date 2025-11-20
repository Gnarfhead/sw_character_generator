"""GUI functions for the dice roller window."""
import tkinter as tk


from src.sw_character_generator.gui.gui_functions.gui_widgets import widget_checkbutton, widget_entry, widget_label, widget_spinbox


def dice_roller(parent: tk.Tk):
    """Open the dice roller window."""

    win = tk.Toplevel()  # Create the modal window
    win.title("Dice Roller")  # Set the title of the window
    win.transient(parent)  # Set to be on top of the main window
    win.grab_set()  # Make modal

    # GUI Elements - row 0
    widget_label(win, "Dice Roller Functionality Here", row=0, column=0, width=30, columnspan=6)

    # row 1
    widget_label(win, "Dice Count:", row=1, column=0, width=10)
    widget_label(win, "Dice Sides:", row=1, column=1, width=10)
    widget_label(win, "Bonus:", row=1, column=2, width=10)
    widget_label(win, "Malus:", row=1, column=3, width=10)

    # row 2
    widget_entry(win, "Count:", row=2, column=0, width=10)
    widget_entry(win, "Sides:", row=2, column=1, width=10)
    widget_spinbox(win, "Bonus:", row=2, column=2, from_=-100, to=100, width=10)
    widget_spinbox(win, "Malus:", row=2, column=3, from_=-100, to=100, width=10)
    widget_checkbutton(win, "Advantage", row=2, column=4)
    widget_checkbutton(win, "Disadvantage", row=2, column=5)
    