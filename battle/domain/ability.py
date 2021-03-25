from enum import Enum


class Ability:
    def __init__(self, name: str, power: float, radius: int, turn_cooldown: int):
        self.name = name
        self.power = power
        self.radius = radius
        self.turn_cooldown = turn_cooldown


class AllAbilities(Enum):
    BASIC_ABILITY = Ability('Basic attack', 1, 0, 0)

    GRENADE = Ability('Grenade', 1.2, 1, 2)

    STIMULANT = Ability('Stimulant', 0, 0, 2)

