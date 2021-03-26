from domain.ability import AllAbilities
from domain.fighter import Fighter, FighterAbility


class Player(Fighter):
    def __init__(self, name: str, health: int, damage: int = 10):
        super().__init__(health, damage)
        self.name = name
        self.abilities.append(FighterAbility(AllAbilities.GRENADE))
