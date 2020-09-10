from random import randint
from typing import List

from domain.monster.monster import Monster
from domain.sector_monsters.sector_monsters import SectorMonster


class SectorMonstersGenerator:
    def __init__(self, available_monsters: List[Monster]):
        self.available_monsters = available_monsters

    def generate_sector_monsters(self) -> List[SectorMonster]:
        random_monster_index = randint(0, len(self.available_monsters) - 1)
        initial_quantity = randint(1, 10)
        sector_monsters = [
            SectorMonster(monster=self.available_monsters[random_monster_index],
                          initial_quantity=initial_quantity)
        ]
        return sector_monsters
