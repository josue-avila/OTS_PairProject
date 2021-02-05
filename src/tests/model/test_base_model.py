import sys
sys.path.append(".")
import pytest
from src.models.product_model import Product
from src.models.base_model import BaseModel


class TestBaseDao:
    @pytest.fixture
    def base_instance(self):
        return BaseModel()

    @pytest.fixture
    def base_not_instance(self):
        return 'BaseModel'

    def test_instance(self, base_instance):
        assert isinstance(base_instance, BaseModel)

    def test_not_instance(self, base_not_instance):
        with pytest.raises(AssertionError):
            assert isinstance(base_not_instance, BaseModel)
