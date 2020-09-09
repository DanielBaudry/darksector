from typing import Optional

from domain.player.player import Player
from domain.player.player_repository import PlayerRepository
from domain.skill.skill_repository import SkillRepository
from infrastructure.repository.db import db
from infrastructure.repository.player.player_sql import PlayerSQL
from infrastructure.repository.player.player_mapper import to_domain, to_sql_entity


class PlayerSQLRepository(PlayerRepository):
    def __init__(self, skill_repository: SkillRepository):
        self.skill_repository = skill_repository

    def get_player_by_user_id(self, user_id: int) -> Optional[Player]:
        player_sql_entity = PlayerSQL.query.filter(PlayerSQL.userId == user_id).first()
        skills = self.skill_repository.get_all_skills()
        return to_domain(player_sql_entity, skills) if player_sql_entity else None

    def save_for_user(self, user_id: int, player: Player) -> None:
        existing_player = PlayerSQL.query \
            .filter(PlayerSQL.userId == user_id) \
            .filter(PlayerSQL.name == player.name) \
            .first()

        if not existing_player:
            existing_player = to_sql_entity(user_id=user_id, player=player)

        db.session.add(existing_player)
        db.session.commit()

    def update(self, player: Player) -> None:
        existing_player = PlayerSQL.query \
            .get(player.identifier)

        existing_player.experience = player.experience
        existing_player.damage = player.damage
        existing_player.energy = player.energy
        existing_player.armor = player.armor
        existing_player.life = player.life

        db.session.add(existing_player)
        db.session.commit()
