"""GUI functions for the dice roller window."""
import tkinter as tk
from sw_character_generator.gui.gui_functions.gui_widgets import widget_button, widget_checkbutton, widget_entry_long, widget_label, widget_spinbox


def dice_roller(parent: tk.Tk):
    """Open the dice roller window."""
    print("DEBUG dice_roller: ----------------------------------------------------------------")
    def on_close():
        """Handle the window close event."""
        win.grab_release()
        win.destroy()

    def clear_fields():
        """Function to clear all input and output fields."""
        pass  # Implement field clearing logic here
    
    def roll_dice():
        """Function to roll the dice based on user input."""
        pass  # Implement dice rolling logic here


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
    widget_entry_long(win, "Count:", row=2, column=0, width=10, textvariable=tk.StringVar(value="1"))
    widget_entry_long(win, "Sides:", row=2, column=1, width=10, textvariable=tk.StringVar(value="6"))
    widget_spinbox(win, "Bonus:", row=2, column=2, from_=-100, to=100, width=10, textvariable=tk.StringVar(value="0"))
    widget_spinbox(win, "Malus:", row=2, column=3, from_=-100, to=100, width=10, textvariable=tk.StringVar(value="0"))
    widget_checkbutton(win, "Advantage", row=2, column=4, variable=tk.BooleanVar(value=False))
    widget_checkbutton(win, "Disadvantage", row=2, column=5, variable=tk.BooleanVar(value=False))
        
    # row 3
    widget_label(win, "Result:", row=3, column=0, width=10)
    widget_label(win, "Total:", row=3, column=1, width=10)
    widget_label(win, "Details:", row=3, column=2, width=30, columnspan=4)

    # row 4
    widget_button(win, "Roll Dice", row=4, column=0, command=roll_dice)
    widget_button(win, "Clear", row=4, column=1, command=clear_fields)
    widget_button(win, "Close", row=4, column=2, command=on_close)
