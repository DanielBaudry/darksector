from abc import ABC, abstractmethod


class EventHandler(ABC):
    @abstractmethod
    def update(self, fight_action, fight):
        pass
