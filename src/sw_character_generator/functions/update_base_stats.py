"""Update the base stats for the player character."""

from sw_character_generator.classes.playerclass import PlayerClass


def update_base_stats(player: PlayerClass):
    """
    Update the total base stats for the player by summing base and temporary stats.
    
    Args:
        player: PlayerClass instance
    """
    print("DEBUG update_base_stats: --------------------------------")
    player.stat_str_total = player.stat_str + player.stat_str_temp
    player.stat_dex_total = player.stat_dex + player.stat_dex_temp
    player.stat_con_total = player.stat_con + player.stat_con_temp
    player.stat_wis_total = player.stat_wis + player.stat_wis_temp
    player.stat_int_total = player.stat_int + player.stat_int_temp
    player.stat_char_total = player.stat_char + player.stat_char_temp