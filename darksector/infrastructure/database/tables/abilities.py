from sqlalchemy import Column, Integer, Table, ForeignKey, Enum
from sqlalchemy.orm import mapper, relationship

from domain.ability import AllAbilities
from domain.fighter import FighterAbility
from domain.player import Player
from infrastructure.database.db import metadata

fighter_ability_entity = Table(
    'fighter_ability', metadata,
    Column('id', Integer, primary_key=True),
    Column('ability', Enum(AllAbilities), nullable=True, index=True),
    Column('player_id', Integer, ForeignKey('player.id'), nullable=False, index=True),
    Column('turn_cooldown', Integer, nullable=False),
)

mapper(FighterAbility, fighter_ability_entity, properties={
    'player': relationship(Player, backref='abilities'),
})
