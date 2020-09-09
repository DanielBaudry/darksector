from random import randint
from typing import List

from domain.monster_repository import MonsterRepository
from domain.sector_monsters import SectorMonster

MAX_TYPE_OF_UNITS = 3


class Sector:
    def __init__(self, monster_repository: MonsterRepository,
                 monsters: List = []):
        self.monster_repository = monster_repository
        self.monsters = monsters if monsters else self.generate_monsters()
        self.experience_reward = sum(
            [monster.monster.experience_gain * monster.initial_quantity for monster in self.monsters])

    def generate_monsters(self) -> List[SectorMonster]:
        monsters = [SectorMonster(monster_repository=self.monster_repository)]
        # monsters_quantity = randint(1, MAX_TYPE_OF_UNITS)
        # for index in range(monsters_quantity):
        return monsters

    def rewards(self) -> int:
        return self.experience_reward

    def get_sector_monster_by_name(self, monster_name: str) -> SectorMonster:
        return [sector_monster for sector_monster in self.monsters if sector_monster.monster.name == monster_name][0]

    def is_cleared(self) -> bool:
        return sum([sector_monster.quantity for sector_monster in self.monsters]) == 0
