from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer, RegisterClientSerializer, ClientConfigSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.permissions import IsClient, IsBarber
from drf_spectacular.utils import extend_schema


@extend_schema(
    tags=["Barbeiro"],
    summary="Rota para a visualização de clientes cadastrados no sistema"
)
class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['get', 'delete']
    permission_classes = [IsAuthenticated, IsBarber]


@extend_schema(
    tags=["Cadastro de Usuário"],
    summary="Rota para o cadastro de clientes",
)
class RegisterClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = RegisterClientSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]


@extend_schema(
    tags=["Cliente"],
    summary="Rota para atualização e exibição de perfil do cliente cadastrado"
)
class ClientConfigView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsClient]
    serializer_class = ClientConfigSerializer

    def get_queryset(self):
        return Client.objects.filter(id=self.request.user.id)

    def get_object(self):
        return self.request.user
