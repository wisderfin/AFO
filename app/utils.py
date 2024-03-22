from app import db


# сохранение строки/модели в бд
def db_save(model):
    db.session.add(model)
    db.session.commit()


# удаление строки/модели из бд
def db_delete(model):
    db.session.delete(model)
    db.session.commit()
