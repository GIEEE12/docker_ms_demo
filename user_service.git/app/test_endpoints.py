from unittest import TestCase

import requests


class TestFlaskApiUsingRequests(TestCase):
    def test_login(self):
        print("Testing user login")
        response = requests.post('http://172.29.96.1:8082/api/login')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        print("testing user logout")
        response = requests.post('http://172.29.96.1:8082/api/user/logout')
        self.assertEqual(response.status_code, 200)

obj = TestFlaskApiUsingRequests()
obj.test_login()
obj.test_logout()