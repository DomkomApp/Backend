from rest_framework import serializers
from rest_framework.response import Response

from .models import *


class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Car
        fields = ('id','car_brand', 'car_model', 'car_number')


class MyUserSerializer(serializers.ModelSerializer):
    owner_type = serializers.CharField(source='owner_type.user_type', read_only=True)
    phone = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    automobile = CarSerializer(many=True,allow_null=True,default=None)

    class Meta:
        model = User
        fields = ('id', 'full_name', 'phone', 'address', 'flat', 'floor',
                  'people', 'owner_type', 'automobile')

    def create(self, validated_data):
        car_data = validated_data.pop('automobile')
        user = User.objects.create(**validated_data)

        for car_data in car_data:
            Car.objects.create(owner=user, **car_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    owner_type = serializers.CharField(source='owner_type.user_type', read_only=True)
    phone = serializers.HiddenField(
        default=serializers.CurrentUserDefault( )
    )
    automobile = CarSerializer(many=True, allow_null=True, default=None)
    class Meta:
        model = User
        fields = ('id', 'full_name', 'phone', 'address', 'flat', 'floor',
                  'people', 'owner_type', 'automobile')

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.address= validated_data.get('address', instance.address)
        instance.flat = validated_data.get('flat', instance.flat)
        instance.floor = validated_data.get('floor', instance.floor)
        instance.people = validated_data.get('people', instance.people)
        instance.save()

        automobile = validated_data.get('automobile')

        for car in automobile:
            try:
                automobile_id = car.get('id')
                inv_item = Car.objects.get(id=automobile_id, owner=instance)
                inv_item.car_brand = car.get('car_brand', inv_item.car_brand)
                inv_item.car_model = car.get('car_model', inv_item.car_model)
                inv_item.car_number = car.get('car_number', inv_item.car_number)
                inv_item.save()
            except Car.DoesNotExist:
                return instance
        return instance
