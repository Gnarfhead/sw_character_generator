from tkinter import ttk, messagebox
import tkinter as tk

from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model

def open_add_item_dialog(app):
    """Open dialog to add an item from the database with ALL properties displayed."""
    dialog = tk.Toplevel(app.root)
    dialog.title("Add Item to Inventory")
    dialog.geometry("900x600")
    
    # Frame für Scrollbar
    main_frame = ttk.Frame(dialog)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Scrollbar
    scrollbar = ttk.Scrollbar(main_frame)
    scrollbar.pack(side="right", fill="y")
    
    # Treeview mit ALLEN Spalten
    columns = (
        "Name",
        "Type",
        "Value",
        "Weight",
        "Damage",
        "AC Bonus",
        "Atck Bonus",
        "Dmg Bonus",
        "Two-Handed",
        "Versatile",
        "Weapon Type",
        "Armor Type",
        "Fire Rate",
        "Range",
        "Count"
    )
    
    tree = ttk.Treeview(
        main_frame,
        columns=columns,
        show="headings",
        height=20,
        yscrollcommand=scrollbar.set
    )
    
    scrollbar.config(command=tree.yview)
    
    # Definiere Spalten-Breiten und Header
    tree.column("Name", anchor="w", width=150)
    tree.column("Type", anchor="center", width=80)
    tree.column("Value", anchor="center", width=80)
    tree.column("Weight", anchor="center", width=60)
    tree.column("Damage", anchor="center", width=70)
    tree.column("AC Bonus", anchor="center", width=70)
    tree.column("Atck Bonus", anchor="center", width=70)
    tree.column("Dmg Bonus", anchor="center", width=70)
    tree.column("Two-Handed", anchor="center", width=80)
    tree.column("Versatile", anchor="center", width=70)
    tree.column("Weapon Type", anchor="center", width=100)
    tree.column("Armor Type", anchor="center", width=90)
    tree.column("Fire Rate", anchor="center", width=70)
    tree.column("Range", anchor="center", width=60)
    tree.column("Count", anchor="center", width=60)
    
    # Header
    for col in columns:
        tree.heading(col, text=col, anchor="center")
    
    # Füge alle Items aus der Datenbank ein
    for item in app.item_database:
        values = (
            item.name,
            item.type or "-",
            item.value or "-",
            f"{item.weight:.1f}" if item.weight else "-",
            item.damage or "-",
            str(item.acbonus) if item.acbonus else "-",
            str(item.atckbonus) if item.atckbonus else "-",
            str(item.dmgbonus) if item.dmgbonus else "-",
            "✓" if item.twohanded else "✗",
            "✓" if item.versatile else "✗",
            item.weapontype or "-",
            item.armortype or "-",
            str(item.firerate) if item.firerate else "-",
            str(item.range) if item.range else "-",
            str(item.count) if item.count else "1"
        )
        tree.insert("", "end", values=values, tags=(item.name,))
    
    tree.pack(fill="both", expand=True, pady=(0, 10))
    
    # Button Frame
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(fill="x", pady=10)
    
    def add_selected_item():
        """Add the selected item to inventory."""
        selection = tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select an item to add.")
            return
        
        # Hole Item-Namen aus Tags
        selected_item_name = tree.item(selection[0])["values"][0]
        
        # Finde Item in Datenbank
        item_to_add = None
        for item in app.item_database:
            if item.name == selected_item_name:
                item_to_add = item
                break
        
        if item_to_add:
            # GEÄNDERT: Füge Item direkt zur Liste hinzu
            app.new_player.inventory_items.append(item_to_add)
            
            # Update GUI
            update_view_from_model(app)
            
            messagebox.showinfo("Success", f"'{item_to_add.name}' wurde zum Inventar hinzugefügt.")
            dialog.destroy()
        else:
            messagebox.showerror("Error", "Item konnte nicht gefunden werden.")
    
    def close_dialog():
        """Close the dialog."""
        dialog.destroy()
    
    # Buttons
    ttk.Button(
        button_frame,
        text="Add to Inventory",
        command=add_selected_item
    ).pack(side="left", padx=5)
    
    ttk.Button(
        button_frame,
        text="Cancel",
        command=close_dialog
    ).pack(side="left", padx=5)
    
    # Info Label
    info_label = ttk.Label(
        main_frame,
        text="Wähle ein Item aus und klicke 'Add to Inventory'",
        font=("Arial", 10, "italic")
    )
    info_label.pack(pady=5)
    
    # Zentriere Dialog
    dialog.transient(app.root)
    dialog.grab_set()
    app.root.wait_window(dialog)