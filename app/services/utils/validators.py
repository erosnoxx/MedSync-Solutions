import re


def EmailValidator(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$'

    match = re.match(pattern, email)

    return bool(match)


def PasswordValidator(password):
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$!%^&+=])\S{8,}$"

    match = re.match(pattern, password)

    return bool(match)
