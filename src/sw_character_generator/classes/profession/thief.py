

def apply_thief_dependent_modifiers(character):
    """Apply thief-specific modifiers to the character."""

    # Set profession attributes
    character.profession = "thief"
    character.hp_dice = 6
    character.main_stats = ("dexterity",)
    character.allowed_alignment = ("neutral", "evil")
    character.allowed_races = ("human", "halfling", "elf", "dwarf")
    character.allowed_weapon = ("light weapons",)
    character.allowed_armor = ("light",)
    character.save_throw = 15
    character.delicate_tasks = 15
    character.hide_in_shadows = 10
    character.hear_sounds = "3:6"
    character.move_silently = 20
    character.open_locks = 10
    character.climb_walls = 85

    character.save_bonuses = set()
    character.save_bonuses.update("+2 against traps and mechanical devices: Include traps, wands and magical devices")

    character.immunity = set()

    character.special_abilities = set()
    character.special_abilities.add("sneak attack: thieves gain a +4 bonus to attack and damage rolls are doubled when attacking opponent from behind")
    character.special_abilities.add("read languages  (Level 3): thieves can read all written languages; 80% chance to understand maps and written information")
    character.special_abilities.add("read magic language (Level 9): thieves can read magic inscriptions on magical items and scrolls and cast wizard-spells from scrolls")
    character.special_abilities.add("create guild (Level 9): thieves can create a thieves' guild to gather followers")

    character.xp_bonus = 0
    character.parry = 0

   # XP progression
    character.xp_progression = {
        1: 0,
        2: 1500,
        3: 3000,
        4: 6000,
        5: 12000,
        6: 24000,
        7: 48000,
        8: 96000,
        9: 192000,
        10: 275000,
        11: 400000,
        12: 550000,
        13: 750000,
        14: 850000,
        15: 1000000,
        16: 1150000,
        17: 1300000,
        18: 1450000,
        19: 1600000,
        20: 1750000,
    }

    # Save throw progression
    character.save_throw_progression = {
        1: 15,
        2: 14,
        3: 13,
        4: 12,
        5: 11,
        6: 10,
        7: 9,
        8: 8,
        9: 7,
        10: 6,
        11: 5,
        12: 4,
        13: 4,
        14: 4,
        15: 4,
        16: 4,
        17: 4,
        18: 4,
        19: 4,
        20: 4,
    }

    # Spells per level
    character.spells_lvl1 = 0
    character.spells_lvl2 = 0
    character.spells_lvl3 = 0
    character.spells_lvl4 = 0
    character.spells_lvl5 = 0
    character.spells_lvl6 = 0
    character.spells_lvl7 = 0
    character.spells_lvl8 = 0
    character.spells_lvl9 = 0
