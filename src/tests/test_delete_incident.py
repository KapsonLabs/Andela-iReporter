"""
Author: Allan Katongole
Date: 20th December 2018
Test file for the get
unique incident route
"""

import unittest
import json
from src.app import app

class TestGetUniqueIncident(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()

    def test_delete_unique_incident():
        pass

    def test_raises_404():
        pass