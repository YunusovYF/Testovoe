from fastapi import HTTPException

from src.database.database import Session
from src.database.models import City
from src.external_requests import CityWeather


def create_city(city):
    if city is None:
        raise HTTPException(status_code=400, detail='Параметр city должен быть указан')
    check = CityWeather()
    if not check.check_existing(city):
        raise HTTPException(status_code=400, detail='Параметр city должен быть существующим городом')

    city_object = Session().query(City).filter(City.name == city.capitalize()).first()
    if city_object is None:
        city_object = City(name=city.capitalize())
        s = Session()
        s.add(city_object)
        s.commit()

    return {'id': city_object.id, 'name': city_object.name, 'weather': city_object.weather}


def cities_list(q):
    if q:
        cities = Session().query(City).filter(City.name == q).all()
        if not cities:
            raise HTTPException(status_code=404, detail=f'Города {q} нет в базе данных')

    else:
        cities = Session().query(City).all()

    return [{'id': city.id, 'name': city.name, 'weather': city.weather} for city in cities]
