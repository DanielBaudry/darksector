from typing import Optional

import bcrypt

from infrastructure.repository.db import db
from infrastructure.repository.user.user_sql import UserSQL


class UserSQLRepository:
    def __init__(self, database: db = db):
        self.db = database

    def save(self, user: UserSQL) -> UserSQL:
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def get_user_by_id(self, user_id: int) -> UserSQL:
        return self.db.session.query(UserSQL).get(user_id)

    def get_user_with_credentials(self, username: str, password: str) -> Optional[UserSQL]:
        user = self.db.session.query(UserSQL).filter(UserSQL.username == username).first()
        if user and bcrypt.hashpw(password.encode('utf-8'), user.password) == user.password:
            return user
        return None
