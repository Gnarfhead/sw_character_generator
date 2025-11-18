def apply_dwarf_dependent_modifiers(character):
    """Apply Dwarf-specific modifiers to the character."""
    character.race = "Dwarf"
    character.darkvision = True
    character.special_abilities += ("Stonecunning", "Saving throw bonus against magic +4",)
    character.add_langs = ("Common", "Dwarvish",)
