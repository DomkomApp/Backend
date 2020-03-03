from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from authen.models import CustomUser
from .models import User,Car,OwnerType
from django.urls import reverse
# Create your tests here.
from .views import MyUserViewSet


class UserTests(APITestCase):
    def setUp(self):
        self.custom_user = CustomUser.objects.create(phone='996777329848')
        self.owner = OwnerType.objects.create(user_type='Owner')
        self.token = Token.objects.create(user=self.custom_user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.custom_user)

    def test_create_car(self):
        data = {
            "car_brand": "Honda",
            "car_model": "CR-V",
            "car_number": "B 1177 AH"
        }
        response = self.client.post('/reg/cars/',data)
        print(response.json())
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(),1)

    def test_create_user(self):
        data = {
            "full_name": "Макс",
            "address": "Миррахимова",
            "flat": 1,
            "floor": 1,
            "people": 1
        }
        response = self.client.post('/reg/users/',data)
        print(response.json())
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count( ), 1)

    def test_create_user_with_car(self):
        data = {
            "full_name": "Макс",
            "address": "Миррахимова",
            "flat": 1,
            "floor": 1,
            "people": 1,
            "automobile": [
        	{
                    "car_brand": "Honda",
                    "car_model": "CR-V",
                    "car_number": "B 1177 AH"
                }
        	]
        }
        response = self.client.post('/reg/users/',data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_create_user_with_no_name(self):
        data = {
            "full_name":"",
            "address": "Миррахимова",
            "flat": 1,
            "floor": 1,
            "people": 1,
            "automobile": [
                {
                    "car_brand": "Honda",
                    "car_model": "CR-V",
                    "car_number": "B 1177 AH"
                }
            ]
        }
        response = self.client.post('/reg/users/',data)
        print(response.json())
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_no_address(self):
        data = {
            "full_name": "Макс",
            "address": "",
            "flat": 1,
            "floor": 1,
            "people": 1,
            "automobile": [
                {
                    "car_brand": "Honda",
                    "car_model": "CR-V",
                    "car_number": "B 1177 AH"
                }
            ]
        }
        response = self.client.post('/reg/users/',data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    # def test_create_user_with_no_flat(self):
    #     data = {
    #         "full_name": "Макс",
    #         "address": "Миррахимова",
    #         "flat":0,
    #         "floor": 1,
    #         "people": 1,
    #         "automobile": [
    #             {
    #                 "car_brand": "Honda",
    #                 "car_model": "CR-V",
    #                 "car_number": "B 1177 AH"
    #             }
    #         ]
    #     }
    #     response = self.client.post('/reg/users/',data)
    #     self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
