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
        incident_data = {"createdBy":"Allan2",
                        "incident_type":"red-flag",
                        "location":"Kampala",
                        "status":"under_investigation",
                        "Image":"come.jpg",
                        "Videos":"come.mp4",
                        "comment":"There is bribery here"}

        self.app_tester.post('/api/v1/red-flags', json=incident_data)
        incident_data = {"createdBy":"Allan",
                        "incident_type":"intervention",
                        "location":"Mbarara",
                        "status":"under_investigation",
                        "Image":"go.jpg",
                        "Videos":"again.mp4",
                        "comment":"There is bribery here assured"}
        self.app_tester.post('/api/v1/red-flags', json=incident_data)

        response = self.app_tester.get('/api/v1/red-flags')
        data = json.loads(response.data)

        id = data['data'][0]['id']
        response_get_unique = self.app_tester.get('/api/v1/red-flags/{0}'.format(id))
        data_get_unique = json.loads(response_get_unique.data)
        print(data_get_unique)
        #self.assertEqual(data_get_unique['data'][0]['createdBy'], 'Allan2')
        self.assertEqual(data_get_unique.get("status"), 200)

    def test_raises_404(self):
        id = randint(1,100)
        response_get_unique_404 = self.app_tester.get('/api/v1/red-flags/{0}'.format(id))
        data_get_unique_404 = json.loads(response_get_unique_404.data)
        print(data_get_unique_404)
        self.assertEqual(data_get_unique_404.get("status"), 404)