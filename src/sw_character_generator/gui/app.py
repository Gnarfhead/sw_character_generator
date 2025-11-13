"""GUI application for the Swords & Wizardry character generator."""
import tkinter as tk

def start_gui():
    """Start the GUI for the character generator."""
    root = tk.Tk()
    root.title("Swords & Wizardry Charaktergenerator")
    
    label1 = tk.Label(
        root, text="Willkommen zum Charaktergenerator!",
        font=("Arial", 16, "bold"))
    label1.grid(row=0, column=0, padx=20, pady=10)

    label2 = tk.Label(
        root, text="GUI-Modus ist noch in Arbeit.") 
    label2.grid(row=1, column=0, padx=5, pady=10)

    label3 = tk.Label(
        root, text="Bitte benutzen Sie die CLI mit dem Parameter '-cli'.")
    label3.grid(row=2, column=0, padx=5, pady=10)

    root.mainloop()
