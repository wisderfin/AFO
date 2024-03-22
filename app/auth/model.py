from app import db, bcrypt
from settings import settings
from app.models import Base


class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, settings.BCRYPT_LOG_ROUNDS
        ).decode()
