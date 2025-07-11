from rest_framework import viewsets
from .models import Barber
from .serializers import BarberSerializer, RegisterBarberSerializer, BarberConfigSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from core.permissions import IsBarber, IsClient


class BarberView(viewsets.ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    http_method_names = ['get']
    permission_classes = [IsClient]


class RegisterBarberView(viewsets.ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = RegisterBarberSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]


class BarberConfigView(viewsets.ModelViewSet):
    permission_classes = [IsBarber, IsAuthenticated]
    serializer_class = BarberConfigSerializer

    def get_queryset(self):
        return Barber.objects.filter(id=self.request.user.id)

    def get_object(self):
        return self.request.user
