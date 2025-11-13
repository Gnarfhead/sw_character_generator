import tkinter as tk

def start_gui():
    root = tk.Tk()
    root.title("Swords & Wizardry Charaktergenerator")
    label = tk.Label(
        root, text="Willkommen zum Charaktergenerator! \n GUI-Modus ist noch in Arbeit, bitte benutzen Sie die CLI mit dem Parameter '-cli'.")
    label.pack(padx=20, pady=20)
    root.mainloop()