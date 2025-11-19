def apply_human_dependent_modifiers(character):
    """Apply Human-specific modifiers to the character."""
    print("DEBUG apply_human_dependent_modifiers: Applying Human dependent modifiers.")
    character.race = "Human"
    character.darkvision = False
    character.add_langs = ("Common",)
