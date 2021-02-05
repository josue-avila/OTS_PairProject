from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class BaseModel(BASE):
    __abstract__ = True
    id_ = Column('id', Integer, primary_key=True, nullable=True)
