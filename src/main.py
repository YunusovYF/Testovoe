from fastapi import FastAPI

from src.routes import all
from src.database.models import Base
from src.database.database import engine

app = FastAPI()

app.include_router(all.router)

Base.metadata.create_all(bind=engine)
