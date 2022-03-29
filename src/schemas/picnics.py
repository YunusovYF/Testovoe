from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from src.schemas.cities import CitiesNameSchema
from src.schemas.users import UserModel


class PicnicOutSchema(BaseModel):
    id: int
    city: CitiesNameSchema
    time: datetime
    users: List[UserModel]

    class Config:
        orm_mode = True


class PicnicRegistrationInSchema(BaseModel):
    user_id: int
    picnic_id: int

    class Config:
        orm_mode = True


class PicnicRegistrationOutSchema(PicnicRegistrationInSchema):
    id: int

    class Config:
        orm_mode = True
