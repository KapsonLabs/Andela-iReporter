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

class TestDeleteUniqueIncident(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()

    def test_delete_unique_incident(self):

        delete_unique = self.app_tester.delete('/api/v1/red-flags/1')
        data_delete_unique = json.loads(delete_unique.data)
        self.assertEqual(data_delete_unique["status"], 200)
        self.assertEqual(data_delete_unique['data'][0]['message'], 'Red-flag record deleted successfully')

    def test_delete_unique_raises_404(self):
        response_delete_unique_404 = self.app_tester.delete('/api/v1/red-flags/6')
        data_delete_unique_404 = json.loads(response_delete_unique_404.data)
        self.assertEqual(data_delete_unique_404.get("status"), 404)