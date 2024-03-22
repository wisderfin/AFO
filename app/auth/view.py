from flask import Blueprint, request, session
from flask.views import MethodView
from app.auth.model import User
from app import bcrypt
from app.auth.utils import get_user
from app.utils import db_save


class Registration(MethodView):
    @staticmethod
    def post():
        email = request.form['email'].strip()
        user = get_user(email)
        if user is None:
            password = request.form['password'].strip()
            if email and password:
                user = User(
                    email=email,
                    password=password
                )
                db_save(user)
                return {'message': 'User successfully registered'}
            return {'message': 'Incorrect data'}
        return {'message': 'User already registered'}


class Login(MethodView):
    @staticmethod
    def post():
        email = request.form['email']
        password = request.form['password']
        user = get_user(email)
        if user is not None and bcrypt.check_password_hash(user.password, password):
            session['session'] = email
            return {'message': 'Entry successful'}
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
    methods=['POST']
)
