"""GUI functions for the dice roller window."""
import tkinter as tk
from sw_character_generator.gui.gui_functions.gui_widgets import widget_button, widget_checkbutton, widget_entry_short, widget_label, widget_spinbox_nolabel


def dice_roller(app):
    """Open the dice roller window."""
    print("DEBUG dice_roller: ----------------------------------------------------------------")
    
    # Create variables FIRST (before any widgets use them!)
    dice_count_var = tk.StringVar(value="1")
    dice_sides_var = tk.StringVar(value="6")
    bonus_var = tk.StringVar(value="0")
    malus_var = tk.StringVar(value="0")
    advantage_var = tk.BooleanVar(value=False)
    disadvantage_var = tk.BooleanVar(value=False)
    result_var = tk.StringVar(value="")
    total_var = tk.StringVar(value="")
    details_var = tk.StringVar(value="")
    
    def on_close():
        """Handle the window close event."""
        win.grab_release()
        win.destroy()

    def clear_fields():
        """Function to clear all input and output fields."""
        dice_count_var.set("1")
        dice_sides_var.set("6")
        bonus_var.set("0")
        malus_var.set("0")
        advantage_var.set(False)
        disadvantage_var.set(False)
        result_var.set("")
        total_var.set("")
        details_var.set("")
    
    def roll_dice():
        """Function to roll the dice based on user input."""
        import random
        
        try:
            count = int(dice_count_var.get())
            sides = int(dice_sides_var.get())
            bonus = int(bonus_var.get())
            malus = int(malus_var.get())
            adv = advantage_var.get()
            disadv = disadvantage_var.get()
            
            if count < 1 or sides < 1:
                raise ValueError("Dice count and sides must be positive")
            
            # Roll dice
            rolls = [random.randint(1, sides) for _ in range(count)]
            
            # Handle Advantage/Disadvantage (only for single die)
            if count == 1:
                if adv and not disadv:
                    roll2 = random.randint(1, sides)
                    final = max(rolls[0], roll2)
                    discarded = min(rolls[0], roll2)
                    rolls = [final]
                    details_var.set(f"Roll: {final} (adv, discarded {discarded})")
                elif disadv and not adv:
                    roll2 = random.randint(1, sides)
                    final = min(rolls[0], roll2)
                    discarded = max(rolls[0], roll2)
                    rolls = [final]
                    details_var.set(f"Roll: {final} (dis, discarded {discarded})")
                else:
                    details_var.set(f"Roll: {rolls[0]}")
            else:
                details_var.set(f"Rolls: {', '.join(map(str, rolls))}")
            
            # Calculate total
            roll_sum = sum(rolls)
            total = roll_sum + bonus - malus
            
            result_var.set(str(roll_sum))
            total_var.set(str(total))
            
        except ValueError as e:
            result_var.set("Error!")
            total_var.set("")
            details_var.set(f"Invalid input: {e}")

    win = tk.Toplevel()
    win.title("Dice Roller")
    win.transient(app.root)
    win.grab_set()

    # GUI Elements - row 0 (Header)
    widget_label(win, "Dice Roller", row=0, column=0, columnspan=6)

    # row 1 (Column Headers)
    widget_label(win, "Dice Count:", row=1, column=0)
    widget_label(win, "Dice Sides:", row=1, column=1)
    widget_label(win, "Bonus:", row=1, column=2)
    widget_label(win, "Malus:", row=1, column=3)

    # row 2 (Inputs) - WICHTIG: Parameter ist "var=", nicht "textvariable="!
    widget_entry_short(win, 2, 0, var=dice_count_var)
    widget_entry_short(win, 2, 1, var=dice_sides_var)
    widget_spinbox_nolabel(win, 2, 2, from_=-100, to=100, var=bonus_var)
    widget_spinbox_nolabel(win, 2, 3, from_=-100, to=100, var=malus_var)
    widget_checkbutton(win, "Adv", 2, 8, var=advantage_var)
    widget_checkbutton(win, "Dis", 2, 10, var=disadvantage_var)

    # row 3 (Results)
    widget_label(win, "Result:", row=3, column=0)
    tk.Label(win, textvariable=result_var, font=("Arial", 12, "bold"), fg="blue").grid(row=3, column=1, padx=8, pady=6, sticky="w")
    
    # row 4 (Total)
    widget_label(win, "Total:", row=4, column=0)
    tk.Label(win, textvariable=total_var, font=("Arial", 12, "bold"), fg="green").grid(row=4, column=1, padx=8, pady=6, sticky="w")

    # row 5 (Details)
    widget_label(win, "Details:", row=5, column=0)
    tk.Label(win, textvariable=details_var, fg="gray").grid(row=5, column=1, columnspan=5, padx=8, pady=6, sticky="w")

    # row 6 (Buttons)
    widget_button(win, "Roll Dice", row=6, column=0, command=roll_dice)
    widget_button(win, "Clear", row=6, column=1, command=clear_fields)
    widget_button(win, "Close", row=6, column=2, command=on_close)

    # Center window on screen
    win.update_idletasks()
    width = win.winfo_reqwidth()
    height = win.winfo_reqheight()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry(f'+{x}+{y}')