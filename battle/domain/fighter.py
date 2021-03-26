from abc import ABC
from typing import Optional, List

from domain.ability import AllAbilities, AbilityEffect


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
        self.turn_cooldown = max(0, self.turn_cooldown - value)


class FighterEffect:
    def __init__(self, effect):
        self.effect = effect
        self.turn_duration = effect.turn_duration

    def decrease_duration(self):
        self.turn_duration = max(0, self.turn_duration - 1)


class Fighter(ABC):
    def __init__(self, health: int, damage: int):
        self.health = health
        self.damage = damage
        self.abilities = [FighterAbility(AllAbilities.BASIC_ABILITY)]
        self.effects = []

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

    # TODO: refactor needed here, probably not the fighter responsibility to compute all this
    def receive_effect(self, effects: List[AbilityEffect]) -> bool:
        for effect in effects:
            if effect.fighter_trait == 'health':
                if effect.fix_amount:
                    self.health = self.health + effect.fix_amount
                else:
                    self.health = self.health + self.health * effect.multiplier
            elif effect.fighter_trait == 'damage':
                if effect.fix_amount:
                    self.damage = self.damage + effect.fix_amount
                else:
                    self.damage = self.damage + self.damage * effect.multiplier
            else:
                return False
        return True

    def reduce_effects_cooldown(self):
        for fighter_effect in self.effects:
            fighter_effect.reduce_cooldown()
            # TODO: removoe not active effects
