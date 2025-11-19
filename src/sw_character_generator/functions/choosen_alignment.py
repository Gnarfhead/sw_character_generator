"""Apply alignment-specific modifiers to the character based on chosen alignment."""
from src.sw_character_generator.classes.playerclass import PlayerClass

def choosen_alignment_modifiers(player_class: PlayerClass, alignment: str):
    """Apply alignment-specific modifiers to the character."""
    if alignment.lower() == "good" and "good" in player_class.allowed_alignment:
        print("DEBUG choosen_alignment_modifiers: Choosing Good alignment - alignment parameter:", alignment)
        player_class.alignment = "Good"
    elif alignment.lower() == "neutral" and "neutral" in player_class.allowed_alignment:
        print("DEBUG choosen_alignment_modifiers: Choosing Neutral alignment - alignment parameter:", alignment)
        player_class.alignment = "Neutral"
    elif alignment.lower() == "evil" and "evil" in player_class.allowed_alignment:
        print("DEBUG choosen_alignment_modifiers: Choosing Evil alignment - alignment parameter:", alignment)
        player_class.alignment = "Evil"
    else:
        raise ValueError("ERROR choosen_alignment_modifiers: Unknown or not allowed alignment:", alignment)
