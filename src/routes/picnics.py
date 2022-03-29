from fastapi import APIRouter
from fastapi import Query
import datetime as dt

from src.crud import picnics


router = APIRouter(
    prefix='/cities',
    tags=['Cities']
)


@router.get('/all-picnics/', summary='All Picnics', tags=['picnic'])
def all_picnics(datetime: dt.datetime = Query(default=None, description='Время пикника (по умолчанию не задано)'),
                past: bool = Query(default=True, description='Включая уже прошедшие пикники')):
    """
    Список всех пикников
    """
    return picnics.all_picnics(datetime, past)


@router.get('/picnic-add/', summary='Picnic Add', tags=['picnic'])
def picnic_add(city_id: int = None, datetime: dt.datetime = None):
    return picnics.picnic_add(city_id, datetime)



@router.get('/picnic-register/', summary='Picnic Registration', tags=['picnic'])
def register_to_picnic(*_, **__,):
    """
    Регистрация пользователя на пикник
    (Этот эндпойнт необходимо реализовать в процессе выполнения тестового задания)
    """
    return picnics.register_to_picnic(*_, **__,)
