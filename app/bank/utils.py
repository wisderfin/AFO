from flask import session
from app import db
from app.auth.model import User
from app.auth.utils import get_user
from app.bank.model import Requisites


def get_user_id():
    return db.session.query(User).filter_by(email=get_user(session.get("session")).email).first().id


def get_requisites(user_id):
    return db.session.query(Requisites).filter_by(user_id=user_id)


def get_requisite(id):
    return db.session.query(Requisites).filter_by(id=id).first()


def get_activity():
    return db.session.query(Requisites).filter(Requisites.user_id == get_user_id(), Requisites.activity is True).first()
