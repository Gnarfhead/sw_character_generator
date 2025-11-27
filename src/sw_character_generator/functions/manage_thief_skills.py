"""Module to manage thief skills for characters in the SW Character Generator."""

def calculate_thief_skills(character):
    """Calculate thief skills based on character attributes."""
    print("DEBUG calculate_thief_skills: ----------------------------------------------------------------")

    # Validate character input
    if character is None:
        raise ValueError("ERROR calculate_thief_skills: No character provided for thief skills calculation.")

    # Only calculate for thief, assassin, or monk professions
    if character.profession.lower() == "thief" or character.profession.lower() == "assassin" or character.profession.lower() == "monk":
        print("DEBUG calculate_thief_skills: Calculating thief skills for profession", character.profession)

        # Convert level to int if it's a string
        try:
            print("DEBUG calculate_thief_skills: character.level type is", type(character.level), "with value", character.level)
            current_level = int(character.level)
            print("DEBUG calculate_thief_skills: current_level converted to int:", current_level)
        except (ValueError, TypeError):
            print("DEBUG calculate_thief_skills: current_level type is", type(current_level))
            print("ERROR calculate_thief_skills: Could not convert level to int, using 1 as fallback")
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
            
        # Helper: sichere Lookup OHNE int-Konvertierung (für hear_sounds)
        def _get_prof_val_str(mapping, lvl, default="0:6"):
            if not mapping:
                return default
            # versuche direkten Key und String-Key
            if lvl in mapping:
                return mapping[lvl]
            elif str(lvl) in mapping:
                return mapping[str(lvl)]
            else:
                return mapping.get(lvl, mapping.get(str(lvl), default))        

        # Convert profession skill mappings to int values
        print("DEBUG calculate_thief_skills: Converting profession skill mappings to int values.")
        character.delicate_tasks_profession_to_int = _get_prof_val_int(character.delicate_tasks_profession, current_level, 0)
        print("DEBUG calculate_thief_skills: delicate_tasks_profession_to_int is type", type(character.delicate_tasks_profession_to_int), "with value", character.delicate_tasks_profession_to_int) 
        character.climb_walls_profession_to_int = _get_prof_val_int(character.climb_walls_profession, current_level, 0) # no race modifier for climb walls
        print("DEBUG calculate_thief_skills: climb_walls_profession_to_int is type", type(character.climb_walls_profession_to_int), "with value", character.climb_walls_profession_to_int) 
        character.hear_sounds_profession_to_int = _get_prof_val_str(character.hear_sounds_profession, current_level, "0:6") # no race modifier for hear sounds
        print("DEBUG calculate_thief_skills: hear_sounds_profession_to_int is type", type(character.hear_sounds_profession_to_int), "with value", character.hear_sounds_profession_to_int) 
        character.hide_in_shadows_profession_to_int = _get_prof_val_int(character.hide_in_shadows_profession, current_level, "0:6")
        print("DEBUG calculate_thief_skills: hide_in_shadows_profession_to_int is type", type(character.hide_in_shadows_profession_to_int), "with value", character.hide_in_shadows_profession_to_int) 
        character.move_silently_profession_to_int = _get_prof_val_int(character.move_silently_profession, current_level, 0)
        print("DEBUG calculate_thief_skills: move_silently_profession_to_int is type", type(character.move_silently_profession_to_int), "with value", character.move_silently_profession_to_int) 
        character.open_locks_profession_to_int = _get_prof_val_int(character.open_locks_profession, current_level, 0)
        print("DEBUG calculate_thief_skills: open_locks_profession_to_int is type", type(character.open_locks_profession_to_int), "with value", character.open_locks_profession_to_int)

        # Calculate thief skills by adding profession and race modifiers
        print("DEBUG calculate_thief_skills: Calculating thief skills by adding profession and race modifiers.")
        character.delicate_tasks = character.delicate_tasks_profession_to_int + character.delicate_tasks_race
        character.climb_walls = character.climb_walls_profession_to_int # no race modifier for climb walls
        character.hear_sounds = character.hear_sounds_profession_to_int # no race modifier for hear sounds
        character.hide_in_shadows = character.hide_in_shadows_profession_to_int + character.hide_in_shadows_race
        character.move_silently = character.move_silently_profession_to_int + character.move_silently_race
        character.open_locks = character.open_locks_profession_to_int + character.open_locks_race

    else:
        print("DEBUG calculate_thief_skills: Character is not a thief, assassin, or monk. Skipping thief skills calculation.")
        return  # No need to calculate thief skills for non-thief professions

    # Final debug output
    print("DEBUG calculate_thief_skills: Thief skills calculation complete.")   

def reset_thief_skills(character):
    """
    Reset thief skills race modifiers to zero.
    Needed when changing profession away from thief/assassin/monk.
    """
    print("DEBUG reset_thief_skills: ----------------------------------------------------------------")
    
    if character is None:
        raise ValueError("ERROR reset_thief_skills: No character provided for thief skills reset.")

    print("DEBUG reset_thief_skills: Resetting thief skills to default values.")
    character.delicate_tasks_race = 0
    character.hide_in_shadows_race = 0
    character.move_silently_race = 0
    character.open_locks_race = 0


    print("DEBUG reset_thief_skills: Thief skills have been reset.")


