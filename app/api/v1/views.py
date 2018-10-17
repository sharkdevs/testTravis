from flask import Flask, Response, make_response, jsonify, request
from flask_restful import Resource

from app.api.v1.models import Product as p, products
from app.api.v1.models import CreateSale as cs
class Products(Resource):

    """Gets all the products in the store"""
    def get(self):
        return make_response(jsonify({
            "Products": products
        }), 200)

    """Add a new product to the store"""
    def post(self):
        data = request.get_json()

        # create one product
        product = p(data['product_name'],data['product_price'],data['description'],data['quantity'],data['product_image']).create_a_product()

        # add to a list and return it
        products.append(product)
        return make_response(jsonify({
            "products" : products
        }), 201)

class OneProduct(Resource):

    """Get the product by their id"""
    def get(self, id):
        self.id=id
        return p.get_one_product(self,self.id)

class SaleProduct(Resource):

    """Get product in the cart and sale it"""
    def get(self, id):
        self.id = id
        # product = p.get_one_product(self, id)
        return cs.sale_a_product(self, self.id)

