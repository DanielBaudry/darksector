from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, List

from domain.fighter import Fighter


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


class EventHandler(ABC):
    @abstractmethod
    def update(self, fight_event: FightEvent, fight):
        pass
