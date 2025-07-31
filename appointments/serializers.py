from rest_framework import serializers
from .models import Appointment


class ClientAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'barber', 'service', 'date', 'status']
        read_only_fields = ['id']
        depth = 1


class BarberAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'client', 'service', 'date', 'status']
        read_only_fields = ['id']
        depth = 1