from typing import List, Optional, Dict

from domain.ability import AllAbilities, SelfAbility, DamageAbility
from domain.event_handler import EventHandler, FightEventType, FightEvent
from domain.monster import Monster
from domain.player import Player


class Fight:
    def __init__(self, player: Player, monsters: List[Monster], fight_turn: int = 1, user_turn: bool = True,
                 is_running: bool = True):
        self.player = player
        self.monsters = monsters
        self.fight_turn = fight_turn
        self.user_turn = user_turn
        self.is_running = is_running
        self.observers = []

    def run(self, monster_index: int, player_ability: AllAbilities = AllAbilities.BASIC_ABILITY) -> Optional[bool]:
        monsters_life = sum([m.health for m in self.monsters])

        if self.player.health > 0 and monsters_life > 0:
            if self.user_turn:
                action_status = self.user_plays(monster_index, player_ability)
                if action_status:
                    self.user_turn = False
                else:
                    raise Exception('Action non autorisée')

            if not self.user_turn:
                self.monsters_plays()

                self.fight_turn += 1
                self.user_turn = True

            monsters_life = sum([m.health for m in self.monsters])

        if self.player.health <= 0 or monsters_life <= 0:
            self.is_running = False
            if self.player.health > 0:
                self.notify(FightEvent(FightEventType.PLAYER_WIN))
                return True
            else:
                self.notify(FightEvent(FightEventType.PLAYER_LOSE))
                return False

    def register(self, event_handler: EventHandler):
        self.observers.append(event_handler)

    def notify(self, action: FightEvent):
        for observers in self.observers:
            observers.update(action, self)

    # TODO: This look like some serialization
    def get_details(self) -> Dict:
        return {
            'fight_turn': self.fight_turn,
            'player': self.player,
            'monsters': self.monsters
        }

    # TODO: probably a class
    # TODO: I dont like isinstance.. maybe some visitor pattern in here ?
    def user_plays(self, monster_index: int, player_ability):
        if self.monsters[monster_index].is_dead:
            return False

        if self.player.is_ability_on_cooldown(player_ability):
            return False

        self.player.use_ability(player_ability)

        ability = player_ability.value
        if isinstance(ability, SelfAbility):
            self.player.add_effects(ability.effects)
        self.player.apply_effects()
        if isinstance(ability, DamageAbility):
            monsters_to_attack = self._monsters_affected_by_ability_radius(ability, monster_index)

            for monster_to_attack in monsters_to_attack:
                if not monster_to_attack.is_dead:
                    total_damage = int(self.player.damage * ability.damage_multiplier)
                    self.player.inflict_damage(monster_to_attack, total_damage)
                    self.notify(FightEvent(FightEventType.USER_ACTION, self.player, [monster_to_attack]))

        self.player.reduce_effects_cooldown()
        self.player.reduce_abilities_cooldown()
        return True

    def _monsters_affected_by_ability_radius(self, ability: DamageAbility, monster_index: int) -> List[Monster]:
        ability_radius = ability.radius
        ability_left_effect = max(0, monster_index - ability_radius)
        ability_right_effect = min(len(self.monsters) - 1, monster_index + ability_radius) + 1
        monsters_affected_by_ability_radius = self.monsters[ability_left_effect:ability_right_effect]
        return monsters_affected_by_ability_radius

    def monsters_plays(self):
        for monster in self.monsters:
            if not monster.is_dead:
                monster.inflict_damage(self.player, monster.damage)
                self.notify(FightEvent(FightEventType.MONSTER_ACTION, monster, [self.player]))
