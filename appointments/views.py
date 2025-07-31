from rest_framework import viewsets
from .models import Appointment
from .serializers import ClientAppointmentSerializer, BarberAppointmentSerializer
from core.permissions import IsClient, IsBarber
from clients.models import Client
from barbers.models import Barber
from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=["Agendamento para Clientes"],
    summary="Rota para agendamento de atendimento no sistema"
)
class ClientAppointmentView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = ClientAppointmentSerializer
    permission_classes = [IsClient]

    def get_queryset(self):
        return Appointment.objects.filter(client=Client.objects.get(user=self.request.user))

    def perform_create(self, serializer):
        client = Client.objects.get(user=self.request.user)
        return serializer.save(client=client)


@extend_schema(
    tags=["Gerenciamento de Agendamentos"],
    summary="Rota para visualização de agendamentos realizados no sistema"
)
class BarberAppointmentView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = BarberAppointmentSerializer
    permission_classes = [IsBarber]

    def get_queryset(self):
        return Appointment.objects.filter(barber=Barber.objects.get(user=self.request.user))

    def perform_create(self, serializer):
        barber = Barber.objects.get(user=self.request.user)
        return serializer.save(barber=barber)
