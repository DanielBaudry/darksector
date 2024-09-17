from sqlalchemy import Column, Integer, Table, Boolean, ForeignKey
from sqlalchemy.orm import mapper, relationship

from domain.fight import Fight
from domain.player import Player
from infrastructure.database.db import metadata

fight_entity = Table(
    'fight', metadata,
    Column('id', Integer, primary_key=True),
    Column('player_id', Integer, ForeignKey('player.id'), nullable=False, index=True),
    Column('fight_turn', Integer, nullable=False),
    Column('user_turn', Boolean, nullable=False),
    Column('is_running', Boolean, nullable=False)
)

mapper(Fight, fight_entity, properties={
    'player': relationship(Player),
})
