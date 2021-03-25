from typing import List

from domain.ability import AllAbilities
from domain.fighter import Fighter


class Player(Fighter):
    def __init__(self, name: str, health: int):
        super().__init__(health)
        self.name = name
        self.damage = 10
        self.abilities.append(AllAbilities.GRENADE)
