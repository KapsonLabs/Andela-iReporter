"""
Author: Allan Katongole
Date: 20th December 2018
Test file for the get
unique incident route
"""

import unittest
import json
from app import app
from random import randint

class TestGetUniqueIncident(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()

    def test_get_unique_incident(self):
        incident_data = {
                        "createdBy":"Allan2",
                        "incident_type":"red-flag",
                        "location":[1,2],
                        "images":["come.jpg"],
                        "videos":["come.mp4"],
                        "comment":"There is bribery here"
                        }

        self.app_tester.post('/api/v1/red-flags/', json=incident_data)

        get_unique = self.app_tester.get('/api/v1/red-flags/2')
        data_get_unique = json.loads(get_unique.data)
        self.assertEqual(data_get_unique["status"], 200)
        self.assertEqual(data_get_unique['data'][0]['_createdBy'], 'Allan')

    def test_get_unique_raises_404(self):
        response_get_unique_404 = self.app_tester.get('/api/v1/red-flags/6')
        data_get_unique_404 = json.loads(response_get_unique_404.data)
        print(data_get_unique_404)
        self.assertEqual(data_get_unique_404.get("status"), 404)
