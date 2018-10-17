from flask import Flask, Blueprint

from flask_restful import Api, Resource

from app.api.v1.views import Products, OneProduct, SaleProduct

v1 = Blueprint('bp', __name__, url_prefix='/api/v1')
api = Api(v1)

api.add_resource(Products,'/products')
api.add_resource(OneProduct,'/products/<int:id>')
api.add_resource(SaleProduct,'/sales/<int:id>')