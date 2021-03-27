from random import randrange
from typing import List


class RewardGeneratorRandom:
    def generate(self, possible_rewards: List):
        random_value = randrange(10)
        rewards = []
        if random_value % 2 == 0:
            rewards = [possible_rewards[0]]
        elif random_value % 3 == 0:
            rewards = [possible_rewards[1]]
        elif random_value % 7 == 0:
            rewards = possible_rewards
        return rewards