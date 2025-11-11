def apply_human_dependent_modifiers(character):
    """Apply Human-specific modifiers to the character."""
    character.race = "Human"
    character.darkvision = False
    character.add_langs += ("Common",)
