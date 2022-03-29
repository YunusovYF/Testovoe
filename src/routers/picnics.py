from fastapi import APIRouter
from fastapi import Query
import datetime as dt

from src.crud import picnics


router = APIRouter(
    prefix='/picnics',
    tags=['Picnics']
)


@router.get('', summary='All Picnics')
def get_all_picnics():
    """
    Список всех пикников

    Args:


    Returns:
    - **id** порядковый номер пикника
    - **city** город пикника
    - **time** время проведения

    **users** пользователи зарегистрированные на пикник:
    - **id** Порядковый номер
    - **name** Имя
    - **surname** Фамилия
    - **age** возвраст
    """
    return picnics.get_all_picnics()


@router.get('/{datetime}/{past}', summary='All Picnics')
def get_picnics_by_date(
        datetime: dt.datetime = Query(default=None, description='Время пикника (по умолчанию не задано)'),
        past: bool = Query(default=True, description='Включая уже прошедшие пикники')):
    """
    Список всех пикников

    Args:
    - **datetime** время пикника
    - **past** фильтр прошедших мероприятий

    Returns:
    - **id** порядковый номер пикника
    - **city** город пикника
    - **time** время проведения

    **users** пользователи зарегистрированные на пикник:
    - **id** Порядковый номер
    - **name** Имя
    - **surname** Фамилия
    - **age** возраст
    """
    return picnics.get_picnics_by_date(datetime, past)


@router.post('')
def create_picnic(city_id: int = None, datetime: dt.datetime = None):
    """
    Регистрация пикника

    Args:
    - **city_id** город пикника
    - **datetime** время пикника

    Returns:
    - **id** порядковый номер пикника
    - **city** город пикника
    - **time** время проведения
    """
    return picnics.create_picnic(city_id, datetime)


@router.post('/registration')
def register_to_picnic(*_, **__,):
    """
    Регистрация пользователя на пикник
    (Этот эндпойнт необходимо реализовать в процессе выполнения тестового задания)
    """
    return picnics.register_to_picnic(*_, **__,)
