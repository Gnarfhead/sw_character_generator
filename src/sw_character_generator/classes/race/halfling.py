"""Apply Halfling-specific modifiers to the character."""

def apply_halfling_dependent_modifiers(character):
    """Apply Halfling-specific modifiers to the character."""
    print("DEBUG apply_halfling_dependent_modifiers: ----------------------------------------------------------------")
    print("DEBUG apply_halfling_dependent_modifiers: Applying Halfling dependent modifiers.")
    character.race = "Halfling"
    character.darkvision = False
    character.ranged_atck_mod += 1
    character.save_bonuses.add("Rettungswurf +4 gegen Magie")

    if character.languages is not None: # Check if languages set exists
        character.languages.clear()
    if not character.languages: # Initialize languages set if it doesn't exist
        character.languages = set()
    character.languages.update("Common", "Halflingisch")
