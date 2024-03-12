from flask import request
from . import auth_api
from app.models.personal.users import User
from app.database.users.create import SetUser, SetProfilePic, SetUserLevel
from app.services.utils.fb_storage import upload
from app.services.utils.validators import EmailValidator, PasswordValidator



@auth_api.route('/register/', methods=['POST'])
def register():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user is None:
        if EmailValidator(data['email']):
            if PasswordValidator(data['password']):
                try:
                    context = {
                        'name': data['name'],
                        'email': data['email'],
                        'password': data['password']
                    }

                    user_id = SetUser(**context)

                    SetUserLevel(level_='adm', user_id=user_id)
                    SetProfilePic(user_id=user_id, url=upload(data['profile_pic']))

                    return {
                        'message': 'user registered',
                        'statuscode': 200
                    }, 200
                except Exception as e:
                    return {
                        'message': f'error: {e}',
                        'statuscode': 500
                    }, 500
            else:
                return {
                    'message': 'weak password',
                    'statuscode': 400
                }, 400
        else:
            return {
                'message': 'invalid email',
                'statuscode': 400
            }, 400
    else:
        return {
            'message': 'user already registered',
            'statuscode': 400
        }, 400
