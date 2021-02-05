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

    def __init__(self, name: str, price: float, height: float, width: float, length: float, weight: float,
                 description: str = None) -> None:
        self.name = name
        self.price = price
        self.height = height
        self.width = width
        self.length = length
        self.weight = weight
        self.description = description

    @validates('height')
    def validates_height(self, key, height: float) -> float:
        if not isinstance(height, float):
            raise TypeError('Box height must be float')
        if 1.0 > height > 100.0:
            raise ValueError('Box height must be between 1.0cm and 100.0cm')
        return height

    @validates('width')
    def validates_width(self, key, width: float) -> float:
        if not isinstance(width, float):
            raise TypeError('Box width must be float')
        if 10.0 > width > 100.0:
            raise ValueError('Box height must be between 10.0cm and 100.0cm')
        return width

    @validates('length')
    def validates_length(self, key, length: float) -> float:
        if not isinstance(length, float):
            raise TypeError('Box length must be float')
        if 15.0 > length > 100.0:
            raise ValueError('Box length must be between 15.0cm and 100.0cm')
        return length

    @validates('weight')
    def validates_length(self, key, weight: float) -> float:
        if not isinstance(weight, float):
            raise TypeError('Box weight must be float')
        if 0.0 > weight > 30.0:
            raise ValueError('Box weight must be between 0.0Kg and 30Kg')
        return weight
