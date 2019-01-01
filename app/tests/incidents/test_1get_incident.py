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

	def test_a_get_empty_data_store(self):

		response = self.app_tester.get('/api/v1/red-flags/')
		data = json.loads(response.data)
		self.assertEqual(data['status'], 200)
		self.assertEqual(data['message'], "There are no incidents yet")

	def test_get_all_red_flags(self):

		incident_data = {
						"createdBy":"Allan",
						"incident_type":"red-flag",
						"location":[1.0, 2.0],
						"images":["come.jpg"],
						"videos":["come.mp4"],
						"comment":"There is bribery here"
						}

		self.app_tester.post('/api/v1/red-flags/', json=incident_data)

		response = self.app_tester.get('/api/v1/red-flags/')
		data = json.loads(response.data)
		self.assertEqual(data['status'], 200)
		self.assertEqual(len(data['data']), 1)
		self.assertEqual(data['data'][0]['createdBy'], 'Allan')

	def test_get_unique_red_flag(self):
		
		get_unique = self.app_tester.get('/api/v1/red-flags/1')
		data_get_unique = json.loads(get_unique.data)
		self.assertEqual(data_get_unique["status"], 200)
		self.assertEqual(data_get_unique['data'][0]['createdBy'], 'Allan')

	def test_get_unique_raises_404(self):
		response_get_unique_404 = self.app_tester.get('/api/v1/red-flags/6')
		data_get_unique_404 = json.loads(response_get_unique_404.data)
		self.assertEqual(data_get_unique_404.get("status"), 404)


if __name__ == '__main__':
    unittest.main()