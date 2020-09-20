import bcrypt
from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, LargeBinary

from src.infrastructure.repository.model import Model


class UserSQL(Model, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)

    username = Column(String(20), nullable=False, unique=True)

    password = Column(LargeBinary(60), nullable=False)

    def __init__(self, username: str, clear_password):
        self.username = username
        self.password = bcrypt.hashpw(clear_password.encode('utf-8'), bcrypt.gensalt())
