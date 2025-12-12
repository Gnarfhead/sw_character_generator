"""Save character data to a JSON file with a timestamped filename."""
import json
import sys
from datetime import datetime
from pathlib import Path
from tkinter import filedialog
from sw_character_generator.classes.playerclass import PlayerClass

def get_default_save_directory() -> str:
    """Get OS-specific default save directory for character files."""
    if sys.platform == "win32":
        # Windows: %USERPROFILE%\Documents\SW Characters
        base = Path.home() / "Documents"
    elif sys.platform == "darwin":
        # macOS: ~/Documents/SW Characters
        base = Path.home() / "Documents"
    else:
        # Linux/Unix: ~/.local/share/sw_character_generator
        base = Path.home() / ".local" / "share" / "sw_character_generator"
    
    save_dir = base / "SW Characters"
    save_dir.mkdir(parents=True, exist_ok=True)
    return str(save_dir)

def save_character(character_data: PlayerClass, parent_window=None) -> None:
    """Save the Character data to a JSON file."""
    print("DEBUG save_character: ----------------------------------------------------------------")
    data = character_data.to_dict()

    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Compose filename
    default_filename = f"{data['player_name']}-{data['profession']}-{data['character_name']}-{timestamp}.json"
    default_filename = default_filename.replace(" ", "_")  # Avoid spaces

    # Get default directory
    default_dir = get_default_save_directory()
    
    # Open file dialog
    file_path = filedialog.asksaveasfilename(
        parent=parent_window,
        title="Save Character As",
        initialdir=default_dir,
        initialfile=default_filename,
        defaultextension=".json",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
    )

    # Check if user cancelled
    if not file_path:
        print("DEBUG save_character: Save operation cancelled by user.")
        return  # User cancelled

    # Write data to file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"DEBUG save_character: Character saved to {file_path}")


def load_character(parent_window=None) -> PlayerClass | None:
    """Load character data from a JSON file."""
    print("DEBUG load_character: ----------------------------------------------------------------")
    
    # get default directory
    default_dir = get_default_save_directory()

    # Ask user for file to load
    file_path = filedialog.askopenfilename(
        parent=parent_window,
        title="Load Character",
        initialdir=default_dir,
        defaultextension=".json",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
    )
    
    # User cancelled
    if not file_path:
        print("Load cancelled by user.")
        return None
    
    # Load file
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    try:
        character = PlayerClass.from_dict(data)
    except KeyError as e:
        raise ValueError("Missing key in character data: {e}") from e

    print("DEBUG load_character: Character loaded from", {file_path})
    return character