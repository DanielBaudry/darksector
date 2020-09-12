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

    max_life = Column(Integer, nullable=False, default=0)

    energy = Column(Integer, nullable=False, default=0)

    max_energy = Column(Integer, nullable=False, default=0)

    damage = Column(Integer, nullable=False, default=0)

    max_damage = Column(Integer, nullable=False, default=0)

    armor = Column(Integer, nullable=False, default=0)

    max_armor = Column(Integer, nullable=False, default=0)

    experience = Column(Integer, nullable=False, default=0)

    credits = Column(Integer, nullable=False, default=0)

    def __init__(self, user_id: int, name: str, life: int, energy: int, max_life: int, max_energy: int,
                 damage: int, max_damage: int, armor: int, max_armor: int, experience: int = 0, credits_amount: int = 0):
        self.name = name
        self.userId = user_id
        self.life = life
        self.max_life = max_life
        self.experience = experience
        self.armor = armor
        self.max_armor = max_armor
        self.damage = damage
        self.max_damage = max_damage
        self.energy = energy
        self.max_energy = max_energy
        self.credits = credits_amount
