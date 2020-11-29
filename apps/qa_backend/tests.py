from django.test import TestCase
from django.test import Client
from rest_framework import status
from rest_framework.test import APIClient

# from django.test.client import Client

# Create your tests here.

class TestClient(TestCase):
    def setUp(self):
        self.client = APIClient()
    def tearDown(self):
        pass

    def test_something(self):
        pass

    def test_view(self):
        # client = Client()
        pass