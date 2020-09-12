from typing import Optional

from domain.gear.gear_repository import GearRepository
from domain.player.player import Player
from domain.player.player_gear import PlayerGear
from domain.player.player_repository import PlayerRepository
from domain.skill.skill_repository import SkillRepository
from infrastructure.repository.db import db
from infrastructure.repository.player.player_gear_sql import PlayerGearSQL
from infrastructure.repository.player.player_sql import PlayerSQL
from infrastructure.repository.player.player_mapper import to_domain, to_sql_entity


class PlayerSQLRepository(PlayerRepository):
    def __init__(self, skill_repository: SkillRepository, gear_repository: GearRepository):
        self.skill_repository = skill_repository
        self.gear_repository = gear_repository

    def get_player_by_user_id(self, user_id: int) -> Optional[Player]:
        player_sql_entity = PlayerSQL.query.filter(PlayerSQL.userId == user_id).first()
        if not player_sql_entity:
            return None
        player_gears = PlayerGearSQL.query.filter(PlayerGearSQL.playerId == player_sql_entity.id).all()
        gears = [PlayerGear(identifier=player_gear.id,
                            gear=self.gear_repository.get_gear(player_gear.gear_id),
                            is_equipped=player_gear.is_equipped) for player_gear in player_gears]
        skills = self.skill_repository.get_all_skills()
        return to_domain(player_sql_entity, skills, gears)

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
