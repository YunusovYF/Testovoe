from fastapi import APIRouter
from fastapi import Query

from src.crud import cities


router = APIRouter(
    prefix='/cities',
    tags=['Cities']
)


@router.get('', summary='Create City', description='Создание города по его названию')
def create_city(city: str = Query(description="Название города", default=None)):
    return cities.create_city(city)


@router.post('/get-cities/', summary='Get Cities')
def cities_list(q: str = Query(description="Название города", default=None)):
    """
    Получение списка городов
    """
    return cities.cities_list(q)
