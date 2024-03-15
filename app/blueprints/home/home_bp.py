from flask import Blueprint, render_template, redirect, url_for, request
from app.models.personal.users import ProfilePic
from flask_login import login_required, current_user
from app.database.users.read import GetLevel


home = Blueprint('home', __name__)

# Context manager
@home.context_processor
def loader():
    def load_pp():
        profile_pic = ProfilePic.query.filter_by(user_id=current_user.id).first()
        return profile_pic.url if profile_pic else None

    user_level = GetLevel(user_id=current_user.id)

    endpoint = request.endpoint.split('.')[1]
    return {'profile_pic': load_pp(), 'endpoint': endpoint, 'user_level': user_level}


@home.route('/')
def init():
    return redirect(url_for('home.index'))


@home.route('/home/')
@login_required
def index():
    return render_template('/home/index.html')