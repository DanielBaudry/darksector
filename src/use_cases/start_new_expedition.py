from src.domain.expedition.expedition import Expedition
from src.domain.expedition.expedition_repository import ExpeditionRepository
from src.domain.monster.monster_repository import MonsterRepository
from src.domain.player.player_repository import PlayerRepository
from src.domain.sector_monsters_generator.sector_monsters_generator import SectorMonstersGenerator


class StartNewExpedition:
    def __init__(self, player_repository: PlayerRepository, expedition_repository: ExpeditionRepository,
                 monster_repository: MonsterRepository):
        self.player_repository = player_repository
        self.expedition_repository = expedition_repository
        self.monster_repository = monster_repository

    def execute(self, user_id: int) -> Expedition:
        player = self.player_repository.get_player_by_user_id(user_id=user_id)
        sector_monsters_generator = SectorMonstersGenerator(
            available_monsters=self.monster_repository.get_all_monsters()
        )
        expedition = Expedition(player=player, sector_monsters_generator=sector_monsters_generator)
        # TODO: remove
        # =================================
        player.life = player.max_life
        player.energy = player.max_energy
        # =================================
        self.expedition_repository.save(expedition)
        return expedition
