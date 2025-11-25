def apply_human_dependent_modifiers(character):
    """Apply Human-specific modifiers to the character."""
    print("DEBUG apply_human_dependent_modifiers: ----------------------------------------------------------------")
    print("DEBUG apply_human_dependent_modifiers: Applying Human dependent modifiers.")
    character.race = "Human"
    character.darkvision = False
    
    # Ensure languages is a set
    print("DEBUG apply_human_dependent_modifiers: type of character.languages before assignment:", type(character.languages))
    if not isinstance(character.languages, set): # Ensure it's a set
        print("DEBUG apply_human_dependent_modifiers: Converting character.languages to set from", type(character.languages))
        if isinstance(character.languages, str): # Single string
            character.languages = {character.languages} if character.languages else set() # single language to set
        elif isinstance(character.languages, (list, tuple)): # Multiple languages
            character.languages = set(character.languages) # convert list/tuple to set
        else:
            character.languages = set() # default to empty set
    character.languages.clear()  # Clear existing languages
    character.languages.add("Common")
    print("DEBUG apply_human_dependent_modifiers: character.languages after assignment:", character.languages)
    print("DEBUG apply_human_dependent_modifiers: type of character.languages after assignment:", type(character.languages))
