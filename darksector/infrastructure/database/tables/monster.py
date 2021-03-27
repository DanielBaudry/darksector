from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import mapper, relationship

from domain.fight import Fight
from domain.monster import Monster
from infrastructure.database.db import metadata

monster_entity = Table(
    'monster', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20), nullable=False),
    Column('health', Integer, nullable=False),
    Column('damage', Integer, nullable=False),
    Column('fight_id', Integer, ForeignKey('fight.id'), nullable=True, index=True),
)

mapper(Monster, monster_entity, properties={
    'fight': relationship(Fight, backref='monsters'),
})
