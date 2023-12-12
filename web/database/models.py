from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime
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

# class Foo(BaseClass):
#     ...
