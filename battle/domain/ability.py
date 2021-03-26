from enum import Enum
from typing import List, Union, Optional


class AbilityEffect:
    # life, armor, damage
    def __init__(self, fighter_trait: Union[str, str, str], multiplier: Optional[float], fix_amount: Optional[int],
                 turn_duration: int = 0):
        self.fighter_trait = fighter_trait
        self.multiplier = multiplier
        self.fix_amount = fix_amount
        self.turn_duration = turn_duration


class DamageAbility:
    def __init__(self, name: str, damage_multiplier: float, radius: int, turn_cooldown: int):
        self.name = name
        self.damage_multiplier = damage_multiplier
        self.radius = radius
        self.turn_cooldown = turn_cooldown


class SelfAbility:
    def __init__(self, name: str, effects: List[AbilityEffect], turn_cooldown: int):
        self.name = name
        self.effects = effects
        self.turn_cooldown = turn_cooldown


class AllAbilities(Enum):
    BASIC_ABILITY = DamageAbility('Basic attack', 1, 0, 0)

    GRENADE = DamageAbility('Grenade', 1.2, 1, 2)

    STIMULANT = SelfAbility('Stimulant', [AbilityEffect('health', -0.2, None), AbilityEffect('damage', None, 10, 2)], 4)
    # stimulant: +10 damage for 2 turn / -20% life