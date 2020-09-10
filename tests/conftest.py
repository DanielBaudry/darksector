from functools import wraps
from typing import Optional

import pytest
from flask import Flask
from flask.testing import FlaskClient
from flask_login import LoginManager, login_user
from requests.auth import _basic_auth_str
from sqlalchemy import orm

from infrastructure.repository.db import db
from infrastructure.repository.expedition.expedition_sql import ExpeditionSQL
from infrastructure.repository.player.player_sql import PlayerSQL
from infrastructure.repository.sector_monster.sector_monster_sql import SectorMonsterSQL
from infrastructure.repository.user.user_sql import UserSQL


def find_user_by_email(user_id: int) -> Optional[UserSQL]:
    return db.session.query(UserSQL).get(user_id)


@pytest.fixture(scope='session')
def app():
    app = Flask(__name__, template_folder='../templates')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/darksector_test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '@##&6cweafhv3426445'
    app.config['REMEMBER_COOKIE_HTTPONLY'] = False
    app.config['SESSION_COOKIE_HTTPONLY'] = False
    app.config['TESTING'] = True
    app.url_map.strict_slashes = False

    login_manager = LoginManager()
    login_manager.init_app(app)
    db.init_app(app)

    app.app_context().push()

    orm.configure_mappers()
    db.create_all()
    db.session.commit()

    @app.route('/test/signin', methods=['POST'])
    def test_signin():
        from flask import request
        identifier = request.get_json().get("identifier")
        user = find_user_by_email(identifier)
        login_user(user, remember=True)
        return '{}', 204

    return app


def truncate_all_tables():
    db.session.query(PlayerSQL).delete()
    db.session.query(SectorMonsterSQL).delete()
    db.session.query(ExpeditionSQL).delete()
    db.session.query(UserSQL).delete()
    db.session.flush()


def clean_database(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        db.session.rollback()
        truncate_all_tables()
        return f(*args, **kwargs)

    return decorated_function


class TestClient:
    WITH_DOC = False
    USER_TEST_ADMIN_EMAIL = "admin0@example.com"
    PLAIN_DEFAULT_TESTING_PASSWORD = 'Administrator@1234'
    LOCAL_ORIGIN_HEADER = {'origin': 'http://localhost:3000'}

    def __init__(self, client: FlaskClient):
        self.client = client
        self.auth_header = {}
        self.email = ''

    def with_auth(self, email: str = None):
        self.email = email
        if email is None:
            self.auth_header = {
                'Authorization': _basic_auth_str(TestClient.USER_TEST_ADMIN_EMAIL, PLAIN_DEFAULT_TESTING_PASSWORD),
            }
        else:
            self.auth_header = {
                'Authorization': _basic_auth_str(email, PLAIN_DEFAULT_TESTING_PASSWORD),
            }

        return self

    def delete(self, route: str, headers=LOCAL_ORIGIN_HEADER):
        result = self.client.delete(route, headers={**self.auth_header, **headers})
        return result

    def get(self, route: str, headers=LOCAL_ORIGIN_HEADER):
        result = self.client.get(route, headers={**self.auth_header, **headers})
        return result

    def post(self, route: str, json: dict = None, headers=LOCAL_ORIGIN_HEADER):
        result = self.client.post(route, json=json, headers={**self.auth_header, **headers})
        return result

    def patch(self, route: str, json: dict = None, headers=LOCAL_ORIGIN_HEADER):
        result = self.client.patch(route, json=json, headers={**self.auth_header, **headers})
        return result

    def put(self, route: str, json: dict = None, headers=LOCAL_ORIGIN_HEADER):
        result = self.client.put(route, json=json, headers={**self.auth_header, **headers})
        return result
