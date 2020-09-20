from random import randint

from src.domain.monster.monster import Monster


class SectorMonster:
    def __init__(self, monster: Monster,
                 initial_quantity: int = None, quantity: int = None):
        self.monster = monster
        self.initial_quantity = initial_quantity if initial_quantity else randint(1, 10)
        self.quantity = quantity if quantity is not None else self.initial_quantity

    def receive_damage(self, damage: int):
        monsters_total_life = self.quantity * self.monster.life
        self.quantity = int(max(0, (monsters_total_life - damage) / self.monster.life))

    def attack(self, player):
        total_damage = self.monster.damage * self.quantity
        player.receive_damage(total_damage)
