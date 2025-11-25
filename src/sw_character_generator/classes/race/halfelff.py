def apply_halfelf_dependent_modifiers(character):
    """Apply Halfelf-specific modifiers to the character."""
    print("DEBUG apply_halfelf_dependent_modifiers: ----------------------------------------------------------------")
    print("DEBUG apply_halfelf_dependent_modifiers: Applying Halfelf dependent modifiers.")
    character.race = "Halfelf"
    character.darkvision = True

    # Ensure special_abilities is a set
    if not isinstance(character.special_abilities, set): # Ensure it's a set
        print("DEBUG apply_halfelf_dependent_modifiers: Converting character.special_abilities to set from", type(character.special_abilities))
        if isinstance(character.special_abilities, str): # Single string
            character.special_abilities = {character.special_abilities} if character.special_abilities else set() # single ability to set
        elif isinstance(character.special_abilities, (list, tuple)): # Multiple abilities
            character.special_abilities = set(character.special_abilities) # convert list/tuple to set
        else:
            character.special_abilities = set() # default to empty set
    character.special_abilities.add("Geheimtüren finden: Aktiv 4:6")
    print("DEBUG apply_halfelf_dependent_modifiers: type of character.special_abilities after assignment:", type(character.special_abilities))

    # Ensure languages is a set
    print("DEBUG apply_halfelf_dependent_modifiers: type of character.languages before assignment:", type(character.languages))
    if not isinstance(character.languages, set): # Ensure it's a set
        print("DEBUG apply_halfelf_dependent_modifiers: Converting character.languages to set from", type(character.languages))
        if isinstance(character.languages, str): # Single string
            character.languages = {character.languages} if character.languages else set() # single language to set
        elif isinstance(character.languages, (list, tuple)): # Multiple languages
            character.languages = set(character.languages) # convert list/tuple to set
        else:
            character.languages = set() # default to empty set
    character.languages.clear()  # Clear existing languages
    character.languages.add("Common")
    character.languages.add("Elbisch")
    print("DEBUG apply_halfelf_dependent_modifiers: character.languages after assignment:", character.languages)
    print("DEBUG apply_halfelf_dependent_modifiers: type of character.languages after assignment:", type(character.languages))
