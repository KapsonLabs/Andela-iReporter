"""
Author: Allan Katongole
Date: 2nd January 2019
Test file for the user api routes
"""

import unittest
import json
from app import app


class TestGetUser(unittest.TestCase):

	def setUp(self):
		self.app_tester = app.test_client()

	def test_a_get_empty_user_data_store(self):

		response = self.app_tester.get('/api/v1/users/')
		data = json.loads(response.data)
		self.assertEqual(data['status'], 200)
		self.assertEqual(data['message'], "There are no registered users yet")

	def test_get_all_red_flags(self):

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

		self.app_tester.post('/api/v1/users/', json=user_data)

		response = self.app_tester.get('/api/v1/users/')
		data = json.loads(response.data)
		self.assertEqual(data['status'], 200)
		self.assertEqual(len(data['data']), 1)
		self.assertEqual(data['data'][0]['firstname'], 'Allan')

	def test_get_unique_user(self):
		
		get_unique = self.app_tester.get('/api/v1/users/1')
		data_get_unique = json.loads(get_unique.data)
		self.assertEqual(data_get_unique["status"], 200)
		self.assertEqual(data_get_unique['data'][0]['firstname'], 'Allan')

	def test_get_unique_raises_404(self):
		response_get_unique_404 = self.app_tester.get('/api/v1/users/6')
		data_get_unique_404 = json.loads(response_get_unique_404.data)
		self.assertEqual(data_get_unique_404.get("status"), 404)


if __name__ == '__main__':
    unittest.main()