from src.infrastructure.repository.expedition.expedition_sql_repository import ExpeditionSQLRepository
from src.infrastructure.repository.gear.gear_in_memory_repository import GearInMemoryRepository
from src.infrastructure.repository.monster.monster_in_memory_repository import MonsterInMemoryRepository
from src.infrastructure.repository.player.player_sql_repository import PlayerSQLRepository
from src.infrastructure.repository.skill.skill_in_memory_repository import SkillInMemoryRepository
from src.use_cases.create_new_player import CreateNewPlayer
from src.use_cases.equip_gear import EquipGear
from src.use_cases.get_current_sector import GetCurrentExpedition
from src.use_cases.get_player_details import GetPlayerDetails
from src.use_cases.player_attack_monster import PlayerAttackMonster
from src.use_cases.player_end_turn import PlayerEndTurn
from src.use_cases.start_new_expedition import StartNewExpedition
from src.use_cases.use_skill_on_monster import UseSkillOnMonster

monster_repository = MonsterInMemoryRepository()
skill_repository = SkillInMemoryRepository()
gear_repository = GearInMemoryRepository()
player_repository = PlayerSQLRepository(skill_repository=skill_repository,
                                        gear_repository=gear_repository)
expedition_repository = ExpeditionSQLRepository(monster_repository=monster_repository,
                                                skill_repository=skill_repository,
                                                gear_repository=gear_repository)

get_player_details = GetPlayerDetails(player_repository=player_repository)
create_new_player = CreateNewPlayer(player_repository=player_repository)
get_current_expedition = GetCurrentExpedition(player_repository=player_repository,
                                              expedition_repository=expedition_repository,
                                              monster_repository=monster_repository)
player_attack_monster = PlayerAttackMonster(player_repository=player_repository,
                                            expedition_repository=expedition_repository)
player_end_turn = PlayerEndTurn(player_repository=player_repository,
                                expedition_repository=expedition_repository)
start_new_expedition = StartNewExpedition(player_repository=player_repository,
                                          expedition_repository=expedition_repository,
                                          monster_repository=monster_repository)
use_skill_on_monster = UseSkillOnMonster(player_repository=player_repository,
                                         expedition_repository=expedition_repository,
                                         skill_repository=skill_repository)
equip_gear = EquipGear(player_repository=player_repository)
