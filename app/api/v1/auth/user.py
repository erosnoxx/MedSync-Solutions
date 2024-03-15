import logging
from flask import Blueprint, request
from app.models.personal.users import User
from app.database.users.create import SetUser, SetUserLevel
from app.database.users.read import GetUser
from app.services.utils.validators import EmailValidator, PasswordValidator
from app.controllers.extensions import db

auth_api = Blueprint('auth_api', __name__, url_prefix='/api/v1/auth')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@auth_api.route('/register/', methods=['POST'])
def register():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user is None:
        if EmailValidator(data['email']):
            if PasswordValidator(data['password']):
                try:

                    user_id = SetUser(
                        **{
                            'name': data['name'],
                            'email': data['email'],
                            'password': data['password']
                        }
                    )

                    SetUserLevel(level_='usr', user_id=user_id)

                    return {
                        'message': 'user registered',
                        'user_id': user_id,
                        'statuscode': 200
                    }, 200
                except Exception as e:
                    db.session.rollback()
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


@auth_api.route('/login/', methods=['POST'])
def login_():
    try:
        data = request.json
        context = {
            'email': data['email'],
            'password': data['password']
        }
        user_info = GetUser(**context)
        if user_info['success']:
            return {
                'message': 'user authenticated',
                'user_id': user_info['user_id'],
                'statuscode': 200
            }, 200
        else:
            return {
                'message': f'authentication failed: {user_info["message"]}',
                'statuscode': 401
            }, 401
    except Exception as e:
        return {
            'message': f'Error: {e}',
            'statuscode': 500
        }, 500
