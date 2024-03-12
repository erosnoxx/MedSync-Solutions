import re


def EmailValidator(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$'

    if re.match(pattern, email):
        return True
    else:
        return False


def PasswordValidator(password):
    pattern = (
        r'^(?=.*[a-z])'
        r'(?=.*[A-Z])'
        r'(?=.*\d)'
        r'(?=.*[@#$%^&+=])'
        r'[A-Za-z\d@#$%^&+=]{8,}$'
    )

    if re.match(pattern, password):
        return True
    else:
        return False
