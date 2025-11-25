def apply_halfelf_dependent_modifiers(character):
    """Apply Halfelf-specific modifiers to the character."""
    print("DEBUG apply_halfelf_dependent_modifiers: ----------------------------------------------------------------")
    print("DEBUG apply_halfelf_dependent_modifiers: Applying Halfelf dependent modifiers.")
    character.race = "Halfelf"
    character.darkvision = True
    character.special_abilities.update("Geheimtüren finden: Aktiv 4:6")

    character.languages = set()
    character.languages.update("Common")
    character.languages.update("Elvish")
