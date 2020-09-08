from domain.expedition.expedition_repository import ExpeditionRepository
from domain.player.player_repository import PlayerRepository


class PlayerAttackMonster:
    def __init__(self, player_repository: PlayerRepository, expedition_repository: ExpeditionRepository):
        self.player_repository = player_repository
        self.expedition_repository = expedition_repository

    def execute(self, user_id: int, monster_name: str):
        player = self.player_repository.get_player_by_user_id(user_id=user_id)
        expedition = self.expedition_repository.get_current_expedition(player=player)
        monster = expedition.sector.get_sector_monster_by_name(monster_name=monster_name)
        player.basic_attack(monster)
        self.expedition_repository.save(expedition)
