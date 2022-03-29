from fastapi import APIRouter
from fastapi import Query

from src.crud import users
from src.schemas import RegisterUserRequest, UserModel


router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.post('', summary='')
def users_list(age: int = Query(description="Количество лет", default=None)):
    """
    Список пользователей
    """
    return users.user_list(age)


@router.post('/register-user/', summary='CreateUser', response_model=UserModel)
def register_user(user: RegisterUserRequest):
    """
    Регистрация пользователя
    """
    return users.register_user(user)
