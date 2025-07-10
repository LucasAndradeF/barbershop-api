from rest_framework import serializers
from .models import Client
from django.contrib.auth import password_validation


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name',
                  'phone', 'email', 'date_joined']
        read_only_fields = ['id']


class RegisterClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[
                                     password_validation.validate_password])

    class Meta:
        model = Client
        fields = ['first_name', 'last_name',
                  'phone', 'email', 'password']

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        client = Client.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username']
        )
        return client
