from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "appointment", "amount",
                  "payment_method", "payment_date"]
        read_only_fields = ["id", "payment_date"]
        depth = 1
        