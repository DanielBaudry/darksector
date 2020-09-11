from random import randint
from typing import List, Optional

from domain.gear.gear import Gear


class ExpeditionRewardsGenerator:
    def __init__(self, available_gears: List[Gear]):
        self.available_gears = available_gears

    def generate_random_gear_rewards(self) -> List[Optional[Gear]]:
        for i in range(100):
            if randint(0, 100) == i:
                gear_index = randint(0, len(self.available_gears))
                return [self.available_gears[gear_index]]
        return []

    def generate_credit_rewards(self) -> int:
        return randint(800, 1000)
