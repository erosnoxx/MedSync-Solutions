import pytz
import requests
import random
import string
from datetime import datetime
from urllib.parse import quote


def get_now():
    return datetime.now(
        pytz.timezone('America/Sao_Paulo'))


def format_path(user_id, file_type):
    path = f'profile_pic/{user_id}.{file_type}'
    formatted_path = quote(path, safe='')

    return formatted_path


def get_token(path):
    url = f"https://firebasestorage.googleapis.com/v0/b/innate-watch-406316.appspot.com/o/{path}"

    response = requests.get(url)
    data = response.json()
    token = data["downloadTokens"]

    return token


def get_url(user_id, file_type):
    path = format_path(user_id, file_type)

    url = f"https://firebasestorage.googleapis.com/v0/b/innate-watch-406316.appspot.com/o/{path}?alt=media&token={get_token(path)}"

    return url


def generate_patient_pwd():
    chars = (
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice('@#$!%^&+=')
    )

    pwd_list = list(chars)

    pwd_list.extend(random.choices(string.ascii_letters + string.digits + '@#$!%^&+=', k=8))
    random.shuffle(pwd_list)

    password = ''.join(pwd_list)

    return password