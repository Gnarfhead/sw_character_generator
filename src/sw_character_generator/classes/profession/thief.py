from src.sw_character_generator.functions.role_dice import wuerfle_1d6

def apply_thief_dependent_modifiers(character):
    """Apply thief-specific modifiers to the character."""

    # Set profession attributes
    character.profession = "thief"
    character.tp_dice = 6
    character.main_stats = ("dexterity",)
    character.allowed_alignment = ("neutral", "evil")
    character.allowed_races = ("human", "halfling", "elf", "dwarf")
    character.allowed_weapon = ("light weapons",)
    character.allowed_armor = ("light",)
    character.save_throw = 15
    character.delicate_tasks = 15
    character.hide_in_shadows = 10
    character.hear_sounds = 3
    character.move_silently = 20
    character.open_locks = 10
    character.climb_walls = 85
    character.special_abilities += (
        "sneak attack: thieves gain a +4 bonus to attack and damage rolls are doubled when attacking opponent from behind",
        "read languages  (Level 3): thieves can read all written languages; 80% chance to understand maps and written information",
        "read magic language (Level 9): thieves can read magic inscriptions on magical items and scrolls and cast wizard-spells from scrolls",
        "create guild (Level 9): thieves can create a thieves' guild to gather followers",
    )
    character.save_bonuses += (
        "+2 against traps and mechanical devices: Include traps, wands and magical devices",
    )  

    # Calculate total TP
    character.tp = wuerfle_1d6("TP", 1) + character.tp_mod
    if character.tp < 1:
        character.tp = 1

    # Calculate XP bonus
    if character.stat_dex >= 13:
        character.xp_bonus += 5