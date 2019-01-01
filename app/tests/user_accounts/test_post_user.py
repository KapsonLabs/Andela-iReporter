"""
Author: Allan Katongole
Date: 19th December 2018
Test file for the user POST endpoint
"""

import unittest
import json
from app import app

class TestPostUser(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()


    def test_add_user(self):
        user_data = {
                        "firstname":"Allan",
                        "lastname":"Katongole",
                        "email":"kapson@gmail.com",
                        "password":"hall65536",
                        "othernames":"",
                        "phoneNumber":"0780820744",
                        "username":"kapy",
                        "isAdmin":"False"
                    }

        response = self.app_tester.post('/api/v1/users/', json=user_data)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 201)

    def test_add_user_improper_email(self):
        user_data = {
                        "firstname":"Allan",
                        "lastname":"Katongole",
                        "email":"kapson@gmailcom",
                        "password":"hall65536",
                        "othernames":"",
                        "phoneNumber":"0780820744",
                        "username":"kapy",
                        "isAdmin":"False"
                    }

        response = self.app_tester.post('/api/v1/users/', json=user_data)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 400)

    def test_add_user_improper_data(self):
        user_data = {
                        "firstname":"Allan",
                        "lastname":"Katongole",
                        "email":"kapson@gmailcom",
                        "password":"hall65536",
                        "phoneNumber":"0780820744",
                        "username":"kapy",
                        "isAdmin":"False"
                    }

        response = self.app_tester.post('/api/v1/users/', json=user_data)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], "Improper data body, Read documentation to send the appropriate data")