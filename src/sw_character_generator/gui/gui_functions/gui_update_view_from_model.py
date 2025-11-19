"""Update view from model function."""
from dataclasses import asdict

def update_view_from_model(app):
    """Update all GUI-bound variables from the new_player model."""
    with app.suppress_updates(): # Prevent recursive updates
        for field, val in asdict(app.new_player).items(): # Iterate over all fields in the dataclass
            var = getattr(app, f"{field}_var", None) # Get the corresponding GUI variable
            if var is None: # If the GUI variable doesn't exist, skip it
                continue # Skip non-GUI fields
            s = str(val) if val is not None else "" # Convert value to string, handle None
            if var.get() != s: # Only update if the value has changed
                var.set(s) # Update the GUI variable