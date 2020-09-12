from random import randint, random
from typing import List, Optional

from domain.gear.gear import Gear


class ExpeditionRewardsGenerator:
    def __init__(self, available_gears: List[Gear]):
        self.available_gears = available_gears

    def generate_random_gear_rewards(self) -> List[Optional[Gear]]:
        if random() > 0.6:
            gear_index = randint(0, len(self.available_gears))
            return [self.available_gears[gear_index]]
        return []

    def generate_credit_rewards(self) -> int:
        return randint(800, 1000)
