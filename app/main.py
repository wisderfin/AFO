from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)


from app.auth.view import router as auth
app.register_blueprint(auth)

from app.bank.view import router as bank
app.register_blueprint(bank)

if __name__ == '__main__':
    app.run(debug=True)