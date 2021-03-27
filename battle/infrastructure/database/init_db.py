import infrastructure.database.db as db_config
from infrastructure.database.tables.player import player_entity


def execute():
    # TODO: i don't undesrtand why create all can't find tables on his own
    db_config.metadata.create_all(bind=db_config.engine, tables=[player_entity], checkfirst=True)
