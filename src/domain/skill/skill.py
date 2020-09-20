class Skill:
    def __init__(self,
                 identifier: str,
                 name: str,
                 energy_cost: int,
                 damage: int = 0,
                 armor_bonus: int = 0,
                 damage_bonus: int = 0,
                 life_bonus: int = 0):
        self.identifier = identifier
        self.name = name
        self.damage = damage
        self.energy_cost = energy_cost
        self.armor_bonus = armor_bonus
        self.damage_bonus = damage_bonus
        self.life_bonus = life_bonus
