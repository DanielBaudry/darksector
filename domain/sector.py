from typing import List

from domain.sector_monsters import SectorMonster
from domain.sector_monsters_generator.sector_monsters_generator import SectorMonstersGenerator

MAX_TYPE_OF_UNITS = 3


class Sector:
    def __init__(self,
                 sector_monsters_generator: SectorMonstersGenerator,
                 monsters: List = []):
        self.sector_monsters_generator = sector_monsters_generator
        self.monsters = monsters if monsters else self.sector_monsters_generator.generate_sector_monsters()
        self.experience_reward = sum(
            [monster.monster.experience_gain * monster.initial_quantity for monster in self.monsters])

    def rewards(self) -> int:
        return self.experience_reward

    def get_sector_monster_by_name(self, monster_name: str) -> SectorMonster:
        return [sector_monster for sector_monster in self.monsters if sector_monster.monster.name == monster_name][0]

    def is_cleared(self) -> bool:
        return sum([sector_monster.quantity for sector_monster in self.monsters]) == 0
