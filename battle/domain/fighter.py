from abc import ABC

from domain.ability import AllAbilities


class Fighter(ABC):
    def __init__(self, health: int):
        self.health = health
        self.abilities = [AllAbilities.BASIC_ABILITY]

    def inflict_damage(self, fighter: 'Fighter', damage: int):
        fighter.receive_damage(damage)

    def receive_damage(self, damage: int):
        self.health = int(max(0, self.health - damage))

    @property
    def is_dead(self):
        return self.health <= 0
