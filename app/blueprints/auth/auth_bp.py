import logging
import requests
from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user
from app.controllers.extensions import lm
from app.models.personal.users import User
from app.forms.auth.login import LoginForm, RegisterForm
from app.database.users.create import SetProfilePic
from app.services.utils.fb_storage import upload
from app.services.requests.auth_request import InsertUser, VerifyUser

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

lm.login_view = 'auth.login_'


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Blueprint name
auth = Blueprint('auth', __name__)


# Register
@auth.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        context = {
            'name': form.name.data,
            'email': form.email.data,
            'password': form.password.data
        }

        response = InsertUser(**context)

        if response['statuscode'] == 200: 
            url = upload(
                profile_pic=request.files['profile_pic'],
                user_id=response['user_id']
            )
            SetProfilePic(url=url, user_id=response['user_id'])
            
            return redirect(url_for('auth.login_'))
        else:
            flash(response['message'])
    return render_template('auth/register.html', form=form)

# Login
@auth.route('/login/', methods=['POST', 'GET'])
def login_():
    form = LoginForm()

    if form.validate_on_submit():
      pass  

    return render_template('auth/login.html', form=form)
