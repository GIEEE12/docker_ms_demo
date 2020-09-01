from unittest import TestCase

import requests


class TestFlaskApiUsingRequests(TestCase):
    def test_home(self):
        print("checking for homepage")
        response = requests.get('http://172.29.96.1')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        print('Checking for login page')
        response = requests.get('http://172.29.96.1/login')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        print("checking for register page")
        response = requests.get('http://172.29.96.1/register')
        self.assertEqual(response.status_code, 200)

    def test_checkout(self):
        print("checking for checkout page")
        response = requests.get('http://172.29.96.1/checkout')
        self.assertEqual(response.status_code, 200)
obj = TestFlaskApiUsingRequests()
obj.test_home()
obj.test_login()
obj.test_register()
obj.test_checkout()