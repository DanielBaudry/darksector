from enum import Enum


class Ability:
    def __init__(self, name: str, power: float, radius: int):
        self.name = name
        self.power = power
        self.radius = radius


class AllAbilities(Enum):
    BASIC_ABILITY = Ability('Basic attack', 1, 1)

    GRENADE = Ability('Grenade', 1.2, 2)
