from sqlalchemy import Column, Integer, Table, String, Float
from sqlalchemy.orm import mapper

from domain.ability import AbilityEffect
from infrastructure.database.db import metadata

ability_effect_entity = Table(
    'effect', metadata,
    Column('id', Integer, primary_key=True),
    Column('fighter_trait', String(40), nullable=False),
    Column('multiplier', Float, nullable=True),
    Column('fix_amount', Integer, nullable=True),
    Column('turn_duration', Integer, nullable=False),
    Column('turn_tick', Integer, nullable=False),
)

mapper(AbilityEffect, ability_effect_entity)
