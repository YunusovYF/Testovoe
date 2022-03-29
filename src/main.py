from fastapi import FastAPI
import logging.config
import os
from fastapi.responses import JSONResponse
from sqlalchemy.exc import OperationalError

from src.routers import all
from src.database.models import Base
from src.database.database import engine

if not os.path.isdir('src/logs'):
    os.makedirs('src/logs')

logging.config.fileConfig('src/logging.conf')
logging.info(f'Конфигурация логов загружена')

app = FastAPI()


@app.exception_handler(Exception)
def validation_exception_handler(request, exc):
    base_error_message = f'Ошибка в исполнении: {request.method}: {request.url}'
    msg = f'{base_error_message}. Детали: {exc}'
    logging.error(msg)
    return JSONResponse(status_code=500, content={'message': msg})


app.include_router(all.router)

try:
    Base.metadata.create_all(engine)
except OperationalError:
    logging.error(f'Ошибка в подключении к базе данных', exc_info=True)


@app.on_event("startup")
def start_backend():
    logging.info(f'Старт сервера.')


@app.on_event("shutdown")
def stop_backend():
    logging.info(f'Остановка сервера.')
