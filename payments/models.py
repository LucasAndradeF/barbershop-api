from django.db import models
from appointments.models import Appointment
import uuid


class Payment(models.Model):
    TYPE_CHOICES = (
        ("dinheiro", "Dinheiro"),
        ("cartao", "Cartão"),
        ("pix", "Pix"),
    )
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    payment_method = models.CharField(
        max_length=20, choices=TYPE_CHOICES, default='dinheiro')
    payment_date = models.DateTimeField(auto_now_add=True)
