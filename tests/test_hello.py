from flask import json
import unittest
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import app
from app.api.v1.views import Products

class TestApp(unittest.TestCase):
    def setUp(self):
        app.create_app().testing = True
        self.app = app.create_app().test_client()

    # def test_returns_hello(self):
    #     response = self.app.get('/hello')
    #     self.assertEqual(response.data,b'hello')
    def test_returns_all_products(self):
        empty_products =  self.app.get('/api/v1/products')
        self.assertEqual(empty_products.status_code, 200)

    def test_adds_a_new_product(self):
        new_product =  self.app.post('/api/v1/products', data= json.dumps({
            "description": "Mwah",
            "product_id": 1,
            "product_image": "/images/chapo.jpg",
            "product_name": "Chapo mandondo",
            "product_price": 70,
            "quantity": 3
            }), content_type='application/json')
        self.assertEqual(new_product.status_code, 201)
    
    def test_returns_one_product(self):
        product = self.app.get('/api/v1/products/1')
        self.assertEqual(product.status_code, 200)


# This one aint running.. You will come to it later
    # def test_returns_error_on_id_values_below_one(self):
    #     response = self.app.get('/api/v1/product/0')
    #     assert b'Sorry, you have entered an invalid Product_id value' in response.data
if __name__ == '__main__':
    unittest.main()

