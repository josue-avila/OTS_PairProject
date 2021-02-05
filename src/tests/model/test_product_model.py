import sys
sys.path.append(".")
import pytest
from src.models.product_model import Product
from src.models.base_model import BaseModel


class TestProduct():

    @pytest.fixture()
    def create_instance(self):
        obj = Product('Smartphone XPTO', 1599.99, 50.00, 10.00,
                      30.00, 0.800, 'Smartphone com 8GB de RAM')
        return obj

    def test_product_instance(self, create_instance):
        assert isinstance(create_instance, BaseModel)
        assert isinstance(create_instance, Product)

    def test_not_name_product(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.name = ''

    def test_len_name_product(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.name = 'Test '*100

    def test_type_name_product(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.name = 10

    def test_len_description_product(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.description = 'Test '*200

    def test_type_description_product(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.description = 10

    def test_not_price_product(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.price = 0.00

    def test_type_price_product(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.price = 'Price'

    def test_value_price_product(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.price = 10.99

    def test_not_height_product(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.height = 0.00

    def test_type_height_product(self, create_instance):
        with pytest.raises(TypeError):
            create_instance.height = 'Price'

    def test_small_value_height_product(self):
        with pytest.raises(ValueError):
            obj = Product('Smartphone XPTO', 1599.99, 50.00, 10.00,
                30.00, 0.800, 'Smartphone com 8GB de RAM')
            obj.height = 150
    # def test_big_value_height_product(self, create_instance):
    #     with pytest.raises(ValueError):
    #         create_instance.height = 150.00
    #


TestProduct().test_small_value_height_product()