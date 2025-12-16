"""GUI functions for magic spell table widget."""

import tkinter.ttk as ttk


def create_spell_table_widget(app):
    """Create a Treeview under magic_content_frame to display character.spell_table."""
    print("DEBUG create_spell_table_widget: ----------------------------------------------------------------")
    
    # Add label above the table
    spell_table_label = ttk.Label(app.magic_content_frame, text="Spells for:", 
                                   font=("TkDefaultFont", 10, "bold"), 
                                   style="Standard.TLabel")
    spell_table_label.grid(row=4, column=0, columnspan=4, sticky="w", padx=6, pady=(12, 2))
    
    # Initial setup with maximum possible columns (will be reconfigured in update)
    spell_levels = [str(i) for i in range(1, 10)]  # ["1", "2", ..., "9"]
    tree = ttk.Treeview(app.magic_content_frame, columns=spell_levels, show="tree headings", height=10)
    
    # Configure first column (tree column) as "Char Level"
    tree.heading("#0", text="Char Level")
    tree.column("#0", width=100, anchor="center")
    
    # Configure all spell level columns (will be hidden/shown dynamically)
    for i, lvl in enumerate(spell_levels, start=1):
        tree.heading(f"#{i}", text=f"Spell Lvl {lvl}")
        tree.column(f"#{i}", width=80, anchor="center")

    # Vertical scrollbar
    vs = ttk.Scrollbar(app.magic_content_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vs.set)
    tree.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=6, pady=6)
    vs.grid(row=5, column=4, sticky="ns", padx=(0,6), pady=6)

    # Store on app for later updates
    app.spell_table_tree = tree
    app.spell_table_label = spell_table_label  # ← Speichere Label für spätere Updates

def update_spell_table_widget(app):
    """Refresh the Treeview to reflect app.new_player.spell_table and highest_spell_level."""
    print("DEBUG update_spell_table_widget: ----------------------------------------------------------------")
    tree: ttk.Treeview = getattr(app, "spell_table_tree", None)
    if tree is None:
        return
    
    # Update label with current profession
    spell_table_label = getattr(app, "spell_table_label", None)
    if spell_table_label:
        profession = getattr(app.new_player, "profession", "Undefined")
        spell_table_label.config(text=f"Spells for Profession: {profession}")

    # Clear existing rows
    for iid in tree.get_children():
        tree.delete(iid)

    # Get highest spell level from character
    max_spell_lvl = getattr(app.new_player, "highest_spell_level", 0)
    if max_spell_lvl <= 0:
        max_spell_lvl = 9  # Fallback to show all columns if not set
    
    # Reconfigure visible columns based on highest_spell_level
    visible_cols = [str(i) for i in range(1, min(max_spell_lvl + 1, 10))]
    tree["displaycolumns"] = visible_cols  # Only show columns up to highest_spell_level
    
    # Update column headings for visible columns
    for i in range(1, len(visible_cols) + 1):
        tree.heading(f"#{i}", text=f"Spell Lvl {i}")

    sp_table = getattr(app.new_player, "spell_table", {}) or {}
    if not isinstance(sp_table, dict) or len(sp_table) == 0:
        # Show empty row with dashes only for visible columns
        tree.insert("", "end", text="-", values=["-"] * len(visible_cols))
        return

    # Determine character levels (sorted)
    char_levels = sorted(sp_table.keys())
    for char_lvl in char_levels:
        spell_slots = sp_table[char_lvl]
        # Build values list: spell slots only up to highest_spell_level
        values = [str(spell_slots.get(spell_lvl, 0)) for spell_lvl in range(1, max_spell_lvl + 1)]
        tree.insert("", "end", text=str(char_lvl), values=values)