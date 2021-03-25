from domain.ability import AllAbilities
from domain.fighter import Fighter, FighterAbility


class Player(Fighter):
    def __init__(self, name: str, health: int):
        super().__init__(health)
        self.name = name
        self.damage = 10
        self.abilities.append(FighterAbility(AllAbilities.GRENADE))
