from fastapi import APIRouter
from fastapi import Query

from src.crud import users
from src.schemas.users import RegisterUserRequest, UserModel


router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('')
def get_all_users():
    """
    Список пользователей

    Args:


    Returns:
    - **id** Порядковый номер
    - **name** Имя
    - **surname** Фамилия
    - **age** возраст
    """
    return users.get_all_users()


@router.get('/{age}')
def get_users_by_age(age: int = Query(description="Количество лет", default=None)):
    """
    Список пользователей

    Args:
    - **age** фильтр списка пользователей по возрасту

    Returns:
    - **id** Порядковый номер
    - **name** Имя
    - **surname** Фамилия
    - **age** возраст
    """
    return users.get_users_by_age(age)


@router.post('', response_model=UserModel)
def create_user(user: RegisterUserRequest):
    """
    Регистрация пользователя

    Args:
    - **user** список данных по пользователю

    Returns:
    - **id** Порядковый номер
    - **name** Имя
    - **surname** Фамилия
    - **age** возраст
    """
    return users.create_user(user)
