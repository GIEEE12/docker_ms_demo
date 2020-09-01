from unittest import TestCase

import requests


class TestFlaskApiUsingRequests(TestCase):
    def test_products(self):
        print("Checking product lists")
        response = requests.get('http://172.29.96.1:8081/api/products')
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        print("Checking create product")
        payload = {
            "product": {
                "image": "banana.png",
                "name": "Product 1",
                "price": 2,
                "slug": "product-1"
            }
        }
        response = requests.post('http://172.29.96.1:8081/api/product/create', payload)
        self.assertEqual(response.status_code, 200)

    def test_product(self):
        print("Checking a single product")
        response = requests.get('http://172.29.96.1:8081/api/product/product-1')
        self.assertEqual(response.status_code, 200)

obj = TestFlaskApiUsingRequests()
obj.test_products()
obj.test_create()
obj.test_product()