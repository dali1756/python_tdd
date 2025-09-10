import re

def is_valid_email(email):
    result = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return bool(re.match(result, email))

def is_password(password):
    if len(password) < 8:
        return False
    upper_password = bool(re.search(r'[A-Z]', password))
    lower_password = bool(re.search(r'[a-z]', password))
    digit_password = bool(re.search(r'\d', password))
    special_password = bool(re.search(r'[!@#$%^&*(),.?":{}|<>_+-;~`]', password))
    return upper_password and lower_password and digit_password and special_password

def is_valid_age(age):
    return 18 <= age < 100