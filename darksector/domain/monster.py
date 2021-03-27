from domain.fighter import Fighter


class Monster(Fighter):
    def __init__(self, health: int, damage: int = 2):
        super().__init__(health, damage)
        self.name = f'Monster'
