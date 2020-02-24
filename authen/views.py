import random
import re
import string

from rest_framework.authtoken.views import ObtainAuthToken

from .models import CustomUser
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, authenticate, login
import requests
from users.models import User
# Create your views here.



class UserloginView(ObtainAuthToken):

    def post(self,request,*args,**kwargs):
        phone = request.data['phone']
        try:
            user = CustomUser.objects.get(phone=phone)
            print(phone)
            print(user.id)
            token, created = Token.objects.get_or_create(user=user)
            user.is_active = True
            user.save()
            return Response(data={'user_id':user.id,
                                          'token':token.key
                                          },status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response(data={'Error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
