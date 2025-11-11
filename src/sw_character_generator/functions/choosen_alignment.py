from sw_character_generator.classes.playerclass import PlayerClass

def choosen_alignment_modifiers(player_class: PlayerClass, alignment: str):

    """Apply alignment-specific modifiers to the character."""
    player_class.alignment = "Neutral"
    