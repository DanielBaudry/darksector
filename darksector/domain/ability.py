from enum import Enum
from typing import List, Union, Optional


# TODO: I don't have a better solution right now,
# so I add +1 to turn duration, to match real fight expected behaviour


class AbilityEffect:
    # TODO: fighter_trait = life, armor, damage, etc.
    def __init__(self, fighter_trait: Union[str, str, str], multiplier: Optional[float], fix_amount: Optional[int],
                 turn_duration: int = 0, turn_tick: int = 0):
        self.fighter_trait = fighter_trait
        self.multiplier = multiplier
        self.fix_amount = fix_amount
        self.turn_duration = turn_duration + 1
        # we want certains ability to have effect each turn
        # so if turn_tick = turn_duration we got one shot abilities
        self.turn_tick = turn_tick

    def compute_effect(self, trait_value: int) -> int:
        if self.fix_amount:
            return trait_value + self.fix_amount
        else:
            return int(trait_value + trait_value * self.multiplier)

    def compute_reverse_effect(self, trait_value: int) -> int:
        if self.fix_amount:
            return trait_value - self.fix_amount
        else:
            return int(trait_value / (1 + self.multiplier))


class DamageAbility:
    def __init__(self, name: str, damage_multiplier: float, radius: int, turn_cooldown: int):
        self.name = name
        self.damage_multiplier = damage_multiplier
        self.radius = radius
        self.turn_cooldown = turn_cooldown + 1


class SelfAbility:
    def __init__(self, name: str, effects: List[AbilityEffect], turn_cooldown: int):
        self.name = name
        self.effects = effects
        self.turn_cooldown = turn_cooldown + 1


class AllAbilities(Enum):
    BASIC_ABILITY = DamageAbility('Basic attack', damage_multiplier=1, radius=0, turn_cooldown=0)

    GRENADE = DamageAbility('Grenade', damage_multiplier=1.2, radius=1, turn_cooldown=2)

    STIMULANT = SelfAbility(
        'Stimulant',
        effects=[
            AbilityEffect('health', multiplier=-0.2, fix_amount=None),
            AbilityEffect('damage', multiplier=None, fix_amount=10, turn_duration=2)
        ],
        turn_cooldown=4
    )
