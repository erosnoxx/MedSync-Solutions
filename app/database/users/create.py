from app.models.personal.users import *
from app.controllers.extensions import db
from werkzeug.security import generate_password_hash


def SetUser(**kwargs):
    hashed_password = generate_password_hash(kwargs.get('password'), method='sha256')
    user = User(
        name=kwargs.get('name'),
        email=kwargs.get('email'),
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return user.id


def SetLevel(level_):
    level = Level.query.all()

    if level == None:
        levels = [
            Level(
            level='usr'
            ),
            Level(
                level='adm'
            ),
            Level(
                level='pat'
            )
        ]

        db.session.add_all(levels)
        db.session.commit()

    level = Level.query.filter_by(level=level_).first()

    return level.id


def SetUserLevel(user_id, level_='usr'):
    level_id = SetLevel(level_)

    user_level = UserLevel(
        user_id=user_id,
        level_id=level_id
    )

    db.session.add(user_level)
    db.session.commit()


def SetProfilePic(user_id, url):
    profile_pic = ProfilePic(
        user_id=user_id,
        url=url
    )

    db.session.add(profile_pic)
    db.session.commit()
