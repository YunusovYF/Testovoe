from fastapi import FastAPI
import logging.config
import os

from src.routers import all
from src.database.models import Base
from src.database.database import engine

if not os.path.isdir('src/logs'):
    os.makedirs('src/logs')

logging.config.fileConfig('src/logging.conf')
logging.info(f'Конфигурация логов загружена')

app = FastAPI()

app.include_router(all.router)

Base.metadata.create_all(bind=engine)
