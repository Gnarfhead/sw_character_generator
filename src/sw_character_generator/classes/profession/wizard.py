from sw_character_generator.functions.role_dice import wuerfle_1d4

def apply_wizard_dependent_modifiers(character):
    """Apply wizard-specific modifiers to the character."""
    character.profession = "wizard"
    character.tp_dice = 4
    character.main_stats = ("intelligence",)
    character.allowed_alignment = ("good", "neutral", "evil")
    character.allowed_races = ("human", "halfelf", "elf")
    character.allowed_weapon = ("staff", "dagger")
    character.allowed_armor = ("none",)
    character.tp = wuerfle_1d4("TP", 1) + character.tp_mod
    character.save_throw = 15

    """Wizards receive an experience bonus based on their intelligence."""
    if character.stat_int >= 13:
        character.xp_bonus += 5
