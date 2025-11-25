"""Apply Halfling-specific modifiers to the character."""

def apply_halfling_dependent_modifiers(character):
    """Apply Halfling-specific modifiers to the character."""
    print("DEBUG apply_halfling_dependent_modifiers: ----------------------------------------------------------------")
    print("DEBUG apply_halfling_dependent_modifiers: Applying Halfling dependent modifiers.")
    character.race = "Halfling"
    character.darkvision = False
    character.ranged_atck_mod += 1

    # Ensure save_bonuses is a set
    if not isinstance(character.save_bonuses, set): # Ensure it's a set
        print("DEBUG apply_halfling_dependent_modifiers: Converting character.save_bonuses to set from", type(character.save_bonuses))
        if isinstance(character.save_bonuses, str): # Single string
            character.save_bonuses = {character.save_bonuses} if character.save_bonuses else set() # single ability to set
        elif isinstance(character.save_bonuses, (list, tuple)): # Multiple abilities
            character.save_bonuses = set(character.save_bonuses) # convert list/tuple to set
        else:
            character.save_bonuses = set() # default to empty set
    character.save_bonuses.add("Rettungswurf +4 gegen Magie")
    print("DEBUG apply_halfling_dependent_modifiers: type of character.save_bonuses after assignment:", type(character.save_bonuses))

    # Ensure languages is a set
    print("DEBUG apply_halfling_dependent_modifiers: type of character.languages before assignment:", type(character.languages))
    if not isinstance(character.languages, set): # Ensure it's a set
        print("DEBUG apply_halfling_dependent_modifiers: Converting character.languages to set from", type(character.languages))
        if isinstance(character.languages, str): # Single string
            character.languages = {character.languages} if character.languages else set() # single language to set
        elif isinstance(character.languages, (list, tuple)): # Multiple languages
            character.languages = set(character.languages) # convert list/tuple to set
        else:
            character.languages = set() # default to empty set
    character.languages.clear()  # Clear existing languages
    character.languages.add("Common")
    character.languages.add("Halflingisch")
    print("DEBUG apply_halfling_dependent_modifiers: character.languages after assignment:", character.languages)
    print("DEBUG apply_halfling_dependent_modifiers: type of character.languages after assignment:", type(character.languages))
