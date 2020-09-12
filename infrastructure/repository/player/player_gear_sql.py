from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from infrastructure.repository.model import Model
from infrastructure.repository.player.player_sql import PlayerSQL


class PlayerGearSQL(Model):
    __tablename__ = 'player_gear'

    id = Column(Integer, primary_key=True, autoincrement=True)

    gear_id = Column(String(50), nullable=False)

    playerId = Column(Integer, ForeignKey("player.id"), nullable=False, index=True)

    player = relationship(PlayerSQL, foreign_keys=[playerId])

    amount = Column(Integer, nullable=False, default=0)

    def __init__(self, gear_id: str, player_id: int, amount: int = 0):
        self.gear_id = gear_id
        self.playerId = player_id
        self.amount = amount
