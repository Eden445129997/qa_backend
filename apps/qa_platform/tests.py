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

        data = {
            "plan_id": 1,
            "case_id": 2,
            "host": "http://localhost:9998",
            "headers": {
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTI4MTI2MDksInVzZXJJZCI6NjI3NDcyNDgxMjI5MjA5NjAwLCJ1c2VyUGxhdGZvcm0iOiJhcHAiLCJ1ZGlkIjoibG9naW4iLCJpc3MiOiJxaWFva3UifQ.vRqZBEvwsU-O70ABy19duz94i8HoP56g2XvYMcnAjaA"
            }
        }
        response = self.client.post(
            '/platform/runTestPlanById/',
            data
        )
        print(response.content_params)