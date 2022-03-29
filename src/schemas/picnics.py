from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class PicnicOutSchema(BaseModel):
    id: int
    city_id: int
    time: datetime

    class Config:
        orm_mode = True
