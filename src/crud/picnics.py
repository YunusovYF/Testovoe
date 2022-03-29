import datetime as dt
from sqlalchemy.orm.session import Session
from fastapi import HTTPException

from src.database.models import DbCity, DbPicnic, DbPicnicRegistration
from src.schemas.picnics import PicnicRegistrationInSchema


def get_all_picnics(db: Session):
    return db.query(DbPicnic).all()
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
    picnics = db.query(DbPicnic).filter(DbPicnic.time == datetime)
    if not past:
        picnics = picnics.filter(DbPicnic.time >= dt.datetime.now())

    return [{
        'id': pic.id,
        'city': db.query(DbCity).filter(DbCity.id == pic.id).first().name,
        'time': pic.time,
        'users': [
            {
                'id': pr.user.id,
                'name': pr.user.name,
                'surname': pr.user.surname,
                'age': pr.user.age,
            }
            for pr in db.query(DbPicnicRegistration).filter(DbPicnicRegistration.picnic_id == pic.id)],
    } for pic in picnics]


def create_picnic(city_id, datetime, db: Session):
    p = DbPicnic(city_id=city_id, time=datetime)
    db.add(p)
    db.commit()

    return {
        'id': p.id,
        'city': db.query(DbCity).filter(DbCity.id == p.city_id).first().name,
        'time': p.time,
    }


def register_to_picnic(db: Session, request: PicnicRegistrationInSchema):
    user_picnic = db.query(DbPicnicRegistration).filter(DbPicnicRegistration.user_id == request.user_id)\
        .filter(DbPicnicRegistration.picnic_id == request.picnic_id).first()
    if user_picnic:
        raise HTTPException(status_code=400, detail='Пользователь уже зарегистрирован на пикник')
    new_user_picnic = DbPicnicRegistration(
        user_id=request.user_id,
        picnic_id=request.picnic_id
    )
    db.add(new_user_picnic)
    db.commit()
    db.refresh(new_user_picnic)

    return new_user_picnic
