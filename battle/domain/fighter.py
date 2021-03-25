from abc import ABC
from typing import Optional

from domain.ability import AllAbilities


class FighterAbility:
    def __init__(self, ability: AllAbilities):
        self.ability = ability
        self.turn_cooldown = 0

    def set_cooldown(self, value: Optional[int] = None):
        self.turn_cooldown = value if value else self.ability.value.turn_cooldown

    def is_on_cooldown(self) -> bool:
        if self.turn_cooldown > 0:
            return True
        return False

    def reduce_cooldown(self, value: int = 1):
        self.turn_cooldown = self.turn_cooldown - value


class Fighter(ABC):
    def __init__(self, health: int):
        self.health = health
        self.abilities = [FighterAbility(AllAbilities.BASIC_ABILITY)]

    def inflict_damage(self, fighter: 'Fighter', damage: int):
        fighter.receive_damage(damage)

    def receive_damage(self, damage: int):
        self.health = int(max(0, self.health - damage))

    @property
    def is_dead(self):
        return self.health <= 0

    def use_ability(self, ability_to_use: AllAbilities) -> bool:
        for fighter_ability in self.abilities:
            if ability_to_use == fighter_ability.ability:
                fighter_ability.set_cooldown()
                return True
        return False

    def reduce_abilities_cooldown(self):
        for fighter_ability in self.abilities:
            fighter_ability.reduce_cooldown()

    def is_ability_on_cooldown(self, ability_to_use: AllAbilities) -> bool:
        for fighter_ability in self.abilities:
            if ability_to_use == fighter_ability.ability:
                return fighter_ability.is_on_cooldown()
        return False
