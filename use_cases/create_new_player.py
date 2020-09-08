from domain.player.player import Player
from domain.player.player_repository import PlayerRepository


class CreateNewPlayer:
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    def execute(self, user_id: int, player_name: str) -> None:
        new_player = Player(name=player_name)
        return self.player_repository.save_for_user(user_id=user_id, player=new_player)
