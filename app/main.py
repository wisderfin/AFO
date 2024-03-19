from flask import Flask, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_jwt_extended import jwt_required

app = Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)


@app.route('/')
@jwt_required()
def main():
    return {'2':'3'}


from app.auth.view import router as auth
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)