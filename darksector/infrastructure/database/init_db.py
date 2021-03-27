import infrastructure.database.db as db_config
from infrastructure.database.tables.abilities import fighter_ability_entity
from infrastructure.database.tables.ability_effect import ability_effect_entity
from infrastructure.database.tables.fighter_effects import fighter_effects_entity
from infrastructure.database.tables.fight import fight_entity
from infrastructure.database.tables.monster import monster_entity
from infrastructure.database.tables.player import player_entity


def execute():
    # TODO: i don't undesrtand why create all can't find tables on his own
    db_config.metadata.create_all(bind=db_config.engine,
                                  tables=[ability_effect_entity,
                                          player_entity,
                                          fighter_ability_entity,
                                          fighter_effects_entity,
                                          monster_entity,
                                          fight_entity],
                                  checkfirst=True)
