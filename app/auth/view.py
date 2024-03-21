from flask import jsonify, Blueprint, request
from flask.views import MethodView
from flask_jwt_extended import create_access_token

from app.auth.model import User
from app import db, bcrypt


class Registration(MethodView):
    @staticmethod
    def post():
        email = request.form['email']
        user = User.query.filter_by(email=request.form['email']).first()
        if user is None:
            user = User(
                email=email,
                password=request.form['password']
            )
            db.session.add(user)
            db.session.commit()
            return {'message': 'User successfully registered'}
        return {'message': 'User already registered'}


class Login(MethodView):
    @staticmethod
    def post():
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=request.form['email']).first()
        if user is not None and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity=email)
            return jsonify(access_token)
        return {'message': 'Credentials Error'}


router = Blueprint('auth', __name__)

router.add_url_rule(
    '/auth/registration',
    view_func=Registration.as_view('registration_api'),
    methods=['POST']
)
router.add_url_rule(
    '/auth/login',
    view_func=Login.as_view('login_api'),
    methods=['POST', 'GET']
)
