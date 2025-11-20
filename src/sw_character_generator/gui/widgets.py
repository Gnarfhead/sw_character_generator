"""Common GUI widgets for the  character generator application."""
import tkinter.ttk as ttk

PADX = 8
PADY = 6
ENTRY_WIDTH = 20

def label_entry(parent, text, row, column, var=None, widget="entry", width=ENTRY_WIDTH, columnspan=1, **grid_opts):
    lbl = ttk.Label(parent, text=text)
    lbl.grid(row=row, column=column, sticky="w", padx=PADX, pady=PADY)
    if widget == "entry":
        ent = ttk.Entry(parent, textvariable=var, width=width)
        ent.grid(row=row, column=column + 1, columnspan=columnspan, sticky="ew", padx=PADX, pady=PADY, **grid_opts)
        return lbl, ent
    elif widget == "combobox":
        cb = ttk.Combobox(parent, textvariable=var, state="readonly", width=width)
        cb.grid(row=row, column=column + 1, columnspan=columnspan, sticky="ew", padx=PADX, pady=PADY, **grid_opts)
        return lbl, cb
    else:
        raise ValueError("Unsupported widget type")