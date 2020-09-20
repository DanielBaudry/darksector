from abc import ABC, abstractmethod

from src.domain.expedition.expedition import Expedition
from src.domain.player.player import Player


class ExpeditionRepository(ABC):
    @abstractmethod
    def get_current_expedition(self, player: Player) -> Expedition:
        pass

    @abstractmethod
    def save(self, expedition: Expedition) -> None:
        pass
