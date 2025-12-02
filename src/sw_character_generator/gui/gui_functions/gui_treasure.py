"""Handle changes to the treasure text widget."""

def on_treasure_changed(app):
    """Handle changes to the treasure text widget."""
    print("DEBUG on_treasure_changed: --------------------------------")

    if getattr(app, "is_updating", False):
        return
    content = app.treasure_txt.get("1.0", "end-1c").strip() # Get content
    new: dict[str,int] = {} # New treasure dictionary
    if content: # If there's content
        lines = content.replace(",", "\n").splitlines() # Split into lines
        for line in lines: # Process each line
            s = line.strip() # Strip whitespace
            if not s: # Skip empty lines
                continue
            qty = 1 # Default quantity
            if " x" in s.lower(): # Check for " xN"
                parts = s.rsplit("x", 1) # Split at last 'x'
                name = parts[0].strip() # Get name
                try:
                    qty = int(parts[1].strip())  # Get quantity
                except Exception: 
                    qty = 1 # Default to 1 on error
            elif ":" in s: # Check for ": N"
                parts = s.rsplit(":", 1) # Split at last ':'
                name = parts[0].strip() # Get name
                try:
                    qty = int(parts[1].strip()) # Get quantity
                except Exception:
                    qty = 1 # Default to 1 on error
            else:
                name = s # Just the name
            new[name] = new.get(name, 0) + qty # Update quantity
    app.new_player.treasure = new
    app.treasure_txt.edit_modified(False)
    print(f"DEBUG on_treasure_changed: Updated treasure to: {app.new_player.treasure}")