from abc import ABC, abstractmethod

from domain.player.player import Player


class PlayerRepository(ABC):
    @abstractmethod
    def get_player_by_user_id(self, user_id: int) -> Player:
        pass

    @abstractmethod
    def save_for_user(self, user_id: int, player: Player) -> None:
        pass
