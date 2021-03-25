from domain.fighter import Fighter


class Monster(Fighter):
    def __init__(self, health: int):
        super().__init__(health)
        self.damage = 2
        self.name = f'Monster'
