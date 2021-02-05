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

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError('Name is not the expected type!')
        if not name.strip():
            raise ValueError('Name can not be empty!')
        if len(name) > 100:
            raise ValueError('Name is not the expected size!')

        return name

    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError('Description is not the expected type!')
        if len(description) > 255:
            raise ValueError('Description is not the expected size!')

        return description

    @validates('price')
    def validate_price(self, key, price):
        if not isinstance(price, float):
            raise TypeError('Price is not the expected type!')
        if not price:
            raise ValueError('Price can not be empty!')
        if price < 14.99:
            raise ValueError('The price must be higher than R$14,99!')

        return price
