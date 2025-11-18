def apply_halfling_dependent_modifiers(character):
    """Apply Halfling-specific modifiers to the character."""
    character.race = "Halfling"
    character.darkvision = False
    character.ranged_atck_mod += 1
    character.save_bonuses += ("Rettungswurf +4 gegen Magie",)
    character.add_langs = ("Common", "Halflingisch",)
