from abc import ABC, abstractmethod
from typing import List

from src.domain.gear.gear import Gear


class GearRepository(ABC):
    @abstractmethod
    def get_gear(self, name: str) -> Gear:
        pass

    @abstractmethod
    def get_all_gears(self) -> List[Gear]:
        pass
