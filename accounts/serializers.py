from rest_framework import serializers
from .models import User
from django.contrib.auth import password_validation


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, validators=[password_validation.validate_password])
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']
        read_only_fields = ['id', 'date_joined']

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']

        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            password=validated_data['password'],
            username=validated_data['username'],
        )
        return user
