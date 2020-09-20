from enum import Enum
from typing import List

from src.domain.gear.gear import Gear
from src.domain.gear.gear_repository import GearRepository
from src.infrastructure.repository.gear.in_memory_gear import InMemoryGears
from src.infrastructure.repository.gear.gear_to_domain import to_domain


class GearInMemoryRepository(GearRepository):
    def __init__(self, gears: Enum = InMemoryGears):
        self.gears = [to_domain(gear.value) for gear in gears]

    def get_gear(self, name: str) -> Gear:
        gear = [gear for gear in self.gears if gear.identifier == name][0]
        return gear

    def get_all_gears(self) -> List[Gear]:
        return self.gears
