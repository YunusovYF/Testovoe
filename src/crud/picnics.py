import datetime as dt
from sqlalchemy.orm.session import Session
from fastapi import HTTPException

from src.database.models import DbCity, DbPicnic, DbPicnicRegistration, DbUser
from src.schemas.picnics import PicnicRegistrationInSchema, PicnicOutSchema


def user_picnic_query(db: Session):
    return db.query(DbPicnic, DbCity, DbUser) \
        .outerjoin(DbCity, DbCity.id == DbPicnic.city_id) \
        .outerjoin(DbPicnicRegistration, DbPicnic.id == DbPicnicRegistration.picnic_id) \
        .outerjoin(DbUser, DbUser.id == DbPicnicRegistration.user_id)


def create_schema(user_picnic):
    picnics = []
    users = []
    for i, el in enumerate(user_picnic):
        picnic = el[0]
        city = el[1]

        if i != len(user_picnic)-1 and el[0] == user_picnic[i+1][0]:
            users.append(el[2])

        else:
            users.append(el[2])
            picnic_schema = PicnicOutSchema(id=picnic.id,
                                            city=city,
                                            time=picnic.time,
                                            users=users)
            picnics.append(picnic_schema)
            users = []

    return picnics

def get_all_picnics(db: Session):
    user_picnic = user_picnic_query(db).all()

    return create_schema(user_picnic)


def get_picnics_by_date(datetime, past, db: Session):

    user_picnic = user_picnic_query(db)

    user_picnic = user_picnic.filter(DbPicnic.time == datetime)
    if not past:
        user_picnic = user_picnic.filter(DbPicnic.time >= dt.datetime.now())
    user_picnic = user_picnic.all()

    return create_schema(user_picnic)


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
