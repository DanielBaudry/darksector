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
    def __init__(self, effect: AbilityEffect, remaining_turns: Optional[int] = None):
        self.effect = effect
        self.remaining_turns = effect.turn_duration if not remaining_turns else remaining_turns

    def decrease_duration(self):
        self.remaining_turns = max(0, self.remaining_turns - 1)


class Fighter(ABC):
    def __init__(self, health: int, damage: int, fighter_effects: List[FighterEffect] = []):
        self.health = health
        self.damage = damage
        self.abilities = [FighterAbility(AllAbilities.BASIC_ABILITY)]
        self.fighter_effects = fighter_effects

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

    def add_effects(self, effects: List[AbilityEffect]):
        for effect in effects:
            self.fighter_effects.append(FighterEffect(effect))

    def apply_effects(self) -> bool:
        for fighter_effect in self.fighter_effects:
            # TODO: very moche (extract in apply_effect method is a start)
            if (fighter_effect.effect.turn_tick == 0
                and fighter_effect.remaining_turns == fighter_effect.effect.turn_duration) \
                    or (fighter_effect.effect.turn_tick != 0 and
                        fighter_effect.remaining_turns % fighter_effect.effect.turn_tick == 0):
                effect = fighter_effect.effect
                # TODO: we can find a better way
                if effect.fighter_trait == 'health':
                    self.health = effect.compute_effect(self.health)
                elif effect.fighter_trait == 'damage':
                    self.damage = effect.compute_effect(self.damage)
                else:
                    return False
        return True

    def reverse_effect(self, fighter_effect) -> bool:
        effect = fighter_effect.effect
        # TODO: we can find a better way
        if effect.fighter_trait == 'health':
            self.health = effect.compute_reverse_effect(self.health)
        elif effect.fighter_trait == 'damage':
            self.damage = effect.compute_reverse_effect(self.damage)
        else:
            return False
        return True

    # TODO: can be better
    def reduce_effects_cooldown(self):
        active_effects = []
        for fighter_effect in self.fighter_effects:
            fighter_effect.decrease_duration()
            if fighter_effect.remaining_turns > 0:
                active_effects.append(fighter_effect)
            else:
                if fighter_effect.effect.turn_duration > 0:
                    self.reverse_effect(fighter_effect)
        self.fighter_effects = active_effects
