from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer
from core.permissions import IsBarber
from barbers.models import Barber
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=["Pagamentos"],
    summary="Rota para a visualização e cadastro de pagamentos"
)
class PaymentView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsBarber]

    def get_queryset(self):
        barber = Barber.objects.get(user=self.request.user)
        return Payment.objects.filter(appointment__barber=barber)
