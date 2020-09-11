from domain.expedition.expedition import Expedition, ExpeditionStatus
from domain.monster.monster import Monster
from domain.expedition.sector import Sector
from domain.sector_monsters.sector_monsters import SectorMonster
from domain.sector_monsters_generator.sector_monsters_generator import SectorMonstersGenerator
from infrastructure.repository.db import db
from infrastructure.repository.expedition.expedition_sql import ExpeditionSQL
from infrastructure.repository.expedition.expedition_sql_repository import ExpeditionSQLRepository
from infrastructure.repository.monster.monster_in_memory_repository import MonsterInMemoryRepository
from infrastructure.repository.player import player_mapper
from infrastructure.repository.player.player_sql import PlayerSQL
from infrastructure.repository.sector_monster.sector_monster_sql import SectorMonsterSQL
from infrastructure.repository.skill.skill_in_memory_repository import SkillInMemoryRepository
from infrastructure.repository.user.user_sql import UserSQL
from tests.conftest import clean_database


class ExpeditionSQLRepositoryTest:
    class SaveTest:
        def setup_method(self):
            monster_repository = MonsterInMemoryRepository()
            skill_repository = SkillInMemoryRepository()
            self.expedition_sql_repository = ExpeditionSQLRepository(monster_repository=monster_repository,
                                                                     skill_repository=skill_repository)
            self.sector_monsters_generator = SectorMonstersGenerator(monster_repository.get_all_monsters())

        @clean_database
        def should_insert_expedition_with_all_sub_elements_in_db(self, app):
            # Given
            user_sql = UserSQL(username='user1', clear_password='azerty123')
            db.session.add(user_sql)
            db.session.commit()
            player_sql = PlayerSQL(
                user_id=user_sql.id,
                name='Player1',
                life=200,
                energy=100,
                max_life=200,
                max_energy=100,
                damage=20,
                max_damage=20,
                armor=10,
                max_armor=10,
                experience=0,
            )
            db.session.add(player_sql)
            db.session.commit()

            expedition = Expedition(
                player=player_mapper.to_domain(player_sql_entity=player_sql, skills=[]),
                sector_monsters_generator=self.sector_monsters_generator
            )

            # When
            self.expedition_sql_repository.save(expedition=expedition)

            # Then
            assert ExpeditionSQL.query.count() == 1
            assert SectorMonsterSQL.query.count() == 1
            assert PlayerSQL.query.count() == 1

        @clean_database
        def should_update_expedition_with_all_sub_elements_in_db(self, app):
            # Given
            user_sql = UserSQL(username='user1', clear_password='azerty123')
            db.session.add(user_sql)
            db.session.commit()
            player_sql = PlayerSQL(
                user_id=user_sql.id,
                name='Player1',
                life=200,
                energy=100,
                max_life=200,
                max_energy=100,
                damage=20,
                max_damage=20,
                armor=10,
                max_armor=10,
                experience=0,
            )
            db.session.add(player_sql)
            db.session.commit()

            expedion_sql = ExpeditionSQL(
                player_id=player_sql.id,
                sector_level=1,
                status=ExpeditionStatus.in_progress,
            )
            expedion_sql.id = 1
            db.session.add(expedion_sql)
            db.session.commit()

            sector_monster_sql = SectorMonsterSQL(
                expedition_id=expedion_sql.id,
                initial_quantity=12,
                quantity=4,
                monster_name='Zergling',
            )
            db.session.add(sector_monster_sql)
            db.session.commit()

            expedition = Expedition(
                identifier=1,
                player=player_mapper.to_domain(player_sql_entity=player_sql, skills=[]),
                sector_monsters_generator=self.sector_monsters_generator,
                sector=Sector(
                    monsters=[
                        SectorMonster(
                            monster=Monster(
                                name='Zergling',
                                life=20,
                                damage=5,
                                armor=0,
                                experience_gain=10,
                            ),
                            initial_quantity=12,
                            quantity=2,
                        )
                    ],
                    sector_monsters_generator=self.sector_monsters_generator,
                )
            )

            # When
            self.expedition_sql_repository.save(expedition=expedition)

            # Then
            assert ExpeditionSQL.query.count() == 1
            assert SectorMonsterSQL.query.count() == 1
            sector_monster = SectorMonsterSQL.query.first()
            assert sector_monster.quantity == 2
            assert PlayerSQL.query.count() == 1
