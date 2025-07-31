from rest_framework import serializers
from .models import Service


class BarberServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'duration', 'price']
        read_only_fields = ['id']


class ClientServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = fields = ['id', 'name', 'duration', 'price']
        read_only_fields = ['id']
