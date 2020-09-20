from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from src.infrastructure.repository.expedition.expedition_sql import ExpeditionSQL
from src.infrastructure.repository.model import Model


class SectorMonsterSQL(Model):
    __tablename__ = 'sector_monster'

    id = Column(Integer, primary_key=True, autoincrement=True)

    expeditionId = Column(Integer, ForeignKey("expedition.id"), nullable=False, index=True)

    expedition = relationship(ExpeditionSQL, foreign_keys=[expeditionId])

    monster_name = Column(String(50), nullable=False)

    initial_quantity = Column(Integer, nullable=False)

    quantity = Column(Integer, nullable=False)

    def __init__(self, expedition_id: int, monster_name: str, initial_quantity: int, quantity: int):
        self.expeditionId = expedition_id
        self.monster_name = monster_name
        self.initial_quantity = initial_quantity
        self.quantity = quantity
