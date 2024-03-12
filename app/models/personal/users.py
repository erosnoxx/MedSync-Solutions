from app.services.utils.generators import get_now
from app.controllers.extensions import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=get_now, nullable=False)
    # Relationships
    profile_pic = db.relationship('ProfilePic', backref='user', uselist=False)
    user_levels = db.relationship('UserLevel', backref='user')
    # User Login
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class Level(db.Model):
    __tablename__ = 'level'

    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(3), nullable=False)
    # Relationships
    user_levels = db.relationship('UserLevel', backref='level')


class UserLevel(db.Model):
    __tablename__ = 'user_level'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)


class ProfilePic(db.Model):
    __tablename__ = 'profile_pic'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    url = db.Column(db.String(255), nullable=False)
