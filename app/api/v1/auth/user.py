import logging
from flask import Blueprint, request
from app.database.users.create import SetUser, SetUserLevel
from app.database.users.read import GetUser
from app.services.utils.validators import EmailValidator, PasswordValidator
from app.controllers.extensions import db

auth_api = Blueprint('auth_api', __name__, url_prefix='/api/v1/auth')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@auth_api.post('/register/')
def register():
    data = request.json

    required_fields = ['email', 'password', 'name']
    if not all(field in data for field in required_fields):
        return {'message': 'missing required fields', 'statuscode': 400}, 400

    user = GetUser(**{'email': data['email'], 'password': data['password']})
    if user['success']:
        return {
            'message': 'user already registered',
            'statuscode': 400
        }, 400

    if not EmailValidator(data['email']):
        return {
                'message': 'invalid email',
                'statuscode': 400
            }, 400

    if not PasswordValidator(data['password']):
        return {
            'message': 'weak password',
            'statuscode': 400
        }, 400

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


@auth_api.post('/login/')
def login_():
    data = request.json

    required_fields = ['email', 'password']
    if not all(field in data for field in required_fields):
        return {'message': 'missing required fields', 'statuscode': 400}, 400
    
    user = GetUser(**{'email': data['email'], 'password': data['password']})

    if not user['success']:
        return {
            'message': f'user not found: {user["message"]}',
            'statuscode': 404
        }, 404

    return{
        'message': 'user authenticated',
        'user_id': user['id'],
        'statuscode': 200
    }, 200
