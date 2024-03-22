from flask import Blueprint, request
from flask.views import MethodView
from app.auth.utils import check_auth
from app.bank.model import Requisites
from app.bank.utils import get_user_id, get_requisite, get_requisites, get_activity
from app.utils import db_save, db_delete
from app import db

router = Blueprint('bank', __name__)


class RequisitesAPI(MethodView):
    @staticmethod
    def post():
        if check_auth():
            try:
                requisites = Requisites(
                    bank=request.form['bank'],
                    bik=request.form['bik'],
                    rs=request.form['rs'],
                    ks=request.form['ks'],
                    user_id=get_user_id()
                )
                db_save(requisites)
            except Exception as _ex:
                return {'message': 'Incorrect data'}
            return {'message': 'Requisites successfully added'}
        return {'message': 'Entry is not executed'}

    @staticmethod
    def get():
        if check_auth():
            list_requisites = get_requisites(get_user_id())
            requisites_dict = {}
            for req in list_requisites:
                requisites_dict[req.id] = {
                    'bank': req.bank,
                    'bik': req.bik,
                    'rs': req.rs,
                    'ks': req.ks
                }
            return requisites_dict
        return {"message": 'Entry is not executed'}

    @staticmethod
    def put():
        if check_auth():
            id = request.form['id']
            bank = request.form.get('bank', None)
            bik = request.form.get('bik', None)
            rs = request.form.get('rs', None)
            ks = request.form.get('ks', None)
            requisite = get_requisite(id)

            if get_user_id() is None or requisite is None:
                return {'message': 'Incorrect id'}

            if requisite.user_id == get_user_id():
                if bank is not None:
                    requisite.bank = bank
                if bik is not None:
                    requisite.bik = bik
                if rs is not None:
                    requisite.rs = rs
                if ks is not None:
                    requisite.ks = ks
                try:
                    db.session.commit()
                except Exception as _ex:
                    if 'InvalidTextRepresentation' in str(_ex):
                        return {'message': 'Incorrect data'}
                    else:
                        return {'message': 'One of the parameters of details with has a value belonging to another '
                                           'account'}
                return {'message': 'Requisites successfully changed'}
            return {'message': 'Credentials Error'}
        return {"message": 'Entry is not executed'}

    @staticmethod
    def delete():
        if check_auth():
            try:
                id = request.form['id']
                requisite = get_requisite(id)
                if requisite.user_id == get_user_id():
                    db_delete(requisite)
                    return {'message': 'Requisites successfully deleted'}
                return {'message': 'Incorrect id'}
            except Exception as _ex:
                return {'message': 'Incorrect data'}
        return {"message": 'Entry is not executed'}


class Activity(MethodView):
    @staticmethod
    def post():
        if check_auth():
            try:
                id = request.form['id']
                requisite = get_requisite(id)
                if requisite.user_id == get_user_id():
                    down_activity = get_activity()
                    if down_activity:
                        down_activity.activity = False
                    requisite.activity = True
                    db.session.commit()
                    return {'message': 'Requisites successfully activated'}
                return {'message': 'Access denied'}
            except Exception as _ex:
                return {'message': 'Incorrect data'}
        return {"message": 'Entry is not executed'}


router.add_url_rule(
    '/requisite',
    view_func=RequisitesAPI.as_view('requisites_api'),
    methods=['POST', 'GET', 'PUT', 'DELETE']
)

router.add_url_rule(
    '/activity',
    view_func=Activity.as_view('activity'),
    methods=['POST']
)
