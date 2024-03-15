import pyrebase
import io
from app.services.utils.generators import get_url

firebase_config = {
  "apiKey": "AIzaSyD-9p72MzAorZTg9dBGO0Nv7V9eQNo3hSQ",
  "authDomain": "innate-watch-406316.firebaseapp.com",
  "databaseURL": "xxxxxx",
  "projectId": "innate-watch-406316",
  "storageBucket": "innate-watch-406316.appspot.com",
  "messagingSenderId": "93128621884",
  "appId": "1:93128621884:web:52dc6b2a0642896f756839",
  "measurementId": "G-RB0D72J8TY"
}


firebase = pyrebase.initialize_app(firebase_config)
fb_storage = firebase.storage()


def upload(profile_pic, user_id):
    with io.BytesIO() as output:
        profile_pic.save(output)
        image_data = output.getvalue()
    try:
        image_type = profile_pic.content_type.split('/')[1]
        fb_storage.child(f"profile_pic/{user_id}.{image_type}").put(image_data)
        url = get_url(user_id, image_type)

        return url
    except:
        url = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png"

    return url


def delete(url):
    try:
        fb_storage.delete(url)
        return True
    except:
        return False
