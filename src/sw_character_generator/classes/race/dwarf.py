"""Apply Dwarf-specific modifiers to the character."""

def apply_dwarf_dependent_modifiers(character):
    """Apply Dwarf-specific modifiers to the character."""
    print("DEBUG apply_dwarf_dependent_modifiers: ----------------------------------------------------------------")
    print("DEBUG apply_dwarf_dependent_modifiers: Applying Dwarf dependent modifiers.")
    character.race = "Dwarf"
    character.darkvision = True

    print("DEBUG apply_dwarf_dependent_modifiers: type of character.special_abilities before assignment:", type(character.special_abilities))
    character.special_abilities.add("Stonecunning")
    character.special_abilities.add("Saving throw bonus against magic +4")
    print("DEBUG apply_dwarf_dependent_modifiers: type of character.special_abilities after assignment:", type(character.special_abilities))

    if character.languages is not None: # Check if languages set exists
        character.languages.clear()
    if not character.languages: # Initialize languages set if it doesn't exist
        character.languages = set()
    character.languages.update("Common", "Dwarvish")

