from src.domain.expedition.expedition_repository import ExpeditionRepository
from src.domain.player.player_repository import PlayerRepository
from src.domain.skill.skill_repository import SkillRepository


class UseSkillOnMonster:
    def __init__(self, player_repository: PlayerRepository,
                 expedition_repository: ExpeditionRepository,
                 skill_repository: SkillRepository):
        self.player_repository = player_repository
        self.expedition_repository = expedition_repository
        self.skill_repository = skill_repository

    def execute(self, user_id: int, monster_name: str, skill_name: str):
        player = self.player_repository.get_player_by_user_id(user_id=user_id)
        expedition = self.expedition_repository.get_current_expedition(player=player)
        monster = expedition.sector.get_sector_monster_by_name(monster_name=monster_name)
        skill = self.skill_repository.get_skill(name=skill_name)
        player.use_skill(skill=skill, sector_monster=monster)
        self.expedition_repository.save(expedition)
