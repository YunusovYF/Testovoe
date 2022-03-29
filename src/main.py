from fastapi import FastAPI

from src.routes import all

app = FastAPI()

app.include_router(all.router)
