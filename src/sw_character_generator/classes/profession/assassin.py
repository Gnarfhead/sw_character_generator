from src.sw_character_generator.functions.role_dice import wuerfle_1d6

def apply_assassin_dependent_modifiers(character):
    """Apply assassin-specific modifiers to the character."""

    # Set profession attributes
    character.profession = "assassin"
    character.hp_dice = 6
    character.main_stats = ("strength", "dexterity", "intelligence")
    character.allowed_alignment = ("neutral", "evil")
    character.allowed_races = ("human",)
    character.allowed_weapon = ("light weapons",)
    character.allowed_armor = ("light",)
    character.save_throw = 15
    character.delicate_tasks = 0
    character.hide_in_shadows = 0
    character.hear_sounds = 0
    character.move_silently = 0
    character.open_locks = 0
    character.climb_walls = 0
    character.save_bonuses = ()
    character.immunity = ()
    character.special_abilities = (
        "sneak attack: assassins gain a +4 bonus to attack and damage rolls are doubled when attacking opponent from behind",
        "poison use: assassins are skilled in the use of poisoning weapons",
        "magic items: assassins can use magic items that are usable by thieves; additionally, they can use magic weapons, leather armor and shields",
        "disguise self: assassins can cast disguise self; danger of being discovered 5% -10% based on intelligence/wisdom of opponent",
        "create guild (Level 14): assassins can create an assassins' guild to gather followers",
    )
    character.xp_bonus = 0
    character.parry = 0

    # Calculate total HP
    character.hp = wuerfle_1d6(1) + character.hp_mod
    if character.hp < 1:
        character.hp = 1

    # Calculate XP bonus
    if character.stat_str >= 13:
        character.xp_bonus += 5
    if character.stat_dex >= 13:
        character.xp_bonus += 5
    if character.stat_int >= 13:
        character.xp_bonus += 5


