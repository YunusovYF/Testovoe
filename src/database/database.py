from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создание сессии
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Подключение базы (с автоматической генерацией моделей)
Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()





