from app.controllers.extensions import db
from app.models.personal.users import *
from app.services.utils.fb_storage import delete


def DeleteUser(user_id):
    user = User.query.filter_by(id=user_id).firt()

    if user is not None:
        db.session.delete(user)
        db.session.commit()

        return True
    return None


def DeleteProfilePic(user_id):
    profile_pic = ProfilePic.query.filter_by(id=user_id).firt()

    if profile_pic is not None:
        delete(profile_pic.url)
        db.session.delete(profile_pic)
        db.session.commit()
        
        profile_pic = ProfilePic(
            user_id=user_id,
            url="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"
        )

        db.session.add(profile_pic)
        db.session.commit()
