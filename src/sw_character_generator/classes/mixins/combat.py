class CombatMixin:
    def deal_melee_damage(self, melee_damage: int) -> int:
        dealt_melee_damage = melee_damage + self.strength_damage_mod
        return dealt_melee_damage

    def deal_ranged_damage(self, ranged_damage: int) -> int:
        dealt_ranged_damage = ranged_damage + self.strength_damage_mod
        return dealt_ranged_damage

    def get_damage(self, damage: int) -> int:
        tp = self.tp - damage
        return tp

    def melee_attack_roll(self) -> int:
        rolled_value = self.roll_dice(1, 20)
        return self.strength_atck_mod + rolled_value

    def ranged_attack_roll(self) -> int:
        rolled_value = self.roll_dice(1, 20)
        return self.ranged_atck_mod + rolled_value

    def roll_initiative(self) -> int:
        rolled_value = self.roll_dice(1, 6)
        return rolled_value