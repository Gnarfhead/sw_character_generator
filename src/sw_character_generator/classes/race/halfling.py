"""Apply Halfling-specific modifiers to the character."""

def apply_halfling_dependent_modifiers(character):
    """Apply Halfling-specific modifiers to the character."""
    print("DEBUG apply_halfling_dependent_modifiers: ----------------------------------------------------------------")
    print("DEBUG apply_halfling_dependent_modifiers: Applying Halfling dependent modifiers.")
    character.race = "Halfling"
    character.darkvision = False
    character.ranged_atck_mod += 1

    # Ensure special_abilities is a set
    if not isinstance(character.special_abilities_race, set): # Ensure it's a set
        print("DEBUG apply_halfling_dependent_modifiers: Converting character.special_abilities to set from", type(character.special_abilities_race))
        if isinstance(character.special_abilities_race, str): # Single string
            character.special_abilities_race = {character.special_abilities_race} if character.special_abilities_race else set() # single ability to set
        elif isinstance(character.special_abilities_race, (list, tuple)): # Multiple abilities
            character.special_abilities_race = set(character.special_abilities_race) # convert list/tuple to set
        else:
            character.special_abilities_race = set() # default to empty set
    character.special_abilities_race.clear()  # Clear existing special abilities
    # print("DEBUG apply_halfling_dependent_modifiers: type of character.special_abilities_race after assignment:", type(character.special_abilities_race))

    # Ensure save_bonuses is a set
    if not isinstance(character.save_bonuses_race, set): # Ensure it's a set
        print("DEBUG apply_halfling_dependent_modifiers: Converting character.save_bonuses to set from", type(character.save_bonuses_race))
        if isinstance(character.save_bonuses_race, str): # Single string
            character.save_bonuses_race = {character.save_bonuses_race} if character.save_bonuses_race else set() # single ability to set
        elif isinstance(character.save_bonuses_race, (list, tuple)): # Multiple abilities
            character.save_bonuses_race = set(character.save_bonuses_race) # convert list/tuple to set
        else:
            character.save_bonuses_race = set() # default to empty set
    character.save_bonuses_race.clear()  # Clear existing save bonuses
    character.save_bonuses_race.add("- Rettungswurf +4 gegen Magie")
    # print("DEBUG apply_halfling_dependent_modifiers: type of character.save_bonuses_race after assignment:", type(character.save_bonuses_race))

    # Ensure immunities is a set
    if not isinstance(character.immunities_race, set): # Ensure it's a set
        print("DEBUG apply_halfling_dependent_modifiers: Converting character.immunities to set from", type(character.immunities_race))
        if isinstance(character.immunities_race, str): # Single string
            character.immunities_race = {character.immunities_race} if character.immunities_race else set() # single ability to set
        elif isinstance(character.immunities_race, (list, tuple)): # Multiple abilities
            character.immunities_race = set(character.immunities_race) # convert list/tuple to set
        else:
            character.immunities_race = set() # default to empty set
    character.immunities_race.clear()  # Clear existing immunities
    # print("DEBUG apply_halfling_dependent_modifiers: type of character.immunities_race after assignment:", type(character.immunities_race))

    # Ensure languages is a set
    print("DEBUG apply_halfling_dependent_modifiers: type of character.languages before assignment:", type(character.languages))
    if not isinstance(character.languages, set): # Ensure it's a set
        print("DEBUG apply_halfling_dependent_modifiers: Converting character.languages to set from", type(character.languages))
        if isinstance(character.languages, str): # Single string
            character.languages = {character.languages} if character.languages else set() # single language to set
        elif isinstance(character.languages, (list, tuple)): # Multiple languages
            character.languages = set(character.languages) # convert list/tuple to set
        else:
            character.languages = set() # default to empty set
    character.languages.clear()  # Clear existing languages
    character.languages.add("Common")
    character.languages.add("Halflingisch")
    # print("DEBUG apply_halfling_dependent_modifiers: type of character.languages after assignment:", type(character.languages))
