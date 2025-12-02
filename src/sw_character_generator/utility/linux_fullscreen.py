"""Utility functions for handling fullscreen and maximized window states on Linux."""

import tkinter as tk

def toggle_maximize(app, event=None):
    """Toggle between maximized and normal window state."""
    print("DEBUG toggle_maximize: --------------------------------")
    try:
        current_state = app.root.state()
        if current_state == 'normal':
            app.root.state('zoomed')
        else:
            app.root.state('normal')
    except tk.TclError:
        # Linux fallback - toggle geometry
        if app.root.geometry().startswith(f"{app.root.winfo_screenwidth()}x"): # currently maximized
            app.root.geometry("900x600+100+100")  # Normal size
        else:
            screen_width = app.root.winfo_screenwidth() # Get screen width
            screen_height = app.root.winfo_screenheight() # Get screen height
            app.root.geometry(f"{screen_width}x{screen_height}+0+0") # Maximize