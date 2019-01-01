"""
Author: Allan Katongole
Date: 19th December 2018
Test file for the api routes
"""

import unittest
import json
from app import app


class TestIncidents(unittest.TestCase):

	def setUp(self):
		self.app_tester = app.test_client()

	def test_all_red_flags(self):

		response = self.app_tester.get('/api/v1/red-flags/')
		data = json.loads(response.data)
		self.assertEqual(data['status'], 200)
		self.assertEqual(len(data['data']), 2)
		self.assertEqual(data['data'][0]['createdBy'], 'Allan')


if __name__ == '__main__':
    unittest.main()