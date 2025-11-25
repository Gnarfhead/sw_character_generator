def apply_elf_dependent_modifiers(character):
    """Apply Elf-specific modifiers to the character."""
    print("DEBUG apply_elf_dependent_modifiers: ----------------------------------------------------------------")
    print("DEBUG apply_elf_dependent_modifiers: Applying Elf dependent modifiers.")
    character.race = "Elf"
    character.darkvision = True
    character.special_abilities.update("Geheimtüren finden: Aktiv 4:6, Passiv:1:6")
    character.immunity.update("Ghulische Lähmung")


    if character.languages is not None: # Check if languages set exists
        character.languages.clear()
    if not character.languages: # Initialize languages set if it doesn't exist
        character.languages = set()
    character.languages.update("Common", "Elbisch")
