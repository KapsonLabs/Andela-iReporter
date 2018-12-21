"""
Author: Allan Katongole
Date: 20th December 2018
Test file for the get
unique incident route
"""

import unittest
import json
from src.app import app
from random import randint

class TestDeleteUniqueIncident(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()

    def test_delete_unique_incident(self):
        pass

    def test_raises_404(self):
        pass