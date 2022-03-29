from fastapi import HTTPException

from sqlalchemy.orm.session import Session
from src.database.models import DbUser
from src.schemas.users import UserModel


def get_all_users(db: Session):
    users = db.query(DbUser).all()
    if not users:
        raise HTTPException(status_code=404, detail=f'В базе данных нет записей о пользователях')
    return [{
        'id': user.id,
        'name': user.name,
        'surname': user.surname,
        'age': user.age,
    } for user in users]


def get_users_by_age(age, db: Session):
    users = db.query(DbUser).filter(DbUser.age == age).all()
    if not users:
        raise HTTPException(status_code=404, detail=f'Пользователей {age} лет нет в базе данных')
    return [{
        'id': user.id,
        'name': user.name,
        'surname': user.surname,
        'age': user.age,
    } for user in users]


def create_user(user, db: Session):
    user_object = DbUser(**user.dict())
    db.add(user_object)
    db.commit()

    return UserModel.from_orm(user_object)
