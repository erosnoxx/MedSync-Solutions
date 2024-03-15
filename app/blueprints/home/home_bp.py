from flask import Blueprint, render_template, redirect, url_for, request
from app.models.personal.users import ProfilePic
from flask_login import login_required, current_user


home = Blueprint('home', __name__)

# Context manager
@home.context_processor
def pp_loader():
    def load_profile_pic():
        profile_pic = ProfilePic.query.filter_by(user_id=current_user.id).first()
        print(profile_pic)
        return profile_pic.url if profile_pic else None
    
    endpoint = request.endpoint.split('.')[1]
    return {'profile_pic': load_profile_pic(), 'endpoint': endpoint}


@home.route('/')
def init():
    return redirect(url_for('home.index'))


@home.route('/home/')
@login_required
def index():
    return render_template('/home/index.html')