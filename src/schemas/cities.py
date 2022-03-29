from pydantic import BaseModel


class CitiesNameSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True
