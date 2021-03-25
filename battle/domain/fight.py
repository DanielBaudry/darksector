from enum import Enum
from typing import List, Optional, Dict

from domain.ability import AllAbilities
from domain.event_handler import EventHandler
from domain.fighter import Fighter
from domain.monster import Monster
from domain.player import Player


class FightEventType(Enum):
    USER_ACTION = 'user_action'
    MONSTER_ACTION = 'monster_action'
    PLAYER_WIN = 'player_win'
    PLAYER_LOSE = 'player_lose'


class FightEvent:
    def __init__(self, fight_event_type: FightEventType,
                 fighter: Fighter = None, receivers: Optional[List] = None):
        self.fighter = fighter
        self.receivers = receivers
        self.fight_action_type = fight_event_type


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

    def get_details(self) -> Dict:
        return {
            'fight_turn': self.fight_turn,
            'player': self.player,
            'monsters': self.monsters
        }

    def user_plays(self, monster_index: int, player_ability):
        
        ability_radius = player_ability.value.radius
        monsters_to_attack = set(self.monsters[monster_index-ability_radius:monster_index+ability_radius])
        for monster_to_attack in monsters_to_attack:
            if not monster_to_attack.is_dead:
                total_damage = self.player.damage * player_ability.value.power
                self.player.inflict_damage(monster_to_attack, total_damage)
                self.notify(FightEvent(FightEventType.USER_ACTION, self.player, [monster_to_attack]))
            return True
        return False

    def monsters_plays(self):
        attackers = []
        for monster in self.monsters:
            if not monster.is_dead:
                attackers.append(monster)
                monster.inflict_damage(self.player, monster.damage)
                self.notify(FightEvent(FightEventType.MONSTER_ACTION, monster, [self.player]))
