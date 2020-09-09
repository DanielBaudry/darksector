from enum import Enum
from random import randint

from domain.sector import Sector
from domain.monster_repository import MonsterRepository
from domain.player.player import Player


class ExpeditionStatus(Enum):
    in_progress = 'IN PROGRESS'
    success = 'SUCCESS'
    failed = 'FAILED'


class Expedition:
    def __init__(self,
                 player: Player,
                 monster_repository: MonsterRepository,
                 identifier: int = None,
                 sector: Sector = None, sector_level: int = 1,
                 status: ExpeditionStatus = ExpeditionStatus.in_progress):
        self.identifier = identifier
        self.monster_repository = monster_repository
        self.player = player
        self.status = status
        if self.status != ExpeditionStatus.in_progress:
            self.sector = None
        else:
            self.sector = sector if sector else Sector(monster_repository=self.monster_repository)
        self.sector_level = sector_level
        self.total_level = 3

    def complete_level(self):
        if not self.sector:
            return

        if not self.sector.is_cleared():
            return

        sector_level_experience = self.sector.rewards()
        self.player.gain_experience(sector_level_experience)
        if self.sector_level == self.total_level:
            self.status = ExpeditionStatus.success
            self.sector = None
            return
        else:
            self.sector_level += 1
            self.sector = Sector(monster_repository=self.monster_repository)
        return

    def end_turn(self):
        if not self.sector:
            return

        sector_monster_number = len(self.sector.monsters)
        monster_index = 0 if sector_monster_number else randint(0, sector_monster_number)
        self.sector.monsters[monster_index].attack(self.player)
        if self.player.is_dead():
            self.status = ExpeditionStatus.failed
