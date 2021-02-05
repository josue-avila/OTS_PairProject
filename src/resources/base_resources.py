from flask import request
from flask_restful import Resource
from src.dao.base_dao import BaseDao
from src.models.base_model import BaseModel


class BaseResource(Resource):
    def __init__(self, dao: BaseDao, model_type: BaseModel) -> None:
        self.__dao = dao
        self.__model_type = model_type

    def get(self, id_=None):
        if id_:
            return self.__dao.read_by_id(id_)
        return self.__dao.read_all()
