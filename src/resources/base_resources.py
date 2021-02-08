from flask import request
from typing import Type
from flask_restful import Resource
from src.dao.base_dao import BaseDao
from src.models.base_model import BaseModel


class BaseResource(Resource):
    def __init__(self, dao: BaseDao, model_type: Type) -> None:
        self.__dao = dao
        self.__model_type = model_type

    def get(self, id_=None):
        if id_:
            return self.__dao.read_by_id(id_)
        return self.__dao.read_all()

    def post(self):
        data = request.json
        model = self.__model_type(**data)
        self.__dao.save(model)

        return model, 200

    def put(self, id_):
        data = request.json

        if data['id_'] == id_:
            model = self.__dao.read_by_id(id_)

            for key, value in data.items():
                setattr(model, key, value)

            return self.__dao.save(model)

        return None, 404

    def delete(self, id_):
        model = self.__dao.read_by_id(id_)
        self.__dao.delete(model)
        return None, 204
