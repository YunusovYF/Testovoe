from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.services.external_requests import CityWeather
from src.database.database import Base


class DbCity(Base):
    """
    Город
    """
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    picnic = relationship('DbPicnic', back_populates='city')

    @property
    def weather(self) -> str:
        """
        Возвращает текущую погоду в этом городе
        """
        r = CityWeather()
        weather = r.get_weather(self.name)
        return weather

    def __repr__(self):
        return f'<Город "{self.name}">'


class DbUser(Base):
    """
    Пользователь
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    picnic_registration = relationship('DbPicnicRegistration', back_populates='user')

    def __repr__(self):
        return f'<Пользователь {self.surname} {self.name}>'


class DbPicnic(Base):
    """
    Пикник
    """
    __tablename__ = 'picnic'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    city = relationship('DbCity', back_populates='picnic')
    time = Column(DateTime, nullable=False)
    picnic_registration = relationship('DbPicnicRegistration', back_populates='picnic')

    def __repr__(self):
        return f'<Пикник {self.id}>'


class DbPicnicRegistration(Base):
    """
    Регистрация пользователя на пикник
    """
    __tablename__ = 'picnic_registration'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('DbUser', back_populates='picnic_registration')
    picnic_id = Column(Integer, ForeignKey('picnic.id'), nullable=False)
    picnic = relationship('DbPicnic', back_populates='picnic_registration')

    def __repr__(self):
        return f'<Регистрация {self.id}>'
