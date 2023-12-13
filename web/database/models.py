from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'web_users'

    id = Column(Integer, primary_key=True)

    username = Column(String, unique=True)
    password = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self):
        return f'{self.id} - {self.username}'


class UserSession(Base):
    __tablename__ = 'user_sessions'

    id = Column(Integer, primary_key=True)

    user_id = Column(ForeignKey('web_users.id'))
    client_id = Column(ForeignKey('clients.id'))

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)

    name = Column(String)
    description = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class InformationChannel(Base):
    __tablename__ = 'channels'

    id = Column(Integer, primary_key=True)

    name = Column(String)
    description = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)

    data = Column(JSONB)
    user_id = Column(ForeignKey('web_users.id'))

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
