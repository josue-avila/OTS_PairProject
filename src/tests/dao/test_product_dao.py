from sqlalchemy.orm.exc import UnmappedInstanceError
from src.dao.product_dao import ProductDao
from src.models.product_model import Product
from src.dao.base_dao import BaseDao
import pytest


class TestProductDao:
    @pytest.fixture
    def product_instance(self):
        product = Product('product', 20.0, 20.0, 20.0, 20.0, 1.0, 'description')
        return product

    @pytest.fixture
    def product_dao(self):
        dao = ProductDao()
        return dao

    def test_product_dao_instance(self, product_dao):
        assert isinstance(product_dao, ProductDao)
        assert isinstance(product_dao, BaseDao)

    def test_save_method(self, product_dao, product_instance):
        product_saved = product_dao.save(product_instance)
        assert product_saved.id_ is not None
        assert product_saved.name == product_instance.name
        assert product_saved.price == product_instance.price
        assert product_saved.height == product_instance.height
        assert product_saved.width == product_instance.width
        assert product_saved.length == product_instance.length
        assert product_saved.weight == product_instance.weight
        assert product_saved.description == product_instance.description
        product_dao.delete(product_saved)

    @pytest.mark.parametrize("fake_product", [
        'string', 1, 1.0, [1, 2, 3]
    ])
    def test_fail_save_method(self, product_dao, fake_product):
        with pytest.raises(UnmappedInstanceError):
            product_dao.save(fake_product)

    def test_read_by_id_method(self, product_dao, product_instance):
        product_saved = product_dao.save(product_instance)
        product_read = product_dao.read_by_id(product_saved.id_)
        assert isinstance(product_read, Product)
        product_dao.delete(product_saved)

    @pytest.mark.parametrize("fake_product", [
        'string', 1.0, [1, 2, 3]
    ])
    def test_fail_read_by_id_method(self, product_dao, fake_product):
        with pytest.raises(TypeError):
            product_dao.read_by_id(fake_product)

    def test_read_all_method(self, product_dao):
        product_list = product_dao.read_all()
        assert isinstance(product_list, list)
        assert all(isinstance(item, Product) for item in product_list)

    def test_delete_method(self, product_dao, product_instance):
        product_saved = product_dao.save(product_instance)
        product_read = product_dao.read_by_id(product_saved.id_)
        product_dao.delete(product_read)
        product_read = product_dao.read_by_id(product_saved.id_)
        assert product_read is None

    @pytest.mark.parametrize("fake_product", [
        'string', 1, 1.0, [1, 2, 3]
    ])
    def test_not_delete(self, product_dao, fake_product):
        with pytest.raises(UnmappedInstanceError):
            product_dao.delete(fake_product)
