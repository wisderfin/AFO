from flask import session
from app import db
from app.auth.model import User


# Возвращает пользователя из бд
def get_user(email):
    user = db.session.query(User).filter_by(email=email).first()
    return user


# проверка авторизации пользователя
def check_auth():
    mail = session.get("session")
    if get_user(mail):
        return True
    return False
