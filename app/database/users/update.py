from app.models.personal.users import *
from app.controllers.extensions import db
from app.services.utils.fb_storage import upload, delete
from app.database.users.Create import SetLevel

def UpdateUser(**kwargs):
    user = User.query.filter_by(email=kwargs.get('email')).first()

    if user is not None:
        user.name, user.email, user.password = (kwargs.get('name'), kwargs.get('email'), kwargs.get('password'))
        db.session.commit()

    return user.id if user is not None else None


def UpdateProfilePic(**kwargs):
    old_url = ProfilePic.query.filter_by(user_id=kwargs.get('user_id')).first()
    
    if old_url is not None:
        delete(old_url.url)
        url = upload(kwargs.get('profile_pic'), kwargs.get('user_id'))
        profile_pic = ProfilePic.query.filter_by(user_id=kwargs.get('user_id')).first()
        profile_pic.url = url
        db.session.commit()

        return url
    return None


def UpdateUserLevel(**kwargs):
    user_level = UserLevel.query.filter_by(user_id=kwargs.get('user_id')).first()
    user_level.level_id = SetLevel(level_={'level': kwargs.get('level')})
    db.session.commit()

    return user_level.level_id
