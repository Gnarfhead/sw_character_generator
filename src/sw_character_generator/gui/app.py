"""GUI application for the Swords & Wizardry character generator."""
import tkinter as tk

def start_gui():
    """Start the GUI for the character generator."""
    root = tk.Tk()
    root.title("Swords & Wizardry Charaktergenerator")
    label = tk.Label(
        root, text="Willkommen zum Charaktergenerator!")
    label.pack(padx=20, pady=20)
    label2 = tk.Label(
        root, text="GUI-Modus ist noch in Arbeit, bitte benutzen Sie die CLI mit dem Parameter '-cli'.")
    label2.pack(padx=20, pady=20)
    root.mainloop()
