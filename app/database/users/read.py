from app.models.personal.users import *
from werkzeug.security import check_password_hash


def GetUser(**kwargs):
    user = User.query.filter_by(email=kwargs.get('email')).first()

    if user is not None:
        if check_password_hash(user.password, kwargs.get('password')):
            return {'success': True, 'user': user}
        else:
            return {'success': False, 'message': 'Invalid password'}
    return {'success': False, 'message': 'User does not exist'}


def GetLevel(user_id):
    user_level = UserLevel.query.filter_by(user_id=user_id).first()
    
    if user_level:
        level = Level.query.filter_by(id=user_level.level_id).first()
        if level:
            return {'success': True, 'level': level.level}
        else:
            return {'success': False, 'message': 'Level not found'}
    else:
        return {'success': False, 'message': 'User level not found'}
