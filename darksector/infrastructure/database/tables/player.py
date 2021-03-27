from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import mapper

from domain.player import Player
from infrastructure.database.db import metadata

player_entity = Table(
    'player', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20), nullable=False),
    Column('health', Integer, nullable=False),
    Column('damage', Integer, nullable=False)
)

mapper(Player, player_entity)
