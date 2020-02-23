from rest_framework import serializers

from .models import User


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'phone', 'address', 'flat', 'floor',
                  'people', 'car', 'car_model', 'car_color', 'owner_type')
