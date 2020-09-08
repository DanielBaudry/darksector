from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from infrastructure.repository.model import Model
from infrastructure.repository.user.user_sql import UserSQL


class PlayerSQL(Model):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(50), nullable=False)

    userId = Column(Integer, ForeignKey("user.id"), nullable=False, index=True)

    user = relationship(UserSQL, foreign_keys=[userId])

    life = Column(Integer, nullable=False, default=0)

    energy = Column(Integer, nullable=False, default=0)

    damage = Column(Integer, nullable=False, default=0)

    armor = Column(Integer, nullable=False, default=0)

    experience = Column(Integer, nullable=False, default=0)

    def __init__(self, user_id: int, name: str, life: int, energy: int, damage: int, armor: int,
                 experience: int = 0):
        self.name = name
        self.userId = user_id
        self.life = life
        self.experience = experience
        self.armor = armor
        self.damage = damage
        self.energy = energy
