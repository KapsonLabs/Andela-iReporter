"""
Author: Allan Katongole
Date: 19th December 2018
Test file for the api routes
"""

import unittest
import json
from api.app import app


class TestProducts(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()

    def test_all_red_flags(self):
        incident_data = {"createdBy":"Allan2",
	                    "incident_type":"red-flag",
	                    "location":"Kampala",
	                    "status":"under_investigation",
	                    "Image":"come.jpg",
	                    "Videos":"come.mp4",
	                    "comment":"There is bribery here"}

        self.app_tester.post('/products', json=incident_data)
        incident_data = {"createdBy":"Allan",
	                    "incident_type":"intervention",
	                    "location":"Mbarara",
	                    "status":"under_investigation",
	                    "Image":"go.jpg",
	                    "Videos":"again.mp4",
	                    "comment":"There is bribery here assured"}
        self.app_tester.post('/red-flags', json=incident_data)

        response = self.app_tester.get('/red-flags')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['data']), 2)
        self.assertEqual(data['data'][0]['createdBy'], 'Allan2')

    def test_add_red_flag(self):
        input_data = {"createdBy":"Allan2",
	                    "incident_type":"red-flag",
	                    "location":"Kampala",
	                    "status":"under_investigation",
	                    "Image":"come.jpg",
	                    "Videos":"come.mp4",
	                    "comment":"There is bribery here"}

        response = self.app_tester.post('/red-flags', json=incident_data)
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()