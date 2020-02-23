from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import CustomUser
User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    validation_code = serializers.CharField(max_length=4,allow_null=True)
    # password = serializers.CharField(max_length=20,read_only=True)

    def create(self,validated_data,*args,**kwargs):
        dict = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['validation_code'],
            validation_code=validated_data['validation_code'],
    )
        return dict

    class Meta:
        model = CustomUser
        fields = ('username','validation_code')
