from rest_framework import serializers

from .models import User


class MyUserSerializer(serializers.ModelSerializer):
    owner_type = serializers.CharField(source='owner_type.user_type', read_only=True)
    class Meta:
        model = User
        fields = ('full_name', 'phone', 'address', 'flat', 'floor',
                  'people', 'car', 'car_model', 'car_color', 'owner_type')
