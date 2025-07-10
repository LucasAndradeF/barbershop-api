from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer, RegisterClientSerializer, ClientConfigSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.permissions import IsClient, IsBarber


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['get', 'delete']
    permission_classes = [IsAuthenticated, IsBarber]


class RegisterClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = RegisterClientSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]


class ClientConfigView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsClient]
    serializer_class = ClientConfigSerializer

    def get_queryset(self):
        return Client.objects.filter(id=self.request.user.id)

    def get_object(self):
        return self.request.user
