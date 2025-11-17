""""Module for rolling and assigning role stats to a character."""
from sw_character_generator.functions.role_dice import wuerfle_3d6

def role_stats(character, chk_opt_4d6dl_var):
    """Rolls and assigns role stats to the character based on the 4d6 drop lowest option."""
    print("Rolling role stats...")
    print("4d6 drop lowest option is set to:", chk_opt_4d6dl_var)

    if chk_opt_4d6dl_var is True:
        character.stat_str = wuerfle_3d6("strength", drop_low=True)
        character.stat_dex = wuerfle_3d6("dexterity", drop_low=True)
        character.stat_con = wuerfle_3d6("constitution", drop_low=True)
        character.stat_int = wuerfle_3d6("intelligence", drop_low=True)
        character.stat_wis = wuerfle_3d6("wisdom", drop_low=True)
        character.stat_cha = wuerfle_3d6("charisma", drop_low=True)
    else:
        character.stat_str = wuerfle_3d6("strength", drop_low=False)
        character.stat_dex = wuerfle_3d6("dexterity", drop_low=False)
        character.stat_con = wuerfle_3d6("constitution", drop_low=False)
        character.stat_int = wuerfle_3d6("intelligence", drop_low=False)
        character.stat_wis = wuerfle_3d6("wisdom", drop_low=False)
        character.stat_cha = wuerfle_3d6("charisma", drop_low=False)
