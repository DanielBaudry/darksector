from abc import abstractmethod
from typing import List

from sqlalchemy.testing.plugin.plugin_base import ABC

from domain.monster.monster import Monster


class MonsterRepository(ABC):
    @abstractmethod
    def get_monster(self, name: str) -> Monster:
        pass

    @abstractmethod
    def get_random_monster(self) -> Monster:
        pass

    @abstractmethod
    def get_all_monsters(self) -> List[Monster]:
        pass
