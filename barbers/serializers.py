from rest_framework import serializers
from .models import Barber
from django.contrib.auth import password_validation


class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = ['id', 'first_name', 'last_name', 'phone',
                  'especialidade', 'date_joined']
        read_only_fields = ['id', 'date_joined']


class RegisterBarberSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=password_validation.validate_password)

    class Meta:
        model = Barber
        fields = ['first_name', 'last_name', 'phone',
                  'especialidade', 'email', 'password']

    def create(self, validated_data):
        validated_data['username'] = validated_data['email'],

        barber = Barber.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            especialide=validated_data['especialidade'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        barber.user_type = 'barber'
        barber.is_superuser = False
        barber.is_staff = False
        barber.save()

        return barber


class BarberConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = ['id', 'first_name', 'last_name', 'phone',
                  'especialidade', 'email', 'date_joined']
        read_only_fields = ['id', 'date_joined']
