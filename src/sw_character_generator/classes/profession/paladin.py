from src.sw_character_generator.functions.role_dice import wuerfle_1d8

def apply_paladin_dependent_modifiers(character):
    """Apply paladin-specific modifiers to the character."""
    
    # Set profession attributes
    character.profession = "paladin"
    character.hp_dice = 8
    character.main_stats = ("strength",)
    character.allowed_alignment = ("good",)
    character.allowed_races = ("human",)
    character.allowed_weapon = ("all",)
    character.allowed_armor = ("all",)
    character.save_throw = 12
    character.special_abilities = (
        "lay on hands: paladins can heal 2 HP by laying on hands or cure a disease once per day",
        "magic items: paladins can use magic items that are usable by fighters. A total of 4 magic items, including max 3 weapons, 1 armor and 1 shield",
        "warhorse: paladins can summon a warhorse which is very intelligent and strong (5 HP dice)",
        "banish evil (Level 8): like the cleric spell",
        "detect evil (Level 8): like the cleric spell",
        "fortress (Level 9): paladins can create a stronghold to gather followers",
    )
    character.immunity += (
        "immunity against disease",
    )

    # Calculate total HP
    character.hp = wuerfle_1d8(1) + character.hp_mod
    if character.hp < 1:
        character.hp = 1

    # Calculate XP bonus
    if character.stat_str >= 13:
        character.xp_bonus += 5
