"""Apply alignment-specific modifiers to the character based on chosen alignment."""
from src.sw_character_generator.classes.playerclass import PlayerClass

def choosen_alignment_modifiers(player_class: PlayerClass, alignment: str):
    """Apply alignment-specific modifiers to the character."""

    if alignment.lower() == "good" and "good" in player_class.allowed_alignment:
        #print("DEBUG: Choosing Good alignment - alignment parameter:", alignment)
        player_class.alignment = "Good"
    elif alignment.lower() == "neutral" and "neutral" in player_class.allowed_alignment:
        #print("DEBUG: Choosing Neutral alignment - alignment parameter:", alignment)
        player_class.alignment = "Neutral"
    elif alignment.lower() == "evil" and "evil" in player_class.allowed_alignment:
        #print("DEBUG: Choosing Evil alignment - alignment parameter:", alignment)
        player_class.alignment = "Evil"
    else:
        #print("All allowed alignments:", player_class.allowed_alignment, "Provided alignment:", alignment)
        raise ValueError("Unknown or not allowed alignment:", alignment)
