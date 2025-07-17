from rest_framework import serializers
from accounts.models import User
from .models import Client
from django.contrib.auth import password_validation


class BaseClientSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(
        source='user.first_name', read_only=True)

    last_name = serializers.CharField(
        source='user.last_name', read_only=True)

    phone = serializers.CharField(source='user.phone', read_only=True)

    email = serializers.EmailField(source='user.email', read_only=True)

    date_joined = serializers.CharField(
        source='user.date_joined', read_only=True)

    is_active = serializers.CharField(
        source='user.is_active', read_only=True)


class ClientSerializer(BaseClientSerializer):

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name',
                  'phone', 'email', 'date_joined', 'is_active']


class RegisterClientSerializer(BaseClientSerializer):
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(write_only=True, required=True)

    password = serializers.CharField(write_only=True, required=True, validators=[
                                     password_validation.validate_password])

    class Meta:
        model = Client
        fields = ['first_name', 'last_name',
                  'phone', 'email', 'password']

    def create(self, validated_data):
        email = validated_data.get('email')

        user_data = {
            'first_name': validated_data.pop('first_name'),
            'last_name': validated_data.pop('last_name'),
            'phone': validated_data.pop('phone'),
            'email': validated_data.pop('email'),
            'password': validated_data.pop('password'),
            'username': email,
        }

        user = User.objects.create_user(**user_data)
        user.user_type = 'client'
        user.save()
        client = Client.objects.create(user=user, **validated_data)

        return client

    def to_representation(self, instance):
        return ClientSerializer(instance, context=self.context).data


class ClientConfigSerializer(BaseClientSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name',
                  'phone', 'email', 'date_joined']
        read_only_fields = ['id', 'date_joined']
