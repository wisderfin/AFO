from flask import Blueprint, request, session
from flask.views import MethodView

from app.auth.model import User
from app import db, bcrypt


class Registration(MethodView):
    @staticmethod
    def post():
        email = request.form['email']
        user = db.session.query(User).filter(User.email == request.form['email']).first()
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
        user = db.session.query(User).filter_by(email=request.form['email']).first()
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
