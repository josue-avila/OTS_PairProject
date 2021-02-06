from flask import Flask
from flask_restful import Api

from src.resources.product_resources import ProductResource

app_api = Flask(__name__)
api = Api(app_api)

api.add_resource(ProductResource, '/api/product', endpoint='products')
api.add_resource(ProductResource, '/api/product/<int:id_>', endpoint='product')


@app_api.route('/')
def index():
    return 'Bem Vindo a API do olist!'
