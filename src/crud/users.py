from fastapi import HTTPException

from src.database.database import Session
from src.database.models import User
from schemas.users import UserModel


def user_list(age):
    if age:
        users = Session().query(User).filter(User.age == age).all()
        if not users:
            raise HTTPException(status_code=404, detail=f'Пользователей {age} лет нет в базе данных')
    else:
        users = Session().query(User).all()
    return [{
        'id': user.id,
        'name': user.name,
        'surname': user.surname,
        'age': user.age,
    } for user in users]


def register_user(user):
    user_object = User(**user.dict())
    s = Session()
    s.add(user_object)
    s.commit()

    return UserModel.from_orm(user_object)