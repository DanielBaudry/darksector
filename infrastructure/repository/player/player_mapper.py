from domain.player.player import Player
from infrastructure.repository.player.player_sql import PlayerSQL


def to_domain(player_sql_entity: PlayerSQL) -> Player:
    return Player(
        identifier=player_sql_entity.id,
        name=player_sql_entity.name,
        life=player_sql_entity.life,
        max_life=player_sql_entity.max_life,
        energy=player_sql_entity.energy,
        max_energy=player_sql_entity.max_energy,
        damage=player_sql_entity.damage,
        armor=player_sql_entity.armor,
        experience=player_sql_entity.experience,
    )


def to_sql_entity(user_id: int, player: Player) -> PlayerSQL:
    return PlayerSQL(
        user_id=user_id,
        name=player.name,
        life=player.life,
        max_life=player.max_life,
        damage=player.damage,
        armor=player.armor,
        energy=player.energy,
        max_energy=player.max_energy,
    )
