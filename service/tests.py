from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import *
from authen.models import CustomUser
# Create your tests here.


class ServiceTest(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(phone='996777329848')
        self.token = Token.objects.create(user=self.user)
        self.create_url = '/service/service/'
        self.client = APIClient()

    def test_create_service(self):
        data = {
            "service_type": "RE",
            "status": "IN",
            "description": "dsdddda"
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.create_url,data)
        print(response.json())
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(Service.objects.count(),1)

    def test_create_service_with_bad_type(self):
        data = {
            "service_type": "",
            "status": "IN",
            "description": "dsdddda"
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.create_url,data)
        print(response.json())
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_create_service_with_bad_status(self):
        data = {
            "service_type": "RE",
            "status": "",
            "description": "dsdddda"
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.create_url,data)
        print(response.json())
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_create_service_with_bad_description(self):
        data = {
            "service_type": "RE",
            "status": "IN",
            "description": ""
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.create_url,data)
        print(response.json())
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

