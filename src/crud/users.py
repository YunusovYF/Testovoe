from fastapi import HTTPException

from src.database.database import SessionLocal
from src.database.models import User
from src.schemas.users import UserModel


def get_all_users(db: SessionLocal):
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail=f'В базе данных нет записей о пользователях')
    return [{
        'id': user.id,
        'name': user.name,
        'surname': user.surname,
        'age': user.age,
    } for user in users]


def get_users_by_age(age, db: SessionLocal):
    users = db.query(User).filter(User.age == age).all()
    if not users:
        raise HTTPException(status_code=404, detail=f'Пользователей {age} лет нет в базе данных')
    return [{
        'id': user.id,
        'name': user.name,
        'surname': user.surname,
        'age': user.age,
    } for user in users]


def create_user(user, db: SessionLocal):
    user_object = User(**user.dict())
    db.add(user_object)
    db.commit()

    return UserModel.from_orm(user_object)
