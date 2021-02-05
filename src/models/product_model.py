from sqlalchemy import Column, String, Float
from src.models.base_model import BaseModel
from sqlalchemy.orm import validates


class Product(BaseModel):
    __tablename__ = 'PRODUCT_G10'
    name = Column('name', String(length=100), nullable=True)
    description = Column('description', String(length=255), nullable=False)
    price = Column('price', Float, nullable=True)
    height = Column('box_height', Float, nullable=True)
    width = Column('box_width', Float, nullable=True)
    length = Column('box_length', Float, nullable=True)
    weight = Column('box_weight', Float, nullable=True)

    def __init__(self, name: str, price: float, height: float, width: float, length: float, weight: float, description: str = None) -> None:
        self.name = name
        self.price = price
        self.height = height
        self.width = width
        self.length = length
        self.weight = weight
        self.description = description
