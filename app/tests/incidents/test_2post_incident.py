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
        incident_data = {
                        "createdBy":"Allan2",
                        "incident_type":"red-flag",
                        "location":[1.0, 2.0],
                        "images":["come.jpg"],
                        "videos":["come.mp4"],
                        "comment":"There is bribery here"
                        }

        response = self.app_tester.post('/api/v1/red-flags/', json=incident_data)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 201)

    def test_add_red_flag_improper_location(self):
        incident_data = {
                        "createdBy":"Allan2",
                        "incident_type":"red-flag",
                        "location":"1.0, 2.0",
                        "images":["come.jpg"],
                        "videos":["come.mp4"],
                        "comment":"There is bribery here"
                        }

        response = self.app_tester.post('/api/v1/red-flags/', json=incident_data)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 400)

    def test_add_red_flag_improper_format(self):
        incident_data = {
                        "createdBy":"Allan2",
                        "incident_type":"red-flag",
                        "images":["come.jpg"],
                        "videos":["come.mp4"],
                        "comment":"There is bribery here"
                        }

        response = self.app_tester.post('/api/v1/red-flags/', json=incident_data)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 400)
        self.assertEqual(data['error'], "Improper data body, Read documentation to send the appropriate data")

    