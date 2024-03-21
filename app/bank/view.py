from flask import Blueprint, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.bank.model import Requisites
from app.auth.model import User
from app import db

router = Blueprint('bank', __name__)


class New_Requisites(MethodView):
    @staticmethod
    @jwt_required()
    def post():
        requisites = Requisites(
            bank=request.form['bank'],
            bik=request.form['bik'],
            rs=request.form['rs'],
            ks=request.form['ks'],
            user_id=User.query.filter_by(email=get_jwt_identity()).first().id
        )
        db.session.add(requisites)
        db.session.commit()
        return {'message': 'Requisites successfully added'}


class Get_List(MethodView):
    @staticmethod
    @jwt_required()
    def get():
        user_id = User.query.filter_by(email=get_jwt_identity()).first().id
        res = Requisites.query.filter_by(user_id=user_id)
        requisites_list = {}
        for req in res:
            requisites_list[req.id] = {
                'bank': req.bank,
                'bik': req.bik,
                'rs': req.rs,
                'ks': req.ks
            }
        return requisites_list


class Edit(MethodView):
    @staticmethod
    @jwt_required()
    def update():
        id = request.form['id']
        bank = request.form.get('bank', None)
        bik = request.form.get('bik', None)
        rs = request.form.get('rs', None)
        ks = request.form.get('ks', None)
        user_id = User.query.filter_by(email=get_jwt_identity()).first().id
        requisite = Requisites.query.filter_by(id=id).first()
        if user_id is None or requisite is None:
            return {'message': 'Incorrect id'}
        if requisite.user_id == user_id:
            if bank is not None:
                requisite.bank = bank
            if bik is not None:
                requisite.bik = bik
            if rs is not None:
                requisite.rs = rs
            if ks is not None:
                requisite.ks = ks
            db.session.commit()
            return {'message': 'Requisites successfully changed'}
        return {'message': 'Credentials Error'}


class Remove(MethodView):
    @staticmethod
    @jwt_required()
    def delete():
        id = request.form['id']
        user_id = User.query.filter_by(email=get_jwt_identity()).first().id
        requisite = Requisites.query.filter_by(id=id).first()
        if requisite.user_id == user_id:
            db.session.delete(requisite)
            db.session.commit()
            return {'message': 'Requisites successfully deleted'}
        return {'message': 'Incorrect id'}


class Activity(MethodView):
    @staticmethod
    @jwt_required()
    def post():
        id = request.form['id']
        user_id = User.query.filter_by(email=get_jwt_identity()).first().id
        requisite = Requisites.query.filter_by(id=id).first()
        down_activity = db.session.query(Requisites).filter(Requisites.user_id == user_id,
                                                            Requisites.activity == True).first()
        if down_activity:
            down_activity.activity = False
        requisite.activity = True
        db.session.commit()
        return {'message': 'Requisites successfully activated'}


router.add_url_rule(
    '/new',
    view_func=New_Requisites.as_view('new_requisites'),
    methods=['POST']
)
router.add_url_rule(
    '/get',
    view_func=Get_List.as_view('get_list'),
    methods=['GET']
)
router.add_url_rule(
    '/edit',
    view_func=Edit.as_view('edit_requisite'),
    methods=['UPDATE']
)
router.add_url_rule(
    '/remove',
    view_func=Remove.as_view('remove_requisite'),
    methods=['DELETE']
)
router.add_url_rule(
    '/activity',
    view_func=Activity.as_view('activity'),
    methods=['POST']
)
