import sys
sys.path.append(".")
from src.models.product_model import Product
from src.models.base_model import BaseModel
import pytest


class TestProduct:
    @pytest.fixture
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

    @pytest.mark.parametrize('value', [('Price'), (50), (0), (True)])
    def test_type_height_product(self, create_instance, value):
        with pytest.raises(TypeError):
            create_instance.height = value

    def test_small_value_height_product(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.height = 0.5

    def test_big_value_height_product(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.height = 150.00

    @pytest.mark.parametrize('value', [('Price'), (50), (0), (True)])
    def test_type_width_product(self, create_instance, value):
        with pytest.raises(TypeError):
            create_instance.width = value

    def test_small_value_width_product(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.width = 9.99

    def test_big_value_width_product(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.width = 150.00

    @pytest.mark.parametrize("length", ['string', 20])
    def test_type_length_product(self, create_instance, length):
        with pytest.raises(TypeError):
            create_instance.length = length

    def test_small_value_length_product(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.length = 10.9

    def test_big_value_length_product(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.length = 110.5

    @pytest.mark.parametrize("weight", ['weight', 110])
    def test_type_weight_product(self, create_instance, weight):
        with pytest.raises(TypeError):
            create_instance.weight = weight

    def test_small_value_weight_product(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.weight = -1.0

    def test_big_value_weight_product(self, create_instance):
        with pytest.raises(ValueError):
            create_instance.weight = 30.5
