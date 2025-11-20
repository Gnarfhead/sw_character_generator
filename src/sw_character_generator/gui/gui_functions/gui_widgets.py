"""Common GUI widgets for the  character generator application."""
import tkinter.ttk as ttk

PADX = 8
PADY = 6
ENTRY_WIDTH = 20

def widget_label(parent, text, row, column, **grid_opts):
    """Create a Label widget in a grid."""
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY, **grid_opts)
    return lbl

def widget_entry(parent, text, row, column, var=None, width=ENTRY_WIDTH, columnspan=1, **grid_opts):
    """Create a labeled Entry widget (or other text input widget) in a grid."""
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY)
    ent = ttk.Entry(parent, textvariable=var, width=width)
    ent.grid(row=row, column=column + 1, columnspan=columnspan, sticky="ew", padx=PADX, pady=PADY, **grid_opts)
    return lbl, ent

def widget_combobox(parent, text, row, column, var=None, values=None, width=ENTRY_WIDTH, **grid_opts):
    """Create a labeled Combobox widget in a grid."""
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY)
    combo = ttk.Combobox(parent, textvariable=var, values=values or [], width=width, state="readonly")
    combo.grid(row=row, column=column + 1, sticky="ew", padx=PADX, pady=PADY, **grid_opts)
    return lbl, combo

def widget_spinbox(parent, text, row, column, var=None, from_=0, to=100, width=ENTRY_WIDTH, **grid_opts):
    """Create a labeled Spinbox widget in a grid."""
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY)
    spin = ttk.Spinbox(parent, textvariable=var, from_=from_, to=to, width=width)
    spin.grid(row=row, column=column + 1, sticky="ew", padx=PADX, pady=PADY, **grid_opts)
    return lbl, spin

def widget_button(parent, text, row, column, command=None, **grid_opts):
    """Create a labeled Button widget in a grid."""
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY)
    btn = ttk.Button(parent, text="Modify", command=command)
    btn.grid(row=row, column=column + 1, sticky="ew", padx=PADX, pady=PADY, **grid_opts)
    return lbl, btn

def widget_checkbutton(parent, text, row, column, var=None, **grid_opts):
    """Create a labeled Checkbutton widget in a grid."""
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY)
    chk = ttk.Checkbutton(parent, variable=var)
    chk.grid(row=row, column=column + 1, sticky="w", padx=PADX, pady=PADY, **grid_opts)
    return lbl, chk