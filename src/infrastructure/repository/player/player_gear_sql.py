from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from src.infrastructure.repository.model import Model
from src.infrastructure.repository.player.player_sql import PlayerSQL


class PlayerGearSQL(Model):
    __tablename__ = 'player_gear'

    id = Column(Integer, primary_key=True, autoincrement=True)

    gear_id = Column(String(50), nullable=False)

    playerId = Column(Integer, ForeignKey("player.id"), nullable=False, index=True)

    player = relationship(PlayerSQL, foreign_keys=[playerId])

    is_equipped = Column(Boolean, nullable=False, default=False)

    def __init__(self, gear_id: str, player_id: int, is_equipped: bool = False):
        self.gear_id = gear_id
        self.playerId = player_id
        self.is_equipped = is_equipped
