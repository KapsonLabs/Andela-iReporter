"""
Author: Allan Katongole
Date: 19th December 2018
Test file for the api routes
"""

import unittest
import json
from app import app

class TestPostIncident(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()


    def test_add_red_flag(self):
        incident_data = {"createdBy":"Allan2",
                        "incident_type":"red-flag",
                        "location":"Kampala",
                        "Image":"come.jpg",
                        "Videos":"come.mp4",
                        "comment":"There is bribery here"}

        response = self.app_tester.post('/api/v1/red-flags/', json=incident_data)
        data = json.loads(response.data)
        print(data)
        self.assertEqual(data['status'], 201)