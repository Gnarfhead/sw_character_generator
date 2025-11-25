"""Apply Dwarf-specific modifiers to the character."""

def apply_dwarf_dependent_modifiers(character):
    """Apply Dwarf-specific modifiers to the character."""
    print("DEBUG apply_dwarf_dependent_modifiers: ----------------------------------------------------------------")
    print("DEBUG apply_dwarf_dependent_modifiers: Applying Dwarf dependent modifiers.")
    character.race = "Dwarf"
    character.darkvision = True

    character.special_abilities.update("Stonecunning")
    character.special_abilities.update("Saving throw bonus against magic +4")

    character.languages = set()
    character.languages.update("Common")
    character.languages.update("Dwarvish")

