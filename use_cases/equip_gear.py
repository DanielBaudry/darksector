from domain.player.player_repository import PlayerRepository


class EquipGear:
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    def execute(self, user_id: int, player_gear_id: int, to_equip: bool):
        player = self.player_repository.get_player_by_user_id(user_id=user_id)
        player.equip_player_gear(player_gear_id=player_gear_id, to_equip=to_equip)
        self.player_repository.update(player=player)
