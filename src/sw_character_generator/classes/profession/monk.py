from src.sw_character_generator.functions.role_dice import wuerfle_1d4

def apply_monk_dependent_modifiers(character):
    """Apply monk-specific modifiers to the character."""
    
    # Set profession attributes
    character.profession = "monk"
    character.hp_dice = 4
    character.main_stats = ("wisdom",)
    character.allowed_alignment = ("neutral", "evil", "good")
    character.allowed_races = ("human",)
    character.allowed_weapon = ("all",)
    character.allowed_armor = ("none",)
    character.save_throw = 15
    character.delicate_tasks = 15
    character.hide_in_shadows = 10
    character.hear_sounds = "3:6"
    character.move_silently = 20
    character.open_locks = 10
    character.climb_walls = 85
    character.save_bonuses = (
        "+2 against paralysis and poison",
    )
    character.immunity = (
        "mastering self (Level 8): immune against mindcontrol, charm and hypnosis; except the spells 'geas' and 'command'",
        "be one with your self (Level 9): also immune against spells 'geas' and 'command'",
    )
    character.special_abilities = (
        "deflect missiles: monks can deflect magic missiles and arrows with a successful save throw",
        "magic items: you can't use magic healing potions. Monks can only use magic weapons and rings",
        "deadly strike: if attack roll is 5 points above opponents AC, chance is 75% to stun opponent for 2d6 rounds; opponents less 1 TP die instantly die by 25% chance",
        "alertness: your group isn't easy to surprise; opponents chance ist 1:6",
        "weapon damage (Level 2): +1 damage when using a weapon",
        "talk to animals (Level 4): monks can communicate with animals",
        "feather fall (Level 5): monks can fall from 6m height without taking damage",
        "mastering silence (Level 5): you can play dead for 1d6 *  monk level * 10 minutes",
        "mastering mind (Level 6): read you thoughts don't work with 90% chance",
        "weaponless combat (Level 6): when fight unarmed, you can strike multiple times",
        "mastering body (Level 7): you can heal yourself 1d6+1 TP per day",
        "create monastery (Level 11): monks can create a monastery to gather followers",
        "harmony touch (Level 13): connect through touch with another living being when TP die is equal or less; stop the heart and kill the being instantly",
        
    )
    character.xp_bonus = 0
    character.parry = 0
    character.spells_lvl1 = 0
    character.spells_lvl2 = 0
    character.spells_lvl3 = 0
    character.spells_lvl4 = 0
    character.spells_lvl5 = 0
    character.spells_lvl6 = 0
    character.spells_lvl7 = 0
    character.spells_lvl8 = 0
    character.spells_lvl9 = 0


    # Calculate total HP
    character.hp = wuerfle_1d4(1) + character.hp_mod
    if character.hp < 1:
        character.hp = 1

    # Calculate XP bonus
    if character.stat_wis >= 13:
        character.xp_bonus += 5
