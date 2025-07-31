from rest_framework import viewsets
from .models import Service
from .serializers import BarberServiceSerializer, ClientServiceSerializer
from core.permissions import IsBarber, IsClient
from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=["Serviços"],
    summary="Rota para clientes visualizarem os serviços da barbearia"
)
class ClientServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ClientServiceSerializer
    http_method_names = ['get']
    permission_classes = [IsClient]


@extend_schema(
    tags=["Serviços"],
    summary="Rota para barbeiros realizarem cadastro, visualização e exclusão de serviços da barbearia"
)
class BarberServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = BarberServiceSerializer
    permission_classes = [IsBarber]
