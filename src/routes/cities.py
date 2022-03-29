from fastapi import APIRouter
from fastapi import Query

from src.crud import cities


router = APIRouter(
    prefix='/cities',
    tags=['Cities']
)


@router.post('')
def create_city(city: str = Query(description="Название города", default=None)):
    """
    Создание города

    Args:
    - **city** Город

    Returns:
    - **id** Порядковый номер города
    - **name** Имя города
    - **weather** Температура в городе
    """
    return cities.create_city(city)


@router.get('')
def get_all_cities():
    """
    Получение города по запросу

    Args:


    Returns:
    - **id** Порядковый номер города
    - **name** Имя города
    - **weather** Температура в городе
    """
    return cities.get_all_cities()


@router.get('/{city_name}')
def get_cities_by_name(city_name: str = Query(description="Название города", default=None)):
    """
    Получение города по запросу

    Args:
    - **city_name** Город

    Returns:
    - **id** Порядковый номер города
    - **name** Имя города
    - **weather** Температура в городе
    """
    return cities.get_cities_by_name(city_name)
