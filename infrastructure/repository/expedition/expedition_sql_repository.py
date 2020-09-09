from typing import Optional

from domain.expedition.expedition import Expedition, ExpeditionStatus
from domain.expedition.expedition_repository import ExpeditionRepository
from domain.monster_repository import MonsterRepository
from domain.player.player import Player
from domain.sector import Sector
from domain.sector_monsters import SectorMonster
from infrastructure.repository.db import db
from infrastructure.repository.expedition.expedition_sql import ExpeditionSQL
from infrastructure.repository.player.player_sql import PlayerSQL

from infrastructure.repository.sector_monster.sector_monster_sql import SectorMonsterSQL


class ExpeditionSQLRepository(ExpeditionRepository):
    def __init__(self, monster_repository: MonsterRepository):
        self.monster_repository = monster_repository

    def get_current_expedition(self, player: Player) -> Optional[Expedition]:
        current_expedition_sql = ExpeditionSQL.query \
            .filter(ExpeditionSQL.playerId == player.identifier) \
            .filter(ExpeditionSQL.status == ExpeditionStatus.in_progress) \
            .first()

        if not current_expedition_sql:
            return None

        sector_monsters_sql = SectorMonsterSQL.query.filter(
            SectorMonsterSQL.expeditionId == current_expedition_sql.id).all()
        monsters = []
        for sector_monster_sql in sector_monsters_sql:
            monsters.append(
                SectorMonster(
                    monster_repository=self.monster_repository,
                    monster=self.monster_repository.get_monster(sector_monster_sql.monster_name),
                    initial_quantity=sector_monster_sql.initial_quantity,
                    quantity=sector_monster_sql.quantity,
                )
            )
        current_sector = Sector(monster_repository=self.monster_repository, monsters=monsters)

        return Expedition(
            identifier=current_expedition_sql.id,
            player=player,
            monster_repository=self.monster_repository,
            sector_level=current_expedition_sql.sector_level,
            sector=current_sector,
            status=current_expedition_sql.status,
        )

    def save(self, expedition: Expedition) -> None:
        current_expedition_sql = ExpeditionSQL.query \
            .filter(ExpeditionSQL.id == expedition.identifier) \
            .first()

        if not current_expedition_sql:
            current_expedition_sql = ExpeditionSQL(
                player_id=expedition.player.identifier,
                sector_level=0,
            )

        current_expedition_sql.sector_level = expedition.sector_level
        current_expedition_sql.status = expedition.status
        db.session.add(current_expedition_sql)
        db.session.commit()

        sector_monsters_sql = SectorMonsterSQL.query.filter(
            SectorMonsterSQL.expeditionId == current_expedition_sql.id).all()

        for sector_monster_sql in sector_monsters_sql:
            db.session.delete(sector_monster_sql)
        db.session.commit()

        if expedition.sector and expedition.status == ExpeditionStatus.in_progress:
            for monster in expedition.sector.monsters:
                sector_monster_sql = SectorMonsterSQL(
                    expedition_id=current_expedition_sql.id,
                    monster_name=monster.monster.name,
                    initial_quantity=monster.initial_quantity,
                    quantity=monster.quantity,
                )
                db.session.add(sector_monster_sql)
            db.session.commit()

        player_sql = PlayerSQL.query.get(expedition.player.identifier)
        player_sql.experience = expedition.player.experience
        player_sql.life = expedition.player.life
        player_sql.energy = expedition.player.energy
        db.session.add(player_sql)
        db.session.commit()
