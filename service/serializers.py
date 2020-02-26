from rest_framework import serializers
from .models import Service
from authen.serializers import UserSerializer


class ServiceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Service
        fields = ('id','service_type','status','description','user')



