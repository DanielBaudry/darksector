class NotAvailableSkill(Exception):
    pass


class Skill:
    def __init__(self, name: str, damage: int, cost: int):
        self.name = name
        self.damage = damage
        self.cost = cost