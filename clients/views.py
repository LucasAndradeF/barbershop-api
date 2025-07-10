from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer, RegisterClientSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ['get', 'delete']
    # permission_classes = [IsAuthenticated]


class RegisterClient(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = RegisterClientSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]
