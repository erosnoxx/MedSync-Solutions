from app.models.personal.users import User, UserLevel, Level, ProfilePic, Employees
from app.controllers.extensions import db
from werkzeug.security import generate_password_hash


def SetUser(**kwargs):
    user = User.query.filter_by(email=kwargs['email']).first()
    if user is None:
        hashed_password = generate_password_hash(
            kwargs.get('password'),
            method='pbkdf2:sha256'
        )
        user = User(
            name=kwargs.get('name'),
            email=kwargs.get('email'),
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return user.id
    return None


def SetLevel(level_):
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


def SetEmployee(user_id, business_id):
    employee = Employees(user_id=user_id, business_id=business_id)

    db.session.add(employee)
    db.session.commit()
