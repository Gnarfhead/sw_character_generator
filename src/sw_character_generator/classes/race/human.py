def apply_human_dependent_modifiers(character):
    """Apply Human-specific modifiers to the character."""
    print("DEBUG apply_human_dependent_modifiers: ----------------------------------------------------------------")
    print("DEBUG apply_human_dependent_modifiers: Applying Human dependent modifiers.")
    character.race = "Human"
    character.darkvision = False
    
    if character.languages is not None: # Check if languages set exists
        character.languages.clear()
    if not character.languages: # Initialize languages set if it doesn't exist
        character.languages = set()
    character.languages.add("Common",)
