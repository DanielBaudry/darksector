from domain.expedition.expedition_repository import ExpeditionRepository
from domain.player.player_repository import PlayerRepository


class EquipGear:
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    def execute(self, user_id: int, player_gear_id: int):
        player = self.player_repository.get_player_by_user_id(user_id=user_id)
        player.equip()
        self.expedition_repository.save(expedition)
