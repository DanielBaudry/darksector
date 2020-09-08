from domain.player.player import Player
from domain.player.player_repository import PlayerRepository


class GetPlayerDetails:
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    def execute(self, user_id: int) -> Player:
        return self.player_repository.get_player_by_user_id(user_id=user_id)
