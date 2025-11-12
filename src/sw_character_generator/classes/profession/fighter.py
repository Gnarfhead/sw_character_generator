from sw_character_generator.functions.role_dice import wuerfle_1d10

def apply_fighter_dependent_modifiers(character):
    """Apply fighter-specific modifiers to the character."""
    character.profession = "fighter"
    character.tp_dice = 10
    character.main_stats = ("strength",)
    character.allowed_alignment = ("neutral", "evil", "good")
    character.allowed_races = ("human", "halfling", "elf", "dwarf", "halfelf")
    character.allowed_weapon = ("all",)
    character.allowed_armor = ("heavy",)
    character.tp = wuerfle_1d10("TP", 1) + character.tp_mod
