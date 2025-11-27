"""Module to manage saving throw for characters in the SW Character Generator."""

def calculate_saving_throw(character):
    """Calculate saving throws based on character attributes."""
    print("DEBUG calculate_saving_throws: ----------------------------------------------------------------")

    # Validate character input
    if character is None:
        raise ValueError("ERROR calculate_saving_throw: No character provided for saving throws calculation.")

    # Convert level to int if it's a string
    try:
        print("DEBUG calculate_saving_throw: character.level type is", type(character.level), "with value", character.level)
        current_level = int(character.level)
        print("DEBUG calculate_saving_throw: current_level converted to int:", current_level)
    except (ValueError, TypeError):
        print("DEBUG calculate_saving_throw: current_level type is", type(current_level))
        print("ERROR calculate_saving_throw: Could not convert level to int, using 1 as fallback")
        current_level = 1

    # Helper: sichere Lookup + Konvertierung in int (falls möglich)
    def _get_prof_val_int(mapping, lvl, default=0):
        if not mapping:
            return default
        # versuche direkten Key und String-Key
        if lvl in mapping:
            val = mapping[lvl]
        elif str(lvl) in mapping:
            val = mapping[str(lvl)]
        else:
            val = mapping.get(lvl, mapping.get(str(lvl), default))
        try:
            return int(val)
        except Exception:
           return default
            
    # Convert profession skill mappings to int values
    print("DEBUG calculate_saving_throw: Converting mappings to int values.")
    character.saving_throw_to_int = _get_prof_val_int(character.save_throw_progression, current_level, 0)
    print("DEBUG calculate_saving_throw: saving_throw_to_int set to", character.saving_throw_to_int)
    character.save_throw = character.saving_throw_to_int
    print("DEBUG calculate_saving_throw: Final save_throw is", character.save_throw)

        