from typing import List

from domain.event_handler import EventHandler
from domain.fight import FightEventType


class DarkZone(EventHandler):
    def __init__(self, levels, possible_rewards, reward_generator, current_level: int = 1):
        self.reward_generator = reward_generator
        self.possible_rewards = possible_rewards
        self.levels = levels
        self.current_level = current_level
        self.rewards = None

    def get_current_level_monsters(self):
        return self.levels[self.current_level - 1]

    def _unlock_reward(self):
        self.rewards = self.reward_generator.generate(self.possible_rewards)

    def update(self, fight_action, fight):
        if fight_action.fight_action_type == FightEventType.PLAYER_WIN and self.current_level == len(self.levels):
            self._unlock_reward()
        elif fight_action.fight_action_type == FightEventType.PLAYER_WIN and self.current_level <= len(self.levels):
            self.current_level += 1

    def get_rewards(self) -> List:
        return self.rewards
