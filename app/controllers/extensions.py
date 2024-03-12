from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
lm = LoginManager()


def init_app(app):
    db.init_app(app)
    lm.init_app(app)
    Migrate(app, db)