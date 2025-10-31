import tkinter as tk
from src.sw_character_generator.functions.roleDice import wuerfle_3d6

class Application:
    """Hauptklasse der Tkinter-Anwendung"""

    def __init__(self):
        # Hauptfenster erstellen
        self.root = tk.Tk()
        self.root.title("Einfache Tkinter OOP App")
        self.root.geometry("300x150")

        # GUI-Elemente erstellen
        self.create_widgets()

    def create_widgets(self):
        """Erzeugt alle Widgets der Benutzeroberfläche"""
        # Eingabefeld
        #self.entry1 = tk.Entry(self.root, width=30)
        #self.entry1.grid(row=0, column=0)

        # Label for Strength
        self.lblStrength = tk.Label(self.root, text="Stärke", fg="blue", width=12)
        self.lblStrength.grid(row=0, column=0)

        # Label for Dex
        self.lblDex = tk.Label(self.root, text="Geschicklichkeit", fg="blue", width=12)
        self.lblDex.grid(row=1, column=0)

        # Label for Con
        self.lblCon = tk.Label(self.root, text="Konstitution", fg="blue", width=12)
        self.lblCon.grid(row=2, column=0)

        # Label for Wis
        self.lblWis = tk.Label(self.root, text="Wisdom", fg="blue", width=12)
        self.lblWis.grid(row=3, column=0)

        # Label for Int
        self.lblInt = tk.Label(self.root, text="Intelligenz", fg="blue", width=12)
        self.lblInt.grid(row=4, column=0)

        # Label for Char
        self.lblChar = tk.Label(self.root, text="Charisma", fg="blue", width=12)
        self.lblChar.grid(row=5, column=0)

        # Button for Strength
        self.btnStrength = tk.Button(self.root, text="X", command=self.on_button_click)
        self.btnStrength.grid(row=0, column=1)


    def on_button_click(self):
        """Wird aufgerufen, wenn der Button gedrückt wird"""
        summe = wuerfle_3d6()  # 3d6 würfeln
        self.lblStrength.config(text=f"{summe}")

    def run(self):
        """Startet die Tkinter-Hauptschleife"""
        self.root.mainloop()
