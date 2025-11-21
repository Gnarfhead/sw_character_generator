"""Common GUI widgets for the  character generator application."""
import tkinter.ttk as ttk

PADX = 8
PADY = 6
WIDTH = 5
ENTRY_WIDTH = 25
COLUMNSPAN_DEFAULT = 1

def _assign(owner, mapping):
    """Assign widget references to the owner."""
    if owner is None:  # If the owner is None, do nothing
        return
    for attr, widget in mapping.items():  # Iterate over the mapping
        if attr:  # If the attribute name is not empty
            setattr(owner, attr, widget)  # Assign the widget to the owner



def widget_label(parent, text, row, column, *, owner=None, name_label=None, **grid_opts):
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY, **grid_opts)
    _assign(owner, {name_label: lbl})
    return lbl

def widget_extlabel(parent, text, row, column, var=None, width=WIDTH, columnspan=1, *, owner=None, name_label=None, name_value=None, **grid_opts):
    """Create a labeled Label widget (with textvariable) in a grid."""
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY, **grid_opts)
    ext_lbl = ttk.Label(parent, textvariable=var, width=width)
    ext_lbl.grid(row=row, column=column + 1, columnspan=columnspan, sticky="w", padx=PADX, pady=PADY, **grid_opts)
    _assign(owner, {name_label: lbl, name_value: ext_lbl})
    return lbl, ext_lbl

def widget_entry(parent, text, row, column, var=None, width=ENTRY_WIDTH, columnspan=1, *, owner=None, name_label=None, name_entry=None, **grid_opts):
    """Create a labeled Entry widget (or other text input widget) in a grid."""
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY)
    ent = ttk.Entry(parent, textvariable=var, width=width)
    ent.grid(row=row, column=column + 1, columnspan=columnspan, sticky="ew", padx=PADX, pady=PADY, **grid_opts)
    _assign(owner, {name_label: lbl, name_entry: ent})
    return lbl, ent

def widget_combobox(parent, text, row, column, var=None, values=None, width=WIDTH, state=None, *, owner=None, name_label=None, name_combo=None, **grid_opts):
    """Create a labeled Combobox widget in a grid."""
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY)
    combo = ttk.Combobox(parent, textvariable=var, values=values or [], width=width, state=state)
    combo.grid(row=row, column=column + 1, sticky="ew", padx=PADX, pady=PADY, **grid_opts)
    _assign(owner, {name_label: lbl, name_combo: combo})
    return lbl, combo

def widget_spinbox(parent, text, row, column, var=None, from_=0, to=100, width=WIDTH, *, owner=None, name=None, **grid_opts):
    """Create a labeled Spinbox widget in a grid."""
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY)
    spin = ttk.Spinbox(parent, textvariable=var, from_=from_, to=to, width=width)
    spin.grid(row=row, column=column + 1, sticky="ew", padx=PADX, pady=PADY, **grid_opts)
    _assign(owner, {"spinbox": spin, "name": name})
    return lbl, spin

def widget_button(parent, text, row, column, command=None, *, owner=None, name=None, **grid_opts):
    """Create a labeled Button widget in a grid."""
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY)
    btn = ttk.Button(parent, text="Modify", command=command)
    btn.grid(row=row, column=column + 1, sticky="ew", padx=PADX, pady=PADY, **grid_opts)
    _assign(owner, {"button": btn, "name": name})
    return lbl, btn

def widget_checkbutton(parent, text, row, column, var=None, *, owner=None, name=None, **grid_opts):
    """Create a labeled Checkbutton widget in a grid."""
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY)
    chk = ttk.Checkbutton(parent, variable=var)
    chk.grid(row=row, column=column + 1, sticky="ew", padx=PADX, pady=PADY, **grid_opts)
    _assign(owner, {"checkbutton": chk, "name": name})
    return lbl, chk