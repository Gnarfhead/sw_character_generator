"""Utility functions for handling fullscreen and maximized window states on Linux."""

import tkinter as tk

def toggle_maximize(self, event=None):
    """Toggle between maximized and normal window state."""
    try:
        current_state = self.root.state()
        if current_state == 'normal':
            self.root.state('zoomed')
        else:
            self.root.state('normal')
    except tk.TclError:
        # Linux fallback - toggle geometry
        if self.root.geometry().startswith(f"{self.root.winfo_screenwidth()}x"):
            self.root.geometry("900x600+100+100")  # Normal size
        else:
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            self.root.geometry(f"{screen_width}x{screen_height}+0+0")