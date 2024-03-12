from . import auth_api
from app.database.users.read import GetUser
from flask import request


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
                'user': user_info['user'],
                'statuscode': 200
            }, 200
        else:
            return {
                'message': f'authentication failed: {user_info['message']}',
                'statuscode': 401
            }, 401
    except Exception as e:
        return {
            'message': f'Error: {e}',
            'statuscode': 500
        }, 500
