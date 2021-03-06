from enum import Enum
from random import randint

from src.domain.expedition_rewards_generator.expedition_rewards_generator import ExpeditionRewardsGenerator
from src.domain.player.player import Player
from src.domain.expedition.sector import Sector
from src.domain.sector_monsters_generator.sector_monsters_generator import SectorMonstersGenerator


class ExpeditionStatus(Enum):
    in_progress = 'IN PROGRESS'
    success = 'SUCCESS'
    failed = 'FAILED'


class Expedition:
    def __init__(self,
                 player: Player,
                 sector_monsters_generator: SectorMonstersGenerator,
                 expedition_rewards_generator: ExpeditionRewardsGenerator = None,
                 identifier: int = None,
                 sector: Sector = None,
                 sector_level: int = 1,
                 status: ExpeditionStatus = ExpeditionStatus.in_progress):
        self.identifier = identifier
        self.sector_monsters_generator = sector_monsters_generator
        self.expedition_rewards_generator = expedition_rewards_generator
        self.player = player
        self.status = status
        if self.status != ExpeditionStatus.in_progress:
            self.sector = None
        else:
            self.sector = sector if sector else Sector(sector_monsters_generator=self.sector_monsters_generator)
        self.sector_level = sector_level
        self.total_level = 3
        self.credit_rewards = None
        self.gear_reward = None

    def complete_level(self):
        if not self.sector:
            return

        if not self.sector.is_cleared():
            return

        sector_level_experience = self.sector.rewards()
        self.player.gain_experience(sector_level_experience)

        # TODO: remove
        self.player.energy = self.player.max_energy
        self.player.armor = self.player.max_armor
        self.player.damage = self.player.max_damage

        if self.sector_level == self.total_level:
            self.status = ExpeditionStatus.success
            self.sector = None
            self.credit_rewards = self.expedition_rewards_generator.generate_credit_rewards()
            self.player.gain_credits(credits_amount=self.credit_rewards)
            self.gear_reward = self.expedition_rewards_generator.generate_random_gear_rewards()
            [self.player.receive_gear(gear) for gear in self.gear_reward]
            return
        else:
            self.sector_level += 1
            self.sector = Sector(sector_monsters_generator=self.sector_monsters_generator)
        return

    def end_turn(self):
        if not self.sector:
            return

        if sum([sector_monster.quantity for sector_monster in self.sector.monsters]) == 0:
            return self.complete_level()

        sector_monster_number = len(self.sector.monsters)
        monster_index = 0 if sector_monster_number else randint(0, sector_monster_number)
        self.sector.monsters[monster_index].attack(self.player)

        self.player.energy = self.player.max_energy

        if self.player.is_dead():
            self.status = ExpeditionStatus.failed
