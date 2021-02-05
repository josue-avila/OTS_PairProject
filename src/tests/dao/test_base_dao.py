from src.dao.base_dao import BaseDao
from src.models.base_model import BaseModel
from src.models.product_model import Product
import pytest


class TestBaseDao:
    @pytest.fixture
    def base_dao_model_instance(self):
        return BaseDao(Product)

    @pytest.fixture
    def base_dao_base_model_instance(self):
        return BaseDao(BaseModel)

    def test_base_dao_instance(self, base_dao_model_instance, base_dao_base_model_instance):
        assert isinstance(base_dao_model_instance, BaseDao)
        assert isinstance(base_dao_base_model_instance, BaseDao)
