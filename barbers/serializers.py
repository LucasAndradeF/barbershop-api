from rest_framework import serializers
from .models import Barber
from accounts.models import User


class BarberBaseSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        source='user.first_name', read_only=True)

    last_name = serializers.CharField(
        source='user.last_name', read_only=True)

    email = serializers.EmailField(
        source='user.email', read_only=True)

    phone = serializers.CharField(
        source='user.phone', read_only=True)

    date_joined = serializers.CharField(
        source='user.date_joined', read_only=True)


class BarberSerializer(BarberBaseSerializer):

    class Meta:
        model = Barber
        fields = ['id', 'first_name', 'last_name',
                  'email', 'phone', 'especialidade']


class RegisterBarberSerializer(BarberBaseSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Barber
        fields = ['first_name', 'last_name', 'phone',
                  'email', 'password', 'especialidade']

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

        user.user_type = 'barber'
        user.save()
        barber = Barber.objects.create(user=user, **validated_data)
        return barber

    def to_representation(self, instance):
        return BarberSerializer(instance, context=self.context).data


class BarberConfigSerializer(BarberBaseSerializer):

    class Meta:
        model = Barber
        fields = ['id', 'especialidade', 'first_name',
                  'last_name', 'email', 'phone', 'date_joined']
        read_only_fields = ['id', 'date_joined']
