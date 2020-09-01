from unittest import TestCase

import requests


class TestFlaskApiUsingRequests(TestCase):
    def test_home(self):
        print("checking for homepage")
        response = requests.get('http://localhost')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        print('Checking for login page')
        response = requests.get('http://localhost/login')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        print("checking for register page")
        response = requests.get('http://localhost/register')
        self.assertEqual(response.status_code, 200)

    def test_checkout(self):
        print("checking for checkout page")
        response = requests.get('http://localhost/checkout')
        self.assertEqual(response.status_code, 200)
