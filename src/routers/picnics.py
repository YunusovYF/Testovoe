from fastapi import APIRouter, Depends
from fastapi import Query
from sqlalchemy.orm.session import Session
import datetime as dt

from src.database.database import get_db
from src.crud import picnics
from src.schemas.picnics import PicnicOutSchema


router = APIRouter(
    prefix='/picnics',
    tags=['Picnics']
)


@router.get('', response_model=PicnicOutSchema)
def get_all_picnics(db: Session = Depends(get_db)):
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
    - **age** возраст
    """
    picnic = picnics.get_all_picnics(db)
    print(picnic)
    return picnic


@router.get('/{datetime}/{past}', summary='All Picnics')
def get_picnics_by_date(
        datetime: dt.datetime = Query(default=None, description='Время пикника (по умолчанию не задано)'),
        past: bool = Query(default=True, description='Включая уже прошедшие пикники'),
        db: Session = Depends(get_db)):
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
    return picnics.get_picnics_by_date(datetime, past, db)


@router.post('')
def create_picnic(city_id: int = None, datetime: dt.datetime = None, db: Session = Depends(get_db)):
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
    return picnics.create_picnic(city_id, datetime, db)


@router.post('/registration')
def register_to_picnic(*_, **__,):
    """
    Регистрация пользователя на пикник
    (Этот эндпойнт необходимо реализовать в процессе выполнения тестового задания)
    """
    return picnics.register_to_picnic(*_, **__,)
