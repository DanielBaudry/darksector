import os

from flask import Flask
from flask_login import LoginManager

from battle.infrastructure.database.db import db_session

# from battle.infrastructure.database.user.user_sql_repository import UserSQLRepository
from infrastructure import controllers
from infrastructure.database import init_db

app = Flask(__name__,
            static_url_path='/static')
app.secret_key = os.environ.get('FLASK_SECRET', '+%+3Q23!zbc+!Dd@')


# login_manager = LoginManager()


# @login_manager.user_loader
# def load_user(user_id: int):
#    return UserSQLRepository().get_user_by_id(user_id)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# login_manager.init_app(app)


with app.app_context():
    controllers.import_routes()
    init_db.execute()

if __name__ == '__main__':
    app.run(use_reloader=True)
