from flask import request
from app import db
from app.auth.model import User


def check_user(email):
    user = db.session.query(User).filter_by(email=email).first()
    return user


def db_save(model):
    db.session.add(model)
    db.session.commit()
