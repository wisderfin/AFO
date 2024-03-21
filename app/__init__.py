from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.config import Config
from flask import Flask
from settings import settings

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = settings.SECRET_KEY
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app.auth.view import router as auth
from app.bank.view import router as bank

app.register_blueprint(auth)
app.register_blueprint(bank)

if __name__ == '__main__':
    app.run(debug=True)
