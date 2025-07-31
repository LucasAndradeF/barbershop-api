from rest_framework import viewsets
from .models import Barber
from .serializers import BarberSerializer, RegisterBarberSerializer, BarberConfigSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from core.permissions import IsBarber, IsClient
from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=["Cliente"],
    summary="Rota para a visualização de barbeiros cadastrados no sistema",
)
class BarberView(viewsets.ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = BarberSerializer
    http_method_names = ['get']
    permission_classes = [IsClient]


@extend_schema(
    tags=["Cadastro de Usuário"],
    summary="Rota para cadastro de barbeiros",
)
class RegisterBarberView(viewsets.ModelViewSet):
    queryset = Barber.objects.all()
    serializer_class = RegisterBarberSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]


@extend_schema(
    tags=["Barbeiro"],
    summary="Rotas para atualizações de cadastro e visualização de perfil"
)
class BarberConfigView(viewsets.ModelViewSet):
    permission_classes = [IsBarber, IsAuthenticated]
    serializer_class = BarberConfigSerializer

    def get_queryset(self):
        return Barber.objects.filter(user=self.request.user)

    def get_object(self):
        return Barber.objects.get(user=self.request.user)
