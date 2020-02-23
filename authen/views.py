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
from .serializers import CustomUserSerializer
# Create your views here.
from domkomApp.settings import NIKITA_SMS_LOGIN, NIKITA_SMS_PASSWORD, NIKITA_SMS_SENDER
User = get_user_model()


def send_sms(validate_code,phone_number,user):
    headers = {'Content-Type': 'application/xml'}
    xml = '''
            <message>
                <login>''' + NIKITA_SMS_LOGIN + '''</login>
                <pwd>''' + NIKITA_SMS_PASSWORD + '''</pwd>
                <id>''' + str(user.id) + '''</id>
                <sender>''' + NIKITA_SMS_SENDER + '''</sender>
                <text>''' + validate_code + '''</text>
                <phones>
                    <phone>''' + str(phone_number) + '''</phone>
                </phones>
            </message>
           '''
    xml = xml.encode('utf-8')
    r = requests.post('https://smspro.nikita.kg/api/message', data=xml, headers=headers)
    prog = re.compile(r'<status>(.*?)</status>')
    status_code = int(prog.findall(r.text)[0])
    print(validate_code)
    print(phone_number)
    print(user.id)
    return status_code == 0


class UserloginView(APIView):

    def post(self,request,*args,**kwargs):
        validate_code = ''.join(random.choice(string.digits) for _ in range(4))
        username = request.data['username']

        user_serializer = CustomUserSerializer(data={
            'username':username,

            'validation_code':validate_code,
        },many=False)
        if user_serializer.is_valid():
            user_serializer.save()
            usr = User.objects.get(username=username)
            usr.is_active=False
            usr.save()
            send_sms(validate_code=validate_code,phone_number=username,user=usr)
            return Response(data={'user_id':usr.id,'code':validate_code},status=status.HTTP_201_CREATED)
        else:
            return Response(data={'Пользователь уже активирован'},status=status.HTTP_400_BAD_REQUEST)


class UserActivateView(APIView):
    def post(self,request,*args,**kwargs):
        code = request.data['code']
        user_id = self.request.data['user_id']
        user = User.objects.get(id=user_id)
        custom_user = CustomUser.objects.get(id=user_id)
        if code == custom_user.validation_code:
            user.is_active=True
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            login(request,user)

            data = {
                'token':token.key,
                'user_id':user_id,
            }
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response(data={'Ошибка: Неправильный код'},status=status.HTTP_400_BAD_REQUEST)


