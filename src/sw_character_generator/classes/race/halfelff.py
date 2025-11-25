def apply_halfelf_dependent_modifiers(character):
    """Apply Halfelf-specific modifiers to the character."""
    print("DEBUG apply_halfelf_dependent_modifiers: ----------------------------------------------------------------")
    print("DEBUG apply_halfelf_dependent_modifiers: Applying Halfelf dependent modifiers.")
    character.race = "Halfelf"
    character.darkvision = True

    print("DEBUG apply_halfelf_dependent_modifiers: type of character.special_abilities before assignment:", type(character.special_abilities))
    character.special_abilities.add("Geheimtüren finden: Aktiv 4:6")
    print("DEBUG apply_halfelf_dependent_modifiers: type of character.special_abilities after assignment:", type(character.special_abilities))

    if character.languages is not None: # Check if languages set exists
        character.languages.clear()
    if not character.languages: # Initialize languages set if it doesn't exist
        character.languages = set()
    character.languages.update("Common", "Elvish")
