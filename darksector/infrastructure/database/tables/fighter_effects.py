from sqlalchemy import Column, Integer, Table, ForeignKey
from sqlalchemy.orm import mapper, relationship

from domain.ability import AbilityEffect
from domain.fighter import FighterEffect
from domain.player import Player
from infrastructure.database.db import metadata

fighter_effects_entity = Table(
    'fighter_effect', metadata,
    Column('id', Integer, primary_key=True),
    Column('effect_id', Integer, ForeignKey('effect.id'), nullable=False, index=True),
    Column('player_id', Integer, ForeignKey('player.id'), nullable=False, index=True),
    Column('remaining_turns', Integer, nullable=False),
)

mapper(FighterEffect, fighter_effects_entity, properties={
    'player': relationship(Player, backref='fighter_effects'),
    'effect': relationship(AbilityEffect),
})
