from app import db
from app.models import Base


class Requisites(Base):
    __tablename__ = 'requisites'

    id = db.Column(db.Integer, primary_key=True)
    bank = db.Column(db.String(100), nullable=False)
    bik = db.Column(db.BigInteger, nullable=False, unique=True)
    rs = db.Column(db.BigInteger, nullable=False, unique=True)
    ks = db.Column(db.BigInteger, nullable=False, unique=True)
    swift = db.Column(db.String(35), nullable=False, unique=True)
    iban = db.Column(db.String(11), default=None)
    user_id = db.Column(db.Integer, nullable=False)
    activity = db.Column(db.Boolean, default=False)
