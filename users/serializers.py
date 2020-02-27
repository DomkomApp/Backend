from rest_framework import serializers

from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class MyUserSerializer(serializers.ModelSerializer):
    owner_type = serializers.CharField(source='owner_type.user_type', read_only=True)
    phone = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = User
        fields = ('full_name', 'phone', 'address', 'flat', 'floor',
                  'people', 'owner_type','automobile')
