from infrastructure.repository.expedition.expedition_sql_repository import ExpeditionSQLRepository
from infrastructure.repository.monster.monster_in_memory_repository import MonsterInMemoryRepository
from infrastructure.repository.player.player_sql_repository import PlayerSQLRepository
from use_cases.complete_sector_level import CompleteSectorLevel
from use_cases.create_new_player import CreateNewPlayer
from use_cases.get_current_sector import GetCurrentExpedition
from use_cases.get_player_details import GetPlayerDetails
from use_cases.player_attack_monster import PlayerAttackMonster
from use_cases.player_end_turn import PlayerEndTurn
from use_cases.start_new_expedition import StartNewExpedition

monster_repository = MonsterInMemoryRepository()
player_repository = PlayerSQLRepository()
expedition_repository = ExpeditionSQLRepository(monster_repository=monster_repository)

get_player_details = GetPlayerDetails(player_repository=player_repository)
create_new_player = CreateNewPlayer(player_repository=player_repository)
get_current_expedition = GetCurrentExpedition(player_repository=player_repository,
                                              expedition_repository=expedition_repository,
                                              monster_repository=monster_repository)
complete_sector_level = CompleteSectorLevel(player_repository=player_repository,
                                            expedition_repository=expedition_repository)
player_attack_monster = PlayerAttackMonster(player_repository=player_repository,
                                            expedition_repository=expedition_repository)
player_end_turn = PlayerEndTurn(player_repository=player_repository,
                                expedition_repository=expedition_repository)
start_new_expedition = StartNewExpedition(player_repository=player_repository,
                                          expedition_repository=expedition_repository,
                                          monster_repository=monster_repository)
