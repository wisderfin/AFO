from app.main import db, bcrypt
from settings import settings


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, login, email, password):
        self.login = login
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, settings.BCRYPT_LOG_ROUNDS
        ).decode()




