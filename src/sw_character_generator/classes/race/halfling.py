"""Apply Halfling-specific modifiers to the character."""

def apply_halfling_dependent_modifiers(character):
    """Apply Halfling-specific modifiers to the character."""
    print("DEBUG apply_halfling_dependent_modifiers: ----------------------------------------------------------------")
    print("DEBUG apply_halfling_dependent_modifiers: Applying Halfling dependent modifiers.")
    character.race = "Halfling"
    character.darkvision = False
    character.ranged_atck_mod += 1
    character.save_bonuses.update("Rettungswurf +4 gegen Magie")

    character.languages = set()
    character.languages.update("Common") 
    character.languages.update("Halflingisch")
