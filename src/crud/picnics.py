import datetime as dt
from sqlalchemy.orm.session import Session

from src.database.models import City, Picnic, PicnicRegistration


def get_all_picnics(db: Session):
    return db.query(Picnic).all()
    # return [{
    #     'id': pic.id,
    #     'city': Session().query(City).filter(City.id == pic.id).first().name,
    #     'time': pic.time,
    #     'users': [
    #         {
    #             'id': pr.user.id,
    #             'name': pr.user.name,
    #             'surname': pr.user.surname,
    #             'age': pr.user.age,
    #         }
    #         for pr in Session().query(PicnicRegistration).filter(PicnicRegistration.picnic_id == pic.id)],
    # } for pic in picnics]


def get_picnics_by_date(datetime, past, db: Session):
    picnics = db.query(Picnic).filter(Picnic.time == datetime)
    if not past:
        picnics = picnics.filter(Picnic.time >= dt.datetime.now())

    return [{
        'id': pic.id,
        'city': db.query(City).filter(City.id == pic.id).first().name,
        'time': pic.time,
        'users': [
            {
                'id': pr.user.id,
                'name': pr.user.name,
                'surname': pr.user.surname,
                'age': pr.user.age,
            }
            for pr in db.query(PicnicRegistration).filter(PicnicRegistration.picnic_id == pic.id)],
    } for pic in picnics]


def create_picnic(city_id, datetime, db: Session):
    p = Picnic(city_id=city_id, time=datetime)
    db.add(p)
    db.commit()

    return {
        'id': p.id,
        'city': db.query(City).filter(City.id == p.city_id).first().name,
        'time': p.time,
    }


def register_to_picnic(*_, **__,):
    # TODO: Сделать логику
    return ...
