from django.test import Client, TestCase
from django.urls import path, reverse
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory


class TestViewCourse(TestCase):
    def setUp(cls):
        factory = APIRequestFactory()
        client = APIClient()
    
    def test_get(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)

    def test_get_id(self):
        response = self.client.get('/api/1/')
        self.assertEqual(response.status_code, 200)

    def test_get_id_if_not(self):
        response = self.client.get('/api/32/')
        self.assertEqual(response.status_code, 404)

    def test_del_id(self):
        response = self.client.delete('/api/32/')
        self.assertEqual(response.status_code, 204)

    def test_post(self):
        post = {
                     "name": "English",
                     "description": "Study english",
                     "category": 1,
                     "logo": "claut",
                         "contacts": [
                                {
                                    "id": 2,
                                    "type": "Email",
                                    "value": "englishmaria@gmail.com"
                                }
                                    ],
                        "branches": [
                                {
                                    "id": 2,
                                    "latitude": "12 Decembre",
                                    "longitude": "09 October",
                                    "address": "Tel Aviv, Israil"
                                }
                                ]
                        }
        response = self.client.post('/api/', post, format='json')
        self.assertEqual(response.status_code, 201)