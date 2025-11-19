def apply_elf_dependent_modifiers(character):
    """Apply Elf-specific modifiers to the character."""
    print("DEBUG apply_elf_dependent_modifiers: Applying Elf dependent modifiers.")
    character.race = "Elf"
    character.darkvision = True
    character.special_abilities += ("Geheimtüren finden: Aktiv 4:6, Passiv:1:6",)
    character.immunity += ("Ghulische Lähmung",)
    character.add_langs = ("Common", "Elbisch",)
