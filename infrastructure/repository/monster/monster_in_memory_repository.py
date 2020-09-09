from enum import Enum
from random import randint

from domain.monster.monster import Monster
from domain.monster.monster_repository import MonsterRepository
from infrastructure.repository.monster.in_memory_monsters import InMemoryMonsters
from infrastructure.repository.monster.monster_to_domain import to_domain


class MonsterInMemoryRepository(MonsterRepository):
    def __init__(self, monsters: Enum = InMemoryMonsters):
        self.monsters = [monster.value for monster in monsters]

    def get_monster(self, name: str) -> Monster:
        monster = [monster for monster in self.monsters if monster['name'] == name][0]
        return to_domain(monster)

    def get_random_monster(self) -> Monster:
        random_monster_index = randint(0, len(self.monsters) - 1)
        return to_domain(self.monsters[random_monster_index])
