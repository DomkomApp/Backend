from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import *
# Create your tests here.


class NewsTest(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(phone="996777329848")
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.news = News.objects.create(title="lalaland",image=None,text='Pomogite')
        self.create_url = reverse('news_comments',kwargs={'pk': self.news.pk})

    def test_create_comment(self):
        data = {
            "comment_field":"testcomment to new",
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.create_url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(),1)

    def test_create_comment_non_auth_user(self):
        data = {
            "comment_field":"cheto ne ochen"
        }
        response = self.client.post(self.create_url,data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
