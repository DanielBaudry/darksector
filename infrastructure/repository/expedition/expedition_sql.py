from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship

from domain.expedition.expedition import ExpeditionStatus
from infrastructure.repository.model import Model
from infrastructure.repository.player.player_sql import PlayerSQL


class ExpeditionSQL(Model):
    __tablename__ = 'expedition'

    id = Column(Integer, primary_key=True, autoincrement=True)

    playerId = Column(Integer, ForeignKey("player.id"), nullable=False, index=True)

    player = relationship(PlayerSQL, foreign_keys=[playerId])

    sector_level = Column(Integer, nullable=False, default=1)

    status = Column(Enum(ExpeditionStatus), nullable=False)

    def __init__(self, player_id: int, sector_level: int = 1, status: ExpeditionStatus = ExpeditionStatus.in_progress):
        self.playerId = player_id
        self.sector_level = sector_level
        self.status = status
