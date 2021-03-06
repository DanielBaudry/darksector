from src.domain.expedition.expedition import Expedition
from src.domain.expedition.expedition_repository import ExpeditionRepository
from src.domain.player.player_repository import PlayerRepository


class PlayerEndTurn:
    def __init__(self, player_repository: PlayerRepository, expedition_repository: ExpeditionRepository):
        self.player_repository = player_repository
        self.expedition_repository = expedition_repository

    def execute(self, user_id: int) -> Expedition:
        player = self.player_repository.get_player_by_user_id(user_id=user_id)
        expedition = self.expedition_repository.get_current_expedition(player=player)
        expedition.end_turn()
        self.expedition_repository.save(expedition)
        return expedition
