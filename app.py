import os

from flask import Flask
from flask_login import LoginManager
from sqlalchemy import orm

from infrastructure.repository.db import db
from infrastructure.repository.user.user_sql_repository import UserSQLRepository

app = Flask(__name__,
            template_folder='infrastructure/views',
            static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/darksector.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('FLASK_SECRET', '+%+3Q23!zbc+!Dd@')
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: int):
    return UserSQLRepository().get_user_by_id(user_id)


db.init_app(app)
login_manager.init_app(app)

with app.app_context():
    import infrastructure.controllers
    orm.configure_mappers()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    app.run(use_reloader=True)
