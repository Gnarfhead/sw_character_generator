"""GUI functions for inventory dialog in the Swords & Wizardry character generator."""

from tkinter import ttk, messagebox
import tkinter as tk

from sw_character_generator.gui.gui_functions.gui_update_view_from_model import update_view_from_model

def open_add_item_dialog(app):
    """Open dialog to add an item from the database with ALL properties displayed."""
    dialog = tk.Toplevel(app.root)
    dialog.title("Add Item to Inventory")
    dialog.geometry("1550x600")
    
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
        "Weight (pound)",
        "Damage",
        "AC Bonus",
        "Attack Bonus",
        "Damage Bonus",
        "Two-Handed",
        "Versatile",
        "Weapon Type",
        "Armor Type",
        "Fire Rate",
        "Range (m)",
        "Count"
    )
    
    tree = ttk.Treeview(
        main_frame,
        columns=columns,
        show="headings",
        height=20,
        yscrollcommand=scrollbar.set,
        selectmode="extended"
    )
    
    scrollbar.config(command=tree.yview)
    
    # Definiere Spalten-Breiten und Header
    tree.column("Name", anchor="w", width=250)
    tree.column("Type", anchor="center", width=100)
    tree.column("Value", anchor="center", width=100)
    tree.column("Weight (pound)", anchor="center", width=100)
    tree.column("Damage", anchor="center", width=100)
    tree.column("AC Bonus", anchor="center", width=100)
    tree.column("Attack Bonus", anchor="center", width=100)
    tree.column("Damage Bonus", anchor="center", width=100)
    tree.column("Two-Handed", anchor="center", width=100)
    tree.column("Versatile", anchor="center", width=100)
    tree.column("Weapon Type", anchor="center", width=100)
    tree.column("Armor Type", anchor="center", width=100)
    tree.column("Fire Rate", anchor="center", width=100)
    tree.column("Range (m)", anchor="center", width=100)
    tree.column("Count", anchor="center", width=100)
    
    # Sortier-Funktion für Spalten
    def sort_treeview(col, reverse):
        """Sort treeview by column."""
        items = [(tree.set(child, col), child) for child in tree.get_children("")]
        
        # Versuche numerische Sortierung, sonst alphabetisch
        try:
            items.sort(key=lambda x: float(x[0].replace("-", "0").replace("✓", "1").replace("✗", "0")), reverse=reverse)
        except ValueError:
            items.sort(reverse=reverse)
        
        # Neuordnen der Items
        for index, (_, child) in enumerate(items):
            tree.move(child, "", index)
        
        # Header aktualisieren mit Sortier-Indikator
        tree.heading(col, command=lambda: sort_treeview(col, not reverse))
    
    # Header mit Sortier-Funktion
    for col in columns:
        tree.heading(
            col,
            text=col,
            anchor="center",
            command=lambda c=col: sort_treeview(c, False)
        )

    
   # Füge alle Items aus der Datenbank ein - ALPHABETISCH SORTIERT
    sorted_items = sorted(app.item_database, key=lambda item: item.name.lower())

    # Füge alle Items aus der Datenbank ein
    for item in sorted_items:
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
        """Add the selected items to inventory."""
        selections = tree.selection()  # ← GEÄNDERT: Kann mehrere Items sein
        
        if not selections:
            messagebox.showwarning("No Selection", "Please select at least one item to add.")
            return
        
        # Liste für erfolgreich hinzugefügte Items
        added_items = []
        
        # Iteriere über alle Selektionen
        for selection in selections:
            # Hole Item-Namen
            selected_item_name = tree.item(selection)["values"][0]
            
            # Finde Item in Datenbank
            item_to_add = None
            for item in app.item_database:
                if item.name == selected_item_name:
                    item_to_add = item
                    break
            
            if item_to_add:
                # Füge Item zum Inventar hinzu
                app.new_player.inventory_items.append(item_to_add)
                added_items.append(item_to_add.name)
        
        # Update GUI
        if added_items:
            update_view_from_model(app)
            
            # Erfolgs-Meldung mit allen hinzugefügten Items
            items_text = "\n- ".join(added_items)
            messagebox.showinfo(
                "Success",
                f"{len(added_items)} Item(s) wurden zum Inventar hinzugefügt:\n\n- {items_text}"
            )
            dialog.destroy()
        else:
            messagebox.showerror("Error", "Keine Items konnten hinzugefügt werden.")
    
    
    def close_dialog():
        """Close the dialog."""
        dialog.destroy()
    
    # Buttons
    ttk.Button(
        button_frame,
        text="Add Selected Items",
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
        text="Select one or more items and click 'Add Selected Items' to add them to your inventory.",
        font=("Arial", 10, "italic")
    )
    info_label.pack(pady=5)
    
    # Zentriere Dialog
    dialog.transient(app.root)
    dialog.grab_set()
    app.root.wait_window(dialog)

def on_edit_item_click(app, inventory_tree):
    """Handle edit button click."""
    selection = inventory_tree.selection()
    if not selection:
        messagebox.showwarning("No Selection", "Please select an item to edit.")
        return
      
    item_index = inventory_tree.index(selection[0])
    item_to_edit = app.new_player.inventory_items[item_index]
    open_edit_item_dialog(app, item_to_edit, item_index)

def open_edit_item_dialog(app, item_to_edit, item_index):
    """Open dialog to edit an existing item in the inventory."""
    dialog = tk.Toplevel(app.root)
    dialog.title(f"Edit Item: {item_to_edit.name}")
    dialog.geometry("600x700")
    
    # Main Frame mit Scrollbar
    main_frame = ttk.Frame(dialog)
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Canvas für Scrolling
    canvas = tk.Canvas(main_frame)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Eingabefelder für alle Properties
    fields = {}
    row = 0
    
    # Name
    ttk.Label(scrollable_frame, text="Name:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["name"] = ttk.Entry(scrollable_frame, width=40)
    fields["name"].insert(0, item_to_edit.name)
    fields["name"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # Type
    ttk.Label(scrollable_frame, text="Type:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["type"] = ttk.Combobox(scrollable_frame, values=["Weapon", "Armor", "shield", "Equipment", "consumable", "Transport"], width=38)
    fields["type"].set(item_to_edit.type or "")
    fields["type"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # Value
    ttk.Label(scrollable_frame, text="Value:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["value"] = ttk.Entry(scrollable_frame, width=40)
    fields["value"].insert(0, item_to_edit.value or "0 GM")
    fields["value"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # Weight
    ttk.Label(scrollable_frame, text="Weight:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["weight"] = ttk.Entry(scrollable_frame, width=40)
    fields["weight"].insert(0, str(item_to_edit.weight or 0))
    fields["weight"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # Damage
    ttk.Label(scrollable_frame, text="Damage:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["damage"] = ttk.Entry(scrollable_frame, width=40)
    fields["damage"].insert(0, item_to_edit.damage or "")
    fields["damage"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # AC Bonus
    ttk.Label(scrollable_frame, text="AC Bonus:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["acbonus"] = ttk.Entry(scrollable_frame, width=40)
    fields["acbonus"].insert(0, str(item_to_edit.acbonus or ""))
    fields["acbonus"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # Attack Bonus
    ttk.Label(scrollable_frame, text="Attack Bonus:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["atckbonus"] = ttk.Entry(scrollable_frame, width=40)
    fields["atckbonus"].insert(0, str(item_to_edit.atckbonus or ""))
    fields["atckbonus"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # Damage Bonus
    ttk.Label(scrollable_frame, text="Damage Bonus:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["dmgbonus"] = ttk.Entry(scrollable_frame, width=40)
    fields["dmgbonus"].insert(0, str(item_to_edit.dmgbonus or ""))
    fields["dmgbonus"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # Two-Handed (Checkbox)
    ttk.Label(scrollable_frame, text="Two-Handed:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["twohanded"] = tk.BooleanVar(value=item_to_edit.twohanded)
    ttk.Checkbutton(scrollable_frame, variable=fields["twohanded"]).grid(row=row, column=1, sticky="w", pady=5)
    row += 1
    
    # Versatile (Checkbox)
    ttk.Label(scrollable_frame, text="Versatile:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["versatile"] = tk.BooleanVar(value=item_to_edit.versatile)
    ttk.Checkbutton(scrollable_frame, variable=fields["versatile"]).grid(row=row, column=1, sticky="w", pady=5)
    row += 1
    
    # Weapon Type
    ttk.Label(scrollable_frame, text="Weapon Type:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["weapontype"] = ttk.Combobox(scrollable_frame, values=["melee", "ranged", "melee, ranged"], width=38)
    fields["weapontype"].set(item_to_edit.weapontype or "")
    fields["weapontype"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # Armor Type
    ttk.Label(scrollable_frame, text="Armor Type:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["armortype"] = ttk.Combobox(scrollable_frame, values=["light", "medium", "heavy", "shield"], width=38)
    fields["armortype"].set(item_to_edit.armortype or "")
    fields["armortype"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # Fire Rate
    ttk.Label(scrollable_frame, text="Fire Rate:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["firerate"] = ttk.Entry(scrollable_frame, width=40)
    fields["firerate"].insert(0, str(item_to_edit.firerate or ""))
    fields["firerate"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # Range
    ttk.Label(scrollable_frame, text="Range:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["range"] = ttk.Entry(scrollable_frame, width=40)
    fields["range"].insert(0, str(item_to_edit.range or ""))
    fields["range"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # Count
    ttk.Label(scrollable_frame, text="Count:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["count"] = ttk.Entry(scrollable_frame, width=40)
    fields["count"].insert(0, str(item_to_edit.count or 1))
    fields["count"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # Description
    ttk.Label(scrollable_frame, text="Description:", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="nw", pady=5)
    fields["description"] = tk.Text(scrollable_frame, width=40, height=4)
    fields["description"].insert("1.0", item_to_edit.description or "")
    fields["description"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # Tags
    ttk.Label(scrollable_frame, text="Tags (comma-separated):", font=("Arial", 10, "bold")).grid(row=row, column=0, sticky="w", pady=5)
    fields["tags"] = ttk.Entry(scrollable_frame, width=40)
    fields["tags"].insert(0, ", ".join(item_to_edit.tags or []))
    fields["tags"].grid(row=row, column=1, sticky="ew", pady=5)
    row += 1
    
    # Button Frame
    button_frame = ttk.Frame(dialog)
    button_frame.pack(fill="x", padx=20, pady=10)
    
    def save_changes():
        """Save the edited item."""
        try:
            # Erstelle aktualisiertes Item
            from sw_character_generator.classes.item import Item
            
            updated_item = Item(
                name=fields["name"].get(),
                type=fields["type"].get(),
                value=fields["value"].get(),
                weight=float(fields["weight"].get() or 0),
                damage=fields["damage"].get() or None,
                acbonus=int(fields["acbonus"].get()) if fields["acbonus"].get() else None,
                atckbonus=int(fields["atckbonus"].get()) if fields["atckbonus"].get() else None,
                dmgbonus=int(fields["dmgbonus"].get()) if fields["dmgbonus"].get() else None,
                twohanded=fields["twohanded"].get(),
                versatile=fields["versatile"].get(),
                weapontype=fields["weapontype"].get() or None,
                armortype=fields["armortype"].get() or None,
                firerate=int(fields["firerate"].get()) if fields["firerate"].get() else None,
                range=int(fields["range"].get()) if fields["range"].get() else None,
                count=int(fields["count"].get()) if fields["count"].get() else 1,
                description=fields["description"].get("1.0", "end-1c"),
                tags=[tag.strip() for tag in fields["tags"].get().split(",") if tag.strip()]
            )
            
            # Ersetze Item im Inventar
            app.new_player.inventory_items[item_index] = updated_item
            
            # Update GUI
            update_view_from_model(app)
            
            messagebox.showinfo("Success", f"Item '{updated_item.name}' wurde erfolgreich bearbeitet.")
            dialog.destroy()
            
        except ValueError as e:
            messagebox.showerror("Error", f"Ungültige Eingabe: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Fehler beim Speichern: {str(e)}")
    
    def cancel_edit():
        """Cancel editing."""
        dialog.destroy()
    
    # Buttons
    ttk.Button(button_frame, text="Save Changes", command=save_changes).pack(side="left", padx=5)
    ttk.Button(button_frame, text="Cancel", command=cancel_edit).pack(side="left", padx=5)
    
    # Konfiguriere Grid-Spalten
    scrollable_frame.columnconfigure(1, weight=1)
    
    # Zentriere Dialog
    dialog.transient(app.root)
    dialog.grab_set()
    app.root.wait_window(dialog)