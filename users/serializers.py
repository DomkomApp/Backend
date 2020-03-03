from rest_framework import serializers

from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('car_brand', 'car_model', 'car_number')


class MyUserSerializer(serializers.ModelSerializer):
    owner_type = serializers.CharField(source='owner_type.user_type', read_only=True)
    phone = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    automobile = CarSerializer(many=True,allow_null=True,default=None)

    class Meta:
        model = User
        fields = ('full_name', 'phone', 'address', 'flat', 'floor',
                  'people', 'owner_type', 'automobile')

    def create(self, validated_data):
        car_data = validated_data.pop('automobile')
        user = User.objects.create(**validated_data)

        for car_data in car_data:
            Car.objects.create(owner=user, **car_data)
        return user
