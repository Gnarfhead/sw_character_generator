def apply_human_dependent_modifiers(character):
    """Apply Human-specific modifiers to the character."""
    print("DEBUG apply_human_dependent_modifiers: ----------------------------------------------------------------")
    print("DEBUG apply_human_dependent_modifiers: Applying Human dependent modifiers.")
    character.race = "Human"
    character.darkvision = False
    
    # Ensure special_abilities is a set
    if not isinstance(character.special_abilities, set): # Ensure it's a set
        print("DEBUG apply_human_dependent_modifiers: Converting character.special_abilities to set from", type(character.special_abilities))
        if isinstance(character.special_abilities, str): # Single string
            character.special_abilities = {character.special_abilities} if character.special_abilities else set() # single ability to set
        elif isinstance(character.special_abilities, (list, tuple)): # Multiple abilities
            character.special_abilities = set(character.special_abilities) # convert list/tuple to set
        else:
            character.special_abilities = set() # default to empty set
    # character.special_abilities.clear()  # Clear existing special abilities
    # print("DEBUG apply_human_dependent_modifiers: type of character.special_abilities after assignment:", type(character.special_abilities))

    # Ensure save_bonuses is a set
    if not isinstance(character.save_bonuses, set): # Ensure it's a set
        print("DEBUG apply_human_dependent_modifiers: Converting character.save_bonuses to set from", type(character.save_bonuses))
        if isinstance(character.save_bonuses, str): # Single string
            character.save_bonuses = {character.save_bonuses} if character.save_bonuses else set() # single ability to set
        elif isinstance(character.save_bonuses, (list, tuple)): # Multiple abilities
            character.save_bonuses = set(character.save_bonuses) # convert list/tuple to set
        else:
            character.save_bonuses = set() # default to empty set
    # character.save_bonuses.clear()  # Clear existing save bonuses
    # print("DEBUG apply_human_dependent_modifiers: type of character.save_bonuses after assignment:", type(character.save_bonuses))

    # Ensure immunities is a set
    if not isinstance(character.immunities, set): # Ensure it's a set
        print("DEBUG apply_human_dependent_modifiers: Converting character.immunities to set from", type(character.immunities))
        if isinstance(character.immunities, str): # Single string
            character.immunities = {character.immunities} if character.immunities else set() # single ability to set
        elif isinstance(character.immunities, (list, tuple)): # Multiple abilities
            character.immunities = set(character.immunities) # convert list/tuple to set
        else:
            character.immunities = set() # default to empty set
    # character.immunities.clear()  # Clear existing immunities
    # print("DEBUG apply_human_dependent_modifiers: type of character.immunities after assignment:", type(character.immunities))

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
    # print("DEBUG apply_human_dependent_modifiers: type of character.languages after assignment:", type(character.languages))
