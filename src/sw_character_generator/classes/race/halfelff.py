def apply_halfelf_dependent_modifiers(character):
    """Apply Halfelf-specific modifiers to the character."""
    print("DEBUG apply_halfelf_dependent_modifiers: Applying Halfelf dependent modifiers.")
    character.race = "Halfelf"
    character.darkvision = True
    character.special_abilities += ("Geheimtüren finden: Aktiv 4:6",)
    character.add_langs = ("Common", "Elvish",)
