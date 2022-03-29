from fastapi import APIRouter, Depends
from fastapi import Query
from sqlalchemy.orm.session import Session
import datetime as dt
from typing import List

from src.database.database import get_db
from src.crud import picnics
from src.schemas.picnics import PicnicOutSchema, PicnicRegistrationOutSchema, PicnicRegistrationInSchema


router = APIRouter(
    prefix='/picnics',
    tags=['Picnics']
)


@router.get('', response_model=List[PicnicOutSchema])
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
    return picnics.get_all_picnics(db)


@router.get('/{datetime}/{past}', response_model=List[PicnicOutSchema])
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


@router.post('/registration', response_model=PicnicRegistrationOutSchema)
def register_to_picnic(request: PicnicRegistrationInSchema, db: Session = Depends(get_db)):
    """
    Регистрация пользователей на пикники

    Args:
    - **user_id** порядковый номер пользователя
    - **picnic_id** порядковый номер пикника

    Returns:
    - **id** порядковый номер регистрации
    - **user_id** порядковый номер пользователя
    - **picnic_id** порядковый номер пикника
    """
    return picnics.register_to_picnic(db, request)
