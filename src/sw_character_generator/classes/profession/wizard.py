from sw_character_generator.functions.role_dice import wuerfle_1d4

def apply_wizard_dependent_modifiers(character):
    """Apply wizard-specific modifiers to the character."""
    character.profession = "Wizard"
    character.tp_dice = 4
    character.main_stats = ("Intelligence",)
    character.allowed_alignment = ("Good", "Neutral", "Evil")
    character.allowed_races = ("Human", "Halfelf", "Elf")
    character.allowed_weapon = ("staff", "dagger")
    character.allowed_armor = ("none",)
    character.tp = wuerfle_1d4("TP", 1) + character.tp_mod