from domain.expedition.expedition import Expedition
from domain.expedition.expedition_repository import ExpeditionRepository
from domain.monster.monster_repository import MonsterRepository
from domain.player.player_repository import PlayerRepository


class GetCurrentExpedition:
    def __init__(self, player_repository: PlayerRepository, expedition_repository: ExpeditionRepository,
                 monster_repository: MonsterRepository):
        self.player_repository = player_repository
        self.expedition_repository = expedition_repository
        self.monster_repository = monster_repository

    def execute(self, user_id: int) -> Expedition:
        player = self.player_repository.get_player_by_user_id(user_id=user_id)
        expedition = self.expedition_repository.get_current_expedition(player=player)
        return expedition
