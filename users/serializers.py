from rest_framework import serializers

from .models import *
from authen.serializers import UserSerializer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class MyUserSerializer(serializers.ModelSerializer):
    owner_type = serializers.CharField(source='owner_type.user_type', read_only=True)
    automobile = CarSerializer()
    phone = UserSerializer()

    class Meta:
        model = User
        fields = '__all__'
