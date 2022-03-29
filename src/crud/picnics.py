import datetime as dt
from src.database import Session, City, Picnic, PicnicRegistration


def all_picnics(datetime, past):
    picnics = Session().query(Picnic)
    if datetime is not None:
        picnics = picnics.filter(Picnic.time == datetime)
    if not past:
        picnics = picnics.filter(Picnic.time >= dt.datetime.now())

    return [{
        'id': pic.id,
        'city': Session().query(City).filter(City.id == pic.id).first().name,
        'time': pic.time,
        'users': [
            {
                'id': pr.user.id,
                'name': pr.user.name,
                'surname': pr.user.surname,
                'age': pr.user.age,
            }
            for pr in Session().query(PicnicRegistration).filter(PicnicRegistration.picnic_id == pic.id)],
    } for pic in picnics]


def picnic_add(city_id, datetime):
    p = Picnic(city_id=city_id, time=datetime)
    s = Session()
    s.add(p)
    s.commit()

    return {
        'id': p.id,
        'city': Session().query(City).filter(City.id == p.city_id).first().name,
        'time': p.time,
    }


def register_to_picnic(*_, **__,):
    # TODO: Сделать логику
    return ...
