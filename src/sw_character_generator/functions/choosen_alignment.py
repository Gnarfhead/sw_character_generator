from sw_character_generator.classes.playerclass import PlayerClass

def choosen_alignment_modifiers(player_class: PlayerClass, alignment: str):

    """Apply alignment-specific modifiers to the character."""

    if alignment.lower() == "good" and "good" in player_class.allowed_alignment:
        return player_class  # No changes for Good alignment
    elif alignment.lower() == "neutral" and "neutral" in player_class.allowed_alignment:
        return player_class  # No changes for Neutral alignment
    elif alignment.lower() == "evil" and "evil" in player_class.allowed_alignment:
        return player_class  # No changes for Evil alignment
    else:
        print("All allowed alignments:", player_class.allowed_alignment)
        raise ValueError("Unknown or not allowed alignment:", alignment)